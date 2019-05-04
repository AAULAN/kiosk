from flask import request
from flask_restplus import Namespace, Resource, fields
from core.database import get_db_products, update_db_product, get_db_sales, add_db_sales, delete_db_sales
from datetime import datetime

api = Namespace('sales', description='Sale related operations')

sale_input = api.model('Sale_request', {
    'product': fields.Integer(required=True, description='The product identifier'),
    'amount': fields.Integer(description='The amount purchased', default=1)
})

sale_output = api.model('Sale_response', {
    'id': fields.Integer(description='The sale identifier'),
    'product': fields.Integer(description='The product identifier'),
    'amount': fields.Integer(description='The amount purchased'),
    'payment': fields.Float(description='Total price for the sale'),
    'timestamp': fields.DateTime(description='The timestamp of the purchase')
})


@api.route('/')
class Sales(Resource):
    @api.doc('Retrieve all sales')
    @api.marshal_list_with(sale_output)
    def get(self):
        return [db_sale.serialize for db_sale in get_db_sales()]

    @api.doc('Add a sale')
    @api.expect(sale_input)
    @api.response(201, "Sale added")
    @api.response(400, "Malformed request or product out of stock")
    @api.response(404, "Product not found")
    def post(self):
        json = request.json
        if not json or 'product' not in json:
            api.abort(400, 'Malformed request')

        amount = json['amount'] if 'amount' in json else 1

        if amount <= 0:
            api.abort(400, "'amount' must be a positive number")

        db_product = get_db_products(product_id=json['product'])
        if not db_product:
            api.abort(404)

        if not db_product.stock == -1:
            if db_product.stock - amount < 0:
                api.abort(400, 'Not enough stock')

            db_product.stock -= amount
            if db_product.collection:
                collection_products = get_db_products(collection=db_product.collection)
                for product in collection_products:
                    product.stock = db_product.stock
                    update_db_product(product.id, product.serialize)

        db_sale = {
            'product': json['product'],
            'amount': amount,
            'payment': db_product.price * amount,
            'timestamp': datetime.utcnow()
        }

        update_db_product(db_product.id, db_product.serialize)
        add_db_sales(db_sale)

        return {'result': 'success'}, 201


@api.route('/<int:product>')
@api.param('product', 'The id for the product of which to get all sales')
class Product(Resource):
    @api.doc('Get total sales for a product')
    @api.response(404, 'No sales for product')
    def get(self, product):
        count = 0
        db_product = get_db_products(product_id=product)
        product_sale = get_db_sales(product_id=product)
        if not product_sale:
            api.abort(404)

        for prod in product_sale:
            count += prod.amount

        return {'product': db_product.serialize, 'count': count}


@api.route('/<int:sale>')
@api.param('sale', 'The id for the sale to delete')
class Sale(Resource):
    @api.doc('Delete a sale')
    @api.response(404, 'Sale not found')
    def delete(self, sale):
        db_sale = get_db_sales(sale_id=sale)
        db_product = get_db_products(db_sale.product)

        if not db_sale or not db_product:
            api.abort(404)

        if not db_product.stock == -1:
            db_product.stock += db_sale.amount

            if db_product.collection:
                collection_products = get_db_products(collection=db_product.collection)
                for product in collection_products:
                    product.stock = db_product.stock
                    update_db_product(product.id, product.serialize)

        update_db_product(db_product.id, db_product.serialize)
        delete_db_sales(sale)
        return {'result': 'success'}

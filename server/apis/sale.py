from flask import request
from flask_restplus import Namespace, Resource, fields
from core.database import get_db_sales, get_db_products, update_db_products, add_db_sales, delete_db_sales
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

        if 'amount' in json and json['amount'] < 0:
            api.abort(400, "'amount' must be a positive number")

        db_product = get_db_products(product_id=json['product']).serialize
        if len(db_product) == 0:
            api.abort(404)

        if db_product['stock'] <= 0:
            api.abort(400, 'Product out of stock')

        db_product['stock'] -= 1

        db_sale = {
            'product': json['product'],
            'amount': json.get('amount', 1),
            'payment': db_product['price'] * json.get('amount', 1),
            'timestamp': datetime.utcnow()
        }

        update_db_products(json['product'], db_product)
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
            count += prod.serialize['amount']

        return {'product': db_product.serialize, 'count': count}


@api.route('/<int:sale>')
@api.param('sale', 'The id for the sale to delete')
class Sale(Resource):
    @api.doc('Delete a sale')
    @api.response(404, 'Sale not found')
    def delete(self, sale):
        db_sale = get_db_sales(sale_id=sale)
        product = get_db_products(db_sale.product)

        product.stock += 1

        if not db_sale:
            api.abort(404)

        update_db_products(db_sale.product, product.serialize)
        delete_db_sales(sale)
        return {'result': 'success'}

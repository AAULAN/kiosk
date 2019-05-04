from flask import request
from flask_restplus import Namespace, Resource, fields
from core.database import get_db_products, add_db_product, delete_db_product, update_db_products
from numbers import Number

api = Namespace('products', description='Product related operations')

product_input = api.model('Product_in', {
    'name': fields.String(description='The product name'),
    'category': fields.String(description='The product category'),
    'price': fields.Float(description='The product price'),
    'stock': fields.Integer(description='The amount in stock'),
    'active': fields.Boolean(description='Whether or not the product is purchasable')
})

product_output = api.model('Product', {
    'id': fields.Integer(description='The product identifier'),
    'name': fields.String(description='The product name'),
    'category': fields.String(description='The product category'),
    'price': fields.Float(description='The product price'),
    'stock': fields.Integer(description='The amount in stock'),
    'active': fields.Boolean(description='Whether or not the product is purchasable')
})


@api.route('/')
class Products(Resource):
    @api.doc('Retrieve all products')
    @api.marshal_list_with(product_output)
    def get(self):
        return [db_product.serialize for db_product in get_db_products()]

    @api.doc('Create a new product')
    @api.response(400, 'Malformed request')
    @api.response(201, 'Product created')
    @api.expect(product_input)
    def post(self):
        json = request.json
        if not json or 'name' not in json:
            api.abort(400)

        if 'stock' in json and json['stock'] < 0:
            api.abort(400, "'stock' must be a positive number")

        db_product = {
            'name': json['name'],
            'category': json.get('category', 'Uncategorized'),
            'price': json.get('price', 0),
            'stock': json.get('stock', 0),
            'active': json.get('active', True)
        }

        add_db_product(db_product)
        return {'result': 'success'}, 201


@api.route('/<int:product>')
@api.param('product', 'Product identifier')
class Product(Resource):
    @api.doc('Get project by identifier')
    @api.response(404, 'Product not found')
    @api.marshal_with(product_output)
    def get(self, product):
        db_product = get_db_products(product_id=product)
        if not db_product:
            api.abort(404)
        return db_product.serialize

    @api.doc('Update a product')
    @api.response(400, 'Malformed request')
    @api.response(404, 'Product not found')
    @api.expect(product_input)
    def put(self, product):
        json = request.json
        if not json:
            api.abort(400)

        db_product = get_db_products(product_id=product).serialize
        if len(db_product) == 0:
            api.abort(404)

        if 'name' in json and type(json['name']) is not str:
            api.abort(400)
        if 'category' in json and type(json['category']) is not str:
            api.abort(400)
        if 'price' in json and not isinstance(json['price'], Number):
            api.abort(400)
        if 'stock' in json and (not isinstance(json['stock'], Number) or json['stock'] < 0):
            api.abort(400)
        if 'active' in json and type(json['active']) is not bool:
            api.abort(400)

        new_product = {
            'name': json.get('name', db_product['name']),
            'category': json.get('category', db_product['category']),
            'price': json.get('price', db_product['price']),
            'stock': json.get('stock', db_product['stock']),
            'active': json.get('active', db_product['active'])
        }

        update_db_products(product, new_product)

        return {'result': 'success'}

    @api.doc('Delete a product')
    @api.response(404, 'Product not found')
    def delete(self, product):
        db_product = get_db_products(product_id=product)
        if not db_product:
            api.abort(404)
        delete_db_product(product)
        return {'result': 'success'}


@api.route('/<string:category>')
@api.param('category', 'Category name')
class ProductCategory(Resource):
    @api.doc('Get products in category')
    @api.response(404, 'No products in category')
    def get(self, category):
        db_products = get_db_products(category=category)
        if len(db_products) == 0:
            api.abort(404)
        return [db_product.serialize for db_product in db_products]

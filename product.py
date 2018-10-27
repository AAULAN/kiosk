from flask import Blueprint, abort, jsonify, request
from database import get_db_products, add_db_products, remove_db_products, update_db_products
from numbers import Number

product_blueprint = Blueprint('product', __name__, url_prefix='/kiosk/api/v1.0/products')


@product_blueprint.route('', methods=['GET'])
def get_products():
    return jsonify([product.serialize for product in get_db_products()])


@product_blueprint.route('', methods=['POST'])
def create_product():
    if not request.json or 'name' not in request.json:
        abort(400)

    product = {
        'name': request.json['name'],
        'category': request.json.get('category', ''),
        'price': request.json['price'],
        'active': True
    }

    add_db_products(product)
    return jsonify({'result': 'success'}), 201


@product_blueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_db_products(product_id=product_id)
    if not product:
        abort(404)
    return jsonify(product.serialize)


@product_blueprint.route('/<string:product_category>', methods=['GET'])
def get_category_products(product_category):
    products = get_db_products(category=product_category)
    if len(products) == 0:
        abort(404)
    return jsonify([product.serialize for product in products])


@product_blueprint.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = get_db_products(product_id=product_id).serialize
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not str:
        abort(400)
    if 'price' in request.json and not isinstance(request.json['price'], Number):
        abort(400)
    if 'active' in request.json and type(request.json['active']) is not bool:
        abort(400)

    new_product = {
        'name': request.json.get('name', product['name']),
        'category': request.json.get('category', product['category']),
        'price': request.json.get('price', product['price']),
        'active': request.json.get('active', product['active'])
    }

    update_db_products(product_id, new_product)

    return jsonify({'result': 'success'})


@product_blueprint.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = get_db_products(product_id=product_id)
    if not product:
        abort(404)
    remove_db_products(product)
    return jsonify({'result': 'success'})

from flask import Blueprint, abort, jsonify, request
from __init__ import authorize, make_public_product, check_duplicate, products

product_blueprint = Blueprint('product', __name__, url_prefix='/kiosk/api/v1.0/products')


@product_blueprint.route('', methods=['GET'])
def get_products():
    return jsonify([product for product in products])


@product_blueprint.route('', methods=['POST'])
def create_product():
    authorize(request)
    if not request.json or 'name' not in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'name': request.json['name'],
        'category': request.json.get('category', ""),
        'price': request.json['price'],
        'active': True
    }

    check_duplicate(product)

    products.append(product)
    return jsonify({product}), 201


@product_blueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    return jsonify(product[0])


@product_blueprint.route('/<string:product_category>', methods=['GET'])
def get_category_products(product_category):
    category_products = [product for product in products if product['category'] == product_category]
    if len(category_products) == 0:
        abort(404)
    return jsonify([product for product in category_products])


@product_blueprint.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    authorize(request)
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    if 'active' in request.json and type(request.json['active']) is not bool:
        abort(400)
    product[0]['name'] = request.json.get('name', product[0]['name'])
    product[0]['category'] = request.json.get('category', product[0]['category'])
    product[0]['price'] = request.json.get('price', product[0]['price'])
    product[0]['active'] = request.json.get('active', product[0]['active'])
    return jsonify({'product': product[0]})


@product_blueprint.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    authorize(request)
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'result': True})

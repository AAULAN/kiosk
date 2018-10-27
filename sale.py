from flask import Blueprint, jsonify, abort, request
from database import get_db_sales, get_db_products, add_db_sales
from datetime import datetime

sale_blueprint = Blueprint('sale', __name__, url_prefix='/kiosk/api/v1.0/sales')


@sale_blueprint.route('', methods=['GET'])
def get_sales():
    return jsonify([sale.serialize for sale in get_db_sales()])


@sale_blueprint.route('', methods=['POST'])
def add_sale():
    if not request.json or 'product' not in request.json:
        abort(400)

    product = get_db_products(product_id=request.json['product']).serialize
    if len(product) == 0:
        abort(404)

    sale = {
        'product': request.json['product'],
        'amount': request.json['amount'],
        'payment': product['price'] * request.json['amount'],
        'timestamp': datetime.now()
    }

    add_db_sales(sale)

    return jsonify({'result': 'success'}), 201


@sale_blueprint.route('/<int:product_id>', methods=['GET'])
def get_sale_count(product_id):
    count = 0
    sale = get_db_sales(product_id)
    if not sale:
        abort(404)

    for product in sale:
        count += product.serialize['amount']

    return jsonify({'product': product_id, 'count': count})


@sale_blueprint.route('/<int:product_id>', methods=['DELETE'])
def delete_sale(sale_id):
    sale = get_db_sales(sale_id)

    if not sale:
        abort(404)

    delete_sale(sale_id)
    return jsonify({'result': 'success'})

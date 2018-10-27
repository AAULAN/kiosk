from flask import Blueprint, jsonify, abort, request
from __init__ import make_public_sale, sales, products

sale_blueprint = Blueprint('sale', __name__, url_prefix='/kiosk/api/v1.0/sales')


@sale_blueprint.route('', methods=['GET'])
def get_sales():
    return jsonify({'sales': [make_public_sale(sale) for sale in sales]})


@sale_blueprint.route('', methods=['POST'])
def add_sale():
    if not request.json or 'product' not in request.json:
        abort(400)

    product = [product for product in products if product['id'] == request.json['product']]
    if len(product) == 0:
        abort(404)

    sale = {
        'product': request.json['product'],
        'amount': request.json['amount'],
        'payed': product[0]['price'] * request.json['amount']
    }

    sales.append(sale)

    return jsonify({'sale': make_public_sale(sale)}), 201


@sale_blueprint.route('/<int:product_id>', methods=['GET'])
def get_sale_count(product_id):
    count = 0
    sale = [sale for sale in sales if sale['product'] == product_id]
    if len(sale) == 0:
        abort(404)

    for product in sale:
        count += product['amount']

    return jsonify({'product': product_id, 'count': count})

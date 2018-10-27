from flask import Flask, abort, url_for
import datetime

products = [
    {
        'id': 1,
        'name': 'Monster White (Crew)',
        'category': 'Monster',
        'price': 12,
        'active': True
    },
    {
        'id': 2,
        'name': 'Monster White (Attendee)',
        'category': 'Monster',
        'price': 15,
        'active': True
    },
    {
        'id': 3,
        'name': 'Coffee (Fri)',
        'category': 'Coffee',
        'price': 35,
        'active': True
    },
    {
        'id': 4,
        'name': 'Coffee (Sat/Sun)',
        'category': 'Coffee',
        'price': 25,
        'active': True
    }
]

sales = [
    {
        'id': 1,
        'timestamp': datetime.datetime.now(),
        'product': 1,
        'amount': 1,
        'payed': 12
    },
    {
        'id': 1,
        'timestamp': datetime.datetime.now(),
        'product': 1,
        'amount': 2,
        'payed': 24
    }
]


def list_categories():
    categories = list()
    for product in products:
        category = dict()
        category["name"] = product["category"]
        if category not in categories:
            categories.append(category)
    return categories


def make_public_category(category):
    new_category = dict()
    new_category["name"] = category["name"]
    new_category['uri'] = url_for('category.get_category_products', product_category=category["name"], _external=True)
    return new_category


def make_public_sale(sale):
    new_sale = dict()
    for field in sale:
        if field == 'id':
            pass
        else:
            new_sale[field] = sale[field]
    return new_sale


def make_public_product(product):
    new_product = dict()
    for field in product:
        if field == 'id':
            new_product['uri'] = url_for('product.get_product', product_id=product['id'], _external=True)
        else:
            new_product[field] = product[field]
    return new_product


def check_duplicate(prod):
    for p in products:
        if p["name"] == prod["name"] and p["category"] == prod["category"]:
            abort(403)


def authorize(req):
    if req.json is None or "key" not in req.json or req.json["key"] != "lookupapikeys":
        abort(401)


def create_app():
    app = Flask(__name__)
    return app

from flask import Flask, jsonify, request, abort, make_response, url_for

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': u'Monster White (Crew)',
        'category': u'Monster'
    },
    {
        'id': 2,
        'name': u'Monster White (Attendee)',
        'category': u'Monster'
    },
    {
        'id': 3,
        'name': u'Coffee (Fri)',
        'category': u'Coffee'
    },
    {
        'id': 4,
        'name': u'Coffee (Sat/Sun)',
        'category': u'Coffee'
    }
]

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)
@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'error': 'Forbidden'}), 403)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

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
    new_category['uri'] = url_for('get_category_products', product_category=category["name"], _external=True)
    return new_category

def make_public_product(product):
    new_product = dict()
    for field in product:
        if field == 'id':
            new_product['uri'] = url_for('get_product', product_id=product['id'], _external=True)
        else:
            new_product[field] = product[field]
    return new_product

def check_duplicate(product):
    for prod in products:
        if prod["name"] == product["name"] and prod["category"] == product["category"]:
            abort(403)


def authorize(request):
    if request.json is None or "key" not in request.json or request.json["key"] != "lookupapikeys":
        abort(401)

@app.route('/kiosk/api/v1.0/categories', methods=['GET'])
def get_categories():
    return jsonify({'categories': [make_public_category(category) for category in list_categories()]})

@app.route('/kiosk/api/v1.0/products', methods=['GET'])
def get_products():
    return jsonify({'products': [make_public_product(product) for product in products]})

@app.route('/kiosk/api/v1.0/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    return jsonify({'product': make_public_product(product[0])})

@app.route('/kiosk/api/v1.0/products/<string:product_category>', methods=['GET'])
def get_category_products(product_category):
    category_products = [product for product in products if product['category'] == product_category]
    if len(category_products) == 0:
        abort(404)
    return jsonify({'products': [make_public_product(product) for product in category_products]})

@app.route('/kiosk/api/v1.0/products', methods=['POST'])
def create_product():
    authorize(request)
    if not request.json or not 'name' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'name': request.json['name'],
        'category': request.json.get('category', "")
    }

    check_duplicate(product)

    products.append(product)
    return jsonify({'product': make_public_product(product)}), 201

@app.route('/kiosk/api/v1.0/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    authorize(request)
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not unicode:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not unicode:
        abort(400)
    product[0]['name'] = request.json.get('title', product[0]['title'])
    product[0]['category'] = request.json.get('description', product[0]['description'])
    return jsonify({'product': make_public_product(product[0])})

@app.route('/kiosk/api/v1.0/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    authorize(request)
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'result': True})
  
if __name__ == "__main__":
  app.run()
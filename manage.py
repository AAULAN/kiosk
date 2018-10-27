from flask import make_response, jsonify
from flask_script import Manager
from flask_cors import CORS
from __init__ import create_app
import product, sale, category


app = create_app()
app.register_blueprint(product.product_blueprint)
app.register_blueprint(sale.sale_blueprint)
app.register_blueprint(category.category_blueprint)
app.app_context().push()
CORS(app)

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


manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()

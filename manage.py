from category import category_blueprint
from product import product_blueprint
from sale import sale_blueprint
from flask import make_response, jsonify
from flask_cors import CORS
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from __init__ import create_app, db

app = create_app()
app.register_blueprint(product_blueprint)
app.register_blueprint(sale_blueprint)
app.register_blueprint(category_blueprint)
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

migrate = Migrate(app, db, compare_type=True)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()

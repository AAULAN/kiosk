from flask import make_response, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from __init__ import db
from core.database import delete_db_sales

app = create_app('prod')


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
    app.run(debug=True)


@manager.command
def clear_sales():
    delete_db_sales()


if __name__ == '__main__':
    manager.run()

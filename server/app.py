from flask import Flask
from flask_cors import CORS
from __init__ import db
from core.config import config_by_name
from apis import api


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(config_by_name[configuration])
    db.init_app(app)
    api.init_app(app)
    CORS(app)

    return app


if __name__ == '__main__':
    create_app('prod').run(debug=True)

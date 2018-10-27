from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_by_name

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name['prod'])
    db.init_app(app)

    return app

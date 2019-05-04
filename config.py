import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "development.db")}'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql://{secrets.db_user}:{secrets.db_pass}@{secrets.db_host}/{secrets.db_table}"


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)

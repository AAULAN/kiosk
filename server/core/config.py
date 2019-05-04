import os
from sqlalchemy import create_engine, Float, Boolean, TIMESTAMP
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "development.db")}'

    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    Base = declarative_base()

    class Product(Base):
        __tablename__ = "product"

        id = Column(Integer, primary_key=True)
        name = Column(String(80), nullable=False)
        category = Column(String(80), nullable=False)
        price = Column(Float, nullable=False)
        stock = Column(Integer, nullable=False)
        active = Column(Boolean, nullable=False)

    class Sale(Base):
        __tablename__ = "sale"

        id = Column(Integer, primary_key=True)
        product = Column(Integer, nullable=False)
        amount = Column(Integer, nullable=False)
        payment = Column(Float, nullable=False)
        timestamp = Column(TIMESTAMP, nullable=False)

    Base.metadata.create_all(engine)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://" \
                              f"{os.environ['KIOSK_DATABASE_USERNAME']}:" \
                              f"{os.environ['KIOSK_DATABASE_PASSWORD']}@" \
                              f"{os.environ['KIOSK_DATABASE_HOST']}/" \
                              f"{os.environ['KIOSK_DATABASE']}"


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)

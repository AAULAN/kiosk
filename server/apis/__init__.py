from flask_restplus import Api

from .category import api as category
from .product import api as product
from .sale import api as sale

api = Api(
    title='AAULAN Kiosk System 2.0',
    version='2.0',
    description='A kiosk system developed for monitoring sales for events hosted by AAULAN',
)

api.add_namespace(category)
api.add_namespace(product)
api.add_namespace(sale)

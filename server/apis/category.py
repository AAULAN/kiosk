from flask_restplus import Namespace, Resource
from core.database import get_db_product_categories

api = Namespace('categories', description='Category related operations')


@api.route('/')
class Categories(Resource):
    @api.doc('Get all categories')
    def get(self):
        return [category for category in get_db_product_categories()]

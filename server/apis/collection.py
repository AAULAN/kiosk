from flask_restplus import Namespace, Resource
from core.database import get_db_product_collections, get_db_product_collection

api = Namespace('collections', description='Collection related operations')


@api.route('/')
class Collections(Resource):
    @api.doc('Get all collections')
    def get(self):
        return [category for category in get_db_product_collections()]

from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger
from resources.score.view import ScoreResource

api_bp = Blueprint('api', __name__)


api = Api(api_bp)

api = swagger.docs(Api(api_bp), apiVersion='0.1',
                   basePath='http://localhost:5000',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/spec',
                   description='Bowling score API')

# Routing
api.add_resource(ScoreResource, '/score')
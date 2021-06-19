from flask_restx import Api
from flask import Blueprint

from app.main.controller.user_controller import api as user_ns
from app.main.controller.auth_controller import api as auth_ns
from app.main.controller.restaurant_controller import api as rest_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='FoodHub API',
    version='1.0',
    description='A FoodHub API web service'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(rest_ns)
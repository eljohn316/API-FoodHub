from flask_restx import Api
from flask import Blueprint

from app.main.controller.user_controller import api as ns1  #user namespace
from app.main.controller.auth_controller import api as ns2  #auth namespace
from app.main.controller.restaurant_controller import api as ns3 #restaurant namespace
from app.main.controller.menu_controller import api as ns4 # menu namespace

blueprint = Blueprint('api', __name__)

api = Api(
  blueprint,
  title='FoodHub API',
  version='1.0',
  description='FoodHub API service'
)

api.add_namespace(ns1, path='/user')
api.add_namespace(ns2, path='/auth')
api.add_namespace(ns3, path='/restaurant')
api.add_namespace(ns4, path='/menu')
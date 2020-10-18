from flask_restx import Api
from flask import Blueprint

from app.main.controller.user_controller import api as ns1  #user namespace
from app.main.controller.auth_controller import api as ns2  #auth namespace

blueprint = Blueprint('api', __name__)

api = Api(
  blueprint,
  title='FoodHub API',
  version='1.0',
  description='FoodHub API service'
)

api.add_namespace(ns1, path='/user')
api.add_namespace(ns2, path='/auth')
from flask_restx import Api
from flask import Blueprint

from app.main.controller.owner_controller import api as owner_ns
from app.main.controller.customer_controller import api as customer_ns
from app.main.controller.auth_controller import api as auth_ns 
from app.main.controller.restaurant_controller import api as restaurant_ns
from app.main.controller.menu_controller import api as menu_ns

blueprint = Blueprint('api', __name__)

# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'X-API-KEY'
#     }
# }

api = Api(
  blueprint,
  title='FoodHub API',
  version='1.0',
  description='FoodHub API service'
  # authorizations = authorizations
)

api.add_namespace(owner_ns, path='/user')
api.add_namespace(customer_ns, path='/customer')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(restaurant_ns, path='/restaurant')
api.add_namespace(menu_ns, path='/menu')
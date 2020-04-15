from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.restaurant_controller import api as rest_ns
from .main.controller.menu_controller import api as menu_ns
from .main.controller.reservation_controller import api as resv_ns
from .main.controller.reviews_controller import api as revs_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FOODHUB',
          version='1.0',
          description='Foodhub API'
          )

api.add_namespace(user_ns)
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(rest_ns, path='/restaurant')
api.add_namespace(menu_ns, path='/menu')
api.add_namespace(resv_ns, path='/reservation')
api.add_namespace(revs_ns, path='/reviews')


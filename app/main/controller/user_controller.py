from flask import request
from flask_restx import Resource

from app.main.util.dto import UserDto
from app.main.util.custom_dto import UserDtoPublic
from app.main.util.decorator import selective_marshal_with, owner_token_required, customer_token_required
from app.main.service.user_service import sign_up_customer, sign_up_owner, get_current_user, get_customers, get_owners, update_user, get_user

api = UserDto.api
_create_user = UserDto.create_user
_update_user = UserDto.update_user

@api.route('/owner/')
class OwnerList(Resource):
  """ Shows all owners and lets you POST to add new owners. """
  @api.doc('get_owners')
  @selective_marshal_with(UserDtoPublic, name='Owners')
  def get(self):
    """ Get all owners """
    return get_owners()

  @api.doc('create_owner')
  @api.expect(_create_user, validate=True)
  @api.response(201, 'Owner successfully created.')
  def post(self):
    """Creates new owner """
    data = request.json
    return sign_up_owner(data=data)

@api.route('/customer/')
class CustomerList(Resource):
  """ Shows all customers and lets you POST to add new customers. """
  @api.doc('get_customers')
  @selective_marshal_with(UserDtoPublic, name="Customers")
  def get(self):
    """ Get all customers """
    return get_customers()

  @api.doc('create_customer')
  @api.expect(_create_user, validate=True)
  @api.response(201, 'Customer successfully created.')
  def post(self):
    """ Creates new customer """
    data = request.json
    return sign_up_customer(data=data)

@api.route('/customer/<public_id>')
class Customer(Resource):
  """ Shows a single customer and lets you update and delete an existing customer."""
  @api.doc('get_a_customer')
  @selective_marshal_with(UserDtoPublic, name="Customer")
  def get(self, public_id):
    """ Get customer """
    return get_user(public_id=public_id)
  
  @api.doc('update_an_existing_customer')
  @api.expect(_update_user, validate=True)
  @api.response(200, 'Successfully updated')
  @api.response(404, 'Customer not found.')
  def put(self, public_id):
    """ Update an existing customer """
    data = request.json
    return update_user(data=data, public_id=public_id)

@api.route('/owner/<public_id>')
class Owner(Resource):
  """ Shows a single owner and lets you update and delete an existing owner."""
  @api.doc('get_a_owner')
  @selective_marshal_with(UserDtoPublic, name="Owner")
  def get(self, public_id):
    """ Get owner """
    return get_user(public_id=public_id)

  @api.doc('update_an_existing_owner')
  @api.expect(_update_user, validate=True)
  @api.response(200, 'Successfully updated')
  @api.response(404, 'User not found.')
  def put(self, public_id):
    """ Update an existing owner """
    data = request.json
    return update_user(data=data, public_id=public_id)

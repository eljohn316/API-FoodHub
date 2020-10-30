from flask import request
from flask_restx import Resource

from app.main.util.dto import UserDto
from app.main.util.custom_dto import UserDtoPublic
from app.main.util.decorator import selective_marshal_with
from app.main.service.user_service import UserService

api = UserDto.api
_create_user = UserDto.create_user
_update_user = UserDto.update_user


@api.route('/')
class UserList(Resource):
  @api.doc('create_user')
  @api.expect(_create_user, validate=True)
  @api.response(201, 'User successfully created.')
  def post(self):
    """Creates new user """
    return UserService.sign_up(data=request.json)

@api.route('/owner/')
class OwnerList(Resource):
  """ Shows all owners and lets you POST to add new owners. """
  @api.doc('get_owners')
  @selective_marshal_with(UserDtoPublic, name='Owners')
  def get(self):
    """ Get all owners """
    return UserService.get_owners()

@api.route('/customer/')
class CustomerList(Resource):
  """ Shows all customers and lets you POST to add new customers. """
  @api.doc('get_customers')
  @selective_marshal_with(UserDtoPublic, name="Customers")
  def get(self):
    """ Get all customers """
    return UserService.get_customers()

@api.route('/customer/<public_id>')
class Customer(Resource):
  """ Shows a single customer and lets you update and delete an existing customer."""
  @api.doc('get_a_customer')
  @selective_marshal_with(UserDtoPublic, name="Customer")
  def get(self, public_id):
    """ Get customer """
    return UserService.get_user(public_id=public_id)
  
  @api.doc('update_an_existing_customer')
  @api.expect(_update_user, validate=True)
  @api.response(200, 'Successfully updated')
  @api.response(404, 'Customer not found.')
  def put(self, public_id):
    """ Update an existing customer """
    user = UserService.get_user(public_id=public_id)
    if not user:
      api.abort(404, 'Customer not found')
    return UserService.update(data=request.json, public_id=public_id)

@api.route('/owner/<public_id>')
class Owner(Resource):
  """ Shows a single owner and lets you update and delete an existing owner."""
  @api.doc('get_a_owner')
  @selective_marshal_with(UserDtoPublic, name="Owner")
  def get(self, public_id):
    """ Get owner """
    return UserService.get_user(public_id=public_id)

  @api.doc('update_an_existing_owner')
  @api.expect(_update_user, validate=True)
  @api.response(200, 'Successfully updated')
  @api.response(404, 'User not found.')
  def put(self, public_id):
    """ Update an existing owner """
    user = UserService.get_user(public_id=public_id)
    if not user:
      api.abort(404, 'Owner not found')
    return UserService.update(data=request.json, public_id=public_id)

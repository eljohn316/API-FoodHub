from flask import request
from flask_restx import Resource

from app.main.util.dto import CustomerDto
from app.main.util.custom_dto import UserDtoPublic
from app.main.util.decorator import selective_marshal_with
from app.main.service.user_service import UserService

api = CustomerDto.api
_create_customer = CustomerDto.create_customer
_update_customer = CustomerDto.update_customer

@api.route('/customer/')
class CustomerList(Resource):
  """
  Shows all customers and lets you POST to add new customers.
  """
  @api.doc('get_customers')
  @selective_marshal_with(UserDtoPublic, name="Customers")
  def get(self):
    """
    Get all customers
    """
    return UserService.get_customers()
  
  @api.doc('create_user')
  @api.expect(_create_customer, validate=True)
  @api.response(201, 'User successfully created.')
  def post(self):
    """
    Sign up customer
    """
    return UserService.sign_up_customer(data=request.json)

@api.route('/customer/<int:id>')
@api.response(404, 'Customer not found.')
class Customer(Resource):
  """
  Shows a single customer and lets you update and delete an existing customer
  """
  @api.doc('get_a_customer')
  @selective_marshal_with(UserDtoPublic, name="Customer")
  def get(self, id):
    """
    Get customer
    """
    user = UserService.get_user(id=id)
    if not user:
      api.abort(404, 'Customer not found')
    return UserService.get_user(id=id)
  
  @api.doc('update_customer')
  @api.expect(_update_customer, validate=True)
  @api.response(200, 'Successfully updated')
  def put(self, id):
    """
    Update an existing customer
    """
    user = UserService.get_user(id=id)
    if not user:
      api.abort(404, 'Customer not found')
    return UserService.update(data=request.json, id=id)


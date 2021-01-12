from flask import request
from flask_restx import Resource

from app.main.util.dto import OwnerDto
from app.main.util.custom_dto import UserDtoPublic
from app.main.util.decorator import selective_marshal_with
from app.main.service.user_service import UserService

api = OwnerDto.api
_create_owner = OwnerDto.create_owner
_update_owner = OwnerDto.update_owner


@api.route('/owner/')
class OwnerList(Resource):
  """
  Shows all owners and lets you POST to add new owners
  """
  @api.doc('get_owners')
  @selective_marshal_with(UserDtoPublic, name='Owners')
  def get(self):
    """
    Get all owners
    """
    return UserService.get_owners()
  
  @api.doc('create_user')
  @api.expect(_create_owner, validate=True)
  @api.response(201, 'User successfully created.')
  def post(self):
    """
    Sign up owner
    """
    return UserService.sign_up_owner(data=request.json)

@api.route('/owner/<int:id>')
@api.response(404, 'User not found.')
class Owner(Resource):
  """
  Shows a single owner and lets you update and delete an existing owner
  """
  @api.doc('get_one_owner')
  @selective_marshal_with(UserDtoPublic, name="Owner")
  def get(self, id):
    """
    Get owner
    """
    user = UserService.get_user(id=id)
    if not user:
      api.abort(404, 'Owner not found')
    return UserService.get_user(id=id)

  @api.doc('update_an_existing_owner')
  @api.expect(_update_owner, validate=True)
  @api.response(200, 'Successfully updated')
  def put(self, id):
    """
    Update an existing owner
    """
    user = UserService.get_user(id=id)
    if not user:
      api.abort(404, 'Owner not found')
    return UserService.update(data=request.json, id=id)

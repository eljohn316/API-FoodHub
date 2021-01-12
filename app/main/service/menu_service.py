from app.main import db
from app.main.model.restaurant import Restaurant
from app.main.model.menu import Menu


class MenuService:

  @staticmethod
  def create(data, restaurant_id):
    restaurant = Restaurant.query.filter(Restaurant.id==restaurant_id).first()
    if not restaurant:
      response_object = {
        'status':'fail',
        'message':'Restaurant does not exists'
      }
      return response_object, 404
    else:
      menu = Menu(restaurant_id=data['restaurant_id'])
      Menu.create(menu)
      response_object = {
        'status':'success',
        'message':'Menu successfully created'
      }
      return response_object, 201

  @staticmethod
  def get(menu_id):
    pass

from app.main import db
from app.main.model.restaurant import Restaurant
from app.main.model.menu import Menu
from app.main.model.item import Item

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
      menu = Menu(restaurant_id=restaurant.id)
      Menu.create(menu)
      response_object = {
        'status':'success',
        'message':'Menu successfully created'
      }
      return response_object, 201

  @staticmethod
  def get_menu(menu_id):
    return Item.query.filter(Item.menu_id == menu_id).all()
    
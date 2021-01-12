from app.main import db
from app.main.model.menu import Menu
from app.main.model.item import Item

class ItemService:

  @staticmethod
  def add_item(data, menu_id):
    menu = Menu.query.filter_by(id=menu_id).first()
    if not menu:
      response_object = {
        'status':'fail',
        'message':'Menu does not exists'
      }
      return response_object, 404
    else:
      item = Item(
        item_name = data['item_name'],
        item_availability = data['item_availability'],
        price = ['price'],
        menu_id = menu.id
      )
      db.session.add(item)
      db.session.commit()
      response_object = {
        'status':'success',
        'message':'Item added'
      }
      return response_object, 201
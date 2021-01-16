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
        is_sold_out = data['is_sold_out'],
        price = data['price'],
        menu_id = menu.id
      )
      db.session.add(item)
      db.session.commit()
      response_object = {
        'status':'success',
        'message':'Item added'
      }
      return response_object, 201
  
  @staticmethod
  def update_item(data, item_id):
    item = Item.query.filter_by(id=item_id).first()
    if not item:
      response_object = {
        'status':'fail',
        'message':'Item does not exists'
      }
      return response_object, 404
    else:
      item.item_name = data['item_name'],
      item.is_sold_out = data['is_sold_out'],
      item.price = data['price']
      db.session.commit()
      response_object = {
        'status':'success',
        'message':'Item successfully updated'
      }
      return response_object, 200

  @staticmethod
  def get_item(item_id):
    return Item.query.filter_by(id=item_id).first()
from app.main import db
from app.main.model.restaurant import Restaurant, Menu, Item

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
    # return Menu.query.filter(Menu.id==menu_id).first()
    # menu = db.session.query(
    #   Menu,
    #   Item
    # ).filter(
    #   Menu.id==menu_id
    # ).outerjoin(
    #   Item, Menu.id == Item.menu_id
    # ).first()

    # return dict(
    #   id = menu[0],

    # )
    menu = db.session.query(
      Menu.id,
      Item.id,
      Item.item_name,
      Item.image_url,
      Item.item_availability
    ).filter(
      Menu.id == Item.menu_id
    ).first()
    return dict(
      menu_id = menu[0],
      item_id = menu[1],
      item_name = menu[2],
      item_image_url = menu[3],
      item_availability = menu[4]
    ) if menu else {
      'status':'fail',
      'message' : 'Menu does not exists.'
    }, 404

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


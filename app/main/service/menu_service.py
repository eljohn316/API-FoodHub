from app.main import db
from app.main.model.menu import Menu
from app.main.model.restaurant import Restaurant

def create_menu(data):
    menu = Menu.query.filter_by(name=data['name']).first()
    if not menu:
        new_menu = Menu(
            menu_pic = data['menu_pic'],
            name = data['name'],
            category = data['category'],
            price = data['price'],
            restaurant_id = data['restaurant_id']
        )
        add(new_menu)
        response_object = {
            'status':'success',
            'message':'Menu successfully created'
        }
        return response_object, 201
    else:
        response_object = {
            'status':'fail',
            'message':'Menu already exist'
        }
        return response_object, 409

def update_menu(data, menu_id):
    menu = Menu.query.filter_by(id=menu_id).first()
    print(menu.restaurant_id)
    if menu is None:
        response_object = {
            'status':'fail',
            'message':'Menu not found'
        }
        return response_object, 404
    else:
        menu.menu_pic = data['menu_pic'],
        menu.name = data['name'],
        menu.category = data['category'],
        menu.price = data['price']
        db.session.commit()
        response_object = {
            'status':'success',
            'message':'Menu successfully updated'
        }
        return response_object, 200

def delete_menu(menu_id):
    menu = Menu.query.filter_by(id=menu_id).first()
    if not menu:
        response_object = {
            'status':'fail',
            'message':'Menu not found'
        }
        return response_object, 404
    else:
        db.session.delete(menu)
        db.session.commit()
        response_object = {
            'status':'success',
            'message':'Menu successfully deleted'
        }
        return response_object, 200

def get_all_menus():
    return Menu.query.all()

def add(data):
    db.session.add(data)
    db.session.commit()


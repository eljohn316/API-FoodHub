from app.main.model import restaurant
from app.main import db
from app.main.model.menu import Menu

class MenuService:

    @staticmethod
    def add_menu(data):
        menu = Menu.query.filter_by(menu_name=data.get('menu_name')).first()
        if not menu:
            new_menu = Menu(
                menu_image=data['menu_image'],
                menu_name=data['menu_name'],
                is_available=data['is_available'],
                price=data['price'],
                restaurant_id=data['restaurant_id']
            )
            db.session.add(new_menu)
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Menu successfully added'
            }
            return response_object, 201
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Menu already exists'
            }
            return response_object, 409
    

    @staticmethod
    def add_multiple_menu(data):
        menu_items = []

        for menu in data:

            new_menu = Menu(
                menu_image=menu['menu_image'],
                menu_name=menu['menu_name'],
                is_available=menu['is_available'],
                price=menu['price'],
                restaurant_id=menu['restaurant_id']
            )
            menu_items.append(new_menu)

        db.session.add_all(menu_items)
        db.session.commit()

        response_object = {
            'status' : 'success',
            'message' : 'Menu items successfully added'
        }
        return response_object, 201

    
    @staticmethod
    def update_menu(id, data):
        current_menu = Menu.query.filter_by(id=id).first()
        if not current_menu:
            response_object = {
                'status' : 'fail',
                'message' : 'Menu does not exist'
            }
            return response_object, 404
        else:
            current_menu.menu_name = data['menu_name']
            current_menu.is_available = data['is_available']
            current_menu.price = data['price']
            db.session.commit()
            response_object = {
                'status' : 'success',
                'message' : 'Menu successfully updated'
            }
            return response_object, 200

    @staticmethod
    def delete_menu(id):
        current_menu = Menu.query.filter_by(id=id).first()
        if not current_menu:
            response_object = {
                'status' : 'fail',
                'message' : 'Menu does not exist'
            }
            return response_object, 404
        else:
            db.session.delete(current_menu)
            db.session.commit()
            response_object = {
                'status' : 'fail',
                'message' : 'Menu successfully deleted'
            }
            return response_object, 200

    @staticmethod
    def get_menu(id):
        return Menu.query.filter_by(id=id).first()

    
    @staticmethod
    def check_menu(name):
        menu = Menu.query.filter_by(menu_name=name).first()
        if not menu:
            response_object = {
                'status' : 'fail',
                'message' : 'Menu not found'
            }
            return response_object, 404
        else:
            response_object = {
                'status' : 'success',
                'message' : 'Menu found'
            }
            return response_object, 200
import uuid

from app.main import db
from app.main.model.restaurant import Restaurant
from app.main.model.reservation import Reservation

def create_reservation(data, customer_id):
    # current_reservation = db.session.query(Reservation).order_by(Reservation.reservation_code.desc()).first()
    new_reservation = Reservation(
        reservation_code = str(uuid.uuid4()),
        no_of_persons = data['no_of_persons'],
        date = data['date'],
        time = data['time'],
        reservation_to = data['reservation_to'],
        reservee = customer_id
    )
    add(new_reservation)
    response_object = {
        'status':'success',
        'message':'Reservation successfully created'
    }
    return response_object, 201

def edit_reservation(data, reservation_code):
    current_reservation = Reservation.query.filter_by(reservation_code=data.get('reservation_code')).first()
    if not current_reservation:
        response_object = {
            'status':'fail',
            'message':'Reservation not found'
        }
        return response_object, 404
    else:
        current_reservation.no_of_persons = data['no_of_persons'],
        current_reservation.date = data['date'],
        current_reservation.time = data['time'],
        reservation_to = data['reservation_to']
        
        db.session.commit()
        
        response_object = {
            'status':'success',
            'message':'Reservation successfully updated.'
        }
        return response_object, 200

def cancel_reservation(reservation_code, customer_id):
    current_reservation = Reservation.query.filter_by(reservation_code=reservation_code).first()
    if current_reservation.reservee == customer_id:
        db.session.delete(current_reservation)
        db.session.commit()
        response_object = {
            'status':'fail',
            'message':'Reservation cancelled'
        }
        return response_object, 200
    else:
        response_object = {
            'status':'fail',
            'message':'Reservation not found'
        }
        return response_object, 404
    
def add(data):
    db.session.add(data)
    db.session.commit()

def get_my_reservations(customer_id):
    return Reservation.query.filter_by(reservee=customer_id).all()
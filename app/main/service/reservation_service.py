import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.reservation import AcceptedReservation, Reservation, DeclinedReservation
from app.main.model.restaurant import Restaurant


class ReservationService:

    """
    Reservation related operations
    """

    @staticmethod
    def create_reservation(data, current_user):
        restaurant = Restaurant.query.filter_by(id=data['restaurant_id']).first()

        if restaurant.no_of_vacancies >= data['num_of_persons'] and restaurant.no_of_vacancies != 0:
            restaurant.no_of_vacancies -= data['num_of_persons'] 
            
            reservation = Reservation(
                customer_id = current_user.get('user_id'),
                restaurant_id = data['restaurant_id'],
                restaurant_owner_id = data['restaurant_owner_id'],
                time = data['time'],
                date = data['date'],
                num_of_persons = data['num_of_persons'],
                status = "Pending",
                created_on = datetime.datetime.utcnow()
            )
            
            db.session.add(reservation)
            db.session.commit()

            response_object = {
                "status" : "success",
                "message" : "Reservation successfully created"
            }

            return response_object, 201
            
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Restaurant has no vacancies at the moment'
            }

            return response_object, 409
    

    @staticmethod
    def update_reservation(data, reservation_id):
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if reservation and reservation.status == "Pending":

            restaurant = Restaurant.query.filter_by(id=reservation.restaurant_id).first()
            if restaurant.no_of_vacancies >= data['num_of_persons'] and restaurant.no_of_vacancies != 0:
                
                restaurant.no_of_vacancies += reservation.num_of_persons
                
                reservation.num_of_persons = data["num_of_persons"]
                reservation.time = data["time"]
                reservation.date = data["date"]

                restaurant.no_of_vacancies -= data['num_of_persons']

                db.session.commit()

                response_object = {
                    'status' : 'success',
                    'message' : 'Reservation successfully updated'
                }
                return response_object, 200
            else:
                response_object = {
                    "status" : "fail",
                    "message" : "Restaurant slots insufficient"
                }

                return response_object, 409

        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Reservation does not exist'
            }
            return response_object, 404

    
    @staticmethod
    def cancel_reservation(reservation_id):
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if reservation and reservation.status == "Pending":
            restaurant = Restaurant.query.filter_by(id=reservation.restaurant_id).first()
            restaurant.no_of_vacancies += reservation.num_of_persons
            
            db.session.delete(reservation)
            db.session.commit()
            
            response_object = {
                'status' : 'success',
                'message' : 'Reservation successfully cancelled'
            }
            
            return response_object, 200
            
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Reservation does not exist'
            }
            return response_object, 404

    # @staticmethod
    # def get_restaurant_reservations():
    #     pas

    @staticmethod
    def accept_reservation(reservation_id, current_user):
        reservation = AcceptedReservation.query.filter_by(accepted_reservation_id=reservation_id).first()
        if not reservation:
            current_reservation = Reservation.query.filter_by(id=reservation_id).first()
            current_reservation.status = "Approved"

            new_reservation = AcceptedReservation(
                accepted_reservation_id=reservation_id,
                owner_id=current_user.get('user_id'),
                date_approved=datetime.datetime.utcnow()
            )

            db.session.add(new_reservation)
            db.session.commit()

            response_object = {
                "status" : "success",
                "message" : "Reservation request approved"
            }

            return response_object, 201
        else:
            response_object = {
                "status" : "fail",
                "message" : "Reservation request already exists"
            }

            return response_object, 409
    
    @staticmethod
    def decline_reservation(data, reservation_id, current_user):
        reservation = DeclinedReservation.query.filter_by(id=reservation_id).first()
        if not reservation:
            current_reservation = Reservation.query.filter_by(id=reservation_id).first()
            current_reservation.status = "Declined"

            new_reservation = DeclinedReservation(
                declined_reservation_id=reservation_id,
                owner_id=current_user.get('user_id'),
                message=data['message']
            )

            db.session.add(new_reservation)
            db.session.commit()

            response_object = {
                "status" : "success",
                "message" : "Reservation request declined"
            }

            return response_object, 201
        else:
            response_object = {
                "status" : "fail",
                "message" : "Reservation request already declined"
            }

            return response_object, 409


    @staticmethod
    def has_already_booked(current_user, restaurant_id):
        reservation = Reservation.query.filter(Reservation.customer_id==current_user.get('user_id'), Reservation.restaurant_id==restaurant_id).first()
        if not reservation:
            response_object = {
                "status" : "fail",
                "message" : "User can still book"
            }
            return response_object, 200
        else:
            response_object = {
                "status" : "success",
                "data" : {
                    'id' : reservation.id,
                    'customer_id' : reservation.customer_id,
                    'restaurant_id' : reservation.restaurant_id,
                    'time' : reservation.time,
                    'date' : reservation.date,
                    'num_of_persons' : reservation.num_of_persons,
                    'status' : reservation.status,
                    'created_on' : str(reservation.created_on)
                }
            }
            return response_object, 409

    @staticmethod
    def get_reservation(reservation_id):
        result = Reservation.query.filter_by(id=reservation_id).first()
        return dict(
                id = result.id,
                customer_id = result.customer_id,
                time = result.time,
                date = result.date,
                num_of_persons = result.num_of_persons,
                status = result.status,
                created_on = result.created_on,
                restaurant = dict(
                    restaurant_id = result.restaurant.id,
                    restaurant_image = result.restaurant.restaurant_image,
                    restaurant_thumbnail = result.restaurant.restaurant_thumbnail,
                    restaurant_thumbnail2 = result.restaurant.restaurant_thumbnail2,
                    restaurant_name = result.restaurant.restaurant_name,
                    restaurant_type = result.restaurant.restaurant_type,
                    location = result.restaurant.location,
                    date_created = result.restaurant.date_created,
                    opening_day = result.restaurant.opening_day,
                    closing_day = result.restaurant.closing_day,
                    opening_time = result.restaurant.opening_time,
                    closing_time = result.restaurant.closing_time,
                    no_of_vacancies = result.restaurant.no_of_vacancies,
                    contact_number = result.restaurant.contact_number,
                    telephone_number = result.restaurant.telephone_number
                )
            )
    
    @staticmethod
    def get_my_reservation(current_user):
        results = [
            dict(
                id = reservation.id,
                customer_id = reservation.customer_id,
                time = reservation.time,
                date = reservation.date,
                num_of_persons = reservation.num_of_persons,
                status = reservation.status,
                created_on = reservation.created_on,
                restaurant = dict(
                    restaurant_id = restaurant.id,
                    restaurant_image = restaurant.restaurant_image,
                    restaurant_thumbnail = restaurant.restaurant_thumbnail,
                    restaurant_thumbnail2 = restaurant.restaurant_thumbnail2,
                    restaurant_name = restaurant.restaurant_name,
                    restaurant_type = restaurant.restaurant_type,
                    location = restaurant.location,
                    date_created = restaurant.date_created,
                    opening_day = restaurant.opening_day,
                    closing_day = restaurant.closing_day,
                    opening_time = restaurant.opening_time,
                    closing_time = restaurant.closing_time,
                    no_of_vacancies = restaurant.no_of_vacancies,
                    contact_number = restaurant.contact_number,
                    telephone_number = restaurant.telephone_number
                )
            )
            for reservation, restaurant in db.session.query(Reservation, Restaurant).join(Restaurant).filter(Reservation.customer_id == current_user.get('user_id')).all()
        ]
        return results
    
    @staticmethod
    def get_restaurant_bookings(current_user):
        reservations = [
            dict(
                reservation_id=reservation.id,
                time = reservation.time,
                date = reservation.date,
                num_of_persons = reservation.num_of_persons,
                status = reservation.status,
                created_on = reservation.created_on,
                customer_details = dict(
                    customer_id = user.id,
                    profile_image = user.profile_image,
                    profile_image2 = user.profile_image2,
                    email = user.email,
                    first_name = user.first_name,
                    last_name = user.last_name,
                    contact_number = user.contact_number
                )
            )
            for reservation, user in db.session.query(Reservation, User).join(User). \
                filter(Reservation.restaurant_owner_id == current_user.get('user_id')). \
                    filter(Reservation.status == "Pending"). \
                        all()
        ]
        return reservations
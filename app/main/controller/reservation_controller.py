from flask import request
from flask_restx import Resource

from app.main.util.dto import ReservationDto
from app.main.service.auth_helper import Auth as auth
from app.main.service.reservation_service import ReservationService as reservation
from app.main.util.decorator import custom_marshal_with, owner_token_required, token_required

api = ReservationDto.api

_create_reservation = ReservationDto.create_reservation
_get_reservation = ReservationDto.get_reservation
_get_customer_reservation = ReservationDto.get_customer_reservation
_update_reservation = ReservationDto.update_reservation
_decline_reservation = ReservationDto.decline_reservation

@api.route('/')
class ReservationList(Resource):
    @token_required
    @api.doc('create_reservation')
    @api.expect(_create_reservation, validate=True)
    @api.response(200, 'Reservation successfully created')
    @api.response(404, 'User does not exist')
    def post(self):
        """
        Create a reservation
        """
        current_user, status = auth.get_logged_in_user(request)
        return reservation.create_reservation(data=request.json, current_user=current_user.get('data'))
    
    @token_required
    @api.doc('get_reservation')
    @custom_marshal_with(_get_customer_reservation, name="Reservation")
    def get(self):
        """
        Get customer's reservations
        """
        current_user, status = auth.get_logged_in_user(request)
        return reservation.get_my_reservation(current_user=current_user.get('data'))

@api.route('/<id>')
@api.doc(params={'id': 'An ID'})
class Reservation(Resource):
    @token_required
    @api.doc('get_a_reservation')
    @custom_marshal_with(_get_customer_reservation, name="Reservation")
    def get(self, id):
        """
        Get a reservation
        """
        return reservation.get_reservation(reservation_id=id)
    
    @token_required
    @api.doc('update_reservation')
    @api.expect(_update_reservation, validate=True)
    @api.response(200, 'Reservation successfully updated')
    @api.response(404, 'Reservation does not exist')
    def put(self, id):
        """
        Update an existing reservation
        """
        return reservation.update_reservation(data=request.json, reservation_id=id)
    
    @token_required
    @api.doc('cancel_reservation')
    @api.response(200, 'Reservation successfully cancelled')
    @api.response(404, 'Reservation does not exist')
    def delete(self, id):
        """
        Cancel an existing reservation
        """
        return reservation.cancel_reservation(reservation_id=id)

# @api.route('/<reservation_id>')
# class CancelReservation(Resource):
#     @token_required
#     @api.doc('cancel_reservation')
#     @api.response(200, 'Reservation successfully cancelled')
#     @api.response(404, 'Reservation does not exist')
#     def delete(self, reservation_id):
#         """
#         Cancel an existing reservation
#         """
#         return reservation.cancel_reservation(reservation_id=reservation_id)

@api.route('/check/<restaurant_id>')
class CheckReservation(Resource):
    @api.doc('check_reservation')
    def get(self, restaurant_id):
        current_user, status = auth.get_logged_in_user(request)
        return reservation.has_already_booked(current_user.get('data'), restaurant_id=restaurant_id)
    
@api.route('/approve/<reservation_id>')
class ApproveReservation(Resource):
    @api.doc('approve_a_reservation')
    @owner_token_required
    def post(self, reservation_id):
        """
        Approve a pending reservation request
        """
        current_user, status = auth.get_logged_in_user(request)
        return reservation.accept_reservation(reservation_id, current_user.get('data'))

@api.route('/decline/<reservation_id>')
class ApproveReservation(Resource):
    @api.doc('decline_a_reservation')
    @api.expect(_decline_reservation, validate=True)
    @owner_token_required
    def post(self, reservation_id):
        """
        Decline a pending reservation request
        """
        current_user, status = auth.get_logged_in_user(request)
        return reservation.decline_reservation(request.json, reservation_id, current_user.get('data'))
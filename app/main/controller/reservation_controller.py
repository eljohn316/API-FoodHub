from flask import request, abort
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from app.main.service.reservation_service import create_reservation, edit_reservation, cancel_reservation, get_my_reservations
from app.main.util.decorator import customer_required, selective_marshal_with
from app.main.util.dto import ReservationDto
from ..util.custom_dto import ReservationDtoPublic

api = ReservationDto.api
_reservation = ReservationDto.reservation

@api.route('/create')
class CreateReservation(Resource):
    @api.doc('create_a_reservation')
    @customer_required
    def post(self):
        """ Create a reservation """
        data = request.json
        customer = Auth.get_logged_in_user(request)
        customer_id = customer[0]["data"]["user_id"]
        print(customer_id)
        return create_reservation(data=data, customer_id=customer_id)

@api.route('/<reservation_code>/')
class ReservationOperations(Resource):
    @api.doc('update_a_reservation')
    @customer_required
    def put(self, reservation_code):
        """ Update an existing reservation """
        data = request.json
        return edit_reservation(data=data, reservation_code=reservation_code)

    @api.doc('cancel_a_reservation')
    @customer_required
    def delete(self, reservation_code):
        """ Cancel a reservation """
        customer = Auth.get_logged_in_user(request)
        customer_id = customer[0]["data"]["user_id"]
        return cancel_reservation(reservation_code=reservation_code, customer_id=customer_id)

@api.route('/')
class GetReservation(Resource):
    @api.doc('get_a_reservation')
    @customer_required
    @selective_marshal_with(ReservationDtoPublic, name='Reservations')
    def get(self):
        """ Get currently logged in user's reservation """
        customer = Auth.get_logged_in_user(request)
        customer_id = customer[0]["data"]["user_id"]
        return get_my_reservations(customer_id)
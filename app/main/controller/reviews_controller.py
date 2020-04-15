from flask_restplus import Resource
from flask import request

from app.main.service.auth_helper import Auth
from app.main.service.reviews_service import create_review, get_all_reviews
from app.main.util.decorator import customer_required, selective_marshal_with

from ..util.dto import ReviewDto
from ..util.custom_dto import ReviewsDtoPublic

api = ReviewDto.api
_reviews = ReviewDto.reviews

@api.route('/create')
class CreateReview(Resource):
    @api.doc('create_a_review')
    @customer_required
    @api.expect(_reviews, validate=True)
    def post(self):
        """ Create a review """
        data = request.json
        author = Auth.get_logged_in_user(request)
        author_id = author[0]["data"]["user_id"]
        return create_review(data=data, author_id=author_id)

@api.route('/all')
class GetReviews(Resource):
    @api.doc('get_all_reviews')
    @customer_required
    @selective_marshal_with(ReviewsDtoPublic, name='Reviews')
    def get(self):
        """ Get all reviews """
        author = Auth.get_logged_in_user(request)
        author_id = author[0]["data"]["user_id"]
        return get_all_reviews(author_id)
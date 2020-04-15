import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.restaurant import Restaurant
from app.main.model.reviews import Reviews

def create_review(data, author_id):
    new_review = Reviews(
        star_rating = data['star_rating'],
        date = datetime.datetime.utcnow(),
        comment = data['comment'],
        reviewer = author_id,
        reviewed_restaurant = data['reviewed_restaurant']   
    )
    add(new_review)
    
    response_object = {
        'status':'success',
        'message':'Review successfully created'
    }
    return response_object, 201


def add(data):
    db.session.add(data)
    db.session.commit()

def get_all_reviews(author_id):
    return Reviews.query.filter_by(reviewer=author_id).first()
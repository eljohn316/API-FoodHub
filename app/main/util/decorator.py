from flask import request
from functools import wraps
from flask_restx import marshal_with

from app.main.service.auth_helper import Auth as auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status
        
        return f(*args, **kwargs)
    
    return decorated

def owner_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        user_role = token.get('user_role')

        if user_role != 'Owner':
            response_object = {
                'status': 'fail',
                'message': 'owner token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated

def customer_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        user_role = token.get('user_role')
        
        if user_role != 'Customer':
            response_object = {
                'status': 'fail',
                'message': 'customer token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated

def custom_marshal_with(fields_private, name):
    """
    Custom response marshalling
    """
    def decorated(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            
            func = marshal_with(fields_private, envelope=name)(f)
            return func(*args, **kwargs)
            
        return wrapper
    return decorated
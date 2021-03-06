from flask import request
from flask_restx import marshal_with
from functools import wraps

from app.main.service.auth_helper import Auth

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status
        
        return f(*args, **kwargs)
    return decorated

def owner_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token or token.get('user_type') != 'Owner':
            response_object = {
                'status':'fail',
                'message': 'Owner token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated

def customer_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token or token.get('user_type') != 'Customer':
            response_object = {
                'status':'fail',
                'message': 'Customer token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated

def selective_marshal_with(fields_private, name):
    """
    Selective response marshalling
    """
    def decorated(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            
            func = marshal_with(fields_private, envelope=name)(f)
            return func(*args, **kwargs)
            
        return wrapper
    return decorated

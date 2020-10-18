from flask_restx import Model, fields

UserDtoPublic = Model('user', {
  'full_name': fields.String(),
  'contact_number': fields.String(),
  'account': {
    'public_id':fields.String(),
    'email': fields.String(),
    'registered_on': fields.DateTime(dt_format='rfc822'),
  }
})

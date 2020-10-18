import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.getenv('SECRET_KEY','foodhub_secret_key')
  DEBUG = False

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/foodhub_db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
  DEBUG = True
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/foodhub_db'
  PRESERVE_CONTEXT_ON_EXCEPTION = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  DEBUG = False
  #uncomment the line to use postgres
  #SQLALCHEMY_DATABASE_URI = 'postgresql://foodhub:password@localhost/foodhub'

config_by_name = dict(
  dev=DevelopmentConfig,
  test=TestingConfig,
  prod=ProductionConfig
)

key = Config.SECRET_KEY

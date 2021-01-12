import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.getenv('SECRET_KEY','foodhub_secret_key')
  DEBUG = False

class DevelopmentConfig(Config):
  DEBUG = True
  # SQLALCHEMY_DATABASE_URI = 'postgres://rijaffxxqcprkb:00229ec11c6ddb945032ccdb6a3e80b0e16fc772582b346e651f6d2075b5b496@ec2-54-146-4-66.compute-1.amazonaws.com:5432/dac0g3or5iltdp'
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/foodhub_2'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
  DEBUG = True
  TESTING = True
  # SQLALCHEMY_DATABASE_URI = 'postgres://rijaffxxqcprkb:00229ec11c6ddb945032ccdb6a3e80b0e16fc772582b346e651f6d2075b5b496@ec2-54-146-4-66.compute-1.amazonaws.com:5432/dac0g3or5iltdp'
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/foodhub_2'
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

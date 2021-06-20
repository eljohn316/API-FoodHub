import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my-precious-secret-key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'development.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:051098@localhost:5432/foodhub_development_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:051098@localhost:5432/foodhub_development_db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://nnznxlqiiahjvl:16f6e383e355f2a41197d43f35f710bfaf6203405ed78558b4209fec4de1b04c@ec2-34-202-54-225.compute-1.amazonaws.com:5432/dc9gvv2q7q3cr5'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
import os
import logging
from flask_compress import Compress
from flask_security import Security, SQLAlchemyUserDatastore
from bookshelf.data.models import db, Role, User

c
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'sqlite://' 

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Temp/bookshelf.db' 

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://' 

config = {
    "development": "bookshelf.config.DevelopmentConfig",
    "testing": "bookshelf.config.TestingConfig",
    "default": "bookshelf.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name]) # object-based default configuration
    app.config.from_pyfile('config.cfg', silent=True) # instance-folders configuration


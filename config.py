import os

class Config(object):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://postgres:root@localhost/login_module"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(object):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://postgres:root@localhost/login_module"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

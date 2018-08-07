import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'postgresql://postgres:@localhost/stream'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='stream'
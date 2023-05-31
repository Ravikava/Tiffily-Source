import logging
import os
import datetime
from dotenv import load_dotenv

# Get the .env variables
load_dotenv()

# Enable modification track
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Jsonify config
JSON_SORT_KEYS = False

# JWT configuration
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_TOKEN_LOCATION = ['headers']
JWT_IDENTITY_CLAIM = 'user_id'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'brief',
            'level': logging.DEBUG,
            'stream': 'ext://sys.stdout'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': logging.DEBUG,
    }
}

# PROFILE_SERVICE_DATABASE = {
#     'host': os.getenv('PROFILE_SERVICE_DB_HOST'),
#     'user': os.getenv('PROFILE_SERVICE_DB_USER'),
#     'password': os.getenv('PROFILE_SERVICE_DB_PASSWORD'),
#     'database': os.getenv('PROFILE_SERVICE_DB_NAME')
# }
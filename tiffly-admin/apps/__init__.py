from flask import Flask,jsonify
import logging
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from flask_migrate import Migrate
from logging.config import dictConfig
from sys import exit
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from flask_jwt_extended import JWTManager
from config import config
from flask_caching import Cache
# from flask_cors import CORS
import os


app = Flask(__name__,template_folder=os.getcwd() + '/templates')
app.config.from_object('config.config')

# Add prefix
app.wsgi_app = DispatcherMiddleware(NotFound(), {'/api': app.wsgi_app})

# Initializing the logger
dictConfig(app.config['LOGGING'])
logger = logging.getLogger()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# CORS(app)


app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_timeout': 1800,
    'pool_pre_ping': True
}
db = SQLAlchemy(app)

migrate = Migrate(compare_type=True)
migrate = migrate.init_app(app, db)

jwt = JWTManager(app)

# @app.route('/health-check/')
# def hello_():
#     """
#     Add health check route
#     """
#     return jsonify({
#         'status': 'Fool'
#     })


from apps.database import models

from apps.api.users import routes
from apps.api.restaurants import routes
from apps.api.market_place import routes
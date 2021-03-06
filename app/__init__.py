from flask import Flask 
from  flask_restful import Api

from instance.config import app_config

def create_app(config_name="development"):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_pyfile('config.py')
	from .api.v1 import version1 as v1
	app.register_blueprint(v1)

	return app

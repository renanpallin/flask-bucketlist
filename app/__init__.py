from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from flask import request

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Bucketlist

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/bucketlists/')
    def bucketlists():
        return Bucketlist.get_all()

    @app.route('/bucketlists/', methods=['POST'])
    def bucketlists_post():
        data = request.get_json()
        b = Bucketlist(data.get('name'))

        print(b)
        return {'aa': 123}

    return app
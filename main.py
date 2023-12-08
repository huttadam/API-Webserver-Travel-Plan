from flask import Flask, jsonify
from init import db, ma, jwt, bcrypt
from os import environ
from blueprints.cli_bp import bp_DBCli
from blueprints.auth_bp import bp_users
from blueprints.trips_bp import bp_trips
from blueprints.destinations_bp import bp_destinations
from blueprints.activities_bp import bp_activities
from blueprints.comments_bp import bp_comments
from sqlalchemy.exc import IntegrityError

def run_app():

    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')


    @app.route("/")
    def hello_world():
        return "Hello, World!"

    # @app.errorhandler(401)
    # def unauthorized(err):
    #     return {'error': 'You are not authorized to access this resource'}

    # @app.errorhandler(IntegrityError)
    # def integrity_error(err):
    #     return {'Error': "This entry already exists in database"}, 400


    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(bp_comments)
    app.register_blueprint(bp_DBCli)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_trips)
    app.register_blueprint(bp_destinations)
    app.register_blueprint(bp_activities)

    return app


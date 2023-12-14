from flask import Flask, jsonify
from init import db, ma, jwt, bcrypt
from os import environ
from blueprints.cli_bp import bp_DBCli
from blueprints.auth_bp import bp_users
from blueprints.trips_bp import bp_trips
from blueprints.destinations_bp import bp_destinations
from blueprints.activities_bp import bp_activities
from blueprints.comments_bp import bp_comments
from sqlalchemy.exc import IntegrityError, DataError
from marshmallow.exceptions import ValidationError
from sqlalchemy.orm.exc import NoResultFound

def run_app():

    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')

    @app.errorhandler(400)
    def bad_request(err):
        return {'Error': str(err)}, 400

    @app.errorhandler(401)
    def unauthorized(err):
        return {'Error': 'You are not authorized to access this information'},401

    @app.errorhandler(IntegrityError)
    def integrity_error(err):
        return {'Error': "Integrity Error, please check inputs and not already created" }, 409

    # @app.errorhandler(ValidationError)
    # def validation_error(err):
    #     return {'Error': err.__dict__['messages']}, 403

    @app.errorhandler(NoResultFound)
    def no_result_found(err):
        return {'Error': "No Result for this reference, please check again."},400

    @app.errorhandler(DataError)
    def data_error(err):
        return {'Error': "Data formatted incorrectly, please check"}, 400

    @app.errorhandler(404)
    def page_not_found(err):
        return {'Error': "Page not found, please try again"}, 404

    @app.errorhandler(405)
    def method_not_allowed(err):
        return {'Error': str(err)}, 405

    @app.errorhandler(KeyError)
    def key_error(err):
        return {'Error': f'The field {err} is required.'}, 400








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
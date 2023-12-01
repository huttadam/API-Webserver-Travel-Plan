from flask import Flask, jsonify
from init import db, ma, jwt, bcrypt
from os import environ
from blueprints.cli_bp import dbcli_bp

def run_app():

    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')


    @app.route("/")
    def hello_world():
        return "Hello, World!"

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': 'You are not authorized to access this resource'}

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)


    app.register_blueprint(dbcli_bp)

    return app


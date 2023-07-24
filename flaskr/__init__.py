# Application Factory
import os
from flask import Flask
from . import db

def create_app(test_config=None): #application factory function
    # create and configure the application
    # creates the Flask instance.the configuration files are relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        #the path where the SQLite database file will be saved
        DATABASE= os.path.join(app.instance_path,'flaskr.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    db.init_app(app)

    return app

# to run the app: flask --app flaskr --debug
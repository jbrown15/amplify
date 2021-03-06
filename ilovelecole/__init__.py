from flask import Flask

from ilovelecole.blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True, static_folder='static/')

    # app.config.from_object('config.settings')
    # app.config.from_pyfile('settings.py', silent=True)
    from ilovelecole.blueprints.page import page
    app.register_blueprint(page, url_prefix='/')

    return app



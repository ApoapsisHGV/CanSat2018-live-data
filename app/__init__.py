from config import RunConfig

import flask

import psycopg2


app = flask.Flask(__name__)


def create_app(config_class=RunConfig):
    app.config.from_object(config_class)
    conn = psycopg2.connect(
        database=app.config["URL"].path[1:],
        user=app.config["URL"].username,
        password=app.config["URL"].password,
        host=app.config["URL"].hostname,
        port=app.config["URL"].port,
    )
    conn.autocommit = True
    app.config["CUR"] = conn.cursor()

    from app.data import bp as data_bp
    app.register_blueprint(data_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return "Hello, welcome to the live data API servers of ApoapsisHGV"

    return app

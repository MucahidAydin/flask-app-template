import os
import logging
from config import Config
import traceback
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from app.utils.access_control import access_control
from app.models import BaseResponse
from app.extensions import make_celery  # , db, jwt

logging.basicConfig(level=logging.INFO)


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    app.app_context().push()

    # db.init_app(app)
    # jwt.init_app(app)

    celery = make_celery(app)

    for key, value in app.config.items():
        if not key.startswith("_"):
            os.environ[key] = str(value)

    from app.weather_forecasts import bp as weather_forecasts_bp

    app.register_blueprint(weather_forecasts_bp, url_prefix="/api/v1/weather-forecasts")

    @app.errorhandler(Exception)
    def handle_exception(e):
        """
        Global error handler for unhandled exceptions.
        """
        # Default response
        response = {"error": "An unexpected error occurred.", "status": 500}

        app.logger.error(f"Exception: {e}")
        app.logger.error(
            "".join(traceback.format_exception(type(e), e, e.__traceback__))
        )

        # Handle HTTPExceptions separately
        if isinstance(e, HTTPException):
            response["error"] = e.description
            response["status"] = e.code
        else:
            if app.config["DEBUG"]:
                response["traceback"] = "".join(
                    traceback.format_exception(type(e), e, e.__traceback__)
                )
            response["error"] = str(e)

        return jsonify(response), response["status"]

    @app.before_request
    def before_request():
        access_data = access_control(request)

        if isinstance(access_data, BaseResponse):
            return jsonify(access_data.to_dict()), access_data.status_code

    @app.after_request
    def after_request(response):
        status_code = response.status_code
        if status_code in [500, 502]:
            logging.error(f"Response: {status_code} {response.data}")
            response.status_code = 500
            response.data = jsonify({"message": "Internal server error"}).data
            response.content_type = "application/json"

        if status_code in [429]:
            logging.error(f"Response: {status_code} {response.data}")
            response.status_code = 429
            response.data = jsonify({"message": "Too many requests"}).data
            response.content_type = "application/json"

        return response

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"status": "ok"})

    return app, celery

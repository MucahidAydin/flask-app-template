from flask import Blueprint

bp = Blueprint("weather_forecasts", __name__)

from app.weather_forecasts import routes

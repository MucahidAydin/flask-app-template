from flask import jsonify, request, redirect, url_for
from app.weather_forecasts import bp
from app.models import BaseResponse
from app.utils.schemas import validate_schema_for_get, WeatherForecastSchema


@bp.route("", methods=["GET"])
def index():
    return redirect(url_for("weather_forecasts.current_weather"))


@bp.route("current", methods=["GET"])
@validate_schema_for_get(WeatherForecastSchema())
def current_weather():
    city = request.args.get("city")

    response = BaseResponse(
        data={"temperature": "20°C", "condition": "Partly cloudy"},
        message=f"Current weather in {city}",
        status_code=200,
    )
    return jsonify(response.to_dict()), response.status_code

import os
import logging
from app.models import BaseResponse


def access_control(request):

    public_endpoints = {
        "weather_forecasts.index",
        "weather_forecasts.current_weather",
    }

    if request.endpoint in public_endpoints:
        logging.info((f"user agent: {request.user_agent}"))

    else:
        return BaseResponse(status_code=404, message="access denied")
    return None

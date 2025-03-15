from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError


def validate_schema_for_post(schema):
    """Validate the schema of the request data"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.json)
                return func(*args, **kwargs)
            except ValidationError as err:
                return jsonify(err.messages), 400

        return wrapper

    return decorator

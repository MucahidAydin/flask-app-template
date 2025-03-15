from marshmallow import Schema, fields, ValidationError


class WeatherForecastSchema(Schema):
    city = fields.String(required=True)

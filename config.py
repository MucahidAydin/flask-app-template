import os
import urllib.parse
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(24)

    # postgresql_password = urllib.parse.quote_plus("password")
    # SQLALCHEMY_DATABASE_URI = (
    #     f"postgresql://postgres:{postgresql_password}@db:5432/test"
    # )

    _CELERY_CONFIG = {
        "timezone": "UTC",
        "imports": ("app.workers.tasks",),
        "result_expires": 3600,
    }

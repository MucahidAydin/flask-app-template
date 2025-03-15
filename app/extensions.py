import os
import logging
from celery import Celery
from flask import Flask, jsonify, request
# from flask_jwt_extended import JWTManager
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
# jwt = JWTManager()

def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config["_CELERY_CONFIG"])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

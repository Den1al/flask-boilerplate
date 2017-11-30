from flask import current_app
import time
from datetime import datetime
from uuid import uuid4
import requests


def timestamp() -> int:
    """ converts the current time to ms timestamp """
    return int(round(time.time() * 1000))


def get_date():
    """ gets current date """
    return datetime.now()


def guid():
    """ returns a GUID """
    return str(uuid4().hex)


def validate_captcha(response):
    """validates with google recpatcha the reponse"""
    secret = current_app.config.get('RECAPTCHA_SECRET_KEY')

    return requests.post('https://www.google.com/recaptcha/api/siteverify',
                         data={
                             'secret': secret,
                             'response': response
                         }).json().get('success')

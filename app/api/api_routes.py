from flask import jsonify
from flask_login import login_required
from . import api
from ..utils import timestamp


@api.route('/now')
@login_required
def get_current_time():
    """ Get Current Time """
    return jsonify(results='success', time=timestamp())

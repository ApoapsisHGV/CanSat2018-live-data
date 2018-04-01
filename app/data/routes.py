from app.data import bp
from flask import request

@bp.route("/data.html")
def data_provider():
    return ""

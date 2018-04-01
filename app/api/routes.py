from app.api import bp
from flask import request, jsonify

@bp.route("/dust_api", methods=["POST"])
def dust_api():
    sensor_values = request.get_json()["sensordatavalues"]
    print(sensor_values)
    return ""

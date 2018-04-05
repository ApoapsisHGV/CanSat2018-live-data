from app.data import bp
from app.sql import get_highest_density, get_latest_density, get_lowest_density

from flask import jsonify


@bp.route("/data")
def data_provider():
    return jsonify({"latest": get_latest_density(),
                    "highest": get_highest_density(),
                    "lowest": get_lowest_density()})

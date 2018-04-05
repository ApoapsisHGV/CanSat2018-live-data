from app.data import bp
from app.sql import get_highest_density, get_latest_density, get_lowest_density

from flask import jsonify


@bp.route("/data")
def data_provider():
    latest = get_latest_density()
    highest = get_highest_density()
    lowest = get_lowest_density()
    latest = {"dustPerVolume": latest[0], "measureDate": latest[1]}
    highest = {"dustPerVolume": highest[0], "measureDate": highest[1]}
    lowest = {"dustPerVolume": lowest[0], "measureDate": lowest[1]}
    return jsonify({"latest": latest,
                    "highest": highest,
                    "lowest": lowest})

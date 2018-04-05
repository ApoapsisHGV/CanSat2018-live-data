import datetime

from app.api import bp
from app.sql import (
                     get_highest_density, get_lowest_density,
                     set_highest_density, set_latest_density,
                     set_lowest_density
                     )


from flask import request


@bp.route("/dust_api", methods=["POST"])
def dust_api():
    sensor_values = request.get_json()["sensordatavalues"]
    print(sensor_values)
    dust_average = (float(sensor_values[0]["value"]) +
                    float(sensor_values[1]["value"])) / 2

    print(get_lowest_density())
    print(get_highest_density())
    if dust_average > get_highest_density()[0]:
        set_highest_density(dust_average, datetime.datetime.now())
    elif dust_average < get_lowest_density()[0]:
        set_lowest_density(dust_average, datetime.datetime.now())

    set_latest_density(dust_average, datetime.datetime.now())
    return "ok"


@bp.route("/dust_api", methods=["GET"])
def dust_api_get():
    return "dust_api"

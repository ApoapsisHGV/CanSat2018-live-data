from app import app


def get_highest_density():
    app.config["CUR"].execute("SELECT value, date FROM sensordata WHERE ID=1;")
    return app.config["CUR"].fetchall()[0]


def get_lowest_density():
    app.config["CUR"].execute("SELECT value, date FROM sensordata WHERE ID=2;")
    return app.config["CUR"].fetchall()[0]


def get_latest_density():
    app.config["CUR"].execute("SELECT value FROM sensordata WHERE ID=3;")
    return app.config["CUR"].fetchall()[0]


def set_highest_density(value, date):
    app.config["CUR"].execute(("UPDATE sensordata SET value=%s, date=%s"
                               "WHERE ID=1;"), (value, date,))


def set_lowest_density(value, date):
    app.config["CUR"].execute(("UPDATE sensordata SET value=%s, date=%s"
                               "WHERE ID=2;"), (value, date,))


def set_latest_density(value, date):
    app.config["CUR"].execute(("UPDATE sensordata SET value=%s, date=%s"
                               "WHERE ID=3;"), (value, date,))

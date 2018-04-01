import os
from urllib import parse

class Config:
    UNITTEST = False

class RunConfig(Config):
    URL = ""
    try:
        URL = parse.urlparse(os.environ["DATABASE_URL"])
    except:
        print("config var not in env")

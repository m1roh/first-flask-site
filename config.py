import os

SECRET_KEY = "NlArl(BRZydZocL)ay`,Y7)*"

FB_APP_ID = 457179715088100

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")

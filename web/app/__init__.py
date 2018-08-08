from flask_migrate import Migrate
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import timedelta as TimeDelta

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

window_start = datetime.datetime(2017, 10, 26, hour=16, minute=40, second=0, microsecond=0)
window_end = window_start + TimeDelta(minutes=5)

from app import routes, models
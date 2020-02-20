from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config.from_object(Config)

bootstrap = Bootstrap(app)
from app import routes, models

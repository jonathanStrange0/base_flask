from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app = Flask(__name__)
app.config.from_object(Configon)

bootstrap = Bootstrap(app)
from app import routes, models

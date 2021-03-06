from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# Initialization
# Create an application instance (an object of class Flask)  which handles all requests.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_all()
db.session.commit()

# login_manager needs to be initiated before running the app
login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap(app)

# Added at the bottom to avoid circular dependencies. (Altough it violates PEP8 standards)
from app import classes
from app import routes

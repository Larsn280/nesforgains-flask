from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# Load configuration
app.config.from_object('app.config.Config')

# Initialize PyMongo
mongo = PyMongo(app)

# Import routes
from app import routes

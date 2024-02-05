from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@localhost/TODO'  
db = SQLAlchemy(app)

from app.services.todo_service import TodoService
todo_service = TodoService()

from app.controllers.todo_controller import *
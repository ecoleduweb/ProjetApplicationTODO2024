from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@localhost/TODO'  
db = SQLAlchemy(app)

from app.services.todo_service import TodoService
todo_service = TodoService()

from app.controllers.todo_controller import *
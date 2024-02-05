from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.API.app.services.todo_service import TodoService
# from backend.API.app.controllers.todo_controller import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@localhost/TODO'  
db = SQLAlchemy(app)

app.route('/addTodo', methods=['POST'])

todo_service = TodoService()

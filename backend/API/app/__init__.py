from flask import Flask
from app.services.todo_service import TodoService

app = Flask(__name__)
todo_service = TodoService()
from app.controllers.todo_controller import *

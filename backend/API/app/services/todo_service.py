from app.models import Todo
from app import db

class TodoService:
    def get_all_todos(self):
        return Todo.query.all()

    def get_todo_by_id(self, todo_id):
        return db.session.get(Todo, todo_id)

    def add_todo(self, todo_data):
        new_todo = Todo(**todo_data)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo

    def delete_todo(self, todo_id):
        todo = db.session.get(Todo, todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return todo
        return None

    def update_todo(self, todo_data):
        todo_id = todo_data.get('id')
        todo = db.session.get(Todo, todo_id)
        if todo:
            todo.task = todo_data.get('task', todo.task)
            todo.completed = todo_data.get('completed', todo.completed)
            db.session.commit()
            return todo
        return None

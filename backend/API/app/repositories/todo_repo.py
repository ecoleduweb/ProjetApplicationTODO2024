from app import db
from app.models import Todo

class TodoRepository:
    def get_all_todos(self):
        return Todo.query.all()

    def add_todo(self, task, completed=False):
        new_todo = Todo(task=task, completed=completed)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo

    def get_todo_by_id(self, todo_id):
        return Todo.query.get(todo_id)

    def delete_todo(self, todo):
        db.session.delete(todo)
        db.session.commit()

    def update_todo(self, todo, task=None, completed=None):
        if task is not None:
            todo.task = task
        if completed is not None:
            todo.completed = completed
        db.session.commit()
        return todo

from app import db
from app.models import Todo

class TodoService:
    def getAllTodos(self):
        todos = Todo.query.all()
        return todos
    
    def addTodo(self, todo):
        new_todo = Todo(task=todo['task'], completed=0)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo

    def deleteTodo(self, todo_id):
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return todo
            
    def updateTodo(self, todo):
        oldtodo = Todo.query.get(todo['id'])
        if oldtodo:
            oldtodo.task = todo.get('task', oldtodo.task)
            oldtodo.completed = todo.get('completed', oldtodo.completed)
            db.session.commit()
            return oldtodo  # Return the updated todo object




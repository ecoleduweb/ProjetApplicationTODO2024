from app.repositories.todo_repo import TodoRepository

class TodoService:
    def __init__(self):
        self.todo_repo = TodoRepository()

    def get_all_todos(self):
        return self.todo_repo.get_all_todos()

    def add_todo(self, todo):
        return self.todo_repo.add_todo(todo['task'], completed=0)

    def delete_todo(self, todo_id):
        todo = self.todo_repo.get_todo_by_id(todo_id)
        if todo:
            self.todo_repo.delete_todo(todo)
            return todo

    def update_todo(self, todo):
        old_todo = self.todo_repo.get_todo_by_id(todo['id'])
        if old_todo:
            return self.todo_repo.update_todo(old_todo, task=todo.get('task'), completed=todo.get('completed'))

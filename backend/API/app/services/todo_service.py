class TodoService:
    def __init__(self):

        self.todos = [
            {'id': 1, 'name': 'Todo 1'},
            {'id': 2, 'name': 'Todo 2'},
            {'id': 3, 'name': 'Todo 3'},
            {'id': 4, 'name': 'Todo 4'},
        ]
    
    def getAllTodos(self):
        return self.todos
    
    def addTodo(self, todo):
        todo['id'] = len(self.todos) + 1
        self.todos.append(todo)
        return todo

    def deleteTodo(self, todo_id):
        for todo in self.todos:
            if todo['id'] == todo_id:
                self.todos.remove(todo)
                return todo
            
    def updateTodo(self, todo_id, new_name):
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['name'] = new_name
                return todo


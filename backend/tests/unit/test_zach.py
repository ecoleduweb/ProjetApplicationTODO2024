from backend.API.app.services.todo_service import TodoService

def test_getAllTodos():
    todo_service = TodoService()
    todos = todo_service.getAllTodos()
    assert len(todos) == 4
    assert todos[0]['name'] == 'Todo 1'
    assert todos[1]['name'] == 'Todo 2'
    assert todos[2]['name'] == 'Todo 3'
    assert todos[3]['name'] == 'Todo 4'
    
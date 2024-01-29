def test_getAllTodos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'name': 'Todo 1'},
        {'id': 2, 'name': 'Todo 2'},
        {'id': 3, 'name': 'Todo 3'},
        {'id': 4, 'name': 'Todo 4'},
    ]
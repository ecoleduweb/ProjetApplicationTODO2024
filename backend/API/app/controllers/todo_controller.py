from flask import jsonify, request
from app import app, todo_service

@app.route('/addTodo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    new_todo = todo_service.add_todo(todo)
    todo_dict = {'id': new_todo.id, 'task': new_todo.task, 'completed': new_todo.completed}
    return jsonify({'message': 'Todo ajouté', 'todo': todo_dict})

@app.route('/deleteTodo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    deleted_todo = todo_service.delete_todo(todo_id)
    return jsonify({'message': f'Todo avec ID {todo_id} supprimé'}) if deleted_todo else jsonify({'message': f'Todo avec ID {todo_id} non trouvé'})

@app.route('/updateTodo', methods=['POST'])
def update_todo():
    todo = request.get_json()
    updated_todo = todo_service.update_todo(todo)
    todo_dict = {'id': updated_todo.id, 'task': updated_todo.task, 'completed': updated_todo.completed}
    return jsonify({'message': f'Todo avec ID {todo["id"]} mis à jour', 'todo': todo_dict}) if updated_todo else jsonify({'message': f'Todo avec ID {todo["id"]} non trouvé'})

@app.route('/getAllTodos', methods=['GET'])
def get_all_todos():
    todos = todo_service.get_all_todos()
    todos_dict = [{'id': todo.id, 'task': todo.task, 'completed': todo.completed} for todo in todos]
    return jsonify({'todos': todos_dict})

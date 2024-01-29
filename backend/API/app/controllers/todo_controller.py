from flask import jsonify, request
from app import app, todo_service


# Route pour ajouter un todo
@app.route('/addTodo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    new_todo = todo_service.addTodo(todo)
    todo_dict = {'id': new_todo.id, 'task': new_todo.task, 'completed': new_todo.completed}
    return jsonify({'message': 'Todo ajouté', 'todo': todo_dict})

# Route pour supprimer un todo par son ID
@app.route('/deleteTodo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    deletedTodo = todo_service.deleteTodo(todo_id)
    # todos_dict = {'id': deletedTodo.id, 'task': deletedTodo.task, 'completed': deletedTodo.completed}
    return jsonify({'message': f'Todo avec ID {todo_id} supprimé'}) if deletedTodo else jsonify({'message': f'Todo avec ID {todo_id} non trouvé'})

# Route pour mettre à jour le nom d'un todo par son ID
@app.route('/updateTodo', methods=['POST'])
def update_todo():
    todo = request.get_json()
    updatedTodo = todo_service.updateTodo(todo)
    todo_dict = {'id': updatedTodo.id, 'task': updatedTodo.task, 'completed': updatedTodo.completed}
    return jsonify({'message': f'Todo avec ID {todo['id']} mis à jour', 'todo': todo_dict}) if updatedTodo else jsonify({'message': f'Todo avec ID {todo['id']} non trouvé'})

# Route pour obtenir tous les todos
@app.route('/getAllTodos', methods=['GET'])
def get_all_todos():
    todos = todo_service.getAllTodos()
    todos_dict = [{'id': todo.id, 'task': todo.task, 'completed': todo.completed} for todo in todos]
    return jsonify({'todos': todos_dict})
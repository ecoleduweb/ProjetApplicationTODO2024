from flask import jsonify, request
from app import app, todo_service


# Route pour ajouter un todo
@app.route('/addTodo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    new_todo = todo_service.addTodo(todo)
    return jsonify({'message': 'Todo ajouté', 'todo': new_todo})

# Route pour supprimer un todo par son ID
@app.route('/deleteTodo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    deletedTodo = todo_service.deleteTodo(todo_id)
    return jsonify({'message': f'Todo avec ID {todo_id} supprimé'}) if deletedTodo else jsonify({'message': f'Todo avec ID {todo_id} non trouvé'})

# Route pour mettre à jour le nom d'un todo par son ID
@app.route('/updateTodo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = request.get_json()
    updatedTodo = todo_service.updateTodo(todo_id, todo['name'])
    return jsonify({'message': f'Todo avec ID {todo_id} mis à jour', 'todo': updatedTodo}) if updatedTodo else jsonify({'message': f'Todo avec ID {todo_id} non trouvé'})

# Route pour obtenir tous les todos
@app.route('/getAllTodos', methods=['GET'])
def get_all_todos():
    todos = todo_service.getAllTodos()
    return jsonify({'todos': todos})
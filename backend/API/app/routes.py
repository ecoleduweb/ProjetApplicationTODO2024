from flask import jsonify, request
from app import app


items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'},
    {'id': 4, 'name': 'Item 4'},
]

# Route pour ajouter un nouvel item
@app.route('/addItem', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = {'id': len(items) + 1, 'name': data['name']}
    items.append(new_item)
    return jsonify({'message': 'Item added successfully', 'item': new_item})

# Route pour supprimer un item par son ID
@app.route('/deleteItem/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': f'Item with ID {item_id} deleted successfully'})

# Route pour mettre à jour le nom d'un item par son ID
@app.route('/updateItem/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item['name'] = data['name']
            return jsonify({'message': f'Item with ID {item_id} updated successfully', 'item': item})
    return jsonify({'error': f'Item with ID {item_id} not found'})

# Route pour obtenir tous les items
@app.route('/getAllItems', methods=['GET'])
def get_all_items():
    return jsonify({'items': items})

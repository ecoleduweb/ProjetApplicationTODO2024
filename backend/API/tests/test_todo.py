import os
import unittest
from flask_testing import TestCase
from pathlib import Path
import sys
from dotenv import load_dotenv

load_dotenv()

current_file = Path(__file__).resolve()
parent_directory = current_file.parent
project_directory = parent_directory.parent

sys.path.append(str(project_directory))

from app import app, db
from app.services.todo_service import TodoService
todo_service = TodoService()
from app.models import Todo

class BaseTestCase(TestCase):
    def create_app(self):
        app.config['TEST'] = "true"
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("mysql://root:admin@144.126.220.39/todotest")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def add_test_todo_to_db(self):
        with self.app.app_context():
            todo = Todo(task='Test Task')
            db.session.add(todo)
            db.session.commit()
            return todo.id

class TestTodoService(BaseTestCase):
    def test_get_all_todos(self):
        with self.app.app_context():
            todos = todo_service.get_all_todos()
            self.assertEqual(len(todos), 0)

    def test_add_todo(self):
        with self.app.app_context():
            todo = {'task': 'Test Task'}
            new_todo = todo_service.add_todo(todo)
            self.assertIsNotNone(new_todo.id)
            self.assertEqual(new_todo.task, 'Test Task')
            self.assertFalse(new_todo.completed)

    def test_delete_todo(self):
        with self.app.app_context():
            todo = {'task': 'Test Task'}
            new_todo = todo_service.add_todo(todo)
            deleted_todo = todo_service.delete_todo(new_todo.id)
            self.assertEqual(deleted_todo.id, new_todo.id)

    def test_update_todo(self):
        with self.app.app_context():
            todo = {'task': 'Test Task'}
            new_todo = todo_service.add_todo(todo)
            updated_todo_data = {'id': new_todo.id, 'task': 'Updated Task', 'completed': True}
            updated_todo = todo_service.update_todo(updated_todo_data)
            self.assertEqual(updated_todo.task, 'Updated Task')
            self.assertTrue(updated_todo.completed)

class TestTodoController(BaseTestCase):
    def test_add_todo_route(self):
        data = {'task': 'Test Task'}
        response = self.client.post('/addTodo', json=data)
        result = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'], 'Todo ajouté')
        self.assertIn('todo', result)

    def test_delete_todo_route(self):
        todo_id = self.add_test_todo_to_db()
        response = self.client.delete(f'/deleteTodo/{todo_id}')
        result = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'Todo avec ID {todo_id} supprimé', result['message'])

    def test_update_todo_route(self):
        todo_id = self.add_test_todo_to_db()
        data = {'id': todo_id, 'task': 'Updated Task', 'completed': True}
        response = self.client.post('/updateTodo', json=data)
        result = response.json
        self.assertEqual(response.status_code, 200)
        if 'todo' in result:
            self.assertIn(f'Todo avec ID {todo_id} mis à jour', result['message'])
            self.assertIn('todo', result)
        else:
            self.fail(f'La mise à jour du todo avec ID {todo_id} a échoué.')


    def test_get_all_todos_route(self):
        response = self.client.get('/getAllTodos')
        result = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('todos', result)

if __name__ == '__main__':
    unittest.main()

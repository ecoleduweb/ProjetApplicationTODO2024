from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pymysql

pymysql.install_as_MySQLdb()
load_dotenv()

app = Flask(__name__)

if app.config.get('TEST') == "true":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_TEST_URL')
    db = SQLAlchemy(app)
    print("Running in test mode.")

    # Exécutez les tests uniquement si la variable d'environnement TEST est définie à "true"
    print('Running tests...')
    import pytest
    pytest.main(['tests/'])
    print('Tests finished. Exiting.')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_DEV_URL')
    db = SQLAlchemy(app)
    print("Running in development mode.")



from app.controllers.todo_controller import *

# API

## Developing

### Prerequisites
```bash
pip install flask
```
#### For the database
```bash
pip install Flask-SQLAlchemy
pip install mariadb
pip install pymysql
```

### Setting up the database
Créer la base de données et la table TODO.
Créer un utilisateur qui à les droits sur la base de données.

Modifier le fichier __init__.py (ligne 5) pour changer les informations de connexion à la base de données. 

```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://utilisateur:motdepasse@localhost/basededonnees'
# Change utilisateur, motdepasse et basededonnees selon votre configuration
```

### Starting the server
```bash
flask run
```

# API

## Developing

### Prerequisites
```bash
pip install flask
pip install Flask-SQLAlchemy
pip install mariadb
pip install pymysql
```

### Setting up the database
Créer la base de données avec ce script:
```sql
CREATE DATABASE todo;
USE todo;
CREATE TABLE todo (
    id int not null auto_increment,
    task varchar(255) ,
    completed boolean ,
    primary key (id)
);
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON todo.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

### Starting the server
```bash
flask run
```

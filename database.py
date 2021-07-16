from main import parser, skeleton_db
import os


'''
To create a table in the database you need to create a class. 

If you already has a models file in your Flask app, you can just copy/paste ithere.

Follow this example from Flask-SQLAlchemy documentation


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


Flask-SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/en/2.x
'''
def read():
    pass

def update():
    pass

def delete():
    pass

def create_db():
    if os.path.exists('./db.sqlite3') == False:
        skeleton_db.create_all() 

create_db()

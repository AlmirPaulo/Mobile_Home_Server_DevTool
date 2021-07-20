from main import parser, skeleton_db, args
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
#CLI Commands
parser.add_argument('-r', '--read', type=str, help='Read all database')
parser.add_argument('-q', '--query', type=str, help='Query some specific data in the database')
parser.add_argument('-u', '--update', type=str, help='Updates the database')
parser.add_argument('-d','--delete', type=str, help='Delete some data from the database')

#CRUD Functions
def read(table):
   return table.query.all()

def query():
    pass

def update():
    skeleton_db.session.add()
    skeleton_db.session.commit()

def delete():
    

#CLI Functions
def read_command():
    print(read(args.read))

def query_command():
    pass
def update_command():
    pass
def delete_command():
    pass


def create_db():
    if os.path.exists('./db.sqlite3') == False:
        skeleton_db.create_all() 

create_db()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import argparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
skeleton_db = SQLAlchemy(app)

#CLI
parser = argparse.ArgumentParser(description='A Mobile Webserver for development purposes.')
parser.add_argument('--host', type=str, help="The host where the webserver would run.", default='127.0.0.1')
parser.add_argument('--port', type=int, help='The port where webserver would run', default=5001)
parser.add_argument('--page', '-p', type=str, help='The page to be rendered')

args = parser.parse_args()
#Functions
def choose_port(port):
    return int(port)

def choose_host(host):
    return str(host)

@app.route('/')
def page():
    if args.page == None:
        return render_template('welcome.html')
    return render_template(args.page)

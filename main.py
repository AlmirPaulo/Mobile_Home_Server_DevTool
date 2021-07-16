from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import argparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
skeleton_db = SQLAlchemy(app)

#CLI
parser = argparse.ArgumentParser(description='A Mobile Webserver for development purposes.')
parser.add_argument('--open', '-o', type=bool, help="If you want to host on 0.0.0.0", default=False)
parser.add_argument('--port', type=int, help='The port where webserver would run', default=5001)
parser.add_argument('--page', '-p', type=str, help='The page to be rendered')

args = parser.parse_args()
#Functions
def choose_port(port):
    return int(port)

def choose_host(open):
    if open == True:
        return '0.0.0.0'
    else:
        return '127.0.0.1'


def render_page(page):
    return render_template(page)


@app.route('/')
def page():
    if args.page == None:
        return render_page('welcome.html')
    return render_page(args.page)


from flask import Flask, Blueprint, render_template
import logging, argparse, time

app = Flask(__name__, template_folder='.')

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
    return render_page(args.page)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


#https://www.youtube.com/watch?v=EE9VPJ14NjY&t=434s
from . import  views, app
import argparse

parser = argparse.ArgumentParser(description='A Mobile Webserver for development purposes.')

parser.add_argument('port', type=int, help='port where webserver would run')
#parser.add_argument('host', type=int, help='host where webserver would run')

args = parser.parse_args()

def choose_port(port):
    return int(port)

@app.route('/welcome')
@app.route('/')
def welcome():
    return views.welcome()

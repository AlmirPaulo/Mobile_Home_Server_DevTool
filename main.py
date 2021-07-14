#https://www.youtube.com/watch?v=EE9VPJ14NjY&t=434s
from flask import Flask, Blueprint, render_template
import logging, argparse, time

app = Flask(__name__, template_folder='.')


parser = argparse.ArgumentParser(description='A Mobile Webserver for development purposes.')

parser.add_argument('port', type=int, help='port where webserver would run')
parser.add_argument('host', type=str, help='host where webserver would run')

args = parser.parse_args()

def choose_port(port):
    return int(port)

def choose_host(host):
    return str(host)

@app.route('/')
def welcome():
    welcome = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Welcome Page</title>
</head>
<body>
        <center>
	<h1>Welcome to Mobile Home Server DevTool!</h1>
	<p>Thank you very much for using this tool in your development process! I hope you like to use this as much as a like to develop it.</p>
	<p>By the way <b>if you are seeing this page, CONGRATULATIONS the server is running all good!</b></p>
	<p>If you run in any kind of bug or hard time with this application, you can check the <a href="https://github.com/AlmirPaulo/Mobile_Home_Server_DevTool">documentation</a> or post an <a href="https://github.com/AlmirPaulo/Mobile_Home_Server_DevTool/issues">issue</a>.</p>
	<p>Thank you again and good code!</p>
	<a href="https://github.com/AlmirPaulo"><i>Almir Paulo</i></a>
</body>
</center>
</html>
    '''
    return welcome 



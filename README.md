# Skeleton Server DevTool
*A project by  [Almir Paulo](https://github.com/AlmirPaulo)*

![logo](https://raw.githubusercontent.com/AlmirPaulo/Mobile_Home_Server_DevTool/main/static/skeleton.png)

This is a simple CLI to serve a basic web server. This web server is not intended to be a production server, but a development one. The idea is to help developers to test and share their applications with their team partners or even with someone who have hired you for a job and wants to take a look at their product.

I know... I know... there are a lot of options out there to do the same. But this one is 100% free, easy and has a lot of features you may like.

## You may use Skeleton Server:

* As a temporary deploy for your app, so you can show it to your partners.
* As a Flask Boiler Plate.
* As your home server.
* As a learn resource for Flask, Python and Backend.


## Features

* Deploy of a single page. (Ideally, a temporary deploy)
* SQL database included (SQLite3 by default, but you can easily change it).
* Jinja2
* Bootstrap 5 locally installed, to make your Frontend life easier.
* For advanced usage (like APIs, authentication, etc), you can paste your own backend features on the "myapp.py" file.

## Dependencies

* Python3
* Flask
* Flask-SQLAlchemy

## Installation 
> I have plans to automate this whole process in a shell script.

1. Clone this repo.
2. Make sure you have Python3 installed
3. Create a virtual environment (optionally, but recommended).
    
        python3 -m venv venv

4. Activate the virtual environment and install the requirements.

        source venv/bin/activate

        pip install -r requirements.txt

If you have choosen to skip step 3, paste just the second command, obviously. 

> If you have pipenv installed you can, of course, use the pipenv way of install the requirements instead of steps 4 and 5. 

5. Paste this line on your .bashrc. If you have not a .bashrc file, create it. The following line just create an alias. You can do this with a text editor like "nano" or "vim", or just use "touch" and "echo" commands.

        alias sdst='python3 ~/skeleton_dev_server/run.py'

6. It's Ready! To make sure it's running all good, simply run:

        sdst  

You should see the welcome page at 127.0.0.1:5001.

## Commands and Usage
All the commands are optionals. 

        usage: run.py [-h] [--open OPEN] [--port PORT] [--page PAGE]

        A Mobile Webserver for development purposes.

        optional arguments:
          -h, --help            show this help message and exit
          --open OPEN, -o OPEN  If you want to host on 0.0.0.0
          --port PORT           The port where webserver would run
          --page PAGE, -p PAGE  The page to be rendered

Default host is localhost (127.0.0.1) and default port is 5001. 

In order to run an html page, you just need to place it in the server directory and run the cli with the "--page" option or simply "-p". This server can handle Jinja2 templates and if you need to run static files, place them in the "/static" directory inside the server folder.


## For bugs 
Please, open an Issue here on Github. 

## Contribute
Pull request me!
Fork it!
Tell people about it! 
Buy me a coffee!
(button soon!)

## Plans for the future

* Enable deploy of multiple pages
* Installation via pip
* Shell script for installation
* Include Redis
* Command for save logs
* A tests file for TDD lovers.
* Configure a database panel interface.
* Make it available for Android 

## Releases

### 0.0.0 - 07/19/2021 
First release. 

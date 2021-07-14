# Mobile Home Server DevTool
*A project by  [Almir Paulo](https://github.com/AlmirPaulo)*

This is a simple CLI to be runned on termux to serve a web server on your mobile device. This web server is not intended to be a production server, but a development one. The idea is to help developers to test and share their applications with their team partners or even with someone who have hired you for a job and wants to take a look at their product.

I know... I know... there are a lot of options out there to do the same. But this one is 100% free, easy and it's on your phone!

## Dependencies

* [termux](https://termux.com/)
* Python3

<!--## Installation 
<blockquote>I have plans to automate this whole process in a shell script.</blockquote>

1. Clone this repo on your android device.
2. Install Termux on your android device.
3. Install python3 via termux

        pkg install python3

4. Paste this line on your termux .bashrc. If you have not a .bashrc file, create it. The following line just create an alias. 

        alias hsdt='python3 ~/mobile_dev_server/run.py'

5. It's Ready! To make sure it's running all good, try to run the server in any port an access the "/welcome" page. 

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

This server also generates log files named by the date time it runs.
## F.A.Q.
### 1. Can I run this on my Iphone?
No, because termux runs on android only. But if you are able to find a way, please let me know. 

### 2. Can I run this on desktop via command line?
If you have Python installed, yes, but why would you do this?

### 3. I think I found a bug!/I need help! 
Please, open an Issue here on Github. 

### 4. How can I contribute to the project?
Pull request me!
Fork it!
Tell people about it! 
Buy me a coffee!

### 5. Would be easier if we could install it directly from pip or pkg...
Maybe in the future... 

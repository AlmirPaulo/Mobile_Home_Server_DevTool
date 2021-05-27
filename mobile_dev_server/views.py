from flask import render_template


def welcome():
    return render_template('welcome.html')

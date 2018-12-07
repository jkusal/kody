#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazw.py
#  
#  Copyright 2018  <>

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Witaj na serwerze!</h2><h2>Aplikacja quiz</h2>"
    
@app.route("/strona")
def strona():
    return render_template('strona.html')

@app.route("/klasa")
def klasa():
    return render_template('klasa.html')

print(__name__)



if __name__ == '__main__':
    app.run(debug=True)

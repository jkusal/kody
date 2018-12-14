#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazw.py
#  
#  Copyright 2018  <>

from flask import Flask, g
from flask import render_template, request
from modele import *

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response
    
@app.route("/")
def hello():
    return "<h1>Witaj na serwerze!</h2><h2>Aplikacja quiz</h2>"
    
@app.route("/quiz")
def quiz():
    pytania = Pytanie.select()
    return render_template('quiz.html', query = pytania)

@app.route("/klasa")
def klasa():
    return render_template('klasa.html')

print(__name__)



if __name__ == '__main__':
    app.run(debug=True)

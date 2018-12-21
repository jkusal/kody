#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazw.py
#  
#  Copyright 2018  <>

from flask import g
from modele import *
from views import *

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE',
))

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route("/klasa")
def klasa():
    return render_template('klasa.html')

print(__name__)



if __name__ == '__main__':
    app.run(debug=True)

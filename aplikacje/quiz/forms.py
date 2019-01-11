#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  forms.py
#  
#  Copyright 2018  <>

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'

class OdpForm(FlaskForm):
    id = HiddenField("Odpowiedz id")
    pytanie = HiddenField("Pytanie id")
    odpowiedz = StringField('Odpowiedź:', 
                                        validators=[Required(message=blad1)],
                                        render_kw={'class' : 'form-control'})
    odpok = BooleanField('Poprawna:')
    
    

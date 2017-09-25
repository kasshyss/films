#!/usr/bin/env python

from flask      import Flask, render_template, request
import m_IO     as io
import m_conf   as conf

app = Flask(__name__)
app_name = 'Filmotron'
language = '_fr'

@app.route('/')
def index():
    label_conf = conf.get_conf('template' + language + '.conf')
    return render_template(
            'index.html'
            ,app_name = app_name
            ,title = label_conf['index_title']
            ,options = label_conf['index_actions'].split(',')
            )

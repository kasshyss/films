#!/usr/bin/env python

from flask      import Flask, render_template, request
import m_IO     as io
import m_conf   as conf

app = Flask(__name__)
language = '_fr'

@app.route('/')
def index():
    label_conf = conf.get_conf('template' + language + '.conf')
    return render_template(
            'index.html'
            ,app_name = label_conf['app_name']
            ,title = label_conf['index_title']
            ,options = label_conf['index_actions'].split(',')
            )

@app.route('/creator/')
def creator():
    label_conf = conf.get_conf('template' + language + '.conf')
    return render_template(
            'creator.html'
            ,app_name = label_conf['app_name']
            ,title = label_conf['creator_title']
            ,directors = io.get_directors_nat()
            )

@app.route('/films/')
def film():
    label_conf = conf.get_conf('template' + language + '.conf')
    return render_template(
            'films.html'
            ,app_name = label_conf['app_name']
            ,title = label_conf['film_title']
            ,films = io.get_films()
            )

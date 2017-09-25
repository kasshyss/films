#!/usr/bin/env python

from flask      import Flask, render_template, request
import m_IO     as io
import m_conf   as conf

app = Flask(__name__)
language = '_fr'

@app.route('/')
@app.route('/index/')
@app.route('/index')
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
            'display.html'
            ,app_name = label_conf['app_name']
            ,button_label = label_conf['return_button']
            ,title = label_conf['creator_title']
            ,display_list = io.get_directors_nat()
            )

@app.route('/films/')
def film():
    label_conf = conf.get_conf('template' + language + '.conf')
    return render_template(
            'display.html'
            ,app_name = label_conf['app_name']
            ,button_label = label_conf['return_button']
            ,title = label_conf['film_title']
            ,display_list = io.get_films()
            )

@app.route('/notes/')
def notes():
    label_conf = conf.get_conf('template' + language + '.conf')
    return render_template(
            'display.html'
            ,app_name = label_conf['app_name']
            ,button_label = label_conf['return_button']
            ,title = label_conf['note_title']
            ,display_list = io.get_notes_films()
            )

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

@app.route('/add_film/', methods=['GET','POST'])
def add_film():
    label_conf = conf.get_conf('template' + language + '.conf')
    if request.method == 'GET':
        return render_template(
            'add_film.html'
            ,app_name = label_conf['app_name']
            ,button_label = label_conf['return_button']
            ,title = label_conf['add_label']
            ,fields = label_conf['add_fields']
            ,buttons = label_conf['add_button']
            ,directors = io.get_directors_short()
            )
    else: #POST
        request_data={}
        request_data['directors']=''
        i=True
        for key in request.form:
            if key[:9:] == 'directors':
                #director
                if i==True:
                    i=False
                    request_data['directors']=request.form[key]
                else:
                    tmp=request_data['directors']
                    request_data['directors']=tmp+','+request.form[key]
            else:
                request_data[key]=request.form[key]
        io.set_film(request_data)
        return film()

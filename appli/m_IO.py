#!/usr/bin/env python

import m_log as log
import psycopg2 as pg
import m_conf as conf

#run a sql query in postgres
#return the result
#use config to connect to the rigth DB
def __pg_request(query):

    db_conf = conf.get_conf('db.conf')
    try:
        conn = pg.connect("dbname='" + str(db_conf['DB']) + "' user='" + str(db_conf['USER']) + "' host='" + str(db_conf['IP']) + "' password='" + str(db_conf['PWD']) +"'")
        cursor =  conn.cursor()
        cursor.execute(query)
        conn.commit()
        if query[:6:] == 'SELECT':
            data = cursor.fetchall()
        else:
            data='Query done : ' + query
        cursor.close()
    except ValueError:
        print 'Unable to connect database : \n' + ValueError
        m_log.write_log('appli.log','m_IO.__pg_request | Unable to manage the database link' + str(ValueError))
        return False
    return data

# add a nationality to the list
# get a dico
# label : label value
# full_name : full name
def set_nationality(data):
    __pg_request(conf.get_conf('queries.conf')['set_nat'].replace('%LABEL%', data['label']).replace('%FULL%', data['full_name']))
    log.write_log('appli.log','m_IO.set_nationality | add new nationality : ' + data['label'])
    return True
#return the nationalities full list
def get_nationalities():
    log.write_log('appli.log','m_IO.get_nationalities | Get nationalities')
    return __pg_request(conf.get_conf('queries.conf')['get_nat'])

# create a film director (with nationality)
# create first director then add nat
# get a dico
# name : name of the director
# death : death date
# birth : birth date
# nationalities : nationalitinies in format n1,n2,n3
def set_director(data_director):
    #insert director
    __pg_request(conf.get_conf('queries.conf')['set_director'].replace('%NAME%', data_director['name']).replace('%BIRTH%', data_director['birth']).replace('%DEATH%', data_director['death']).replace("''", 'null'))
    for i in data_director['nationalities'].split(','):
        #insert nationalities
        __pg_request(conf.get_conf('queries.conf')['set_director_nat'].replace('%NAME%', data_director['name']).replace('%NATID%', i))
    log.write_log('appli.log','m_IO.set_director | Create a new director '+data_director['name'])
    return True

# get directors data without nationality
def get_directors():
    log.write_log('appli.log','m_IO.get_director | Get directors')
    return __pg_request(conf.get_conf('queries.conf')['get_director'])

def get_directors_short():
    log.write_log('appli.log','m_IO.get_director_short | Get directors name and ID')
    return __pg_request(conf.get_conf('queries.conf')['get_creator_short'])

# get directors data with nationality
def get_directors_nat():

     data_nat = {}
     # compress director nat into list l[name] = {nat1, nat2}
     for record in __pg_request(conf.get_conf('queries.conf')['get_director_nat']):
         if record[0] in data_nat.keys():
             data_nat[record[0]] = data_nat[record[0]] + ', ' + record[2]
         else:
             data_nat[record[0]] = record[2]

     directors=[]
     for director in __pg_request(conf.get_conf('queries.conf')['get_director']):
         
         tmp = []
         for item in list(director):
             tmp.append(item)
         tmp.append(data_nat[director[0]])
         directors.append(tuple(tmp))

     log.write_log('appli.log','m_IO.get_director_nat | Get directors with nationality')
     return directors

# create a film, you need to have a existing director in the db
# get dico
# name : film name
# creation : creation date
# resume : resume of the film
# directors : d1,d2,d3
def set_film(data_film):
    __pg_request(conf.get_conf('queries.conf')['set_film'].replace('%NAME%', data_film['name']).replace('%CDATE%', data_film['creation']).replace('%RESUME%', data_film['resume']))
    for director in data_film['directors'].split(','):
        __pg_request(conf.get_conf('queries.conf')['set_film_creator'].replace('%NAME%', data_film['name']).replace('%CREATOR%', director))
    log.write_log('appli.log','m_IO.set_film | Create a new film '+data_film['name'])
    return True

# return film list
def get_films():
    log.write_log('appli.log','m_IO.get_films | Get films without director')
    return __pg_request(conf.get_conf('queries.conf')['get_films_full'])


# Get note as is without film data
def get_notes():
    log.write_log('appli.log','m_IO.get_notes | Get note table AS IS')
    return __pg_request(conf.get_conf('queries.conf')['get_notes_full'])

# Get last notes - to be display
def get_notes_films():
    log.write_log('appli.log','m_IO.get_notes_films | Get note table link with film name')
    return __pg_request(conf.get_conf('queries.conf')['get_notes'])

# get notes for a specific film
# param = film ID
def get_notes_spe(film_id):
    log.write_log('appli.log','m_IO.get_notes_films_spec | Get note table link with film name for one specific film')
    return __pg_request(conf.get_conf('queries.conf')['get_notes_spec'].replace('%FILMID%', film_id))

# create a new note
# get dico
# note_by : people who wote the film
# finale_note : the true noe without detail
# art_note : artistique note
# story_note : is the story good
# fun_note : is the film fun
# film_id : the id the film which deal with
def set_note(data_note):
    __pg_request(conf.get_conf('queries.conf')['set_note'].replace('%NOTEBY%', data_note['note_by']).replace('%FNOTE%', data_note['final_note']).replace('%ART%', data_note['art_note']).replace('%STORY%', data_note['story_note']).replace('%FUN%', data_note['fun_note']).replace('%FILM%', data_note['film_id']).replace('%COM%', data_note['comment'].replace("'", "''")))
    log.write_log('appli.log','m_IO.get_notes_films | Get note table link with film name for one specific film')
    return True


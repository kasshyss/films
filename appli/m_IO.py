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
        m_log.write_log('appli.log','m_IO.add_bottle_pg | Unable to manage the database link' + str(ValueError))
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
    log.write_log('appli.log','m_IO.get_nationalities | Get directors')
    return __pg_request(conf.get_conf('queries.conf')['get_director'])

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

     return directors

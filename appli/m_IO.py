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
        print conn
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

# get a dico
# label : label value
# full_name : full name
def set_nationality(data):
    __pg_request(conf.get_conf('queries.conf')['set_nat'].replace('%LABEL%', data['label']).replace('%FULL%', data['full_name']))
    log.write_log('appli.log','m_IO.set_nationality | add new nationality : ' + data['label'])
    return True

def get_nationalities():
    return __pg_request(conf.get_conf('queries.conf')['get_nat'])


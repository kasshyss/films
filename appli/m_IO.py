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
        data = cursor.fetchall()
        cursor.close()
    except ValueError:
        print 'Unable to connect database : \n' + ValueError
        m_log.write_log('appli.log','m_IO.add_bottle_pg | Unable to manage the database link' + str(ValueError))
        return False
    return data



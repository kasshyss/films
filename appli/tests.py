#!/usr/bin/env python

import sys
import m_IO as io

if sys.argv[1] == 'nat':
    print 'IO nationality'
    tmp={}
    tmp['label']=raw_input('Set nat label : ')
    tmp['full_name']=raw_input('Set nat full name : ')
    print io.set_nationality(tmp)
    print io.get_nationalities()
elif sys.argv[1] == 'dir':
    print 'IO director'
    tmp = {}
    param = {'name', 'birth', 'death','nationalities'}
    for country in io.get_nationalities():
        print country
    for p in param:
        tmp[p] = raw_input(p + ' : ')
    print io.set_director(tmp)
    print io.get_directors()
    print io.get_directors_nat()
elif sys.argv[1] == 'film':
    print 'IO films'
    tmp = {}
    param = {'name', 'creation', 'resume','directors'}
    for director in io.get_directors_nat():
        print director
    for p in param:
        tmp[p] = raw_input(p + ' : ')
    print io.set_film(tmp)
    print io.get_films()
elif sys.argv[1] == 'query':
    print sys.argv[2]
    print io.__pg_request(sys.argv[2])
    print io.get_films()
elif sys.argv[1] == 'note':
    print io.get_films()
    param = {'note_by', 'final_note', 'art_note', 'story_note', 'fun_note', 'comment','film_id'}
    tmp={}
    for p in param:
        tmp[p] = raw_input(p + ' : ')
    print io.set_note(tmp)
    print io.get_notes()
    print io.get_notes_films()
    print io.get_notes_spe(raw_input('ID du film - historique notation : '))
else:
    print 'chose a test'
    print 'nat = test nationality'
    print 'dir = director'

#!usr/bin/env python

import m_IO as io

print io.__pg_request_postgres('CREATE DATABASE films;')
print io.__pg_request('CREATE TABLE creator(creator_id serial primary key, creator_name VARCHAR(140), creator_birth DATE, creator_death DATE);')
print io.__pg_request('CREATE TABLE films(film_id serial primary key, name VARCHAR(140), creation_date DATE, resume VARCHAR(500));')
print io.__pg_request('CREATE TABLE note(note_id serial primary key, note_by VARCHAR(140), art INTEGER, story INTEGER, fun INTEGER, fk_film INT REFERENCES film(film_id))')

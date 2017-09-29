#!/usr/bin/env python

import os, sys


print 'Get data from ' + sys.argv[1]
file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+sys.argv[1], "r")
lines = file.readlines()
file.close()
print 'Run queries'
file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+sys.argv[1].split('.')[0]+'.sql', "a")
file.write('DELETE FROM ref_nationality;\n')
print 'Inserts'
for line in lines:
    file.write('INSERT INTO ref_nationality(nat_label, nat_full_name, insert_date) VALUES (' + line.split(',')[5][:-1:].replace('"', '\'') + ",'" + line.split(',')[4][1:-1:] + '\',now());\n')
file.close()


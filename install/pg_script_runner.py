#!/usr/bin/env python

import os, sys

print 'Run sql script : ' + sys.argv[1]

cmd = 'psql -h 127.0.0.1 -d films -U meriadoc -f ' + sys.argv[1]
print cmd
os.system(cmd)

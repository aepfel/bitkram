#!/usr/bin/python

import sys

for line in sys.stdin:
	print "line:" + line
	print "repr:" + repr(line)
	print "len:" + str(len(line))

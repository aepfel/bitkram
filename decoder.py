#!/usr/bin/python

import base64
import sys


for line in sys.stdin :
	print line
	print len(line)
	if line[5:12]=='message':
		print 'gefunden'
		break

msgtextb64=line[16:len(line)-5]
print msgtextb64
print len(msgtextb64)
print 'lets decode it'
decoded=base64.b64decode(msgtextb64)
print decoded

#msgtext = str(line[16:-5])
#print 'geht los\n'+msgtext+'\nist vorbei'
#print 'text ist so lang:'+str(len(msgtext))
#lens = len(line)
#lenx = lens - (lens % 4 if lens % 4 else 4)
#decoded = base64.b64decode(msgtext)
#print decoded

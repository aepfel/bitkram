#!/usr/bin/python
import xmlrpclib
import json
import time
import requests
import urllib
import dbzugang


bmapi = xmlrpclib.ServerProxy("http://apiich:apiichpasswort@localhost:8442/")

allemsg = ""
for x in json.loads(bmapi.getAllInboxMessages())['inboxMessages']:
	#allemsg = allemsg + "id:\"" + x['msgid'] + "\"\n" + "Betreff:\"" + x['subject'].decode('base64') + "\"\n"       + "Nachricht:\"" + x['message'].decode('base64') + "\"\n" + "von:\"" + x['fromAddress'] + "\"\n\n"
	dbzugang.data2db(x['fromAddress'][3:],x['msgid'])
	bmapi.trashMessage(x['msgid'])
#print allemsg
dbzugang.closedb()

#inboxMessages = json.loads(bmapi.getAllInboxMessages())
#neuste nachricht?
#print "\n\nneuste nachricht:"
#print inboxMessages['inboxMessages'][0]['message'].decode('base64')


#print "\n msg nach id"
#print json.loads(bmapi.getInboxMessageByID('8278091bfa7d763b3a7d220811bf390a2bd5ee60c1092c2b21623821da72149f'))['inboxMessage'][0]['message'].decode('base64')



#!/usr/bin/python
import xmlrpclib
import json
import time
import requests
import urllib


bmapi = xmlrpclib.ServerProxy("http://apiich:apiichpasswort@localhost:8442/")

allemsg = ""
for x in json.loads(bmapi.getAllInboxMessages())['inboxMessages']:
	allemsg = allemsg + "id:\"" + x['msgid'] + "\"\n" + "Betreff:\"" + x['subject'].decode('base64') + "\"\n"       + "Nachricht:\"" + x['message'].decode('base64') + "\"\n" + "von:\"" + x['fromAddress'] + "\"\n\n"

print allemsg

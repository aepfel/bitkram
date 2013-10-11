#!/usr/bin/python

import xmlrpclib
import json
import time
import requests
import urllib

api = xmlrpclib.ServerProxy("http://apiich:apiichpasswort@localhost:8442/")

print 'Let\'s test the API first.'
inputstr1 = "hello"
inputstr2 = "world"
print api.helloWorld(inputstr1, inputstr2)
print api.add(2,3)

print 'Let\'s now print all of our inbox messages:'
#print api.getAllInboxMessages()
inboxMessages = json.loads(api.getAllInboxMessages())
#print inboxMessages

theJson = "{"
for s in inboxMessages['inboxMessages']:
	theJson = theJson + "\"" + s['receivedTime'] + "\"" + ":" + "\"" + s['message'].decode('base64') + "\"" + ",";	
theJson = theJson+"}"
print theJson

theRemoteURL = 'http://THEWEBSERVER.COM/_dev_bittweet/bittweet_process_00.php'

#for s in inboxMessages['inboxMessages']:
#	theString=s['receivedTime']+s['message'].decode('base64');payload = {'key1':theString};r = requests.post(theRemoteURL, payload);print r.text

#WIPE DB FIRST
#theString="delete";payload = {'APIKEYHERE1':theString};r = requests.post(theRemoteURL, payload);print r.text

#make JSON
#for s in inboxMessages['inboxMessages']:
#	theString=s['message'].decode('base64');theString=unicode(theString,errors='ignore');theTime=s['receivedTime'];payload = {'APIKEYHERE1':theString,'APIKEYHERE2':theTime};r = requests.post(theRemoteURL, payload);print r.text

#print inboxMessages['inboxMessages'][0]['message'].decode('base64')
#theString = api.getAllInboxMessages()
#print theString
#payload = {'key1':theString}
#r = requests.post(theRemoteURL, payload)

#print r.text

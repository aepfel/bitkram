#!/usr/bin/python
import xmlrpclib
import json
import time
import requests
import urllib
import sys


bmapi = xmlrpclib.ServerProxy("http://apiich:apiichpasswort@localhost:8442/")
print json.loads(bmapi.getInboxMessageByID(sys.argv[1]))['inboxMessage'][0]['subject'].decode('base64')


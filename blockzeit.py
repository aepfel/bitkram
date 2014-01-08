import json
import urllib2 
import datetime
import pytz

utc = pytz.utc
height = json.load(urllib2.urlopen("https://blockchain.info/latestblock"))['height']
hours = height/6.0
days = hours/24.0
seconds = height*600
genesissecond = 1231002940
now = genesissecond + seconds
print "Bitcointime: " , datetime.datetime.fromtimestamp(now , utc)
print "UTC: " , datetime.datetime.utcnow()

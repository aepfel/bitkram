#!/usr/bin/python
import sys
import MySQLdb
#parameter nutzen statt stdin erster parameter=bm-adresse zweiter parameter=msgid
bmaddress = sys.stdin.readline()
print bmaddress
db = MySQLdb.connect(user="root",passwd="aeaeae",host="localhost",db="bm")
cur = db.cursor()
if cur.execute("SELECT * FROM bm WHERE bmaddress = %s", (bmaddress)) = 1:
	for x in cur.fetchall():
		print x[0] + " " + x[1]
else
	cur.execute("INSERT INTO bm VALUES



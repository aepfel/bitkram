#!/bin/bash
#curl -s -u apiich:apiichpasswort --data "<?xml version='1.0'?><methodCall><methodName>getAllInboxMessages</methodName><params></params></methodCall>" http://127.0.0.1:8442

#curl -s -u apiich:apiichpasswort --data "<?xml version='1.0'?><methodCall><methodName>listAddresses2</methodName><params></params></methodCall>" http://127.0.0.1:8442



SUBJECT=`echo -n This is the subject | base64`
BODY=`echo -ne "this is\na little test" | base64`


curl -s -u apiich:apiichpasswort --data "<?xml version='1.0'?>
<methodCall>
<methodName>helloWorld</methodName>
<params>
<param><value><string>hello</string></value></param>
<param><value><string>World</string></value></param>
</params>
</methodCall>" http://127.0.0.1:8442 >> /dev/null


MSGID=`echo 3b24c797bcd21cab6678721a9dac8a135f60ed8cc8b6dbabc193a99339623b1e`
curl -s -u apiich:apiichpasswort --data "<?xml version='1.0'?>
<methodCall>
<methodName>getInboxMessageByID</methodName>
<params>
<param><value><string>$MSGID</string></value></param>
</params>
</methodCall>" http://127.0.0.1:8442

#!/usr/bin/env python
import httplib, urllib, os
shell = os.popen("route -n | grep UH | awk '{print $1 \":80\"}'")
nguk = shell.read()
params = urllib.urlencode({'a': 1, 'b': 2, 'c': 0})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection(nguk)
conn.request("POST", "/info.php", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()

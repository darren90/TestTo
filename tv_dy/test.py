#-*-coding:utf8-*-
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import httplib

conn = httplib.HTTPSConnection("www.youtube.com")
conn.request("GET", "/")

response = conn.getresponse()
print response.status, response.reason
# data = response.read()
# print data


# html = requests.get('https://www.youtube.com')
# print html.text


# -*- coding: UTF-8 -*-

import urllib2


response1 = urllib2.urlopen("https://www.youtube.com")

print response1.getcode()
print response1.read()

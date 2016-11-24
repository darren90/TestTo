#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import types
import urlparse
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'-- 开始爬取内容。。。'

#getsource用来获取网页源代码
    def getsource(self,url):
        response = requests.get(url)
        response.encoding = 'gb2312'
        return response.text


#得到所有的待爬取的链接
    def get_content_recursion(self,url):
        if url is None:
            return
        print 'url--:%s' % url
        html = self.getsource(url)
        if html is None:
            return
        print 'start-- : %s ' % html
        soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
        content = soup.find('ol', class_="item-section")
        if content is None:
            return
        # links = content.find_all('table')
        print '------ok----'


if __name__ == '__main__':
    fout = open('output_youtube.sql','w')
    fialCount = 1
    count = 1
    classinfo = []
    url = 'https://www.youtube.com/results?q=1m'
    mySpider = spider()
    mySpider.get_content_recursion(url) #所有的页面
    fout.close()
 






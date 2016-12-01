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
        # response = requests.get(url)
        # payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        # requests.get('http://httpbin.org/get', params=payload)
        headers_download_html = {
            'Host': 'www.tv.com',
            'Referer': 'http://www.tv.com/',
            'Proxy-Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'DNT': 1,
            'Cookie': 'QSI_HistorySession=http%3A%2F%2Fwww.tv.com%2Fnews%2F~1480586172677',
            # 'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2,und;q=0.2'
        }
        # requests.get(url, verify=False)
        response = requests.get(url, params=headers_download_html)
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
    # url = 'http://www.youtube.com/results?q=1m'
    url = 'http://www.tv.com/'
    mySpider = spider()
    mySpider.get_content_recursion(url) #所有的页面
    fout.close()
 






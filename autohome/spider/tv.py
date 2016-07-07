#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import urlparse
from models import User
from models import Spiderdb

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os
import hashlib


import sys
reload(sys)
sys.setdefaultencoding("gb2312")

class spider(object):
    def __init__(self):
        print u'-- 开始爬取内容。。。'

#getsource用来获取网页源代码
    def getsource(self,url):
        response = requests.get(url)
        # response.encoding = 'gb2312'
        md5 = hashlib.md5(response.text.encode('utf-8')).hexdigest()
        return response.text

#changepage用来生产不同页数的链接
    def changepage(self,url,total_page):
        pages_arary = []
        pages_arary.append(url)
        count = 2
        for i in range(1,total_page):
            new_url =  '%d' % count
            new_full_url = urlparse.urljoin(url,new_url)
            # print new_full_url
            pages_arary.append(new_full_url)
            count = count + 1
        return pages_arary


#解析具体的数据
    def parse_html_data(self,html_countent,url):

    # 都不为空的时候，存储爬取的链接
     isHadSpider = Spiderdb.isThisHadSpider(url,html_countent)
     # print '---url:%s,hadSpider:%d'%(url,isHadSpider)
     if isHadSpider == True:
         print '地址：%s 已经爬取，并且内容没有更新'%url
         return
     else:
        print '地址：%s 没有爬取' % url
        Spiderdb.saveSpider(url,html_countent)
        

     res_array = []
     res_data = {}
     soup = BeautifulSoup(html_countent, "html.parser",from_encoding='gb2312')
     links = soup.find('ul', class_="content position")

     if links is None:
        return []

     for link in links.find_all('li'):
        new_link = link.find('a')

        # 帖子的详情地址
        detail_url = new_link['href']

        # 帖子的标题
        title = new_link['title']

        # 图片地址
        icon_url = new_link.find('img')['src']

        # 副标题
        sub_title = link.find('span').get_text()

        # 发帖人id
        bbs_id = link.find('dt').find('a').get_text()

        bbs__ = link.find('dd', class_="font12NoLine").find('a')

        # 文章所在的论坛名字
        bbs_name = bbs__.get_text()

        #文章所在轮胎的地址
        bbs_url = urlparse.urljoin("http://club.autohome.com.cn",bbs__['href'])

        user = User(title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url)
        user.save()

def runapp():
    print('Tick1! The time is: %s' % datetime.now()) 
    fialCount = 1
    count = 1
    classinfo = []
    url = 'http://club.autohome.com.cn/JingXuan/104/'
    mySpider = spider()
    all_pages = mySpider.changepage(url,20)
    # all_links = mySpider.getAllLines(all_pages)
    for link in all_pages:
        print link
        try:
            html = mySpider.getsource(link)
            mySpider.parse_html_data(html,link)
            count = count +1
        except Exception as e:
            if fialCount == 10200:
                fout.close()
                break
            fialCount = fialCount + 1
            count = count +1


# 配置爬虫，每10个小时爬一次
if __name__ == '__main__':
    runapp()
    # scheduler = BlockingScheduler()
    # # scheduler.add_job(runapp,'cron', second='*/12', hour='*')
    # scheduler.add_job(runapp,'cron', hour='*/6')
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     scheduler.shutdown()






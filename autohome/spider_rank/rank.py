# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import urlparse

from rankModel import  *


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

    # getsource用来获取网页源代码
    def getsource(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        md5 = hashlib.md5(response.text.encode('utf-8')).hexdigest()
        return response.text

    # changepage用来生产不同页数的链接
    def changepage(self, url, total_page):
        pages_arary = []
        pages_arary.append(url)
        count = 2
        for i in range(1, total_page):
            new_url = '%d' % count
            new_full_url = urlparse.urljoin(url, new_url)
            # print new_full_url
            pages_arary.append(new_full_url)
            count = count + 1
        return pages_arary

    # 解析具体的数据
    def parse_html_content(self, url,rank_year):
        html_countent = self.getsource(url)

        # # 都不为空的时候，存储爬取的链接
        # isHadSpider = Spiderdb.isThisHadSpider(url, html_countent)
        # # print '---url:%s,hadSpider:%d'%(url,isHadSpider)
        # if isHadSpider == True:
        #     print '地址：%s 已经爬取，并且内容没有更新' % url
        #     return
        # else:
        #     print '地址：%s 没有爬取' % url
        #     Spiderdb.saveSpider(url, html_countent)

        res_array = []
        res_data = {}
        soup = BeautifulSoup(html_countent, "html.parser", from_encoding='gb2312')
        #  2015 的世界数据抓取
        # body = soup.find('tbody')#find('table',class_="rankingtable dataTable")

        body = soup.find('table', class_='rankingtable')
        # print body

        if body is None:
            return []
        count = 0
        print len(body.findAll('tr'))
        for trs in body.findAll('tr'):
            # print trs
            if count == 0:
                count = count + 1
                continue

            tds = trs.findAll('td')
            # print len(tds)
            # rank_year, rank, last_rank,co_name,co_detailurl,  income, profit, nation
            rank = tds[0].get_text()
            last_rank = tds[1].get_text()
            co_name = tds[2].find('a').get_text().replace("'", "''")
            co_detailurl = tds[2].find('a')['href']
            co_detailurl = urlparse.urljoin(url,co_detailurl)
            income = tds[3].get_text().replace(",","")
            profit = tds[4].get_text().replace(",","")
            nation = tds[5].get_text()


            rand_word = Rank_Word(rank_year, rank, last_rank,co_name,co_detailurl,  income, profit, nation)
            rand_word.save()


def runapp():
    print('Tick1! The time is: %s' % datetime.now())
    fialCount = 1
    count = 1
    url = 'http://www.fortunechina.com/fortune500/c/2013-07/08/2013G500.htm'
    mySpider = spider()
    mySpider.parse_html_content(url,'2013')
    # all_pages = mySpider.changepage(url, 20)
    # # all_links = mySpider.getAllLines(all_pages)
    # for link in all_pages:
    #     print link
    #     try:
    #         mySpider.parse_html_content(link)
    #         count = count + 1
    #     except Exception as e:
    #         if fialCount == 10200:
    #             fout.close()
    #             break
    #         fialCount = fialCount + 1
    #         count = count + 1


# 配置爬虫，每10个小时爬一次
if __name__ == '__main__':
    runapp()
    # scheduler = BlockingScheduler()
    # # scheduler.add_job(runapp,'cron', second='*/12', hour='*')
    # scheduler.add_job(runapp, 'cron', hour='*/6')
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     scheduler.shutdown()






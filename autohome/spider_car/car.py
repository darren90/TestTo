#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import urlparse
# from carModel import *

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
    def get_scraw_urls(self):
        scraw_urls = []
        brandlist = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'X',
                     'Y', 'Z']
        baseUrl = 'http://www.autohome.com.cn/grade/carhtml/'
        for list in brandlist:
            url = baseUrl + list + '.html'
            scraw_urls.append(url)
        return scraw_urls

    # 解析全部的品牌信息
    def parse_html_data_brand(self,html_countent,url):

        soup = BeautifulSoup(html_countent, "html.parser", from_encoding='gb2312')
        brands = soup.find('div', class_="tab-content-item current")
        print brands
        if brands is None:
            return []

        for sbrand in brands.find_all('div'):
            brand_class = sbrand.find('div', class_="tab-content-item current")

            print brand_class.find('span').get_text()


            # # 帖子的详情地址
            # detail_url = new_link['href']
            #
            # # 帖子的标题
            # title = new_link['title']
            #
            # # 图片地址
            # icon_url = new_link.find('img')['src']
            #
            # # 副标题
            # sub_title = sbrand.find('span').get_text()
            #
            # # 发帖人id
            # bbs_id = sbrand.find('dt').find('a').get_text()
            #
            # bbs__ = sbrand.find('dd', class_="font12NoLine").find('a')
            #
            # # 文章所在的论坛名字
            # bbs_name = bbs__.get_text()
            #
            # # 文章所在轮胎的地址
            # bbs_url = urlparse.urljoin("http://club.autohome.com.cn", bbs__['href'])
            #
            # user = User(title, detail_url, icon_url, bbs_id, bbs_name, sub_title, bbs_url)
            # user.save()


#解析具体的数据
    def parse_html_data(self,html_countent,url):

    # # 都不为空的时候，存储爬取的链接
    #  isHadSpider = Spiderdb.isThisHadSpider(url,html_countent)
    #  print '---url:%s,hadSpider:%d'%(url,isHadSpider)
    #  if isHadSpider == True:
    #      print '地址：%s 已经爬取，并且内容没有更新'%url
    #      return
    #  else:
    #     print '地址：%s 没有爬取' % url
    #     Spiderdb.saveSpider(url,html_countent)
        
     soup = BeautifulSoup(html_countent, "html.parser",from_encoding='gb2312')
     all_dls = soup.find_all('dl')
     #
     # print links
     # if links is None:
     #    return []
     for dl in all_dls:
        brand_item = dl.find('a')

        # 品牌 - 如 本田
        brand_url = brand_item['href']
        brand_img = brand_item.find('img')['src']
        brand_name = dl.find('dt').find('div').get_text()

        # 子品牌 - 如 广汽本田
        sbrand_item = dl.find('dd').find_all('div',class_='h3-tit')
        for ssbran_item in sbrand_item:
            sbrand_name = ssbran_item.get_text()
            print '%s-%s' % (brand_name,sbrand_name)

            car_types = dl.find('dd').find_all('ul', class_='rank-list-ul')
            for car_type in car_types:
                car_models = car_type.find_all('li')
                # print  car_models
                for car_model in car_models:
                    # print '%s-%s'% (sbrand_name,car_model.find('h4').get_text())

            # 子品牌下的具体车型,如 雅阁


        # # 帖子的标题
        # title = new_link['title']
        #
        # # 图片地址
        # icon_url = new_link.find('img')['src']
        #
        # # 副标题
        # sub_title = link.find('span').get_text()
        #
        # # 发帖人id
        # bbs_id = link.find('dt').find('a').get_text()
        #
        # bbs__ = link.find('dd', class_="font12NoLine").find('a')
        #
        # # 文章所在的论坛名字
        # bbs_name = bbs__.get_text()
        #
        # #文章所在轮胎的地址
        # bbs_url = urlparse.urljoin("http://club.autohome.com.cn",bbs__['href'])
        #
        # user = User(title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url)
        # user.save()

def runapp():
    print('Tick1! The time is: %s' % datetime.now()) 
    fialCount = 1
    count = 1
    classinfo = []
    mySpider = spider()
    # html = mySpider.getsource(url)
    # mySpider.parse_html_data_brand(html, url)
    # # all_links = mySpider.getAllLines(all_pages)
    all_pages = mySpider.get_scraw_urls()
    for link in all_pages:
        print '-%d-%s'%(count,link)
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






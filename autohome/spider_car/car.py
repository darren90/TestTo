#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import urlparse
from carModel import *

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os
import hashlib


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class spider(object):
    def __init__(self):
        print u'-- 开始爬取内容。。。'

#getsource用来获取网页源代码
    def getsource(self,url):
        response = requests.get(url)
        # response.encoding = 'gb2312'
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

        soup = BeautifulSoup(html_countent, "html.parser", from_encoding='utf-8')
        brands = soup.find('div', class_="tab-content-item current")
        print brands
        if brands is None:
            return []

        for sbrand in brands.find_all('div'):
            brand_class = sbrand.find('div', class_="tab-content-item current")

            print brand_class.find('span').get_text()


    def parse_html_car_level(self,car_dict):
        car_name = car_dict['car_name']
        car_url = car_dict['car_url']

        car_level_array = []

        if car_url is None:
            return
        html_content = self.getsource(car_url)
        soup = BeautifulSoup(html_content, "html.parser", from_encoding='utf-8')

        # 解析 车的级别 如 中型车
        car_levelc_c = soup.find('div',class_='breadnav fn-left')
        if car_levelc_c is None:
            return
        car_levelc_s =  car_levelc_c.find_all('a')
        if car_levelc_s is None or len(car_levelc_s)<2:
            return
        car_level = car_levelc_s[1].get_text()

        # 解析视频的地址

        car_itemc = soup.find('div',class_='nav-typebar nav-typebar-g12 fn-clear')
        if car_itemc is None:
            return
        car_items = car_itemc.find('ul').find_all('li')
        if car_items is None or len(car_items)<8:
            return
        # print car_items
        car_videl_url = ''
        car_videl_title = ''
        car_videl_title_c  = car_items[7].find('a')
        if car_videl_title_c is not None:
            car_videl_url = car_items[7].find('a')['href']
            car_videl_title = car_videl_title_c.get_text()

        # print '%s-%s-%s-%s' %(car_name,car_level,car_videl_title,car_videl_url)

       #  直接开始解析视频
        if car_videl_url is None or len(car_videl_url) == 0:
            # 直接在这里进行一遍存储
            car_videos = Car_Videos(car_name,car_level,car_videl_url,'','','','')
            car_videos.save()
            return

        #  再次解析网页 最后的视频网页
        html_content_c = self.getsource(car_videl_url)

        if html_content_c is None:
            return

        # 都不为空的时候，存储爬取的链接
        isvideoHadSpider = Spiderdb.is_carvideo_HadSpider(car_videl_url,html_content_c)
        print '---url:%s,hadSpider:%d'%(car_videl_url,isvideoHadSpider)
        if isvideoHadSpider == True:
            print '视频,地址：%s 已经爬取，并且内容没有更新'%car_videl_url
            return []
        else:
            print '视频,地址：%s 没有爬取' % car_videl_url
            Spiderdb.save_carvideo_spider(car_videl_url,html_content_c)

        soup = BeautifulSoup(html_content_c, "html.parser", from_encoding='gb2312')

        videos_cont = soup.find('ul',class_='videocont')
        if videos_cont is None:
            return
        videos_c = videos_cont.find_all('li')
        if videos_c is None:
            return
        for video_c in videos_c:
            vide_play_url = video_c.find('div',class_='videocont-img').find('a')['href']
            video_imgurl = video_c.find('div',class_='videocont-img').find('a').find('img')['src']
            video_timel = video_c.find('div',class_='videocont-img').find('i').get_text()
            vide_title = video_c.find('div', class_='videocont-text').find('a').get_text().replace("\"","\'").replace("\t","").replace('\n','').replace(' ','')
            print '%s  %s  %s  %s' % (vide_title,vide_play_url,video_timel,video_imgurl)
            car_videos = Car_Videos(car_name,car_level,car_videl_url,vide_title,video_imgurl,video_timel,vide_play_url)
            car_videos.save()

    #解析品牌数据
    def parse_html_brand(self,html_countent,url):

    # 都不为空的时候，存储爬取的链接
     isHadSpider = Spiderdb.is_sbrand_HadSpider(url,html_countent)
     print '---url:%s,hadSpider:%d'%(url,isHadSpider)
     if isHadSpider == True:
         print '大类,地址：%s 已经爬取，并且内容没有更新'%url
         return []
     else:
        print '大类,地址：%s 没有爬取' % url
        Spiderdb.save_sbrand(url,html_countent)
        
     soup = BeautifulSoup(html_countent, "html.parser",from_encoding='gb2312')
     all_dls = soup.find_all('dl')

     car_array = []

     for bdl in all_dls:
        brand_item = bdl.find('a')
        if brand_item is None:
            continue
        # print brand_item
        # 品牌 - 如 本田
        brand_url = brand_item['href']
        brand_imgurl = brand_item.find('img')['src']
        brand_name = bdl.find('dt').find('div').get_text()

        # 子品牌 - 如 广汽本田
        sbrand_items = bdl.find('dd').find_all('div',class_='h3-tit')
        print len(sbrand_items)
        sbrand_index = 0
        for sbran_item in sbrand_items:
            # 子品牌名字 - 如 广汽本田

            sbrand_name = sbran_item.get_text()
            print '%s-%s-%d' % (brand_name,sbrand_name,len(sbrand_items))

            car_types = bdl.find('dd').find_all('ul', class_='rank-list-ul')
            if car_types is None:
                continue

            # 子品牌下的具体车型,如 雅阁
            car_models = car_types[sbrand_index].find_all('li')
            if car_models is None:
                continue
            for car_model in car_models:
                if car_model is None:
                    continue
                if car_model.find('h4') is None:
                    continue

                car_dict = {}

                #  具体的车的名字 "雅阁"
                car_name = car_model.find('h4').get_text()
                # 车的主页
                car_url = car_model.find('h4').find('a')['href']
                print '%s-%s-%s'%(sbrand_name,car_name,car_url)
                autobrand = Auto_Brand(brand_name,brand_url,brand_imgurl,sbrand_name,car_name,car_url)
                autobrand.save()
                car_dict['car_name'] = car_name
                car_dict['car_url'] = car_url
                car_array.append(car_dict)
            sbrand_index = sbrand_index +1

     return car_array
                # print '%s-3-%s' % (sbrand_name,car_model.find('h4').get_text())

def runapp():
    print('Tick1! The time is: %s' % datetime.now())
    count = 1
    mySpider = spider()
    all_pages = mySpider.get_scraw_urls()
    for link in all_pages:
        print '-%d-%s'%(count,link)
        html = mySpider.getsource(link)
        cars_array = mySpider.parse_html_brand(html,link)
        for car_dict in cars_array:
            mySpider.parse_html_car_level(car_dict)
        count = count + 1
    # car_dict = {}
    # car_dict['car_name'] = '思域'
    # car_dict['car_url'] = 'http://www.autohome.com.cn/135/#levelsource=000000000_0&pvareaid=101594'
    # mySpider.parse_html_car_level(car_dict)


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






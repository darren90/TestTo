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
    def get_all_pages(self,url,total_page):
        pages_arary = []
        pages_arary.append(url)
        count = 2
        for i in range(1,total_page):
            new_url = "index" + '_%d' % count + ".html"
            new_full_url = url + new_url
            print new_full_url
            pages_arary.append(new_full_url)
            count = count + 1
        return pages_arary
        
# 获取每个页面待爬取的item具体内容的链接
    def get_all_urls(self,all_pages):
       links_arary = [] #set()
       for page_url in all_pages:
           if page_url is None:
             break
           html = mySpider.getsource(page_url)
           if html is None:
             break
           # print 'start-- : %s ' % html 
           soup = BeautifulSoup(html, "html.parser",from_encoding='utf-8') 
           content = soup.find('div',class_="co_content8")
           if content is None:
              continue
           links = content.find_all('table')
           for link in links:
             if link.get_text() is not None:
                # print type(link)
                # print len(link.contents)

                # 装一下数据的字典
                link_dic = {}

                # 时间，日期
                t_time = ""

                # 简介
                t_info = ""

                # 标题
                t_title = ""

                # 链接
                t_url = ""

                for sub_link in link.find_all('td'):
                    if sub_link is None or sub_link == '':
                        continue
                    tag_a = sub_link.find('a')
                    if tag_a is None:
                      titleStr = sub_link.get_text().replace(" ","").replace("\"","\'").replace("\t","").replace('\n','').replace(' ','').strip().lstrip().rstrip(',')   
                      if "日期" in titleStr:
                        t_time = titleStr
                      else:
                        t_info = titleStr
                      # continue
                    # 类别的名称
                    else: 
                        t_title = sub_link.get_text().strip('\n').replace(" ","").replace("\"","\'").replace("\t","").replace('\n','').replace(' ','').strip().lstrip().rstrip(',')
                        # 类别对应的链接地址
                        new_url = tag_a['href']
                        t_url = urlparse.urljoin(page_url,new_url)
                link_dic["time"] = t_title
                link_dic["info"] = t_info
                link_dic["title"] = t_title
                link_dic["url"] = t_url

                print "---title:%s" % t_title
                links_arary.append(link_dic)
       return links_arary

#解析具体的数据
    def parse_html_data(self,link_dic):
     t_time = link_dic["time"]
     t_info = link_dic["info"]
     t_title = link_dic["title"]

     t_url = link_dic["url"] # 带爬去下载地址的文件

     html = mySpider.getsource(t_url)
     if html is None:
        return

     res_array = []

     soup = BeautifulSoup(html, "html.parser",from_encoding='utf-8') 

     content = soup.find('div',class_="co_content8")
     if content is None:
        return
     links = content.find_all('table')
     for link in links:
        res_data = {}
        url = link.get_text().replace(" ","").replace("\"","\'").replace("\t","").replace('\n','').replace(' ','').strip().lstrip().rstrip(',')   
        # print 'url:%s' % url 
        # ftp://bbs.forlu.com_free:forlu_2ra6r@ftp.forlu.com/new/03.12/" target="_blank
        url = url.replace("\" target=\"_blank","").replace("<a%20href=\\","").replace("\\","\\\\")
        sql = "insert into DYURL (tv_name,tv_iconUrl,tv_state,tv_viewcount,tv_type,tv_dub,tv_showtime,tv_updatetime,tv_info,tv_downType,tv_downSeries,tv_downSeries_url) \
             values (\"%s\",'%s',\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % (t_title,"","",t_time,"","","",t_time,t_info,"", "", url)
        res_data["sql"] = sql
        # print sql
        res_array.append(res_data)
     return res_array
 
if __name__ == '__main__':
    fout = open('output_dy.sql','w')
    fialCount = 1
    count = 1
    classinfo = []
    # url = 'http://www.dy2018.com/html/dongman/'
    url = 'http://www.dy2018.com/6/'
    mySpider = spider()
    all_pages = mySpider.get_all_pages(url,36) #所有的页面
    all_links = mySpider.get_all_urls(all_pages)
    for link_dic in all_links:
        try:
            res_array = mySpider.parse_html_data(link_dic)
            for res_data in res_array:
                fout.write(res_data["sql"].encode('utf-8') + '\n')
                print 'success:%d' % (count)
            count = count +1
        except Exception as e:
            print '-- Craw fail %d ,excepton:%s' % (count,e)
            if fialCount == 10200:
                fout.close()
                break
            fialCount = fialCount + 1
            count = count +1
            fout.write("-- Craw fail %d " % count + '\n')
    fout.close()
 






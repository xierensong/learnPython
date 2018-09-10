import requests
import re
import sys
import os

from lxml import etree


class spider(object):

    # 获取url对应的网页源码
    def getSource(self,url):
        headers = {"User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        sourceHtml = requests.get(url, headers=headers)
        print(headers)
        return sourceHtml.text

    # 从html中解析我们需要的数据
    def getNeedInfo(self, sourceHtml):
        currentAllInfo = []
        selector = etree.HTML(sourceHtml)
        #titles = selector.xpath('//dl[@class="blog_list clearfix"]//dd')
        titles = selector.xpath('//ul[@class="feedlist_mod home"]/li[@data-type="blog"]')
        # print(titles)

        for vs in titles:
            singlePageInfo = {}
            # info = vs.xpath('h3[@class="tracking-ad"]/a/text()') li[@data-type="blog"]/div/div/h2/a/text()
            info = vs.xpath('div/div/h2/a/text()')
            #if len(info):
            #   break
            print("标题:" + info[0].strip())
            singlePageInfo['title'] = info[0].strip()
            # time = vs.xpath('div[@class="blog_list_b clearfix"]/div[@class="blog_list_b_r fr"]/label/text()')
            # print("时间:" + time[0])
            # singlePageInfo['time'] = time[0]
            # readCount = vs.xpath('div/div/p[@class="num"]/text()')
            readCount = vs.xpath('div/dl/div[@class="interactive floatR"]/dd[@class="read_num"]/a/span[@class="num"]')
            print("阅读次数:" + readCount[0].text)
            currentAllInfo.append(singlePageInfo)
        print(currentAllInfo)


if __name__ == '__main__':
    spider = spider()
    url = "https://projects.apache.org/projects.html?language"
    allPage = []
    allPage.append(url)
    allPageInfo = []
    for link in allPage:
        print('正在处理：' + link)
        sourceHtml = spider.getSource(link)
        print(sourceHtml)
        spider.getNeedInfo(sourceHtml)
        os.system("pause")
    print("===hello word===")
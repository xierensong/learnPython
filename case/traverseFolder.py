import requests
from lxml import etree

if __name__ == '__main__':

    # 目录页面处理
    download_urls = []
    download_urls.append('http://www.apache.org/dist/zookeeper/')

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36'}
    sourceHTML = requests.get(download_urls[0], headers=headers)
    print('sourceHTML ', sourceHTML.text)

    folder_selector = etree.HTML(sourceHTML.text)
    # 选择第一个pre元素所有的带href属性的a元素
    folder_lists = folder_selector.xpath('//pre[position()=1]/a[@href]')
    # print('folder_lists: ', folder_lists)

    versions = []
    for elmt in folder_lists:
        # 遍历folder list
        href = elmt.get('href')
        if href[len(href) - 1] == '/':
            versions.append(href[:-1])
    for x in versions:
        print('x ', x)

    # 生成版本包路径
    version_URLs = []
    # 遍历版本包，排除第一个'parent directory'
    for x in versions[1:]:
        version_URLs.append(download_urls[0] + x + '/')

    for x in version_URLs:
        print('x', x)

    # 逐版本包路径下载版本
    for url in version_URLs:
        sourceHTML = requests.get(url, headers=headers)
        file_selector = etree.HTML(sourceHTML.text)
        file_lists = file_selector.xpath('//pre[position()=1]/a[@href]')
    files = []
    for elmt in file_lists:
        # 遍历file list
        file_href = elmt.get('href')
        print('file_href ', file_href, file_href[-2:])
        if file_href[-2:] == 'gz':
            files.append(file_href)
    for x in files:
        print('x ', x)




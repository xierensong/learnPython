import requests
from lxml import etree

if __name__ == '__main__':
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://www.apache.org/dist/ant/'
    sourceHTML = requests.get(url, headers = headers)
    selector = etree.HTML(sourceHTML.text)
    folder_list = selector.xpath('//pre[position()=1]/a[@href]')
    for elmt in folder_list:
        #
        href_TT = elmt.get('href')
        print('href_TT ', href_TT)
        if href_TT[len(href_TT)-1] == '/':
            print('folder_list', elmt.attrib)
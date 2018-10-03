#encoding:utf-8
'''
Created on 2018年9月11日

@author: aa
'''
import os
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#建立Chrome driver
chrome_driver_path = r"H:\Program Files\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
m = 1
#读取文件
f = open(r"C:\Users\aa\Desktop\text\FRAttachment\FRAttachment_xerces-for_java_xml_parser.csv")
line = f.readline()
while line:
    st = line.split(",")
    if (st[1]!=None or st[1]!=0) and ('jira' in st[1])and(re.match(r'^https?:/{2}\w.+$', st[1])):
        driver.get(st[1])
        patch = driver.find_element_by_tag_name("pre")
        path = r"C:\Users\aa\Desktop\text\FRAttachment\FRAttachment_xerces-for_java_xml_parser\\"+st[0]
        #要写入的文件         
        if not os.path.isdir(path):
            os.makedirs(path)
            m = 1
        filePath = path+"\\patch"+str(m)+".txt"
        file = open(filePath,mode='w',encoding='utf-8')
        file.write(patch.text)
        m = m+1
        print(patch.text)
    line = f.readline()
    
print("-----------end-------------")
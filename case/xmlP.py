# code=utf-8
'''
 process xml plugin filed
'''

from pathlib import Path
from lxml import etree
from io import StringIO

xml_file = Path('../data/pom.xml')

xml_content = xml_file.read_text()
# print('xml content: ', xml_content)

# etree.tostring(xml_content, encoding='UTF-8')
root = etree.XML(xml_content)

plugin_list = root.xpath('/build/plugins')

print('plugin list: ', list(plugin_list))



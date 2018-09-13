from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''

html = etree.HTML(text)

print('text: ', etree.tostring(html, pretty_print=True))

result = html.xpath('//li')
# result = etree.tostring(new_html)
print('result: ', result)
print('result length: ', len(result))
for x in result:
    # 获取某个tag的具体属性值，如class属性的名字
    # (方法1)使用x.get获取某属性值
    print('x: ', x.get('class'), x.get('id'), x.tag)
    # (方法2)使用x.attrib获取属性列表字典
    attributes = x.attrib
    print('x: ', attributes['class'])
    # （方法3)使用x.attrib获取属性列表，dict格式化.items方法返回所有属性信息
    d = dict(x.attrib)
    print('x: ', d.items())
    print('x\'s path: ', html.getpath(x))

result1 = html.xpath('//text()')
print('result1: ', result1)

root = etree.Element("root")
etree.SubElement(root, 'child').text = 'Child 1'
etree.SubElement(root, 'child').text = 'Child 2'
etree.SubElement(root, 'another').text = 'Child 3'

print('construct html: ', etree.tostring(root, pretty_print=True))


# code=utf-8
'''
 process xml plugin filed
 with namespace
'''

from pathlib import Path
from lxml import etree
from io import StringIO

xml_file = Path('../data/pom2.xml')

xml_content = xml_file.read_text()
# print('xml content: ', xml_content)

# etree.tostring(xml_content, encoding='UTF-8')
#xml_tree = etree.parse('../data/pom.xml')

parser = etree.XMLParser(ns_clean=True, remove_blank_text=True)
try:
    xml_tree = etree.parse('../data/pom1.xml')
except etree.XMLSyntaxError as e:
    print(str(e.error_log.last_error))
    pass

# print('root xml_version', xml_tree.docinfo.xml_version)
# print('root ', xml_tree.getroot())
root = xml_tree.getroot()
# print(etree.tostring(root, pretty_print=True))
# 获取groupId
groupIds = []
groupId_list = root.xpath('/ns:project/ns:dependencyManagement/ns:dependencies/ns:dependency/ns:groupId',
                           namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
for groupId in groupId_list:
    print('child', etree.tostring(groupId, pretty_print=True))
    print('child', groupId.text)
    groupIds.append(groupId.text)
print('groupId length', len(groupIds))

# 获取artifactId
artifactIds = []
artifactId_list = root.xpath('/ns:project/ns:dependencyManagement/ns:dependencies/ns:dependency/ns:artifactId',
                         namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
for artifactId in artifactId_list:
    print('child', etree.tostring(artifactId, pretty_print=True))
    print('child', artifactId.text)
    artifactIds.append(artifactId.text)
print('artifactId length', len(artifactIds))

# 获取version
versions = []
version_list = root.xpath('/ns:project/ns:dependencyManagement/ns:dependencies/ns:dependency/ns:version',
                         namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
for version in version_list:
    print('child', etree.tostring(version, pretty_print=True))
    print('child', version.text)
    versions.append(version.text)
print('version length', len(versions))


# 获取plugin
plugin_list = []
plugin = {}
plugins = root.xpath('/ns:project/ns:dependencyManagement/ns:dependencies/ns:dependency',
                           namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
print('len', len(plugin_list))
for i in range(len(plugins)):

    plugin.clear()

    plugin['name'] = 'hbase-checkstyle'
    '''
    print('plugins', i, etree.tostring(plugins[i]))
    for x in plugins[i]:
        print('x', x)
    '''
    group_Id = plugins[i].xpath('ns:groupId',
                           namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
    print('group_Id', group_Id)
    if len(group_Id) == 0:
        plugin['groupId'] = 'N/A'
    else:
        plugin['groupId'] = group_Id[0].text

    artifact_Id = plugins[i].xpath('ns:artifactId',
                                namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
    print('artifact Id', artifact_Id)
    if len(artifact_Id) == 0:
        plugin['artifactId'] = 'N/A'
    else:
        plugin['artifactId'] = artifact_Id[0].text

    version_Id = plugins[i].xpath('ns:version',
                                   namespaces={'ns': 'http://maven.apache.org/POM/4.0.0'})
    print('version Id', version_Id)
    if len(version_Id) == 0:
        plugin['version'] = 'N/A'
    else:
        version_Id_text = version_Id[0].text
        if version_Id_text[0] == '$':
            version_name = version_Id_text[2:-1]
            # search for variety in xml
            for version_v in root.iter('{http://maven.apache.org/POM/4.0.0}' + version_name):
                print('version_v', version_v)
                plugin['version'] = version_v.text
        else:
            plugin['version'] = version_Id_text

    print('plugin', dict(plugin))

    plugin_list.append(plugin)

print('plugin_list length', len(plugin_list))

for javac_version in root.iter('{http://maven.apache.org/POM/4.0.0}javac.version'):
    print('javac_version:', javac_version.tag, javac_version.attrib, javac_version.text)




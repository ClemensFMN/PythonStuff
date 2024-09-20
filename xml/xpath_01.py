import lxml.etree as ET

tree = ET.parse('file_01.xml')
root = tree.getroot()

res = root.xpath(".//book[id/ida='34']/title")

for elem in res:
    print(elem.text)




import lxml.etree as ET

tree = ET.parse('file_01.xml')
root = tree.getroot()

for child in root:
    print(child.tag)
    for bk in child:
        print("....", bk.tag, "->", bk.text)



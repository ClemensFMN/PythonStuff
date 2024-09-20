import lxml.etree as ET
import glob

""" 
this script goes over all xml files in the current dir, extracts the attributes from the list `attrs`
and writes the output (together with the filename) onto the console (attribues are separated by `sep_char`)

This is handy if there are several xml files all with the same structure and we want to get an overview
over the files; ie their attribute values
"""

# TODO: Take from command line
files = glob.glob('*.xml')
# TODO: Take from command line
sep_char = ';'
# TODO get from command line or file(?), allow different namespace
attrs = [".//book/id/ida", ".//book/title", ".//book/author"]


for file in files:
    tree = ET.parse(file)
    root = tree.getroot()

    es = [root.xpath(it) for it in attrs]

    # this is somewhat unpythonic... probably more elegant to zip the iterators into one
    # num_results = len(es[0])
    # for i in range(num_results):
    #     s = file + sep_char
    #     for j in range(len(attrs)):
    #         e = es[j][i].text
    #         s = s + e + sep_char
    #     print(s)

    # this does not work
    esiters =zip((*es,))

    for e in esiters:
        print(e)

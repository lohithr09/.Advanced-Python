# xml Parsing by using xml.dom(minidom) package in python.
from xml.dom import minidom

xmldoc = minidom.parse('/home/affine/iput_data/items.xml')

itemlist = xmldoc.getElementsByTagName('item')

print(len(itemlist))

print(itemlist[0].attributes['name'].value)

for s in itemlist:
    print(s.attributes['name'].value)
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement

tree = ET.ElementTree(file='alajuelacalles.osm')

root = tree.getroot()


# price - raise the main price and insert new tier
for elem in tree.iterfind('way'):
    for subelem in tree.iterfind('tag'):
        print(subelem.attrib)
    print("_________________________________________________________")
#     for elem in root:
#         for subelem in elem:
#        print(subelem.attrib)
    #price = elem.text
    #newprice = (float(price.replace(",", ".")))*1.2

    #newtier = "NEW TIER"
    #SubElement(root[0][pos][5], newtier)
    #pos+=1

#tree.write('pricelist.xml', "UTF-8")

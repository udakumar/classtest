import xml.etree.ElementTree as ET
import pdb


tree = ET.parse(r'C:\Users\Admin\Downloads\sample.xml')

#pdb.set_trace()
doc = tree.getroot()

#print(doc.tag)  --> reading data from tag
#print(doc.attrib) --> Null

#for rec in doc.iter('recor
#   print(rec.attrib)

# for rec in doc.iter('record'):
#     print(rec.attrib)
#     print(rec.find('Age').text)
#     print(rec.find('First_Name').text)
#
# for rec1 in doc.iter('Country'):
#     print(rec1.text)
#
# for rec2 in doc.iter('columns'):
#     print(rec2.find('Age').attrib)
#     print(rec2.find('Id').attrib)
#
# for rec4 in doc.iter('Age'):
#     for i in rec4.iter('Age'):
#         print(i.text)
# for rec5 in doc.iter('records'):
#     print(rec5.keys())


# for rec5 in doc.iter('records'):
#     new = int(rec5.text) + 1
#     rec5.text = str(new)
#     rec5.set('updated', 'yes')
#
# tree.write(r'C:\Users\Admin\Desktop\sample.xml')
# print(doc[0].tag)
# for y in doc[0]:
#     print(y.tag, y.attrib)
#
# print(doc[1].tag)
# for y in doc[1]:
#     print(y.tag, y.attrib)

#reading
# for a in doc[1].iter('record'):
#     age = a.find('Age').text
#     name = a.find('First_Name').text
#   print(age, name)

# writing
# ET.SubElement(doc[0], 'NewID')
# for  x in doc[0].iter('NewID'):
#     b = "NEW ID"
#     x.text = str(b)
#
# tree.write(r'C:\Users\Admin\Desktop\new2.xml')

#wrirint individual
# for y in doc[1][0].iter('record'):
#     age = y.find('Age').text
#     d = int(age) + 2
#     y.find('Age').text  = str(d)
#
# tree.write(r'C:\Users\Admin\Desktop\new4.xml')








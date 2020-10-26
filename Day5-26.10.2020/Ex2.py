import xml.etree.ElementTree as ET
import base64

tree = ET.parse('corect_task2.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for child in root:
    if child.tag == "request":
        print(child.attrib)
        print(child.text)
        print(base64.b64decode(child.text))

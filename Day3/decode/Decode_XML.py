import xml.etree.ElementTree as ET
import sys
import base64
from os import name


class Decode_XML:
	def __init__(self, fisier):
		self.xml = fisier

	def read_from_xml(self):
		self.tree = ET.parse(self.xml)
		#print("Am intrat in metoda de read", self.tree)

	def decode_XML(self):
		self.read_from_xml()
		root = self.tree.getroot()
		for child in root:
			if child.tag == "request":
				print(base64.b64decode(child.text))
if __name__ == "__main__":
	# print(sys.argv[1])
	variabila = Decode_XML(sys.argv[1])
	# print(variabila.xml)
	variabila.read_from_xml()
	variabila.decode_XML()



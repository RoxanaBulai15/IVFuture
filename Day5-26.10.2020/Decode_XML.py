import xml.etree.ElementTree as ET
import argparse
import base64
from os import name


def parse_args():
	parser = argparse.ArgumentParser(description='Start application')

	parser.add_argument("--xml",
						dest="xml",
						required=True,
						help="I needed an folder what contains xml files")

	return parser.parse_args()


class Decode_XML:
	def __init__(self, fisier):
		self.xml = fisier

	def read_from_xml(self):
		self.tree = ET.parse(self.xml)

	def decode_XML(self):
		self.read_from_xml()
		root = self.tree.getroot()
		for child in root:
			if child.tag == "request":
				print(base64.b64decode(child.text))


if __name__ == "__main__":

	args = parse_args()
	xml_path = args.xml
	print(xml_path)
	variabila = Decode_XML(xml_path)
	# print(variabila.xml)
	variabila.read_from_xml()
	variabila.decode_XML()






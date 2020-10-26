import xml.etree.ElementTree as ET
import argparse
import base64
from os import name
import xlwt
from xlwt import Workbook
import logging

logging.basicConfig(filename="log_corect_task2.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


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
		logging.info("Fisierul xml a fost citit!")

	def decode_XML(self):
		self.read_from_xml()
		root = self.tree.getroot()
		for child in root:
			if child.tag == "request":
				logging.info("Cuvantul a fost gasit si textul este decodat: ")
				logging.info(base64.b64decode(child.text))
			else:
				logging.warning("Acesta nu este cuvantul cautat!!!")


if __name__ == "__main__":

	args = parse_args()
	xml_path = args.xml
	print(xml_path)
	variabila = Decode_XML(xml_path)

	variabila.read_from_xml()
	variabila.decode_XML()






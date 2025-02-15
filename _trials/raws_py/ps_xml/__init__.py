"""
# PS_xml (ps_xml)
This module extends builin minidom functionalty to be more handy
"""


import subprocess, os, sys
import xml.dom.minidom as mdom

class ps_Xml_Document(mdom.Document):
	"""
	this class extends minidom functionality with varos function. Check docs to decide if you need it
"""
	def __init__ (self):
		return super().__init__()

	def getChildByTagName(self, parent:mdom.Node, childTag:str)->mdom.Node|NoneType:
		children=parent.childNodes
		for cn in children:
			if cn.nodeName==childTag:
				return ch
		return None
				
def ps_xml_parseString (self, xml_str: str)->ps_xml_Document:
	doc=mdom.parseString(xml_str)
	
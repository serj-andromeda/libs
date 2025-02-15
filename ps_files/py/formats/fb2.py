__doc__="""
This module contains classes for working with .fb2 format files
See: https://en.m.wikipedia.org/wiki/FictionBook
"""


from . import PS_FileFormat
#import xml.etree.ElementTree as ET
import xml.dom.minidom as mdom
import ps_funcs, shcolar
import os, sys, re


unkn_str="@fb2_unknown"
default_encoding_str="utf-8"


eol="\n"


class fb2():

	def _set_defaults (self):
		self.getset_filename_str(None)
		self.getset_encoding_str(self.default_encoding_str)
		
		self.config = {
			"str": {
				"title": True,\
				"author": True,\
				"genre": True,\
				"serie": True,\
				"annotation": True,
			},
			"encoding": self.default_encoding_str,
		}		

	def getset_filename_str(self, filename_str:str|None=None)->str|None:
		"""
		Return filename, given if provided or from config otherwise
		"""
		if filename_str is not None:
			self.filename_str=filename_str
			return filename_str
		if self.filename_str is not None:
			return self.filename_str
		else:
			return self.unkn_str #return unkn_str by default. Most likely this will lead to FileNotFound exception. It's ok since either argument of this function or object should contains filename


	def getset_encoding_str(self, encoding_str:str|None=None)->str:
		"""
		Return encoding, given if provided or from config otherwise
		"""
		if encoding_str is not None:
			self.encoding=encoding_str
			return encoding_str
		if self.encoding_str is not None:
			return self.encoding_str
		else:
			return default_encoding_str #return unk

	def __init__ (self):
		self._set_defaults()
		self.mdxml_elems=dict()
		self.title=unkn_str
		self.author_lst=[]
		self.genre_lst=[]
		self.annotation=unkn_str


	def detect_encoding (self, filename_str:str|None, initial_encoding_str="cp1252")->str:
		"""
		Detects encoding using initial_encoding for initial read
		"""
		fn_str=self.getset_filename_str(filename_str)
		line1=''


		with open (fn_str, encoding=initial_encoding_str) as in_fp:
			line1=in_fp.readline().strip()
		if line1=='':
			raise ps_funcs.PSException("Could not read 1st linebofvfile to detect encoding", fatal=True)
		
		
		rx_enc_pcre_str="encoding=(['\"])(?P<enc>[^'\"]+)\\1"
		m_match = re.search (rx_enc_pcre_str, line1)
		if m_match is None:
			print (f"@ps No encoding info found in '{fn_str}'. Line1 and pcre below.")
			print ("@ps Line1:", line1)
			print ("@ps pcre:", rx_enc_pcre_str)
		else:
			print ("@ps enc_match_dict", m_match.groupdict())
			gd_dict=m_match.groupdict()
			encoding_str=gd_dict["enc"]
			encoding_str=encoding_str.replace("windows-", "cp")
			print ("@ps encoding:", encoding_str)
			return self.getset_encoding_str(encoding_str)
		
		

	def read_file (self, filename_str=None, encoding_str=None)->bool:
		"""
		Reads file from self.config["filename"] and fill it content to self.content

		Return True on success, False otherwise
		"""
		filename_str=self.getset_filename_str(filename_str)
		if encoding_str is None:
			return read_file (filename_str, encoding_str)
		else:
			res_read_file_bool=super().read_file(filename_str)
			return res_read_file_bool

	def parse(self)->bool:
#		print ("start fb2 parse method")
		if not type(self.content) is str:
			print ("Error: content in fb2 class is not string but", type(self.content),". Only string parsing supported.")
			return False
		xml_str=self.content
		doc=mdom.parseString(xml_str)
		self.mdxml_elems["doc"]=doc
		root_el=doc.documentElement

		self.mdxml_elems["root"]=root_el
		root_children=root_el.childNodes
		self.mdxml_elems["root_childs"]=root_children
		desc_el=ps_funcs.getChildByTagName(root_el, "description")
		self.mdxml_elems["desc"]=desc_el
		titleinf_el=ps_funcs.getChildByTagName(desc_el, "title-info")
		self.mdxml_elems["titleinf"]=titleinf_el
		genre_el_lst=ps_funcs.getChildrenByTagName_node_lst(titleinf_el, "genre")
		author_el_lst=ps_funcs.getChildrenByTagName_node_lst(titleinf_el, "author")
		self.mdxml_elems["genre_lst"]=genre_el_lst
		self.mdxml_elems["author_lst"]=author_el_lst
		for gel in genre_el_lst:
			genre_str=ps_funcs.getNodeText_str(gel)
			self.add_genre_str (genre_str)
		for autel in author_el_lst:
			author_str=ps_funcs.getFullPersonName_str(autel)
			self.add_author_str (author_str)
		title_el=ps_funcs.getChildByTagName(titleinf_el, "book-title")
		title_str=ps_funcs.getNodeText_str(title_el)
		self.title=title_str



	def  get_title_str(self)->str:
		return self.title
		
	def  get_author_str(self)->str:
		return  ", ".join(self.author_lst)


	def  get_author_lst(self)->list:
		return self.author_lst
		
		
	def add_author_str (self, val:str):
		self.author_lst.append (val)

	def  get_genre_str(self)->str:
		return ", ".join(self.genre_lst)

	def  get_genre_lst(self)->list:
		return self.genre_lst
		
	def add_genre_str (self, val:str):
		self.genre_lst.append (val)


	def  get_annotation_str(self)->str:
		return self.annotation

	def  get_str_includes_annotation_bool(self)->bool:
		return self.str_includes_annotation


	def  set_str_includes_annotation_bool(self, val):
		self.str_includes_annotation=val

	def __str__ (self)->str:
#		print ("start fb2 str method")
		res="Title: "+self.get_title_str()+eol+\
		"Author: "+self.get_author_str()+eol+\
		"Genre: "+self.get_genre_str()+eol+\
		("Annotation: "+self.get_annotation_str()+eol if self.get_str_includes_annotation_bool() else "")+\
		eol
		return res
		
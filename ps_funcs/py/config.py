import os,sys,configparser
import ps_funcs, ps_shcolar








class PSConfig (configparser.ConfigParser):





	def __init__ (self, filename: str):
		self.filename=filename
		self.parse()
		
	def parse (self, filename: str|None=None)->bool:
		if filename is None:
			if self.filename is None:
				raise PSException ("Filename should be passed to PSConfig either by constructor or to parse function", colorize=True, fatal=True)


	def get (self, path: str|tuple)->str:
	
		res = ""
		if isinstance(path, tuple):
			res+="tuple got: "+str(path)
		elif isinstance (path, str):
			res+="str got: "+str(path)
		else:
			res +="wrong type got: "+str(type(path))
		return "just test as for "+res
	
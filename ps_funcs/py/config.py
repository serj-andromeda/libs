import os,sys,configparser
import ps_funcs, ps_shcolar








class PSConfig (configparser.ConfigParser):





	def set_filename (self, filename_str: str):
		self.filename=filename_str

	def get_filename (self)->str:
		return self.filename

	def __init__ (self, filename_str: str):
		self.set_filename (filename_str)
		self.parse()
		
	def parse (self, filename_str: str|None=None)->bool:
		if filename_str is not None:
			self.set_filename (filename_str)
			if self.get_filename_str() is None:
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
	
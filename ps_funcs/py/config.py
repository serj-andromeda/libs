import os,sys,configparser
import ps_funcs, ps_shcolar




ps_funcs_config_verbose_level_str='dbg'



class PSConfig (configparser.ConfigParser):





	def set_filename (self, filename_str: str):
		self.filename=filename_str

	def get_filename (self)->str:
		return self.filename

	@classmethod
	def default_config_dn (cls)->str:
		from . import path
		return path.get_homedir_str()

	@classmethod
	def default_config_fn (cls)->str:
		return '.ps_config.ini'

	@classmethod
	def get_default_separator_str (cls)->str:
		return '/'


	@classmethod
	def default_config_absfn (cls)->str:
		return os.path.join (cls.default_config_dn(), cls.default_config_fn())


	def __init__ (self, filename_str: str|None=None):
		super().__init__()
		if filename_str is None:
			filename_str=self.default_config_absfn()
		self.set_filename (filename_str)
		self.parse()
		
	def parse (self, filename_str: str|None=None)->bool:
		if filename_str is not None:
			self.set_filename (filename_str)
			if self.get_filename_str() is None:
				raise PSException ("Filename should be passed to PSConfig either by constructor or to parse function", colorize=True, fatal=True)


	def get (self, path: str|tuple)->str:
	
		res = ""
		sep=self.get_default_separator_str()
		if isinstance (path, str):
			if sep in path:
				path=tuple(path.split(sep))
			else:
				raise PSException ("No separator '{sep}' found in string '{path}' passed to PSConfig.get", colorize=True, fatal=True)
			
		
		if isinstance(path, tuple):
			res+=f"tuple got in {__class__}: "+str(path)
		else:
			res +="wrong type got: "+str(type(path))
		return "just test as for "+res
	
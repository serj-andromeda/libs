import traceback, os, sys
import ps_zip, shcolar, ps_funcs
class PS_FileFormat:



	def _setConfigDefaults(self):
		self._config=dict()

	def get_filename_str(self)->str:
		return self.filename
		
	def set_filename(self, filename):
		print ("@ps_ff_setfn:", filename)
		self.filename=filename
		
	def get_content_misc(self):
		print ("@start method ps_ff_getcontent")
		return self.content
		
	def set_content(self, content):
		print ("@start method ps_ff_setcontent")
		self.content=content
		
	def read_file_bool (self, filename_str=None, *, dontDecode:bool=True, isBinFile:bool=False, encoding:str="utf-8")->bool:
		"""
		Reads file from self.filename and fill it content to self.content
		Return True on success, False otherwise
		"""
		print (shcolar.fg.brightGreen+"@ps start ff.read_file_str method"+shcolar.reset)
		if filename_str is None:
			filename_str=self.getFilename()
		if filename_str is None:
			raise ps_funcs.PSException ("filename_str passed to fb2.read_file is None both with self.filename", fatal=True)
		print ("@ps ps_fileformat_read_file fn:", filename_str)
		
		try:
			if filename_str.endswith(".zip"):
				filename_str+=":#0"
			else:
				file_access_sfx_str="b" if isBinFile else "t"
				file_access_mode_str="r"+file_access_sfx_str
				f=open(filename_str, file_access_mode_str)
				print ("@ps ### acmd: "+file_access_mode_str)
				content_str=f.read()
				self.set_content(content_str)
				
				print ("@ps @@@ dontDecode:"+str(dontDecode)+" isbinfile:"+str(isBinFile), "dec:", str(not dontDecode and not isBinFile))
				print ("content type: ", type(self.get_content_misc()))
				if not dontDecode and not isBinFile:
					self.setContent(self.getContent().decode(encoding))
				f.close()
		except Exception as e:
			print (shcolar.fg.brightRed+"Exception:in readFile while reading/decoding:", e)
			print ("info from traceback:")
			traceback.print_exc()
			print (shcolar.reset)
			return False
		return True
		
		
		
	def __init__ (self):
		self.filename=None
		self.content=None
		self._setConfigDefaults()
	
	def parse (self):
		"""
		This method MUST be overriden in concrete realizations.
		It's for parsing self.content and filling appropriate fields
		"""
		pass
		
	def process_file_bool (self, filename_str: str, *, do_print_bool=True, colorize_bool=True)->bool:
		"""
		Set filename and parse correspoding file
		"""
		read_file_res_bool=self.read_file_bool(filename_str)
		if not read_file_res_bool:
			return False
		parse_res_bool=self.parse()
		if not parse_res_bool:
			return False
		if do_print_bool:
			if colorize_bool:
				print (color_esc_ccode_str+self+shcolar.reset)
			else:
				print (self)
		return True

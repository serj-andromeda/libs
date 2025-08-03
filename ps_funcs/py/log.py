"""
This module contain functions for logging functionality.
Most of logging parameters configurable through function arguments.
"""
import os, sys; import ps_funcs, ps_shcolar

class PSLog:
	def process_tpl(self, tpl:str)->str:
		pass
	def set_fn_tpl (self, fn_tpl:str):
		self._fn_tpl=fn_tpl
	def set_dn_tpl (self, dn_tpl:str):
		self._dn_tpl=dn_tpl
	def get_fn_tpl (self)->str:
		return self._fn_tpl
	def get_dn_tpl (self)->str:
		return self._dn_tpl
	def set_line_tpl (self, line_tpl:str):
		self._line_tpl=line_tpl
	def set_tag (self, tag_str:str):
		self._tag_str=tag_str
	def __init_ (self, log_dn_tpl: str, tag_str: str, line_tpl: str):
		self.set_dn_tpl (log_dn_tpl)
		self.set_fn_tpl (log_fn_tpl)
		self.set_line_tpl (line_tpl)
	def log (self, msg):
		pass
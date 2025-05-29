"""
This module contain functions for work with paths.
No matter it is path to file or some folder.
"""
import os, sys; import ps_funcs, ps_shcolar

def expand_dirs_str (dn:str)->str:
	"""
	This is an alias for native os.path.expanduser functon jusr because it's nsme is lame
	"""
	return os.path.expanduser(dn)


def is_fn_absolute (fn: str)->bool:
	"""
	Simple check if given filename is absolute
	Checks if first symbol is slash
	NOTE: this function most likely won't work on Windows machines cause there absolute paths started with drive letter
	"""
	return fn[0]=="/";
	
	
	
	
	
	
	
	
	
def get_homedir_str()->str:
	"""
	Just return home dir of user from hosts OS
	"""
	return os.getenv ("HOME");
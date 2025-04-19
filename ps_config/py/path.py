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


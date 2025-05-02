"""
Module with functions for working with
various structurrs like dicts, lists, tuples etc.
"""
from encodings import *

#@ps section list functions
def list_get (lst_list, index_int: int, default=None):
	"""
	Safe get value of list by index returning default value if index out of range
	"""
	try:
		return lst_list[index_int]
	except:
		return default

def strip_list_items (lst:list)->list:
	"""
	Apply `strip` method to every element in list
	"""
	return [li.strip() for li in lst]
#@ps /section list functions

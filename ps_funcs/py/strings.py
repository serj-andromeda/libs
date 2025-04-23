"""
Module with functions for working with strings
"""

import os, sys, re

def split_text_by_seplist_list (text: str, sep_list=[' ', '\n'])->list:
	"""
	Split given text by separators in sep_list (default - spaces and line breaks
	"""
	text=text.strip()
	rx_seps_rxstr='|'.join(map(re.escape, sep_list))

	print ("@ps repr of rxseps", repr(rx_seps_rxstr))
	text_list=re.split(rx_seps_rxstr, text)
	return text_list










def wrap (text:str, width:int=20, *, sep_list=[' ', '\n'])->str:
	"""
	Function that breaks trxt into
	srparate words and try to fit'em
	in desired width
	"""
	text_list=split_text_by_seplist_list(text, sep_list)
	
	print ("@ps text_list:", text_list); exit;
	
	res=""
	res_list=[]
#	for w in text_list:
#		res +=(sep if res!='' else '')+w
	
	
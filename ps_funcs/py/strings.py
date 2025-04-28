"""
Module with functions for working with strings
"""

import os, sys, re, ps_funcs

def split_text_by_seplist_list (text: str, sep_list=[' ', '\n'])->list:
	"""
	Split given text by separators in sep_list (default - spaces and line breaks
	"""
	text=text.strip()
	rx_seps_rxstr='|'.join(map(re.escape, sep_list))

	text_list=re.split(rx_seps_rxstr, text)
	return text_list










def wrap (text:str, width_int:int=20, *, sep_list=[' ', '\n'], newsep_str=' ', newlinesep_str='\n', do_strip_before_process=True)->str:
	"""
	Function that breaks trxt into
	srparate words and try to fit'em
	in desired width
	"""
	text_list=split_text_by_seplist_list(text, sep_list)
	
#	print ("@ps text_list:", text_list); exit;
	
	res_list=[]
	row_list=[]
	for w in text_list:
		row_str=newsep_str.join(row_list)
		new_len_int = len (row_str)+len(newsep_str)+len(w)
		if new_len_int>width_int:
			continue
		else:
			row_list.append(w)
			row_str=newsep_str.join(row_list)
			res_list.append(row_str)
	res_str=newlinesep_str.join(res_list)
	return res_str







def gen_nums_str (start_int:int|None=None, stop_int:int|None=None, step_int:int|None=None):
	"""
	Generate string with digits ending numbers from start_int to stop_int (exclusive)
	
	Trying the best to simulate `range` arguments behavior). Should worksvforvall cases sincevargs actually passing to `range` function but in the case please let me know.
	"""
	rng_args_lst=ps_funcs.args_to_list_lst (start_int,  stop_int, step_int)
	if len(rng_args_lst)==0:
		raise PSException("Cannot call func gen_nums_str without arguments", fatal=True)
	res=""
	for n in range(*rng_args_lst):
		res +=str(n%10)
	return res










def add_word (text: str, word: str, *, sep: str=' ')->str:
	if text=="":
		return word
	else:
		return text+sep+word
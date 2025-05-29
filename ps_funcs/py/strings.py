"""
Module with functions for working with strings
"""
import os, sys, re, enum
import ps_funcs

def split_text_by_seplist_list (text: str, sep_list=[' ', '\n'])->list:
	"""
	Split given text by separators in sep_list (default - spaces and line breaks
	"""
	text=text.strip()
	rx_seps_rxstr='|'.join(map(re.escape, sep_list))

	text_list=re.split(rx_seps_rxstr, text)
	return text_list




class WrapMode_enum (enum.Enum):
	BREAK_WORDS = object()
	CUT_TRAILS = object()







def str2row (text_str:str, width_int:int=20, *, txtsep_list=[' ', '\n'], wordsep_str=' ', linesep_str='\n', do_strip_before_process_bool=True, linecont_str='…')->tuple:
	"""
	Function that breaks trxt into
	srparate words and try to fit'em
	in desired width.
	It returns tuple of two strings: first is portion of text that should be printed on current row and second is thevrest of string
	"""
	





def wrap_str (text_str:str, width_int:int=20, *, txtsep_list=[' ', '\n'], wordsep_str=' ', linesep_str='\n', do_strip_before_process_bool=True, linecont_str='…')->str:
	"""
	Function that breaks text into
	srparate words and try to fit'em
	in desired width
	"""
	if do_strip_before_process_bool:
		text_str=text_str.strip()
	text_list=split_text_by_seplist_list(text_str, txtsep_list)

	print ("@ps enum text_list:", enumerate(text_list));
	
	res_list=[]
	row_list=[]
	for i, word_str in enumerate(text_list):
		print (f"@ps word #{i}: {word_str}", end=" ")
		row_str=wordsep_str.join(row_list)
		new_len_int = len (row_str)+len(wordsep_str)+len(word_str)
		if new_len_int>width_int:
			print ("@continue");
			continue
		else:
			print ("@add");
			row_list.append(word_str)
			row_str=wordsep_str.join(row_list)
			if row_str=="Lorem ipsum dolor at":
				print (f"@ps catch bad string with index {i} and word '{word_str}'")
			res_list.append(row_str)
	res_str=linesep_str.join(res_list)
	print (f"@ps finished at index {i}. Returning from wrap_str")
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
		
		
		
		
		
		
		
		
unicode2ascii_dict={
ord("\u302f") : ord(" ")
}

def func_translate_str (txt_str: str, translate_dict: dict = unicode2ascii_dict)->str:
	"""
	Functional replacement of `translate` method to use in `map` and similar functions
	"""
	return txt.translate(translate_dict)
		
def func_strip_str (txt_str: str)->str:
	"""
	Functional replacement of `strip` method to use in `map` and similar functions
	"""
	return txt.strip()




def func_join_str (iterable: list|tuple, separator_str: str=',')->str:
	"""
	Converts list or tuple to string to list. Especially useful for values like RGB e.g. 0,128,0
	Note that any non-relevant symbols like whitespaces should be cleared before call. E. g. [0,128,0] - ok, but ['0 ', '128 ', '0 '] -bad
	"""
	return separator_str.join (iterable)
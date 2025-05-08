__doc__="""
This module provides funcs to work with tables printed in terminal
"""
import os, sys, re
import ps_funcs, ps_shcolar







def print_table (header_list: list, widths_list: list, data_list: list, *, sep_v_str: str|None = '|', sep_h_str: str|None = None, linecont_str: str ='…')->bool:
	"""
	This function prints table with given params
	"""
	
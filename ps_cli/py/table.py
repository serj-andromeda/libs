__doc__="""
This module designed to print tables in console
"""
_PS_table_undef_data_str="@ps undefined"; _PS_table_undef_width_int=len(_PS_table_undef_data_str)
import ps_funcs, shcolar




def convert_raw_var_to_print_var_str(v, *, meta_dict: dict|None=None)->str:
	"""
	Converts simgle var to printable depends on its type and/or metadata
	meta_dict contains metadata to speedup things and reduce unnecessary checks
	meta_dict sample:
	[
	
	'is_filename': True, # bool, string in v contains filename so will be shortened as path
	'bool_chars': 'YN', # string|None contains chars for bool values. If it is string, must contains exactly two chars, first for True, second for False
	"""
	return _PS_table_undef_data_str










def convert_raw_data_to_print_data_list (raw_data_list:list=[[_PS_table_undef_data_str, _PS_table_undef_data_str], [_PS_table_undef_data_str, _PS_table_undef_data_str]], width_list: list=[_PS_table_undef_width_int, _PS_table_undef_width_int], raw_data_dialect_str: str='unchanged_raw', borders_char_dict: dict={'-': '-', '|': '|', '+': '+'}, root_dn_str: str|None=None)->list:
	"""
	Convert raw data list to printable one
	
	Subj. Using `raw_data_dialect_str` to understand howbto handle raw data. Currently following dialects are supported (maybe subject of change so don't rely on this list too much):
	- bad_files
	- unchanged_raw
	You are free to add your own dialects if need it
	"""
	print_data_list=[]
	for raw_data_line_list in raw_data_list:
		print_data_line_list=raw_data_line_list
		match raw_data_dialect_str:
			case 'unchanged_raw':
				pass
			case 'bad_files':
				if root_dn_str is None:
					raise ps_funcs.PSException ("You MUST specify `root_dn_str` param while calling `print_table` function in `ps_cli` module` with `bad_files` dialect", fatal=True)
				# get rel fn basedvonbabs fn and root info in raw data list
				raw_data_line_list[0]=ps_funcs.get_rel_fn_str( raw_data_line_list[0], root_dn_str)
				# cut non-printable info in raw data list
				print_data_line_list=raw_data_line_list[:5]
			case _:
				raise ps_funcs.PSException ("Unknown dialect",raw_data_dialect_str,"passed to convert_raw_data_to_print_data_list", fatal=True)
		print_data_list.append (print_data_line_list)
	return print_data_list


def print_table_row (row_data_list:list, width_list:list):
	"""
	Prints row of table or border depends on what data passed
	"""

def print_table (header_list:list, width_list: list, raw_data_list: list, *,
		border_char_dict: dict={'-':'-', '|': '|', '+': '+'},
		raw_data_dialect_str='unchanged_raw',
		print_data_list: list|None=None,
		root_dn_str: str|None=None):
	"""
	
	Function for print table in console
	
	Prints table in console like below:
	
	+--------+-----+-----+-----+
	|long…hea|  1  |  2  |  3  |
	+--------+-----+-----+-----+
	|long…dat| d1  |  d2 |  d3 |
	+--------+-----+-----+-----+
	
	"""
	print (shcolar.fg.brightMagenta+"@ps start in_funcs_print_table, head, widths, raw_data_lst, border_chars, dialect", header_list, width_list, raw_data_list, border_char_dict, raw_data_dialect_str)

	if print_data_list is None:
		print_data_list= convert_raw_data_to_print_data_list (raw_data_list, width_list, raw_data_dialect_str, border_char_dict, root_dn_str)
	print (shcolar.fg.brightGreen+"@ps print_data_list in cli.print_table after convert from raw:", print_data_list)

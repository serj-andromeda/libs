"""
# PS_funcs (ps_funcs)
This module provides various utility functions for [Python](https://python.org) programs
"""
#print ("\033[92m@ps start of ps_funcs/init")

import subprocess, os, sys, zipfile, datetime, ps_funcs, ps_shcolar
import xml.dom.minidom as mdom
import ps_cli as cli

from . import encodings


from . import shfuncs
from . import path
from . import cli

from . import files
from . import ps_csv
from . import structs
from . import strings
from . import config
from . import log





__all__=[
encodings,
cli,
#shfuncs,
path,
#files,
ps_csv,
config
]
# [@ps_section]  OS related helpers

def backtick (cmd):
	"""
	Execute command in shell and return result like backtick in shell and PHP
	Actual code moved to shfuncs.py. Here is just stub.
:param cmd: command to execute
:type cmd: str
:returns: what command cmd sends to stdout (basically just output of command)
:rtype: str
	"""
	return shfuncs.backtick(cmd);
def system (cmd: str)->int:
	"""
	Exec cmd and return exit code
	Actual code moved to shfuncs.py. Here is just stub.
	"""
	return shfuncs.system(cmd)

# [@ps_section]  CLI functions


def arg_value (arg_name_variants_str_lst : list, default : str | None=None, verbose_bool=False)->str|None:
	"""
	Function to get certain argument value
	"""
	for arg_str in sys.argv[1:] :
		arg_lst=arg_str.split ('=')
#		print ("@ps arg_lst:", arg_lst)
		if len(arg_lst)!=2:
			# most likely not argument. skipping
			if verbose_bool:
				print ("arg", arg_str, "seems like not argument. skip in ps_funcs/arg_value")
			else:
#				print ("@ps arg_value func isbnot verbose now so skipping", arg_str, "silently. Thisvpribt only for test. Safe to rm it.")
				continue
		if arg_lst[0] in arg_name_variants_str_lst:
			# found! it's argument we looking for
			return arg_lst[1]
	return default


def opt_exists (opt : str, prependDash : bool = True, singleDashPrepend=False) -> bool :
	"""
	 Check if passed option exists in CLI call
	 
	 :param opt: option name to check
	 
	 :param prependDash: whether need to prepend opt with dash or not. Default True, so opt could be passed here without dash
	 
	 :param singleDashPrepend: if prependDash arg isvtrue prepend only in option style with single dash, otherwise prepend long (with len not equal to one) options with double dash
	 
	"""
	_opt=opt
	if prependDash :
		if len(_opt)==1 or singleDashPrepend:
			_opt = "-"+_opt
		else:
			_opt = "--"+opt
	for o in sys.argv :
		if o==_opt:
			return True

	return False
	
# [@ps_section]  Files/folders functions

def file_exists (filename, dirIsOk=False)->bool:
	"""
	Check if file exists
	"""
	if dirIsOk:
		return os.path.exists(filename)
	else:
		return os.path.isfile(filename)


def strip_list_items (lst:list)->list:
	"""
	Apply `strip` method to every element in list
	"""
	return [li.strip() for li in lst]

def file_get_contents (filename, binary=False, forceZip=False, return_lst_bool:bool=False)->str|list|None:
	"""
	Function mimics PHP file_get_contents minimal behavior - reads file specified by *filename* arg and return its content.
	However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename*
	"""
	return files.file_get_contents (filename, binary=binary, forceZip=forceZip, return_lst_bool=return_lst_bool)
	
def file_put_contents (filename_fnstr, data, overwrite=False, return_none_on_exists=False)->int|None:
	"""
	Function mimics PHP file_put_contents minimal behavior - reads file specified by *filename* arg and return its content.
	However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename* and *data*
	"""
	return files.file_put_contents (filename_fnstr, data, overerite, return_none_on_exists)

# [@ps_section]  structures helpers

def dict_val (d: dict, key:str, default_val=None):
	"""
	Return value of dict by key or default passed in default_val
	"""
	return d.get(key, default_val)

def keybyval_dct (d:dict, val):
	"""
	Return key or keys in dictionary having passed value.
	In ideal case (only one key has given value returns this key,
	If no keys have given value returns None
	If more than one key have given value returns list of such keys
	"""
	keys=[k for k, v in d.items() if v==val]
	keysn=len(keys)
	if keysn==1:
		return keys[0]
	elif keysn==0:
		return None
	else:
		return keys


def var_type_str (v)->str:
	vt_w_class_str=str(type(v))
	ind_start_int=vt_w_class_str.find("\'")+1
	ind_end_int=vt_w_class_str.find("\'", ind_start_int)
	return vt_w_class_str[ind_start_int:ind_end_int]
def keybyval (d:dict, val):
	"""
	Backwrd compatibility function
	"""
	return keybyval_dct (d,val)
def keybyval_lst (l:list, val)->int:
	'''
	Return index of val in list
	'''
	res=-1
	try:
		res=l.index(val)
	except ValueError as e:
		res=-1
	return res
		
def list_replace (lst, repl, ind)->list:
	"""
	Replace values in lst with repl values at index ind
	"""
	res=lst[:ind]+repl+lst[ind+1:]
	return res
	
def key_in_dict_and_true (d_dct:dict={}, key_str:str='')->bool:
	"""
	Return true only if key pesents in dict and True
	"""
	return key_str in d_dct and d_dct[key_str]


def val_for_int_in_dict_or_default (d_dct:dict={}, key_str:str='', default_val_int:int=-1)->int:
	"""
	Return int value for key in dict or default value if there is no such key
	"""
	if key_str in d_dct:
		return d_dct[key_str]
	else:
		return default_val_int

# [@ps_section]  misc functions

def press_enter () :
	"""
	Wait for user pressing Enter key
	"""
	nointer_bool=ps_funcs.opt_exists("no-inter")
	if not nointer_bool:
		input ("Press Enter to continue...")

def system (cmd) :
	"""
	system equal to PHP system
	"""
	return os.system(cmd)
	
def print_help (help_str: str, exit_on_complete_bool: bool=True, exit_code_int:int=0):
	"""
	Print help and optionally exit with guven code
	"""
	print (help_str)
	
	
	if exit_on_complete_bool:
		exit (exit_code_int)

# [@ps_section]  date/time funcs

def now_dt()->datetime.datetime:
	return datetime.datetime.now()

ps_funcs_date_cl_fmt="%Y/%m/%d"
ps_funcs_date_log_fmt="%Y-%m-%d"
ps_funcs_date_default_fmt= "%g%m%d"
def psdate_str(log_fmt_bool:bool=False, cl_fmt_bool:bool=False, fmt_str=None)->str:
	"""
	Returns current date in format yymmdd
	Could be overriden by pass explicit format through fmt param
	"""
	nowdt=now_dt()
	fmt= ps_funcs_date_default_fmt
	if fmt_str is not None:
		return nowdt.strftime(fmt_str)
	if cl_fmt_bool:
		fmt=ps_funcs_date_cl_fmt
	elif log_fmt_bool:
		fmt=ps_funcs_date_log_fmt
	return nowdt.strftime(fmt)

def pstime_str(longFmt:bool=False)->str:

	nowdt=now_dt()
	fmt="%H:%M" if longFmt else "%H%M"
	return nowdt.strftime(fmt)
	

def get_bool_val_str (val_bool:bool, type_str:str='✅❌')->str:
	"""
	Return 1st symbol in type_str if val is True, second otherwise.
	
	Recomended most popular values for type_str:
	YN (default, Y/N depends on val)
	10 (bool vals)
	TF (shorthand for True/False)
	+- (+ for True, - otherwise)
	✔️✖️ - this and following one variants look fancy but supported only on unicode-friendly terminals (most of modern ones though)
	✅❎ - see above note
	✅❌ - see above note
	(shcolar.fg.colors['BrightGreen']+'\u2714'+ps_shcolar.fg_reset, ps_shcolar.fg["BrightRed"]+'\u2718'+shcolar.fg_reset) - you could use array-like objects as well (like lists, tuples, etc)
	"""
	return type_str [0 if val_bool else 1]
	
# [@ps_section]  Const funcs
	
def get_path_sep_str()->str:
# todo: make OS check
	return "/"
	
def getnl_str()->str:
# todo: make OS check
	return "\n"

# [@ps_section]  string funcs

def quote_str (s:str)->str:
	"""
	
	As name said it quotes string
	: param s: string to quote
	: type s: str
	: return: quoted string
	: rtype: str
	"""
	escaped_s_str=s.replace ('\"', '\\\"')
	return "\""+escaped_s_str+'\"'


# [@ps_section]  clipboard funcs


def str_to_cb (s:str)->bool:
	"""
	Copy string to clipboard
	: param s: string to copy
	: type s: str
	: return: True on success, False otherwise
	: rtype: bool
	"""
	cbcopy_cmd_str='cbcopy'
	cmd_str='printf '+quote_str(s)+' | '+cbcopy_cmd_str
	res_int=system(cmd_str)
	return res_int==0

def cb_to_str ()->str:
	"""
	Returns string data from clipboard
	"""
		
def _exactargs_gen_nums_str(start_int:int=1, len_int:int=10, step_int=1)->str:
	"""
	Generate string with digits ending numbers from start_int (optional. default is 1) to len_int (optional, inclusive, default is 10)
	"""
	res=""
	for i in range(start_int,len_int+1,step_int):
		res+=str(i%10)
	return res


def args_to_list_lst (*args, include_nones_bool:bool=False)->list:
	"""
	Convert non-None (if include_nones_bool is False, all otherwise) args to list
	"""
	if include_nones_bool:
		return list(args)
	else:
		return [a for a in args if a is not None]
	
	

		
# [@ps_section]  XML funcs

xml_entities_map_dict={
"&": "&amp;",
"\'": "&apos;",
">": "&gt;",
"<": "&lt;",
"\"": "&quot;",
}

xml_entities_map_transtbl=str.maketrans(xml_entities_map_dict)

def xmlentities (in_str: str)->str:
	"""
	 replaces basic XML entities (see xml_entities_map_dict for list of replacements)
	 """
	 # todo: numeric entities
	return  in_str.translate (xml_entities_map_transtbl)





def getNodeAttrs_dict(node:mdom.Node)->dict:
	res= dict()
	for key, val in node.attributes.items():
		res[key]=val
	return res
		
		
def getNodeAttrs_str (node:mdom.Node)->str:
	node_attrs_dict=getNodeAttrs_dict(node)
	node_attrs_lst=[key+"=\""+xmlentities(val)+"\"" for key, val in node_attrs_dict.items()]
	print ("@@lst?", node_attrs_lst)
	node_attrs_str=' '.join (node_attrs_lst)
	return node_attrs_str
	
def getChildByTagNameIter_node(parent:mdom.Node, childTag:str)->mdom.Node|None:
	children=parent.childNodes
	for cn in children:
		if cn.nodeName==childTag:
			return cn
	return None
                
def getChildrenByTagName_node_lst(parent:mdom.Node, childTag:str)->list:
                children=parent.childNodes
                res=[]
                for cn in children:
                        if cn.nodeName==childTag:
                                res.append (cn)
                return res


def getChildByTagName(parent:mdom.Node, childTag:str)->mdom.Node|None:
	children= getChildrenByTagName_node_lst(parent, childTag)
	if len(children)>=1:
		return children[0]
	else:
		return None


def getChildrenFromAllDescByTagName_node_lst (parent:mdom.Node, childTag:str)->list:
	"""
	Get children from all descendants of Node parent (direct and indirect) using native DOM method
	"""
	return parent.getElementsByTagName(childTag)

def getNodeText_str (node:mdom.Node)->str:
	return (node.firstChild.nodeValue if node.firstChild.nodeType==node.TEXT_NODE else "fb2_unknown")
	
def getFullPersonName_str (node:mdom.Node)->str:
	fn_node=getChildByTagName(node, "first-name")
	mn_node=getChildByTagName(node, "middle-name")
	ln_node=getChildByTagName(node, "last-name")
	fn=""
	mn=""
	ln=""
	if not fn_node is None:
		fn=getNodeText_str (fn_node)
	if not mn_node is None:
		mn=getNodeText_str (mn_node)
	if not ln_node is None:
		ln=getNodeText_str (ln_node)
	res=" ".join([fn, mn, ln] if mn!="" else [fn, ln])
	return res

class PSException (Exception):
	def __init__(self, /, *args_passed_lst:list, **kwargs_passed_dict:dict):
		args_lst=[]
		kwargs, args={},[]
		if len(kwargs)==0:
			kwargs={
				"colorize":True,
				"fatal": False,
				"exit_code": 1
			}
		kwargs.update (kwargs_passed_dict)
		args.extend(args_passed_lst)
		print ('kwa in psexc:', kwargs, 'len:', len(kwargs))
		opt_colorize_bool = key_in_dict_and_true(kwargs,"colorize")
		opt_fatal_bool = key_in_dict_and_true(kwargs,"fatal")
		opt_exit_code = val_for_int_in_dict_or_default (kwargs, "exit_code", 1)
		for arg in args:
			arg_str=str(arg)
			args_lst.append(arg_str)
		print ((shcolar.fg.red if opt_colorize_bool else "")+(" ".join(args_lst))+(shcolar.reset if opt_colorize_bool else ""))
		print ("@ps colorize:", opt_colorize_bool, "fatal:", opt_fatal_bool)
		if opt_fatal_bool:
			sys.exit (opt_exit_code)















# [@ps_section]  CLI output funcs

def adjust_str (s: str, width:int=10,  pad_width_int=1, adjust_mode_str: str= "c", adjust_char_str=" ", trim_mode_str: str= "l")->str:
        res=""
        print ("@ps funcadjustin:",s)
        print ("@ps funcadjustinlocals:",locals())
        content_width_int=width-pad_width_int*2
        trimmed_str=s[len(s)-content_width_int:] if trim_mode_str=='l' else s[:content_width_int]
        print ("@ps afttrim_b4adjust src trimmed, trim_mode, cw:", s, trimmed_str, trim_mode_str, content_width_int)
        match adjust_mode_str:
                case "c":
                        res=trimmed_str.center(width, adjust_char_str)
                case "l":
                        res=trimmed_str.ljust(width, adjust_char_str)
                case "r":
                        res=trimmed_str.rjust(width, adjust_char_str)
                case _:
                        raise ps_funcs.PSException("Unknown adjust_mode ", adjust_mode_str, " in adjust_str func for string", s, fatal=True)
        print ("@ps funcadjout:",res)
        return res


def get_rel_fn_str(filename_str:str, root_dn_str:str)->str:
        """
        Function to remove prefix path from filename e. g. path to libs. See example below

        E. g.: /data/data/com.termux/files/home/dev/_libs/ps_funcs/py/ >/ps_funcs/py/
        where  /data/data/com.termux/files/home/dev/_libs is root_path_str
        """
#        print (shcolar.fg.brightWhite+"@ps params and types", [(k, v, type(v)) for k,v in locals().items()])
        return os.path.relpath(filename_str, start=root_dn_str)
        
#print ("\033[91m@ps end of ps_funcs/init\033[0m")

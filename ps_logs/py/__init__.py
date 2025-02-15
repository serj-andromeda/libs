"""
# PS_logs (ps_logs)
This module provides various logging functions and constants for [Python](https://python.org) programs
"""


import ps_funcs, shcolar


# [@ps_section]  OS related helpers

def backtick (cmd):
	"""
Execute command in shell and return result like backtick in shell and PHP
:param cmd: command to execute
:type cmd: str
:returns: what command cmd sends to stdout (basically just output of command)
:rtype: str
	"""
	cp=subprocess.run(cmd, shell=True, capture_output=True);

	ba=cp.stdout;
	res=ba.decode('utf-8');
	return res;
	

# [@ps_section]  CLI functions


def arg_value (arg_name_variants_str_lst : list, default : str | None=None )->str|None:
	"""
	Function to get certain argument value
	"""
	for arg_str in sys.argv[1:] :
		arg_lst=arg_str.split ('=')
		if len(arg_lst)!=2:
			# most likely not argument. skipping
			print ("arg", arg_str, "seems like not argument. skip in ps_funcs/arg_value")
			continue
		if arg_lst[0] in arg_name_variants_str_lst:
			# found!
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
	
# [@ps_section]  Files functions

def file_exists (filename, dirIsOk=False)->bool:
	"""
	Check if file exists
	"""
	if dirIsOk:
		return os.path.exists(filename)
	else:
		return os.path.isfile(filename)


def file_get_contents (filename, binary=False, forceZip=False):
	"""
	Function mimics PHP file_get_contents minimal behavior - reads file specified by *filename* arg and return its content.
	However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename*
	"""
	res=None
	with open (filename, "rb" if binary else "r") as inf:
		res=inf.read()
	return res
	
def file_put_contents (filename, data, overwrite=False):
	"""
	Function mimics PHP file_put_contents minimal behavior - reads file specified by *filename* arg and return its content.
	However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename* and *data*
	"""
	with open (filename, 'w' if overwrite else 'x') as outf:
		outf.write(data)

# [@ps_section]  structures helpers

def keybyval (d, val):
	'''
Return key or keys in dictionary having passed value.
In ideal case (only one key has given value returns this key
If no keys have given value returns None
If more than one key have given value returns list of such keys
	'''
	keys=[k for k, v in d.items() if v==val]
	keysn=len(keys)
	if keysn==1:
		return keys[0]
	elif keysn==0:
		return None
	else:
		return keys
		
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
	os.system(cmd)
	
# [@ps_section]  date/time funcs

def now_dt()->datetime.datetime:
	return datetime.datetime.now()

def psdate_str(longFmt:bool=False)->str:
	"""
	Returns current date in format yymmdd
	"""
	nowdt=now_dt()
	fmt="%Y-%m-%d" if longFmt else "%g%m%d"
	return nowdt.strftime(fmt)

def pstime_str(longFmt:bool=False)->str:

	nowdt=now_dt()
	fmt="%H:%M" if longFmt else "%H%M"
	return nowdt.strftime(fmt)
	
def correctForm_str (term:str, nmb:int, lang:str="en", includeNmb=True, case:str="и")->str:
	res="unknown language or params in correctForm function"
	match lang:
		case "en":
			sfx=""
			if nmb!=1:
				sfx="s"
			res=(str(nmb)+ " " if includeNmb else "")+term+sfx
		case _:
			res="unknown language "+lang+" in correctForm function"
	return res
	
	
def get_bool_val_str (val_bool:bool, type_str:str="YN")->str:
	"""
	Return 1st symbol in type_str if val is True, second otherwise.
	
	Recomended most popular values for type_str:
	YN (default, Y/N depends on val)
	10 (bool vals)
	TF (shorthand for True/False)
	+- (+ for True, - otherwise)
	✔️✖️ - this and following one variants look fancy but supported only on unicode-friendly terminals (most of modern ones though)
	✅❎ - see above note
	"""
	return type_str [0 if val_bool else 1]
	
# [@ps_section]  Const funcs
	
def get_path_sep_str()->str:
# todo: make OS check
	return "/"
	
def getnl_str()->str:
	return "\n"
	
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
		print ("@ps c:", opt_colorize_bool, "f:", opt_fatal_bool)
		if opt_fatal_bool:
			sys.exit (opt_exit_code)
	
__doc__="""
This module contains functions to work with `dialog` utility in *nix
"""
import shutil
import ps_funcs, ps_shcolar

_DIALOG_CMD_str='dialog'
_WHIPTAIL_CMD_str='whiptail'
_SIMPLE_MODE_TOOL_str='simple'
_DEFAULT_TOOL_str='whiptail'
_SUPPORTED_TOOLS_lst=['dialog', 'whiptail', 'simple']
_selected_tool_str='whiptail'




def set_extras_bool (extras_dict: dict|None)->bool:
	global _selected_tool_str
	if extras_dict is None:
		raise ps_funcs.PSException ("set_extras could not be called without param or with param eq to None", fatal=True)
	if len(extras_dict)==0:
		return False
	_selected_tool_str=ps_funcs.dict_val (extras_dict, "tool", _selected_tool_str)

def set_selected_tool_str (tool: str=_DEFAULT_TOOL_str)->str:
	"""
	Set prefered tool to create dialogs
	Set tool available in system and will be used for dialogs creation.
	Currently one of the followng supported:
	- whiptail (default, no this functuon call required)
	- dialog
	- simple simple mode using internal functions without using external tools
	:param tool: tool to use ('whiptail' or 'dialog')
	:type tool: str
	:return: former tool
	:rtype: str
	"""
	if tool not in _SUPPORTED_TOOLS_lst:
		raise PSExceptiion ("Tool", tool, "not supported", fatal=True)
	former_tool=_PREFERED_TOOL_str
	_selected_tool_str=tool
	return former_tool

def set_simple_mode (mode: bool=True)->str:
	"""
	Sets simple mode for dialogs
	:param mode: if about to enable simple mode
	:type mode: bool
	:return: former tool
	:rtype: str
	"""
	former_tool=_PS_dialog_simple_mode_bool
	if mode:
		return set_prefered_tool_str(_SIMPLE_MODE_TOOL_str)
	else:
		return set_prefered_tool_str(_DEFAULT_TOOL_str)
		
	



def is_dialog_util_avail()->bool:
	return shutil.which(DIALOG_CMD_str) is not None


def yesno (text_str: str, extras_dict: dict|None=None)->bool:
	if extras_dict is not None:
		 
		res=set_extras_bool(extras_dict)
		if not res:
			raise ps_funcs.PSException ("Extras provided but empty. It could omitted, setted to None but must not be empty dict", fatal=True)
	if _selected_tool_str==_SIMPLE_MODE_TOOL_str:
		# simple mode logic
		ans = input (text_str+" (Yes/No) ? ")
		return ans.lower() in ['y', 'yes']
	else:
		# simple mode disabled so using `dialog/whiptail` utility
		cmd_str = _DIALOG_CMD_str+' --yesno '+ps_funcs.quote_str (text_str)+' 0 0'
		print ("@ps cmd", cmd_str)
		res_int=ps_funcs.system(cmd_str)
		return res_int==0
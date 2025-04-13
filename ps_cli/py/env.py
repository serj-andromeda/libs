__doc__="""
This module contains functions for working with environment variables of users shell in CLI tools
"""
import os, sys
import ps_funcs, ps_shcolar

def get_envvars_dict (envvars_list: list=["HOME"])->dict:
	"""
	Get dict with values for envvars listed in envvars_list
	
	Get envvars from system and return dict with their values
	e. g.:
	["HOME"] > {"HOME": "/Users/user1"}
	"""
	res = dict()
	for envvar in envvars_list:
		val=os.getenv (envvar)
		res [envvar]=val
	print (f"@ps get_envvar_dict res for list {envvars_list}:\n{res}")
	return res
def expand_envvars_str (in_str : str, *, prefix_str: str='$', envvars_list: list=["HOME"]) -> str :
	"""
	Expand env vars in passed string to corresponding values
	
	It converts all envvar values listed in `envvars_list` param to their names

	e.g.:
	$HOME/foo/bar.txt > /Users/user1/foo/bar.txt if $HOME var set to /Users/user1/
	Backward converting available using `compact_env_vars` function in same module
	This function do it's best to get valid values using `get_envvars_dict` function
	
	:param in_str: string expand variables in
	:type in_str: str
	
	:param prefix_str: prefix to prepend env var names while search in in_str (does not affects on value retrirving, so prefix `$` is ok for var `$HOME` if you are ok with it's value getting by executing cmd like `echo $HOME` in your shell), defaults to '$'
	:type prefix_str: str, optional
	
	:param envvars_list: list of env var names for search in in_str (do not include prefix - it would be done automatucallly, so list `["HOME", "COLORTERM"]`  is ok for vars `$HOME` and `$COLORTERM` if you are ok with their values getting by executing cmd like `echo -e "home dir: $HOME\ncolor term: $COLORTERM"` in your shell and didn't change prefix explicitly), defaults to '["HOME"]'
	:type envvars_list: list, optional
	
	
	:return: processed string
	:rtype: str
	"""
	
	
	
	envvars_dict = get_envvars_dict( envvars_list )
	print (f"@ps got dict {envvars_dict} for list {envvars_list} in expand_envvars_str")
	res=in_str
	for envvar_str in envvars_list:
		res = res.replace (prefix_str+envvar_str, envvars_dict[envvar_str])
	return res
	
def compact_envvars_str (in_str : str, *, prefix_str: str='$', envvars_list: list=["HOME"]) -> str :
	"""
	Compact values of env vars in passed string to corresponding env var names
	
	It converts all values of env vars listed in `envvars_list` param to it's names

	e.g.:
	/Users/user1/foo/bar.txt > $HOME/foo/bar.txt if $HOME var set to /Users/user1/
	Backward converting available using `expand_env_vars` function in same module
	This function do it's best to get valid values using `get_envvars_dict` function
	

	:param in_str: string to compact variables in
	:type in_str: str
	
	:param prefix_str: prefix to prepend env var names while replacing in in_str (does not affects on value retrirving, so prefix `$` is ok for var `$HOME` if you are ok with it's value getting by executing cmd like `echo $HOME` in your shell), defaults to '$'
	:type prefix_str: str, optional
	
	:param envvars_list: list of env var names for search in in_str (do not include prefix - it would be done automatucallly, so list `["HOME", "COLORTERM"]`  is ok for vars `$HOME` and `$COLORTERM` if you are ok with their values getting by executing cmd like `echo -e "home dir: $HOME\ncolor term: $COLORTERM"` in your shell and didn't change prefix explicitly), defaults to '["HOME"]'
	:type envvars_list: list, optional
	
	
	:return: processed string
	:rtype: str
	"""
	
	
	
	envvars_dict = get_envvars_dict( envvars_list )
	print (f"@ps got dict {envvars_dict} for list {envvars_list} in expand_envvars_str")
	res=in_str
	for envvar_str in envvars_list:
		res = res.replace (prefix_str+envvar_str, envvars_dict[envvar_str])
	return res
		
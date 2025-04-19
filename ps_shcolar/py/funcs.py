__doc__="""
This module provides various functions related to colorizing/styling strings
"""
import os, sys, re, ps_shcolar
ps_reset_all_seq_str='\033[0m'

def strip_escapes (s: str)->str:
	"""
	Returns string without escape sequences
	
	Currently only SGR sequences supported
	"""
	rx='\033\\[(?P<seq>[^m]+)m'
	res=re.sub (rx, '', s)
	
	return res
	

def real_strlen (s:str)->int:
	"""
	Returns real length of string stripping escape codes in advance

	Currently only SGR sequences supported
	"""
	return len(strip_escapes(s))




def wrap (s: str, wrapper: str, resetter: str=ps_reset_all_seq_str)->str:
	"""
	Wrap string `s` using `wrapper` on the left side and `resetter` on thevright
	
	Please note that by default this functuon resets all attributes, not only ones were set. If you need to reset only certain ones please provide `resetter` argument
	"""
	return wrapper+s+resetter
	
	
	
	
	
	
	
	
	
	
	
	
	
def GetFgColor_str(color: str)->str:
    """
    Returns FG color changing SGR string
    Camel case used in name for uniformity with GoLang exported functions
    """
    return ps_shcolar.fg.colors[color]
    
def GetBgColor_str(color: str)->str:
    """
    Returns BG color changing SGR string
    Camel case used in name for uniformity with GoLang exported functions
    """
    return ps_shcolar.bg.colors[color]
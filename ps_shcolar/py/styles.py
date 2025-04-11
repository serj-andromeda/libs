__doc__="""
This module contains escape codes to set (reset) styles of following text
"""
from . import lists
from . import consts

pfx_str=consts.sgr_prefix_str
sfx_str=consts.sgr_suffix_str
styles={itm["name"]:pfx_str+itm["on"]+sfx_str for itm in lists.styles_list}
styles_off={itm["name"]:pfx_str+itm["off"]+sfx_str for itm in lists.styles_list}
reset='\033[0m'
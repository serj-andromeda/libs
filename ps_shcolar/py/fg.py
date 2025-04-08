__doc__="""
This module contains escape codes to set (reset) foreground colors of following text
"""
from . import lists
from . import consts

pfx_str=consts.sgr_prefix_str
sfx_str=consts.sgr_suffix_str
colors={itm["name"]:pfx_str+itm["fg"]+sfx_str for itm in lists.colors_list}
reset='\033[0m'
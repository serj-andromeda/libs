__doc__="""
This module contains indexes of all colors available to setup as back/fore-ground using values in bg/fg modules respectively. Also it contains some useful constants like `esc_str`.
"""
import ps_funcs, os, sys, re, json, pathlib


datadn="_data"
colorslist_json_fn_str="colors.json"
styleslist_json_fn_str="styles.json"
cfn=pathlib.Path(__file__).resolve()
cdn=cfn.parent
pardn=cdn.parent

datadn=os.path.join(pardn,datadn)

colorslist_json_fn=os.path.join(datadn, colorslist_json_fn_str)
styleslist_json_fn=os.path.join(datadn, styleslist_json_fn_str)

dbg=False
if dbg:
        tracker_fn='/data/data/com.termux/files/home/trackwithshlist.txt'
        with open(tracker_fn, 'w') as track_f:
                print ("cfn:", cfn,
                "cdn:", cdn,
                'pardn:', pardn,
                'datadn:', datadn,
                'colorsjson:', colorslist_json_fn,
                'stylesjson:', styleslist_json_fn,
                sep='\n', file=track_f)

#print ('@ps cfn?', cfn)
colors_fn=cfn

import json


styles_list=colors_list=[]



with open (colorslist_json_fn, 'r') as colorslist_f:
        colors_list=json.load(colorslist_f)
with open (styleslist_json_fn, 'r') as styleslist_f:
        styles_list=json.load(styleslist_f)

#! /usr/bin/env python3

import ps_shcolar

colors2exclude_list=["White"]

rows={col:ps_shcolar.bg.colors[col] for col in ps_shcolar.bg.colors if col not in colors2exclude_list}
fg_dict=cols={col:ps_shcolar.fg.colors[col] for col in ps_shcolar.fg.colors if col not in colors2exclude_list}

print (ps_shcolar.styles.styles["Underline"], 'Colors', ps_shcolar.styles.styles_off["Underline"])




corner_filler_str='XX'

def header_val_str (in_sgr_val_str: str, pfx_len:int=2, sfx_len: int=1)->str:
	res=in_sgr_val_str[pfx_len:-sfx_len]
	if len(res)!=2:
		res=ps_shcolar.styles.styles["Italic"]+res[-2:]+ps_shcolar.reset
	return res


def cell_value_from_fgbg_sgr_str (fg_sgr_str: str, bg_sgr_str: str)->str:
	"""
	Get cell value from fg and bg SGR strs
	"""
	
	fg_code_str=fg_sgr_str[2:-1]
	bg_code_str=bg_sgr_str[2:-1]
#	print ("@ps fg bg code", fg_code_str, bg_code_str)
	fg_code_int=int(fg_code_str)
	bg_code_int=int(bg_code_str)
	fg_lastdig_int=fg_code_int%10
	bg_lastdig_int=bg_code_int%10
	fg_lastdig_str=fg_code_str[-1:]
	bg_lastdig_str=bg_code_str[-1:]

#	print ("@ps fg bg codes  & lasrdigs", fg_code_str, bg_code_str, fg_lastdig_str, bg_lastdig_str)
	res=fg_sgr_str+bg_sgr_str+fg_lastdig_str+bg_lastdig_str+ps_shcolar.reset
#	print (repr(res))
#	print ("@ps fg bg res:", repr(fg_sgr_str), repr(bg_sgr_str), repr(res))
	return res






#print ("@ps colsvals", cols.values()); exit;
header_row_str_list=[corner_filler_str]+[header_val_str(col) for col in cols.values()]
header_row_str='|'.join(header_row_str_list)

print (header_row_str)
for row, row_val_str in rows.items():
	bg_sgr_str=row_val_str
	row_str_list = [header_val_str(bg_sgr_str)]
	for col, col_val_str in cols.items():
		fg_sgr_str=col_val_str
		row_str_list.append (cell_value_from_fgbg_sgr_str(fg_sgr_str, bg_sgr_str))
	row_str='|'.join (row_str_list)

	print (row_str)        






print (ps_shcolar.styles.styles["Underline"], 'Styles', ps_shcolar.styles.styles_off["Underline"])
for style_name,style_val_on in ps_shcolar.styles.styles.items():
	print (style_val_on+style_name+ps_shcolar.reset)

#! /usr/bin/env python3

import ps_shcolar



rows=ps_shcolar.bg.colors
cols=ps_shcolar.fg.colors

print (ps_shcolar.styles.styles["Underline"], 'Colors', ps_shcolar.styles.styles_off["Underline"])



def cell_value_from_fgbg_sgr_str (fg_sgr_str: str, bg_sgr_str: str)->str:
	"""
	Get cell value from fg and bg SGR strs
	"""
	fg_code_str=fg_sgr_str[2:-1]
	bg_code_str=bg_sgr_str[2:-1]
	fg_code_int=int(fg_code_str)
	bg_code_int=int(bg_code_str)
	fg_lastdig_int=fg_code_int%10
	bg_lastdig_int=bg_code_int%10
	res=fg_sgr_str+bg_sgr_str+str(fg_lastdig_int)+str(bg_lastdig_int)+ps_shcolar.reset
	return res





header_row_dec_list=[int(col[2:-1]) for col in cols.values()]
header_row_hex_str_list=[hex(col)[2:].upper().zfill(2) for col in header_row_dec_list]
header_row_str='|'.join(header_row_hex_str_list)

print (header_row_str)
print (len(header_row_str)*'-')
for row in rows:
	bg_sgr_str=rows[row]
	row_str_list = [str(hex(int(bg_sgr_str[2:-1])))[2:-1].zfill(2)]
	for col in cols:
		fg_sgr_str=cols[col]
	row_str_list.append (cell_value_from_fgbg_sgr_str(fg_sgr_str, bg_sgr_str))
	print ("@ps rowstrlist", row_str_list); exit();
	row_str='|'.join (row_str_list)
	border_str='-'*len(row_str)

	print (row_str)        
	print (border_str)
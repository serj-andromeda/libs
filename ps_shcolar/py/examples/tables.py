#! /usr/bin/env python3

import ps_shcolar



rows=ps_shcolar.bg.colors
cols=ps_shcolar.fg.colors

print (ps_shcolar.styles.styles["Underline"], 'Colors', ps_shcolar.styles.styles_off["Underline"])




header_row_list=[col[2:-1] for col in cols.values()]+['FG']
header_row_str='|'.join(header_row_list)

print (header_row_str)
print (len(header_row_str)*'-')
for row in rows:
	print (row, rows[row])
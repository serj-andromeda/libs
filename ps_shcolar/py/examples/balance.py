#! /usr/bin/env python3

expenses={
"paper pack": (1, 20),
"ink cartridge": (10, 70),

"stapler": (5, 30),
"paper clips": (1, 20),
"markers": (2, 70),
"binder": (1, 20),
"map-case":(10,70),
"taxes":(100, 5000, 1),
}




profits={
"contract close": (100, 50000),
"sales": (100, 100000),
"tax returns": (1, 500, 1),
"profit from partners": (100, 50000, 1),
}

def format_money (money_float: float, currency_symbol='$', currency_is_prefix_bool=True, add_plus_sign_bool=True)->str:
	res=""
	if money_float<=0:
		res += ps_shcolar.fg.colors["BrightRed"]
	elif add_plus_sign_bool:
		res +=  ps_shcolar.fg.colors["BrightGreen"]+'+'
	res += "{:.2}".format(money_float)




def print_row (row_list: list)->int:
	row_str='|'.join(row_list)
	print (row_str)
	return len(row_str)


import random
import ps_shcolar


rows_number=10

header_list=["No", ('-'*10)+"Item"+('-'*10), "Qty", "Price", "Sum"]

chars_n_int=print_row(header_list)
print ('-'*chars_n_int)


for row_i in range(1, rows_number+1):

	record_type=random.randint(0,1) # 0 for expenses, 1 for profits
	data_source_dict=expenses if record_type==0 else profits
	key_str=random.choice(list(data_source_dict.keys()))
	print (key_str, data_source_dict[key_str])

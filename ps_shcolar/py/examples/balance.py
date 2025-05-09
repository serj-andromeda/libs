#! /usr/bin/env python3
import ps_shcolar




expenses_list=[
{'item': "paper pack", "price": (1, 20),},
{'item': "ink cartridge", 'price': (10, 70),},
{'item': "stapler", 'price':(5, 30),},
{'item': "paper clips", 'price': (1, 20),},
{'item': "markers", 'price': (2, 70),},

{'item': "binder", 'price': (1, 20),},
{'item': "map-case", 'price':(10,70),},
{'item': "taxes", 'price':(100, 5000), "single": True},
]




profits_list=[
{"item": "contract close", 'price':(100, 50000)},
{"item":"sales", "price": (100, 100000), "single": True},
{"item":"tax returns", "price": (1, 500), "single": True},
{"item": "profit from partners", "price": (100, 50000), "single": True},
]

def format_money_str (money_float: float, currency_symbol='$', currency_is_prefix_bool=True, add_plus_sign_bool=True, positive_val_sgr_str=ps_shcolar.fg.colors["BrightGreen"], negative_vals_sgr_str=ps_shcolar.fg.colors["BrightRed"], reset_sgr_str=ps_shcolar.reset)->str:
	res=""
	if money_float<=0:
		res += ps_shcolar.fg.colors["BrightRed"]
	elif add_plus_sign_bool:
		res +=  ps_shcolar.fg.colors["BrightGreen"]+'+'
	res += "{:.2}".format(money_float)

def add_item_to_list (lst: list, item: dict)->bool:
	"""
	Adds item to given list with checks and calculations
	"""
	name_key="item"
	single_key="single"
	name_str=item[name_key]
	add_item_bool = True
	
	
	indices_list=["nmb_idx", "name_idx", "price_idx"]
	if item [single_key]:
		for itm2chck in list:
			if itm2chk[name_key]==item[name_key]:
				add_item_bool=False
	


def print_row (row_list: list)->int:
	row_str='|'.join(row_list)
	print (row_str)
	return len(row_str)


import random
import ps_shcolar



rows_number=10
item_width_int=20

header_list=["#","Item".center(item_width_int), "Qty", "Price", "Sum"]

chars_n_int=print_row(header_list)
print ('-'*chars_n_int)


for row_idx_int in range(1, rows_number+1):

	record_type=random.randint(0,1) # 0 for expenses, 1 for profits
	data_source_list=expenses_list if record_type==0 else profits_list
	key_int=random.randint(0, len(data_source_list))
	print (key_int)
	print (data_source_list[key_int])

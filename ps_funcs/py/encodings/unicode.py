chars={
'Horizontal Ellipsis':'…',
}



def get_hex_chars_list ()->list:
	return list(map (str,range(10)))+[chr(c) for c in range(ord('a'), ord('g'))]+[chr(c) for c in range(ord('A'), ord('G'))]



def print_char_from_hexcode (code_str)->bool:
	"""
		Convert hex=code to Unicode char
		Cut non-hexades chars from beginning
	"""
	hex_chars_list=get_hex_chars_list()
	while code_str[0] not in hex_chars_list:
		code_str=code_str[1:]
	print (f"@ps list of hex chars and str after clean: {hex_chars_list} {code_str}")
	char_str=get_char_from_hexcode (code_str)
	print (char_str)








def get_char_from_hexcode (code_str)->str:
	code_int=int(code_str, 16)
	return chr (code_int)




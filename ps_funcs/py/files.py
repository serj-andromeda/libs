from . import structs

def file_get_contents (filename, *, binary=False, forceZip=False, return_lst_bool:bool=False)->str|list|None:
	"""
	Function mimics PHP file_get_contents minimal behavior - reads file specified by *filename* arg and return its content.
	However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename*
	"""
	try:
		res=None
		with open (filename, "rb" if binary else "rt") as inf:
			if return_lst_bool:
				res=structs.strip_list_items(inf.readlines())
			else:
				res=inf.read()
		return res
	except FileNotFoundError:
		raise PSException ("File", filename, "not found", fatal=True)
	return None
	
def file_put_contents (filename, data, overwrite=False, return_none_on_exists=False)->int|None:
	"""
	Function mimics PHP file_put_contents minimal behavior - reads file specified by *filename* arg and return its content.
	However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename* and *data*
	"""
	try:
		outf=open (filename, 'w' if overwrite else 'x')
		written_bytes_int=outf.write(data)
		outf.close()
		return written_bytes_int
	except Exception as e:
		if isinstance(e, FileExistsError):
			return None
		else:
			return 0

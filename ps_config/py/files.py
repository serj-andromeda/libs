"""
This module contains functions to work with files (dirs/symlinks also treated as files)
"""
import os, sys, shutil
import ps_funcs, ps_shcolar

def get_file_type_str (fn_str: str)->str:
	"""
	Do check of file type
	
	Returns one letter with type of file or 'n' if file not exists: l/d/f which means link(symlink, not working with hard links yet)/dir(whether with content o$ not)/file (just usual file that is neither not dir nor symlink)
	"""
	
	if not os.path.exists (fn_str):
		return 'n'
		
	if os.path.islink (fn_str):
		return 'l'

	if os.path.isdir (fn_str):
		return 'd'

	if os.path.isfile (fn_str):
		return 'f'


def get_type_names_tuple (file_type_str: str)->tuple:
	"""
	Get tuple of full names of type.
	
	Tuple contains two values:
	first (index 0) is singular form of name,
	second (index 1) is plural form of name
	"""
	match file_type_str:
		case 'l':
			return ("symlink", "symlinks")
		case 'f':
			return ("file", "files")
		case 'd':
			return ("directory", "directories")
		case _:
			return ("@unknown_type_"+file_type_str+"@", "@unknown_type_"+file_type_str+"@")
		
def get_file_type_name_str (fn_str: str)->str:
	"""
	Return single form of type name for given filename
	"""
	type_names_tuple=get_type_names_tuple(get_file_type_str(fn_str))
	return type_names_tuple[0]

def remove_file_bool (fn_str: str, force=False)->bool:
	"""
	Removes file/dir/symlink
	"""
	
	file_type_str=get_file_type_str (fn_str)
	if file_type_str is None:
		raise ps_funcs.PSException ("Could not find file", fn_str, fatal=True)
	do_rm_bool = force
	type_name_str = get_file_type_name_str(fn_str)
	
	if not force:
		do_rm_bool = ps_funcs.cli.dialog.yesno ("Are you sure want to remove "+type_name_str+" '"+fn_str+"'")
	if not do_rm_bool:
		return False
	match file_type_str:
		case 'l':
			try:
				os.unlink (fn_str)
			except Exception:
				return False
		case 'f':
			try:
				os.remove (fn_str)
			except Exception:
				return False
		case 'd':
			try:
				shutil.rmtree (fn_str)
			except Exception:
				return False
		case 'n':
			raise ps_funcs.PSException (f"File '{fn_str}' not found. Unable to remove non-existent file.", fatal=True)
		case _:
			raise ps_funcs.PSException ("Unknown file type '"+file_type_str+"'. Don't know how to remove it.", fatal=True)
	return True




def file_exists (filename, dirIsOk=False)->bool:
        """
        Check if file exists
        """
        if dirIsOk:
                return os.path.exists(filename)
        else:
                return os.path.isfile(filename)


def strip_list_items (lst:list)->list:
        """
        Apply `strip` method to every element in list
        """
        return [li.strip() for li in lst]

def file_get_contents (filename, binary=False, forceZip=False, return_lst_bool:bool=False)->str|list|None:
        """
        Function mimics PHP file_get_contents minimal behavior - reads file specified by *filename* arg and return its content.
        However it is not fully compatible substitution cause it doesn't supports any psrameters beside *filename*
        """
        try:
                res=None
                with open (filename, "rb" if binary else "rt") as inf:
                        if return_lst_bool:
                                res=strip_list_items(inf.readlines())
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
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
def file_contains_str_bool (filename_str: str, subject_str: str)->bool:
	"""
	This function checks if subject_str exidts in file filenme_str and if this file exists at all
	"""
	if not file_exists (filename_str):
		 return False
	content_str = file_get_contents (filename_str)

	return subject_str in content_str
	
	
	
	
	
	
	
	
	
	
	
def find_files_list (root_dn_str, *, search_str: str|None=None)->list:
	"""
	Return all files in directory root_dn_str and all it'sbsubdirectories containing subject_str if passed and not None
	"""
	res = []
	walk_obj=os.walk(root_dn_str)
	for leaf_dn_str, dirs_list, files_list in walk_obj:
		for fn_found_str in files_list:
			fn_str=os.path.join(leaf_dn_str, fn_found_str)
			if search_str is None:
				res.append (fn_str)
			else:
				if file_contains_str_bool (fn_str, search_str):
					res.appendb(fn_str)
	return res


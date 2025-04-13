## 04/12/24
### ps_funcs
added gen_nums_str func

## 10/12/24
### ps_funcs
file_get_contents returns None on `File not Found` error now

## 11/12/24
### ps_funcs
moved adjust_str func here

## 12/12/24
### ps_funcs
file_put_contents existing files behavior and return type changed

## 13/12/24
### ps_funcs
- added keybyval_lst and keybyval_dct funcs
- keybyval func is now synonim for keybyval_dct for backward compatibility

## 14/12/24
### ps_funcs
- renamed gen_nums_str to _exactargs_gen_nums_str

## 16/12/24
- rewrote gen_nums_str. Now it,s arguments  working exactly like in `range` function
- added `args_to_list_lst` function

## 22/12/24
### ps_funcs
- added quote_str func
- added str_to_cb func
- added system func

## 23/12/24
### ps_funcs
- added var_type_str


## 23/12/24
### ps_funcs
- added var_type_str


## 23/12/24
### ps_funcs
- added var_type_str


## 23/12/24
### ps_funcs
- added var_type_str func

## 24/12/24
### ps_funcs
- added table module
- change plural forms of argument names to singular


## 29/12/24
### ps_funcs
- moved table module to ps_cli module
- added ps_cli module as sub-module





## 05/01/25
### ps_funcs
- added dict_val function
### shfuncs.py
- imports added


## 06/01/25
### ps_funcs
- moved unicode.py to encodings sub-package



## 09/01/25
### ps_funcs
- texting in psexception extended: c>colorize f>fatal
### [files.py](./files.py)
- new submodule
- get_file_type_str function added
- renamed to files.py since `file` seems like keyword in Python2 (however this lib is not supports Python2 but just in case)

## 21/01/25
### [files.py](./files.py)
- added get_file_type_str func
- added get_type_names_tuple func
- added remove_file_bool func

### path.py
- added expand_dirs_str function

## 03/02/25
### [files.py](files.py)
- added `encoding_str` param to `get_file_contents` function




## 06/02/25
### [__init__.py](__init__.py)
- make `arg_value` func less verbose - added `verbose_bool` arg to be able to revert to old functionality

## 07/02/25
### [__init__.py](__init__.py)
- added todo section to `get_nl_str` func



## 08/02/25
### [files.py](files.py)
- renamed `binary` param to `binary_mode_bool` for uniformity
- replaced `None` in encoding_str param with `utf-8`
- moved default encoding to separate 'hidden' `_default_encoding' variable
- added return type-hint to `file_get_contents` func
- added check for binary mode to `file_get_contents` func for list mode (it's impossible set of params)






## 06/04/25
### [ps_structs.py](ps_structs.py)
- added section comment
### [ps_strings.py](ps_strings.py)
- added this submodule and few functions there
### [strings.py](strings.py)
- renamed to from `ps_strings` as prefix already 
there in main module
- added docstring to `rmchars` function
- fixed indebtarion errors
### [files.py](files.py)
- addded `start of` message





### [__init__.py](__init__.py)
- changed `ps_files` back to `files` again

## 11/04/25
- changed color of `end of ...` message

## 13/04/25
- added `reset` SGR code to `end of...` message


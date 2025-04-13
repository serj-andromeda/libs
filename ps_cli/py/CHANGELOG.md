## 22/12/24
### dialog.py
- added function `is_dialog_util_avail` to check if dialog utility available in system

## 26/12/24
### dialog.py
- added function `set_simple_mode` along with simple mode itself


## 29/12/24
### ps_cli
- moved table module here from ps_funcs

### table.py
- added defaults to first params of `convert_raw_data_to_print_data_list` func
- added debug statements for `convert_raw` func



## 03/01/25
### table.py
- added default tool const
- added logic for setting/resetting simple mode
- added convert_raw_var_to_print_var_dtr function stub


### dialog.py
- simple mode set/reset logic

## 05/01/25
### dialog.py
- added set_extras_bool function
- set_extras_bool now raise exception if called with None parameter (None is default so no param passed cause exception as well)
- yesno tested success in simple mode


## 27/01/25
### env.py
- added this sub-module and first functions (hope either last ones - but will dre for sure)










## 31/01/25
### [env.py](env.py)
- finished `expand_envvars_str` function
- finished `get_envvars_dict` function
















## 13/04/25
### [table.py](table.py) [dialog.py](dialog.py) [env.py](env.py)
- renamed `shcolar` to `ps_shcolar` as well as API calls


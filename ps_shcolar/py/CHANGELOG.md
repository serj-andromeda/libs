## 08/12/24
### sholar
renamed esc to esc_str
removed styles.py & stylres.py


## 11/12/24
### shcolar
added funcs module
### funcs.py
added strip_escapes,real_strlen, wrap funcs
## 12/12/24
### fg.py , bg.py
added docs for `reset` values in these modules


## 22/12/24
updated docs both in __init__ package descs and in child modules

## 04/04/25
### [__init__.py](__init__.py)
- updated to support `lists` sub-module instead of `colors`
- disabled importing `lists` since they aren't finished yet



## 07/04/25
### [lists.py](lists.py)
- added logging to file json files with their paths
- added `dbg` var for debug functionality and check for it
### [__init__.py](__init__.py)
- moved `lists` module above `fg` and `bg` to make'em able to use lists
## 08/04/25
### [fg.py](fg.py)
- added list of fg color codes

### [consts.py](consts.py)
- added this submodule and it's stuff to `fg` module
### [bg.py](bg.py)
- make this module works
### [styles.py](styles.py)
- make this module works







## 19/04/25
### [__init__.py](__init__.py) [funcs.py](funcs.py)
- moved `Get...` functions from `funcs` to `__init` (main) cause in golang version snyhoe there is no eay to access `funcs`


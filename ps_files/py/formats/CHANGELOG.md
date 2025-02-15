## 10/01/25
### fb2.py
- aadded detect_encoding function



## 13/01/25
### fb2.py , PS_FileFormat.py
- move default encoding to fileformat class and set it to utf-8 indtead of ascii
- makes dontDecode and isBinFile params in read_file_bool keyword only params









## 15/01/25
### PS_FileFormat.py
- colorize read/decode error




## 16/01/25
### fb2.py
- fix naming bugs in `read_file`method







## 17/01/25
### PS_FileFormat.py
- added process_file function for read/parse in one place
- fixing bugs






## 20/01/25
### fb2.py
- rewrite to untie it from parent PS_FileFormat.py class since it is meaningless to have parent class just for reading

## 21/01/25
### __init__.py
- fixed import problems appeared due to removal of PS_FileFormats.py and mp3.py



### fb2.py
- PCRE for detect encoding fix (underquoting)
- added getset_encoding_str function
- renamed get_filename_str to getset_filename_str









## 06/02/25
### [fb2.py](fb2.py)
- moved defaults init with config to `_defaults_init` renamed from `config_defaults_init` and removed config stuff from dunder func `__init__`







## 13/02/25
### [fb2.py](fb2.py)
- added default encoding `utf-8` to `set_defaults` function
- changed default encoding from hardcoded one to `self .defaault_encoding_str`. However it is still `utf-8`
- `filename_str` and `encoding_dtr` moved from confug to obect properties since it is obviously not config values


__doc__="""
This module contains functions for parsing arguments of CLI tools
"""
def opt_exists (opt : str, prependDash : bool = True, singleDashPrepend=False) -> bool :
        """
        Check if passed option exists in CLI call
        
          Using this function while calling script.py --opt will return True if `opt` param is 'opt'
        
         :param opt: option name to check
         :type opt: str

         :param prependDash: whether need to prepend opt with dash or not. Default True, so opt could be passed here without dash. Optuonal. Default: True
         :type prependDash: bool, optional

         :param singleDashPrepend: if prependDash arg isvtrue prepend only in option style with single dash, otherwise prepend long (with len not equal to one) options with double dash. Optional. Default: False (double dash will be prepended e. g. `opt1` > `--opt1`
         :type singleDashPrepend: bool, optional

        """
        _opt=opt
        if prependDash :
                if len(_opt)==1 or singleDashPrepend:
                        _opt = "-"+_opt
                else:
                        _opt = "--"+opt
        for o in sys.argv :
                if o==_opt:
                        return True

        return False
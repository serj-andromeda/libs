function var_is_set_boolint {
	declare -p "$1" &>/dev/null
}



function is_silent_boolint {
	var_is_set_boolint 'ps_silence'
}
is_silent_boolint || echo "start of ps_funcs.sh"

# arguments: src (file/dir name ?), target (link name ?)
function symlink {
	ln -s $1 $2;
}

default_tag="home_phone"
<< doc_01
@ arg1 file to log
@ arg2 message to log
@ arg3 tag
doc_01
function log {
tag=$3
echo "@$tag "`date +"[%D %T]"` $2 >>$1
}

<< doc_02
Returns backup dir based on current date and time. Creates it if need.
doc_02
function get_bak_tm_dir_or_mk_it_str {
	ps_bak_root_dir_str="$HOME/Backups"
        ps_date_str=`psdate.sh`
        ps_time_str=`pstime.sh`
        ps_dir_sep='/'

#       echo "root is $ps_bak_root_dir_str"

        ps_bak_tm_dir_str="${ps_bak_root_dir_str}${ps_dir_sep}${ps_date_str}${ps_dir_sep}${ps_time_str}"
        if [ -d $ps_bak_tm_dir_str ]; then
                noop
        else
                mkdir -p $ps_bak_tm_dir_str
        fi

        echo $ps_bak_tm_dir_str
}
echo -e "@ps\033[93m" "bashsrc: {realpath $BASH_SOURCE}  "\033[0m"
is_silent_boolint || echo "end of ps_funcs.sh"

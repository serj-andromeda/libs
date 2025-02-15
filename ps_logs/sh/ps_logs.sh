default_fn="~/logs/common.log"
default_tag="phone_honor"
<< doc
@ arg1 file to log
@ arg2 message to log
@ arg3 tag
doc
function log {
date_format_str="%y-%m-%d"
fn_str="$1"
msg_str="$2"
tag_str="$3"
echo "@ps [$tag_str] "`date +"[$date_format_str %T]"` msg_str >> fn_str
}
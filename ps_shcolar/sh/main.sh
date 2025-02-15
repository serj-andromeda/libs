# main module of SHColAr lib. Must be sourced where it using like this: `source $path_to_libs/shcolar/sh/main.sh`

lib_dn_str=$(realpath $(dirname BASH_SOURCE[0]))
echo "sh dir: $lib_dn_str"


source $lib_dn_str/fg.sh
source $lib_dn_str/bg.sh
source $lib_dn_str/ctrl.sh

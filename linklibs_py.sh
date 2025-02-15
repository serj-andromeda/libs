#! /usr/bin/env bash
. ~/dev/_libs/ps_funcs/sh/ps_funcs.sh
dir_sep="/"; set -x
libs_dir_src_str="."
links_dir_str=`print_py_libs_dir.py`

lib_subdir_str="py"
libs_dir_abs_str="`realpath $libs_dir_src_str`"
wrk_dir_str= $libs_dir_abs_str

echo src: $libs_dir_src_str abs: $libs_dir_abs_str wrk: $wrk_dir_str

libs_dirs_arr=$(find $wrk_dir_str -maxdepth 2 -mindepth 2 -type d -name $lib_subdir_str)

echo Traverse through array \( $libs_dirs_arr \):
for lib_dir_str in $libs_dirs_arr
do
	lib_dir_abs_str=`realpath $lib_dir_str`
	lib_name_str=`echo $lib_dir_str | grep -oP '(?<=\/)([^\/]+)(?=\/py)'`
	link_name_str=`echo $links_dir_str$dir_sep$lib_name_str`
	echo Lib dir: $lib_dir_str
	echo Lib dir abs: $lib_dir_abs_str
	echo Lib name: $lib_name_str
	echo Link name: $link_name_str


	echo Trying to create symlink from $link_name_str to $lib_dir_abs_str
	ln -s $lib_dir_abs_str $link_name_str && echo "Success!" || echo "Failed!"
done


ln -s /data/data/com.termux/files/home/dev/_common/py_headers /data/data/com.termux/files/usr/lib/python3.12/site-packages/ps_py_headers && echo "Success! Symlink to py_headers created successfully" || echo " Failed! Symlink to py_headers create failed with exit code $?";
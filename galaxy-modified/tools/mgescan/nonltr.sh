#!/bin/bash
if [ ! -f ~/.mgescanrc ]
then
	".mgescanrc is not found."
	exit
fi
. ~/.mgescanrc

user_dir=$MGESCAN_HOME
script_program=`which python`
script=$user_dir/mgescan/mgescan/nonltr.py
program=$1
input_file=$2
input_file_name=`basename $input_file`
hmmsearch_version=$4
output_file=$5

source $user_dir/virtualenv/mgescan/bin/activate >> /dev/null

$script_program $script $program $input_file --output=$output_file

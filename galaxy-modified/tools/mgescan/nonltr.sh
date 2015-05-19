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
input_file_name=$3
input_file_name=`basename $input_file`
hmmsearch_version=$4
output_file=$5

source $user_dir/virtualenv/mgescan/bin/activate >> /dev/null

if [ "$program" == "qvalue" ]
then
	input_file2=$4
	input_file_name2=`basename $input_file2`
	hmmsearch_version=$6
	output_file=$7
fi
$script_program $script $program $input_file --output=$output_file

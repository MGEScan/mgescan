#!/bin/bash
#user_dir=/u/lee212
#source ~/virtualenv/retrotminer/bin/activate

if [ ! -f ~/.mgescanrc ]
then
	".mgescanrc is not found."
	exit
fi
. ~/.mgescanrc
userdir=$MGESCAN_HOME
script_program=`which python`
script=$user_dir/github/retrotminer/retrotminer/ltr/toGFF.py

input_file=$1
output_file=$2

#move to the working directory
work_dir=`dirname $script`
cd $work_dir

#create directory for input and output
t_dir=`mktemp -p input -d` #relative path
input_dir="$work_dir/$t_dir/seq" # full path
output_dir="$work_dir/$t_dir/data"
mkdir -p $input_dir
mkdir -p $output_dir

#make a copy of input
/bin/cp $input_file $input_dir/$input_file

#run
$script_program $script $input_dir/$input_file $output_file

if [ $? -eq 0 ]
then
	rm -rf $work_dir/$t_dir
else
	cp -pr $work_dir/$t_dir $work_dir/error-cases/
fi

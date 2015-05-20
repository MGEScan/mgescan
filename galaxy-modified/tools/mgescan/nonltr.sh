#!/bin/bash
if [ ! -f ~/.mgescanrc ]
then
	".mgescanrc is not found."
	exit
fi
. ~/.mgescanrc

user_dir=$MGESCAN_HOME
source $user_dir/virtualenv/mgescan/bin/activate >> /dev/null
script_program=`which python`
script=$user_dir/mgescan/mgescan/nonltr.py
program_name=$1
input_file=$2
input_file_name=$3
input_file_name=`basename $input_file`
hmmsearch_version=$4
output_file=$5


if [ "$program_name" == "qvalue" ]
then
	input_file2=$4
	input_file_name2=`basename $input_file2`
	hmmsearch_version=$6
	output_file=$7
fi

#move to the working directory
work_dir=`dirname $script`
cd $work_dir
#create directory for input and output
mkdir -p input
t_dir=`mktemp -p input -d` #relative path
input_dir="$work_dir/$t_dir/seq" # full path
output_dir="$work_dir/$t_dir/data"
mkdir -p $input_dir
mkdir -p $output_dir

# Check tar.gz
tar tf $input_file 2> /dev/null
ISGZ=$?
if [ -z $ISGZ ]
then
	tar xzf $input_file -C $input_dir
else
	/bin/ln -s $input_file $input_dir/$input_file_name
fi

$script_program $script $program_name $input_dir --output=$output_dir
FILES=`ls $output_dir`
tar czf $output_file --directory=$output_dir $FILES

#!/bin/bash
#user_dir=/u/lee212
#source ~/virtualenv/retrotminer/bin/activate

if [ ! -f ~/.mgescanrc ]
then
	".mgescanrc is not found."
	exit
fi
. ~/.mgescanrc
user_dir=$MGESCAN_HOME
script_program=`which perl`
script=$user_dir/github/retrotminer/retrotminer/ltr/pre_processing.pl

input_file=$1
input_file_name=$2
output_file=$3
scaffold_YN=$4
repeatmasker_YN=$5

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
/bin/cp $input_file $input_dir/$input_file_name

#run
$script_program $script -genome=$input_dir/ -data=$output_dir/ -sw_rm=${repeatmasker_YN} -scaffold=${scaffold_YN} 

if [ "$scaffold_YN" == "Yes" ]
then
	temp_file=`mktemp -p ./`
	tar cvzf ${temp_file}.tar.gz $output_dir/genome/
	/bin/cp ${temp_file}.tar.gz $output_file
	rm -rf $temp_file
	rm -rf ${temp_file}.tar.gz
fi

if [ "$repeatmasker_YN" == "Yes" ]
then
	# chr2L.fa.cat.gz  chr2L.fa.masked  chr2L.fa.out  chr2L.fa.out.pos  chr2L.fa.tbl
	temp_file=`mktemp -p ./`
	tar cvzf ${temp_file}.tar.gz $output_dir/repeatmasker/
	/bin/cp ${temp_file}.tar.gz $output_file
	rm -rf $temp_file
	rm -rf ${temp_file}.tar.gz
fi

if [ $? -eq 0 ]
then
	rm -rf $work_dir/$t_dir
else
	cp -pr $work_dir/$t_dir $work_dir/error-cases/
fi

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

program_name=$1
input_file=$2
input_file_name=$3
output_file=$4
scaffold_YN=$5

if [ "$program_name" == "repeatmasker" ]
then
	repeatmasker_YN="Yes"
else
	repeatmasker_YN="No"
fi

#move to the working directory
work_dir=$MGESCAN_SRC/mgescan
cd $work_dir

#create directory for input and output
mkdir -p input
t_dir=`mktemp -p input -d` #relative path
input_dir="$work_dir/$t_dir/seq" # full path
output_dir="$work_dir/$t_dir/data"
mkdir -p $input_dir
mkdir -p $output_dir

# Check tar.gz
tar tf $input_file &> /dev/null
ISGZ=$?
if [ 0 -eq $ISGZ ]
then
	tar xzf $input_file -C $input_dir
else
	/bin/ln -s $input_file $input_dir/$input_file_name
fi

#run
$script_program $script -genome=$input_dir/ -data=$output_dir/ -sw_rm=${repeatmasker_YN} -scaffold=${scaffold_YN} 

if [ "$scaffold_YN" == "Yes" ]
then
	temp_file=`mktemp -p ./`
	tar cvzf ${temp_file}.tar.gz $output_dir/genome/
	/bin/mv ${temp_file}.tar.gz $output_file
	rm -rf $temp_file
	#rm -rf ${temp_file}.tar.gz
fi

if [ "$repeatmasker_YN" == "Yes" ]
then
	# chr2L.fa.cat.gz  chr2L.fa.masked  chr2L.fa.out  chr2L.fa.out.pos  chr2L.fa.tbl
	temp_file=`mktemp -p ./`
	tar cvzf ${temp_file}.tar.gz $output_dir/repeatmasker/
	/bin/mv ${temp_file}.tar.gz $output_file
	rm -rf $temp_file
	#rm -rf ${temp_file}.tar.gz
fi

if [ $? -eq 0 ]
then
	rm -rf $work_dir/$t_dir
else
	# DEBUG CODE
	# cp -pr $work_dir/$t_dir $work_dir/error-cases/
fi

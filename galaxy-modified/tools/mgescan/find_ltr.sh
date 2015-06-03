#!/bin/bash
if [ ! -f ~/.mgescanrc ]
then
	".mgescanrc is not found."
	exit
fi
. ~/.mgescanrc
user_dir=$MGESCAN_HOME
source $user_dir/virtualenv/mgescan/bin/activate >> /dev/null
script_program=`which perl`
script=$user_dir/mgescan/mgescan/ltr/find_ltr.pl
input_file=$1
input_file_name=$2
output_file=$3
min_dist=$4
max_dist=$5
min_len_ltr=$6
max_len_ltr=$7
ltr_sim_condition=$8
cluster_sim_condition=$9
len_condition=${10}
hmmsearch_version=3 # version 3 fixed

# $HOME/mgescan/galaxy-dist/tools/mgescan/find_ltr.sh /$HOME/mgescan/galaxy-dist/database/files/000/dataset_1.dat /$HOME/mgescan/galaxy-dist/database/files/000/dataset_3.dat

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

$script -genome=$input_dir/ -data=$output_dir/ -hmmerv=$hmmsearch_version -min_dist=$min_dist -max_dist=$max_dist -min_len_ltr=$min_len_ltr -max_len_ltr=$max_len_ltr -ltr_sim_condition=$ltr_sim_condition -cluster_sim_condition=$cluster_sim_condition -len_condition=$len_condition

FILES=`ls $output_dir`
tar czf $output_file --directory=$output_dir $FILES

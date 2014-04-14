#!/bin/bash

user_dir=/u/lee212/
script=$user_dir/retrotminer/wazim/MGEScan1.0/run_MGEScan.pl
input_file=$1
hmmsearch_version=$2
output_file=$3
program=$4 # N is nonLTR, L is LTR and B is both
# /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/tools/retrotminer/find_ltr.sh /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/database/files/000/dataset_1.dat /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/database/files/000/dataset_3.dat

input_dir=`mktemp -d`
output_dir=`mktemp -d`

#set path for transeq
export PATH=$user_dir/retrotminer/EMBOSS/bin/:$PATH

#make a copy of input
/bin/cp $input_file $input_dir

#run
$script -genome=$input_dir/ -data=$output_dir/ -hmmerv=$hmmsearch_version -program=$program

#make a coput of output
/bin/cp $output_dir/ltr/ltr.out $output_file

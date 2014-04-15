#!/bin/bash

user_dir=/u/lee212/
script=$user_dir/retrotminer/wazim/MGEScan1.0/run_MGEScan.pl
input_file=$1
hmmsearch_version=$2
output_file=$3
program=$4 # N is nonLTR, L is LTR and B is both
# Optional output parameters for nonLTR
clade=$5
en=$6
rt=$7
# /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/tools/retrotminer/find_ltr.sh /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/database/files/000/dataset_1.dat /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/database/files/000/dataset_3.dat


input_dir=`mktemp -d`
output_dir=`mktemp -d`

#set path for transeq
export PATH=$user_dir/retrotminer/EMBOSS/bin/:$PATH

#make a copy of input
/bin/cp $input_file $input_dir

#run
#$script -genome=$input_dir/ -data=$output_dir/ -hmmerv=$hmmsearch_version -program=$program

#output_dir=/tmp/tmp.jAhYBeN8tz
#make a coput of output
if [ "$program" == "L" ] || [ "$program" == "B" ]
then
	/bin/cp $output_dir/ltr/ltr.out $output_file
fi
if [ "$program" == "N" ] || [ "$program" == "B" ]
then

	#compressed_file=$output_dir/$RANDOM.tar.gz
	#/bin/tar cvzfP $compressed_file $output_dir/info
	#/bin/cp $compressed_file $output_file
	/bin/cp $output_dir/info/full/*/* $clade
	/bin/cp $output_dir/info/validation/en $en
	/bin/cp $output_dir/info/validation/rt $rt
#else
	# Both LTR, nonLTR executed
	#compressed_file=$output_dir/$RANDOM.tar.gz
	#/bin/tar cvzfP $compressed_file $output_dir
	#/bin/cp $compressed_file $output_file
fi

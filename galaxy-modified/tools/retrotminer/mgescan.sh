#!/bin/bash

user_dir=/u/lee212
script=$user_dir/retrotminer/wazim/MGEScan1.1/run_MGEScan.pl
input_file=$1
input_file_name=$2
hmmsearch_version=$3
output_file=$4
program=$5 # N is nonLTR, L is LTR and B is both
# Optional output parameters for nonLTR
clade=$6
en=$7
rt=$8
ltr_gff3=$9
nonltr_gff3=${10}

# /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/tools/retrotminer/find_ltr.sh /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/database/files/000/dataset_1.dat /nfs/nfs4/home/lee212/retrotminer/galaxy-dist/database/files/000/dataset_3.dat

#load env?
source $user_dir/.bashrc
source $user_dir/.bash_profile

#set path for transeq
export PATH=$user_dir/retrotminer/EMBOSS/bin:/usr/bin:$PATH

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

if [ "2" == "$hmmsearch_version" ]
then
	export PATH=$user_dir/retrotminer/HMMER2.0/bin:$PATH
else
	export PATH=/usr/bin:$PATH
fi

#run
/usr/bin/perl $script -genome=$input_dir/ -data=$output_dir/ -hmmerv=$hmmsearch_version -program=$program
#RES=`ssh -i $user_dir/.ssh/.internal silo.cs.indiana.edu "/usr/bin/perl $script -genome=$input_dir/ -data=$output_dir/ -hmmerv=$hmmsearch_version -program=$program > /dev/null"`

#make a copy of output
if [ "$program" != "N" ]
then
	/bin/cp $output_dir/ltr/ltr.out $output_file
	if [ "$ltr_gff3" != "" ]
	then
		/bin/cp $output_dir/ltr/ltr.gff3 $ltr_gff3
	fi
fi
if [ "$program" != "L" ]
then

	#compressed_file=$output_dir/$RANDOM.tar.gz
	#/bin/tar cvzfP $compressed_file $output_dir/info
	#/bin/cp $compressed_file $output_file
	/bin/cp $output_dir/info/full/*/* $clade
	/bin/cp $output_dir/info/validation/en $en
	/bin/cp $output_dir/info/validation/rt $rt
	if [ "$nonltr_gff3" != "" ]
	then
		/bin/cp $output_dir/info/nonltr.gff3 $nonltr_gff3
		# nonltr.gff3
		##gff-version 3
		#chr2L.fa        MGEScan_nonLTR  mobile_genetic_element  19670384        19676921        .       .       .       ID=chr2L.fa_19670384
		#chr2L.fa        MGEScan_nonLTR  mobile_genetic_element  17689430        17695994        .       .       .       ID=chr2L.fa_17689430
		#chr2L.fa        MGEScan_nonLTR  mobile_genetic_element  11897186        11903717        .       .       .       ID=chr2L.fa_11897186
		#chr2L.fa        MGEScan_nonLTR  mobile_genetic_element  49574   56174   .       .       .       ID=chr2L.fa_49574
	fi

#else
	# Both LTR, nonLTR executed
	#compressed_file=$output_dir/$RANDOM.tar.gz
	#/bin/tar cvzfP $compressed_file $output_dir
	#/bin/cp $compressed_file $output_file
fi

# delete temp directory
rm -rf $work_dir/$t_dir

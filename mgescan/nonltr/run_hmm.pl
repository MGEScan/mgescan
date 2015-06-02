#!/usr/bin/perl  -w
use strict;
use Getopt::Long;
use Cwd 'abs_path';
use File::Basename;

my $pdir = dirname(abs_path($0))."/";
my $phmm_dir = $pdir."pHMM/";
my $hmmerv;
##########################################################
# get input parameter of dna file, pep file, output dir
##########################################################
#print "Getting input parameter...\n";
my ($dna_file, $pep_file, $out_dir, $dna_name, $command);
my ($out1_dir, $out_file, $pos_dir);
get_parameter(\$dna_file, \$out_dir, \$hmmerv);
get_id(\$dna_file, \$dna_name);

$out1_dir = $out_dir."out1/";
if (-e $out1_dir){
}else{
	system("mkdir ".$out1_dir);
}
$pos_dir = $out_dir."pos/";
if (-e $pos_dir){
}else{
	system("mkdir ".$pos_dir);
}


##########################################################
# get signal for some state of ORF1, RT, and APE
# need HMMSEARCH
##########################################################
print "Getting signal...\n";
my ($phmm_file, $domain_rt_pos_file, $domain_ape_pos_file, $domain_orf1_pos_file);

print "    Protein sequence...\n";
$pep_file = $out_dir.$dna_name.".pep";
$command = $pdir."translate -d ".$dna_file." -h ".$dna_name." -p ".$pep_file;
system($command);

print "    RT signal...\n";
$phmm_file = $phmm_dir."ebi_ds36752_seq.hmm";
$domain_rt_pos_file = $pos_dir.$dna_name.".rt.pos";
get_signal_domain(\$pep_file, \$phmm_file, \$domain_rt_pos_file);

print "    APE signal...\n";
$phmm_file = $phmm_dir."ebi_ds36736_seq.hmm";
$domain_ape_pos_file = $pos_dir.$dna_name.".ape.pos";
get_signal_domain(\$pep_file, \$phmm_file, \$domain_ape_pos_file);

##############################################################################
# generate corresponsing empty domains files if either of them does not exist 
##############################################################################
if (-e $domain_rt_pos_file  || -e $domain_ape_pos_file ){

	print $dna_name."\n";

	if (! -e $domain_rt_pos_file){
		open OUT, ">$domain_rt_pos_file";
		print OUT "";
		close(OUT);
	}elsif (! -e $domain_ape_pos_file){
		open OUT, ">$domain_ape_pos_file";
		print OUT "";
		close(OUT);
	}

	$command = $pdir."match_pos.pl -rt=".$domain_rt_pos_file." -ape=".$domain_ape_pos_file;
	#system($command);
	###########################################################
	# run hmm
	###########################################################
	#print "Running HMM...\n";

	$out_file = $out1_dir.$dna_name;
	$command = $pdir."hmm/MGEScan -m ".$pdir."hmm/chr.hmm -s ".$dna_file." -r ".$domain_rt_pos_file." -a ".$domain_ape_pos_file." -o ".$out_file." -p ".$pdir." -d ".$out1_dir." -v ".$hmmerv;
	#print $command."\n";
	system($command); 
}


if (-e $pep_file){
	#system("rm ".$pep_file);
}

###########################################################
#                        SUBROUTINE                       #
###########################################################


sub get_signal_domain{

	#$_[0]: pep seq file
	#$_[1]: domain hmm file
	#$_[2]: output domain dna position file

	my %domain_start=();
	my %domain_end=();
	my $evalue;
	my $temp_file = ${$_[2]}."temp";
	my $temp_file2 = ${$_[2]}."temp2";
	my $output_file = ${$_[2]};
	my $fh;
	my $tmpfile;
	my $template;

	use File::Temp qw/ tempfile tempdir /;
	($fh, $tmpfile) = tempfile( $template, DIR => $phmm_dir, SUFFIX => '.tbl');

	open (OUT, ">$temp_file");
	if ($hmmerv == 3){
		#system("hmmconvert ".${$_[1]}." > ".${$_[1]}."c");
		my $hmm_command = "hmmsearch  -E 0.00001 --noali --domtblout ".$tmpfile." ".${$_[1]}."3 ".${$_[0]}." > /dev/null";
		system($hmm_command);
		$hmm_command = "cat ".$tmpfile;
		my $hmm_result = `$hmm_command`;
		system("rm -rf ".$tmpfile);
		# run hmmsearch to find the domain and save it in the temprary file   
		while ($hmm_result =~ /\n((?!#).*)\n/g){
			my @temp = split(/\s+/, $1);
			if ($temp[11]<0.001 ){
				print OUT eval($temp[17]*3)."\t".eval($temp[18]*3)."\t".$temp[15]."\t".$temp[16]."\t".$temp[13]."\t".$temp[11]."\n";
			}
		}

	}else{
		my $hmm_command = "hmmsearch  -E 0.00001 ".${$_[1]}." ".${$_[0]};
		my $hmm_result = `$hmm_command`;
		# run hmmsearch to find the domain and save it in the temprary file    
		while ($hmm_result =~ /((\S)+\s+\d+\/\d+\s+\d+\s+\d+\s+(\[|\.)(\]|\.)\s+\d+\s+\d+\s+(\[|\.)(\]|\.)\s+(-)*\d+\.\d+\s+((\d|\-|\.|e)+))\s*/g){
			my @temp = split(/\s+/, $1);
			if ($temp[9]<0.001 ){
				print OUT eval($temp[2]*3)."\t".eval($temp[3]*3)."\t".$temp[5]."\t".$temp[6]."\t".$temp[8]."\t".$temp[9]."\n";
			}
		}
	}
	close(OUT);
	if (-s $temp_file >0){
		system("sort +0 -1n ".$temp_file." > ".$temp_file2);

		my $start = -1;
		my $end = -1;
		my @pre = (-1000, -1000, -1000, -1000, -1000, -1000);
		open(IN, $temp_file2);
		open OUT, ">$output_file";
		while(my $each_line=<IN>){
			my @temp = split(/\s+/, $each_line);

			if ($temp[0] - $pre[1] < 300 ) {
				$end = $temp[1];
				$evalue = $evalue * $temp[5];
			}else{
				if($start>=0 && $evalue < 0.00001){
					print OUT $start."\t".$end."\t".$pre[4]."\t".$pre[5]."\n";
				}
				$start = $temp[0];
				$end = $temp[1];
				$evalue = $temp[5];
			}
			@pre = @temp;
		}
		if($start>=0 && $evalue < 0.00001){ 
			print OUT $start."\t".$end."\t".$pre[4]."\t".$pre[5]."\n";
		}
		close(IN);
		close(OUT);
		#system("rm ".$temp_file2);
	}
	#system("rm ".$temp_file);
}

sub get_id{

	my @temp = split(/\//, ${$_[0]});
	${$_[1]} = $temp[$#temp];
	
	# use Bio::SeqIO;
	# my $seqio_obj = Bio::SeqIO->new(-file => ${$_[0]}, -format => "fasta" );
	# my $seq = $seqio_obj->next_seq;
	# ${$_[1]} = $seq->display_id;


	# post_process.pl searches original sequence files with its id. The file
	# name, because of that, needs to be changed to id.
	# my $name;
	# my $path;
	# my $suffix;
	# ($name,$path,$suffix) = fileparse(${$_[0]});
	# rename(${$_[0]}, $path ."/".${$_[1]});
	# ${$_[0]} = $path ."/".${$_[1]};
}


sub usage {
	die "Usage: run_hmm.pl --dna=<dna_file_path>  --out=<output_dir> --hmmerv=<2,3>";
}


sub get_parameter{

	my ($dna, $out, $hmmerv);

	GetOptions(
		'dna=s' => \$dna,
		'out=s' => \$out,
		'hmmerv=s' => \$hmmerv,
	);

	if (! -e $dna){
		print "ERROR: The file $dna does not exist.\n";
		usage();
	}
	if (length($hmmerv)==0){
		print "ERROR: HMMER version not provided.\n";
		usage();
		exit;
	}
	if (! -d $out){
		system("mkdir ".$out);
	}

	${$_[0]} = $dna;
	${$_[1]} = $out;
	${$_[2]} = $hmmerv;
}



sub get_sequence{  # file name, variable for seq, variable for head                                   \


	open(GENOME, $_[0])|| die("ERROR: Couldn't open genome_file $_[0]!\n");
	while( my $each_line=<GENOME>)  {

		if ($each_line =~ m/>/){
			${$_[1]} = "";
			chomp($each_line);
			${$_[2]} = $each_line;
		}else{
			chomp($each_line);
			${$_[1]} .= $each_line;
		}
	}
	close(GENOME);
}


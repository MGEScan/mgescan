#!/usr/bin/perl
use strict; 
use Getopt::Long;

my $seq; 
my $phmm_file;
my $out_dir;
my $seq_file;
my $pep_file;
my $command;
my @hmm_results;
my $hmm_result;
my $hmmerv;
my $phmm_dir;

GetOptions(    'seq=s' => \$seq,
	'hmmfile=s' => \$phmm_file,
	'odir=s' => \$out_dir,
	'v=s' => \$hmmerv,
	'd=s' => \$phmm_dir,
);

my $fh1;
my $fh2;
my $tmpfile1;
my $tmpfile2;
my $template1;
my $template2;

use File::Temp qw/ tempfile tempdir /;
($fh1, $tmpfile1) = tempfile( $template1, DIR => $out_dir, SUFFIX => '.aaaaa');
($fh2, $tmpfile2) = tempfile( $template2, DIR => $out_dir, SUFFIX => '.bbbbb');

$seq_file = $tmpfile1;#$out_dir."aaaaa";
$pep_file = $tmpfile2;#$out_dir."bbbbb";

system("echo ".$seq." > ".$seq_file);
system("transeq -frame=f ".$seq_file." -outseq=".$pep_file." 2>/dev/null");
system("rm -f ".$seq_file);

if ($hmmerv == 3){
	my $fh;
	my $tmpfile;
	my $template;
	($fh, $tmpfile) = tempfile( $template, DIR => $phmm_dir, SUFFIX => '.tbl');
	#system("hmmconvert ".$phmm_file." > ".$phmm_file."c");
	#system("hmmsearch  --noali --domtblout ".$phmm_dir."tbl ".$phmm_file."c ".$pep_file." > /dev/null");
	system("hmmsearch  --noali --domtblout ".$tmpfile." ".$phmm_file."3 ".$pep_file." > /dev/null");
	my $command = "cat ".$tmpfile;
	my $hmm_result = `$command`;
	system("rm -f ".$tmpfile);
	@hmm_results = split(/\n/, $hmm_result);
	for (my $i=0; $i<=$#hmm_results; $i++){
		
		if ($hmm_results[$i] =~ /^\#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\s\-\-\-\-\-\-\-\-\-\-\s/){
		if ($hmm_results[$i+1] =~ /^\S/){
			my @temp = split(/\s+/, $hmm_results[$i+1]);
			print $temp[11];
		}else{
			print "1";
		}
		last;
		}
	}
}else{
	$command = "hmmsearch ".$phmm_file." ".$pep_file;
	#print $command;
	$hmm_result = `$command`;
	 
	@hmm_results = split(/\n/, $hmm_result);
	for (my $i=0; $i<=$#hmm_results; $i++){
		
		if ($hmm_results[$i] =~ /^\-\-\-\-\-\-\-\-\s\-\-\-\-\-\-\-\s/){
		if ($hmm_results[$i+1] =~ /^\S/){
			my @temp = split(/\s+/, $hmm_results[$i+1]);
			print $temp[9];
		}else{
			print "1";
		}
		last;
		}
	}	
}

system("rm -f ".$pep_file);

#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
	print sys.argv[0], "LTRout new-GFF-file"
	sys.exit()

infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
cluster = ""
print >>outfile, "##gff-version 3"
for aline in infile:
	aline = aline.strip()
	words = aline.split(None)
	if len(words) == 1:
		cluster = aline[:aline.find("-")]
	else:
		if len(words) == 0:
			continue
		seqid = words[0][:words[0].rfind("_")]
		id = cluster + "_" + words[0]
		des = [seqid, "MGEScan_LTR", "mobile_genetic_element", words[1], words[4], ".", words[5], ".", "ID=" + id + ";name=cluster_"+cluster] 
		print >>outfile, "\t".join(des)
outfile.close()
infile.close()
		


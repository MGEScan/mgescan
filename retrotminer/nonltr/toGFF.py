#!/usr/bin/env python

import sys
import os
import glob
import re

if len(sys.argv) < 3:
	print sys.argv[0], "outdir new-GFF-file"
	sys.exit()
	
def readFASTA(filename):
 fastalines = []
 f = open(filename)
 lines = f.readlines()
 f.close()
 if lines[0][0] != '>':
  sys.exit("Invalid FASTA file: "+filename)
 seq = ""
 header = ""
 for line in lines:
  if len(line) > 0:
   if line[0]=='>':
    if seq != "":
     fastalines.append([header,seq])
     seq = ""
    header = line.strip()[1:]
   else:
    line = re.sub(r'\s','',line)
    seq = seq + line
 if seq != "":
  fastalines.append([header,seq])
 return fastalines

outfile = open(sys.argv[2], "w")
print >>outfile, "##gff-version 3"
 
for cladeDir in glob.glob( os.path.join(sys.argv[1], '*') ):
	basename = os.path.basename(cladeDir)
	filepath = cladeDir + "/" + basename + ".dna"
	fastalist = readFASTA(filepath)
	for fastaitem in fastalist:
		header = fastaitem[0]
		seq = fastaitem[1]
		seqid = header[:header.find("_")]
		start = int(header[header.rfind("_")+1:])
		des = [seqid, "MGEScan_nonLTR", "mobile_genetic_element", str(start), str(start+len(seq)), ".", ".", ".", "ID=" + header] 
		print >>outfile, "\t".join(des)

outfile.close()

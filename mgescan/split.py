from Bio import SeqIO
record_iter = SeqIO.parse(open("large.fasta"),"fasta")
for val in record_iter:
    filename=val.id+".fa"
    handle = open(filename, "w")
    SeqIO.write([val], handle, "fasta")
    handle.close()


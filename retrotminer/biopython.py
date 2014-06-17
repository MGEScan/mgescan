from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import ntpath
import os

def make_rc_record(record):
    """Returns a new SeqRecord with the reverse complement sequence."""
    """Ref: https://www.biostars.org/p/14614/"""
    return SeqRecord(seq = record.seq.reverse_complement(), \
           id = record.id, \
           # "rc_" + record.id, \
           description = record.description) # "reverse complement")

def reverse_complement_fasta(filepath, dest):
    filename = ntpath.basename(filepath)
    dest_path = os.path.abspath(dest + "/" + filename)
    records = map(make_rc_record, SeqIO.parse(filepath, "fasta"))
    SeqIO.write(records, dest_path , "fasta")

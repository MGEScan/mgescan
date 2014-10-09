"""split.py: separate a large file

Usage:
    split.py <genome_dir> [--output=<data_dir>]
    split.py (-h | --help)
    split.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
    --output=<data_dir> Directory results will be saved

"""
from docopt import docopt
from Bio import SeqIO
def split_file(filename, output_path):

    record_iter = SeqIO.parse(open("large.fasta"),"fasta")
    for val in record_iter:
        filename=val.id+".fa"
        handle = open(filename, "w")
        SeqIO.write([val], handle, "fasta")
        handle.close()


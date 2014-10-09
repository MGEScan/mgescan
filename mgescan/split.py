"""split.py: separate a large file

Usage:
    split.py <filename> [--output=<data_dir>]
    split.py (-h | --help)
    split.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
    --output=<data_dir> Directory results will be saved

"""
from docopt import docopt
from Bio import SeqIO
from mgescan import utils

class Split(object):

    data = None
    default_output = "./split-output"

    def __init__(self, args):
        self.args = args
        self.set_inputs()
        self.set_defaults()

    def set_inputs(self):
        self.data_dir = utils.get_abspath(self.args['--output'])
        self.input_file = utils.get_abspath(self.args['<filename>'])

    def set_defaults(self):
        """Set default values to run programs

        """

        self.data_dir = utils.create_directory(self.data_dir or
                self.default_output)

    def run(self):
        print self.args

    def split_file(self, filename, output_path):

        record_iter = SeqIO.parse(open("large.fasta"),"fasta")
        for val in record_iter:
            filename=val.id+".fa"
            handle = open(filename, "w")
            SeqIO.write([val], handle, "fasta")
            handle.close()

def main():
    arguments = docopt(__doc__, version='split.py 0.1')
    split = Split(arguments)
    split.run()

if __name__ == "__main__":
    main()

"""split.py: separate a large file

Usage:
    split.py <filename> [--output=<results>]
    split.py (-h | --help)
    split.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
    --output=<results> Directory results will be saved

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
        self.result_path = utils.get_abspath(self.args['--output'])
        self.input_file = utils.get_abspath(self.args['<filename>'])

    def set_defaults(self):
        """Set default values to run programs"""
        self.result_path = utils.create_directory(self.result_path or
                self.default_output)

    def run(self):
        self.split_file(self.input_file, self.result_path)

    def split_file(self, filename, output_path):

        record_iter = SeqIO.parse(open(filename),"fasta")
        for val in record_iter:
            filename=val.id+".fa"
            handle = open(output_path + "/" + filename, "w")
            SeqIO.write([val], handle, "fasta")
            handle.close()

def main():
    arguments = docopt(__doc__, version='split.py 0.1')
    split = Split(arguments)
    split.run()

if __name__ == "__main__":
    main()

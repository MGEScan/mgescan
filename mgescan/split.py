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
from os import listdir
from os.path import isfile, join
from mgescan import utils

class Split(object):

    data = None
    result_path = None
    default_output = "./split-output"

    def __init__(self, args=None):
        self.args = args
        if args:
            self.set_parameters()
            self.set_defaults()

    def set_parameters(self):
        self.set_output(self.args['--output'])
        self.set_input(self.args['<filename>'])

    def set_output(self, path):
        self.result_path = utils.get_abspath(path)

    def set_input(self, path):
        self.input_file = utils.get_abspath(path)

    def set_defaults(self):
        """Set default values to run programs"""
        if self.result_path:
            self.result_path = utils.create_directory(self.result_path, False)
        else:
            self.result_path = utils.create_directory(self.default_output)

    def run(self):
        self.split_file(self.input_file, self.result_path)

    def split_file(self, filename, output_path):

        record_iter = SeqIO.parse(open(filename),"fasta")
        for val in record_iter:
            filename=val.id+".fa"
            handle = open(output_path + "/" + filename, "w")
            SeqIO.write([val], handle, "fasta")
            handle.close()

    def split_files(self, dirpath=None, output_path=None):

        if not dirpath:
            dirpath = self.input_file
        if not output_path:
            output_path = self.result_path

        onlyfiles = [ f for f in listdir(dirpath) if isfile(join(dirpath,f)) ]
        for file in onlyfiles:
        self.split_file(file, output_path)

def main():
    arguments = docopt(__doc__, version='split.py 0.1')
    split = Split(arguments)
    split.run()

if __name__ == "__main__":
    main()

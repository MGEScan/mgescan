"""RetroTMiner

Usage:
    retrotminer.py <genome_dir> [--output=<data_dir>]
    retrotminer.py ltr <genome_dir> [--output=<data_dir>]
    retrotminer.py nonltr <genome_dir> [--output=<data_dir>]
    retrotminer.py (-h | --help)
    retrotminer.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
    --output=<data_dir> Directory results will be saved

"""
from docopt import docopt

class retroTMiner:

    genome_dir = None
    data_dir = None
    ltr_enabled = False
    nonltr_enabled = False

    args = None

    def __init__(self, args):
        self.args = args
        self.set_inputs()

    def set_inputs(self):
        self.data_dir = self.args['--output']
        self.genome_dir = self.args['<genome_dir>']
        self.ltr_enabled = self.args['ltr']
        self.nonltr_enabled = self.args['nonltr']

    def run(self):
        # ltr
        # nonltr
        pass

if __name__ == "__main__":
    arguments = docopt(__doc__, version='RetroTMiner 0.1')
    rtm = retroTMiner(arguments)
    rtm.run()

"""RetroTMiner: identifying ltr and non-ltr in genome sequences

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
from multiprocessing import Process
from subprocess import Popen

class RetroTMiner:
    """ RetroTMiner runs mgescan for identifying ltr and nonltr in genome
    sequence """

    genome_dir = None
    data_dir = None
    ltr_enabled = False
    nonltr_enabled = False

    args = None

    def __init__(self, args):
        self.args = args
        self.set_inputs()
        self.set_defaults()

    def set_inputs(self):
        self.data_dir = self.args['--output']
        self.genome_dir = self.args['<genome_dir>']
        self.ltr_enabled = self.args['ltr']
        self.nonltr_enabled = self.args['nonltr']

    def set_defaults(self):
        """Set default values to run programs

        For LTR,
        min_dist: minimum distance(bp) between LTRs.
        max_dist: maximum distance(bp) between LTRS
        min_len_ltr: minimum length(bp) of LTR.
        max_len_ltr: maximum length(bp) of LTR.
        ltr_sim_condition: minimum similarity(%) for LTRs in an element.
        cluster_sim_condition: minimum similarity(%) for LTRs in a cluster
        len_condition: minimum length(bp) for LTRs aligned in local alignment.
        """

        self.hmmerv = 3
        self.min_dist = 2000
        self.max_dist = 20000
        self.min_len_ltr = 130
        self.max_len_ltr = 2000
        self.ltr_sim_condition = 70
        self.cluster_sim_condition = 70
        self.len_condition = 70

        self.sw_rm = "No" # or Yes
        self.scaffold = None # or directory

    def run(self):
        # ltr
        p1 = Process(target=self.ltr)
        p1.start()
        # nonltr
        p2 = Process(target=self.nonltr)
        p2.start()
        p1.join()
        p2.join()

    def ltr(self):
        print 'ltr: starting'
        # scaffold
        # repeatmasker
        res0 = subprocess.Popen("ltr/pre_process.pl -genome=%(genome_dir)s
        -data=%(data_dir)s -sw_rm=%(sw_rm)s -scaffold=%(scaffold)s" %
        vars(self), stdout=Pipe).stdout.read()
        # find-ltr
        res1 = subprocess.Popen("ltr/find_ltr.pl -genome=%(genome_dir)s \
        -data=%(data_dir)s -hmmerv=%(hmmerv)s -min_dist=%(min_dist)s \
        -max_dist=%(max_dist)s -min_len_ltr=%(min_len_ltr)s \
        -max_len_ltr=%(max_len_ltr)s -ltr_sim_condition=%(ltr_sim_condition)s \
        -cluster_sim_condition=%(cluster_sim_condition)s \
        -len_condition=%(len_condition)s" % vars(self), stdout=PIPE).stdout.read()
        # gff3
        print 'ltr: finishing'

    def nonltr(self):
        print 'nonltr: starting'
        # nonltr
        # gff3
        print 'nonltr: finishing'

if __name__ == "__main__":
    arguments = docopt(__doc__, version='RetroTMiner 0.1')
    rtm = RetroTMiner(arguments)
    rtm.run()

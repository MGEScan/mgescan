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
from subprocess import Popen, PIPE
import os

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
        self.data_dir = self.get_abspath(self.args['--output'])
        self.genome_dir = self.get_abspath(self.args['<genome_dir>'])
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

        self.data_dir = self.data_dir or self.create_directory("./output")

        self.hmmerv = 3
        self.min_dist = 2000
        self.max_dist = 20000
        self.min_len_ltr = 130
        self.max_len_ltr = 2000
        self.ltr_sim_condition = 70
        self.cluster_sim_condition = 70
        self.len_condition = 70

        self.sw_rm = "No" # or Yes
        self.scaffold = "" # or directory

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
        cmd0 = "ltr/pre_process.pl \
                -genome=%(genome_dir)s \
                -data=%(data_dir)s \
                -sw_rm=%(sw_rm)s \
                -scaffold=%(scaffold)s"
        res0 = self.run_cmd(cmd0)

        # find-ltr
        cmd1 = "ltr/find_ltr.pl \
                -genome=%(genome_dir)s \
                -data=%(data_dir)s \
                -hmmerv=%(hmmerv)s \
                -min_dist=%(min_dist)s \
                -max_dist=%(max_dist)s \
                -min_len_ltr=%(min_len_ltr)s \
                -max_len_ltr=%(max_len_ltr)s \
                -ltr_sim_condition=%(ltr_sim_condition)s \
                -cluster_sim_condition=%(cluster_sim_condition)s \
                -len_condition=%(len_condition)s"
        res1 = self.run_cmd(cmd1)

        # gff3
        self.ltr_out_path = self.get_abspath(self.data_dir + "/ltr/ltr.out")
        self.ltr_gff_path = self.get_abspath(self.data_dir + "/ltr/ltr.gff3")
        cmd2 = "ltr/toGFF.py %(ltr_out_path)s %(ltr_gff_path)s"
        res2 = self.run_cmd(cmd2)

        print 'ltr: finishing'

    def nonltr(self):
        print 'nonltr: starting'
        # nonltr
        cmd0 = "nonltr/run_MGEScan.pl \
                -genome=%(genome_dir)s \
                -data=%(data_dir)s \
                -hmmerv=%(hmmerv)s"
        res0 = self.run_cmd(cmd0)
        
        # gff3
        self.nonltr_out_path = self.get_abspath(self.data_dir + "/info/full/")
        self.nonltr_gff_path = self.get_abspath(self.data_dir + "/info/nonltr.gff3")
        cmd1 = "nonltr/toGFF.py %(nonltr_out_path)s %(nonltr_gff_path)s"
        res1 = self.run_cmd(cmd1)

        print 'nonltr: finishing'

    def run_cmd(self, cmd):
        return Popen((cmd % vars(self)).split(), stdout=PIPE).stdout.read()

    def get_abspath(self, path):
        try:
            return os.path.abspath(path)
        except:
            # print [DEBUG] Failed to convert a path to an absolute path
            return path

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            return self.get_abspath(path)
        else:
            new_path = path + ".1"
            return self.create_directory(new_path)

if __name__ == "__main__":
    arguments = docopt(__doc__, version='RetroTMiner 0.1')
    rtm = RetroTMiner(arguments)
    rtm.run()

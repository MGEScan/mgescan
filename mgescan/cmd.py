"""MGEScan: identifying ltr and non-ltr in genome sequences

Usage:
    mgescan.py <genome_dir> [--output=<data_dir>] [--mpi=<num>]
    mgescan.py ltr <genome_dir> [--output=<data_dir>] [--mpi=<num>]
    mgescan.py nonltr <genome_dir> [--output=<data_dir>] [--mpi=<num>]
    mgescan.py (-h | --help)
    mgescan.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
    --output=<data_dir> Directory results will be saved

"""
import os
from docopt import docopt
from multiprocessing import Process
from subprocess import Popen, PIPE
from mgescan import utils
from mgescan.split import Split
import shutil

class MGEScan(object):
    """ MGEScan runs mgescan for identifying ltr and nonltr in genome
    sequence """

    default_output_path = "./output"
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
        self.data_dir = utils.get_abspath(self.args['--output'])
        self.genome_dir = utils.get_abspath(self.args['<genome_dir>'])
        self.mpi_enabled = self.args['--mpi']
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

        if self.data_dir:
            self.data_dir = utils.create_directory(self.data_dir, False)
        else:
            self.data_dir = \
            utils.create_directory(utils.get_abspath(self.default_output_path))

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

    def split_files(self):
        split = Split()
        split.set_input(self.genome_dir)
        new_genome_dir = split.set_output(self.genome_dir + "/divided-genome")
        split.split_files()
        self.genome_dir =  new_genome_dir

    def run(self):
        # split a large file
        self.split_files()

        # ltr
        if not self.nonltr_enabled:
            p1 = Process(target=self.ltr)
            p1.start()
        # nonltr
        if not self.ltr_enabled:
            p2 = Process(target=self.nonltr)
            p2.start()
        if 'p1' in locals():
            p1.join()
        if 'p2' in locals():
            p2.join()

        # remove splitted files
        shutil.rmtree(self.genome_dir)

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
#        if self.mpi_enabled:
#            cmd0 = (cmd0 + " -mpi=%(mpi_enabled)s")
        res1 = self.run_cmd(cmd1)

        # gff3
        self.ltr_out_path = utils.get_abspath(self.data_dir + "/ltr/ltr.out")
        self.ltr_gff_path = utils.get_abspath(self.data_dir + "/ltr/ltr.gff3")
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
        if self.mpi_enabled:
            cmd0 = (cmd0 + " -mpi=%(mpi_enabled)s")
        res0 = self.run_cmd(cmd0)
        
        # gff3
        self.nonltr_out_path = utils.get_abspath(self.data_dir + "/info/full/")
        self.nonltr_gff_path = utils.get_abspath(self.data_dir + "/info/nonltr.gff3")
        cmd1 = "nonltr/toGFF.py %(nonltr_out_path)s %(nonltr_gff_path)s"
        res1 = self.run_cmd(cmd1)

        print 'nonltr: finishing'

    def run_cmd(self, cmd):
        return Popen((cmd % vars(self)).split(), stdout=PIPE, stderr=PIPE).stdout.read()

def main():
    arguments = docopt(__doc__, version='MGEScan 0.1')
    mge = MGEScan(arguments)
    mge.run()

if __name__ == "__main__":
    main()

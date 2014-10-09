"""MGEScan-nonLTR: identifying non-ltr in genome sequences

Usage:
    rtm-nonltr.py <genome_dir> [--output=<data_dir>]
    rtm-nonltr.py forward <genome_dir> [--output=<data_dir>]
    rtm-nonltr.py backward <genome_dir> [--output=<data_dir>]
    rtm-nonltr.py reverseq <genome_dir> [--output=<data_dir>]
    rtm-nonltr.py qvalue <genome_dir> [--output=<data_dir>]
    rtm-nonltr.py (-h | --help)
    rtm-nonltr.py --version

Options:
    -h --help   Show this screen
    --version   Show version
    --output=<data_dir> Path where results will be saved

"""

from docopt import docopt
from multiprocessing import Process
from subprocess import Popen, PIPE
from mgescan.cmd import MGEScan
import os
from biopython import reverse_complement_fasta

class nonLTR(MGEScan):

    main_dir = "nonltr"
    cmd_hmm = main_dir + "/run_hmm.pl"
    cmd_post_process = main_dir + "/post_process.pl"
    cmd_validate_q_value = main_dir + "/post_process2.pl"
    cmd_togff = main_dir + "/toGFF.py"

    processes = set()
    max_processes = 5

    def set_inputs(self):
        self.data_dir = self.get_abspath(self.args['--output'])
        self.genome_dir = self.get_abspath(self.args['<genome_dir>'])

    def set_defaults(self):
        super(nonLTR, self).set_defaults()
        self.plus_dir = self.genome_dir
        self.minus_dir = self.get_abspath(self.genome_dir + "/../") + "/_reversed/"

        self.plus_out_dir = self.data_dir + "/f/"
        self.minus_out_dir = self.data_dir + "/b/"

    def run(self):
        p1 = Process(target=self.forward_strand)
        p1.start()

        # Reverse complement before backward strand
        self.reverse_complement()
        p2 = Process(target=self.backward_strand)
        p2.start()

        p1.join()
        p2.join()

        # validation for q value
        self.post_processing2()

        # convert to gff3
        self.toGFF()

    def forward_strand(self):
        print "Running forward...\n"
        mypath = self.plus_dir
        out_dir = self.plus_out_dir
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            break
        for name in filenames:
            file_path = self.get_abspath(dirpath + "/" + name)
            command = self.cmd_hmm + (" --dna=%s --out=%s --hmmerv=%s" % 
                    (file_path, out_dir, self.hmmerv))
            command = command.split()
            self.processes.add(Popen(command, stdout=PIPE,
                stderr=PIPE))
            if len(self.processes) >= self.max_processes:
                time.sleep(.1)
                self.processes.difference_update([p for p in self.processes if
                    p.poll() is not None])
        #print dirpath, dirnames, filenames
        for p in self.processes:
            if p.poll() is None:
                p.wait()

        self.post_processing_after_forward_strand()

    def backward_strand(self):
        print "Running backward...\n"
        mypath = self.minus_dir
        out_dir = self.minus_out_dir
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            break
        for name in filenames:
            file_path = self.get_abspath(dirpath + "/" + name)
            command = self.cmd_hmm + (" --dna=%s --out=%s --hmmerv=%s" % 
                    (file_path, out_dir, self.hmmerv))
            command = command.split()
            self.processes.add(Popen(command, stdout=PIPE,
                stderr=PIPE))
            if len(self.processes) >= self.max_processes:
                time.sleep(.1)
                self.processes.difference_update([p for p in self.processes if
                    p.poll() is not None])
        #print dirpath, dirnames, filenames
        for p in self.processes:
            if p.poll() is None:
                p.wait()

        self.post_processing_after_reverse_strand()

    def post_processing_after_forward_strand(self):
        self.post_processing(self.plus_out_dir, self.plus_dir, 0)

    def post_processing_after_reverse_strand(self):
        self.post_processing(self.minus_out_dir, self.minus_dir, 1)

    def post_processing(self, out_dir, dir, reverse_yn):
        os.remove(self.get_abspath(out_dir + "/out1/aaaaa"))
        os.remove(self.get_abspath(out_dir + "out1/bbbbb"))
        os.remove(self.get_abspath(out_dir + "out1/ppppp"))
        os.remove(self.get_abspath(out_dir + "out1/qqqqq"))
        cmd = self.cmd_post_process + (" --dna=%s --out=%s --rev=%s" %
                (dir, out_dir, reverse_yn))
        self.run_cmd(cmd)

    def reverse_complement(self):
        mypath = self.genome_dir
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            break
        directory = self.minus_dir
        if not os.path.exists(directory):
            os.makedirs(directory)
        for name in filenames:
            file_path = self.get_abspath(dirpath + "/" + name)
            reverse_complement_fasta(file_path, directory)

    def post_processing2(self):

        cmd = self.cmd_validate_q_value + \
                " --data_dir=%(data_dir)s --hmmerv=%(hmmerv)s"
        self.run_cmd(cmd)

    def toGFF(self):

        # gff3
        self.nonltr_out_path = self.get_abspath(self.data_dir + "/info/full/")
        self.nonltr_gff_path = self.get_abspath(self.data_dir + "/info/nonltr.gff3")
        cmd = self.cmd_togff + " %(nonltr_out_path)s %(nonltr_gff_path)s"
        res = self.run_cmd(cmd)

def main():
    arguments = docopt(__doc__, version="rtm-nonltr 0.1")
    nonltr = nonLTR(arguments)
    nonltr.run()

if __name__ == "__main__":
    main()

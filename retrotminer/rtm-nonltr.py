"""RetroTMiner-nonLTR: identifying non-ltr in genome sequences

Usage:
    rtm-nonltr.py <genome_dir> [--output=<data_dir>]
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
from retrotminer import RetroTMiner
import os
from biopython import reverse_complement_fasta

class nonLTR(RetroTMiner):

    main_dir = "nonltr"
    cmd_hmm = main_dir + "/run_hmm.pl"
    cmd_post_process = main_dir + "/post_process.pl"
    cmd_validate_q_value = main_dir + "/post_proces2.pl"

    processes = set()
    max_processes = 5

    def set_inputs(self):
        self.data_dir = self.get_abspath(self.args['--output'])
        self.genome_dir = self.get_abspath(self.args['<genome_dir>'])

    def set_defaults(self):
        super(nonLTR, self).set_defaults()
        self.plus_dir = self.genome_dir
        self.minus_dir = self.get_abspath(self.genome_dir + "/../_reversed/")

        self.plus_out_dir = self.get_abspath(self.data_dir + "/f/")
        self.minus_out_dir = self.get_abspath(self.data_dir + "/b/")

    def run(self):
        p1 = Process(target=self.forward_strand)
        p1.start()
        self.reverse_complement()
        p2 = Process(target=self.backward_strand)
        p2.start()
        p1.join()
        p2.join()

        # validation for q value
        self.post_processing()

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

    def post_processing(self):
        return

    def toGFF(self):
        return

def main():
    arguments = docopt(__doc__, version="rtm-nonltr 0.1")
    nonltr = nonLTR(arguments)
    nonltr.run()

if __name__ == "__main__":
    main()

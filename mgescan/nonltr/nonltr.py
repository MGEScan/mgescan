import os.path
from mgescan import utils
from docopt import docopt
from multiprocessing import Process

class NonLTR(object):
    """MGEScan Non-LTR

    Usage:
      nonltr.py <input> <output> [--mpi=<num>]
      nonltr.py -h | --help
      nonltr.py --version

    Options:
      -h --help     show help message
      --version     show version

    """

    name = "nonltr"
    ver = 'MGEScan NonLTR 3.0.0'
    mpi_cmd = "mpi_mgescan"
    hmmerv = "3"

    def __init__(self):
        self.set_inputs()
        self.get_env()
        self.set_param()
        self.set_cmd()

    def set_cmd(self):
        self.run_hmm_cmd = self.base_path + "nonltr/" + "run_hmm.pl"
        self.run_post_cmd = self.base_path + "nonltr/" + "post_process.pl"
        self.run_post2_cmd = self.base_path + "nonltr/" + "post_process2.pl"

    def get_env(self):
        self.base_path = os.environ.get("MGESCAN_SRC") + "/mgescan/"
        self.hmmerv = os.environ.get("MGESCAN_HMMER_VERSION") or self.hmmerv

    def set_param(self):
        if self.nmpi:
            self.p_np = "-n " + self.nmpi
        self.p_prg = "--prg " + self.name
        self.p_mgescan_mpi_cmd = self.base_path + self.mpi_cmd
        self.p_genome_f = "--genome " + self.genome_path
        self.p_genome_b = "--genome " + self.genome_path + "_b"
        self.p_data_f = "--data " + self.output_path + "/f/"
        self.p_data_b = "--data " + self.output_path + "/b/"
        self.p_hmmerv = "--hmmerv " + self.hmmerv
        self.set_mpi_option()

    def set_mpi_option(self):
        self.read_mpi_host_file()
        self.p_mpi_option = self.p_hf_option + " -mca btl ^openib"

    def read_mpi_host_file(self):
        fname = os.environ.get("MGESCAN_SRC") + "host_file"
        if os.path.isfile(fname):
            self.p_hf_option = "-hostfile " + fname
        self.p_hf_option = ""

    def forward(self):
        utils.create_directory(self.output_path, False)
        if self.nmpi:
            cmd = self._padding("mpirun", self.p_np, self.p_mpi_option,
                    self.p_mgescan_mpi_cmd, self.p_prg, self.p_genome_f,
                    self.p_data_f, self.p_hmmerv)
            self.run_cmd(cmd)
        else:
           from os import listdir
           from os.path import isfile, join
           mypath = self.genome_path
           for f in listdir(mypath):
               fpath = join(mypath, f)
               if isfile(fpath):
                   p = Process(target=self.run_hmm, args=("forward", fpath,))
                   p.start()
        self.post_process("forward")

    def post_process(self, t):
        if t == "forward":
            cmd = self.run_post_cmd + " --dna=" + self.genome_path + " --out=" + self.output_path + "/f/" + " --rev=0"
        elif t == "backward":
            cmd = self.run_post_cmd + " --dna=" + self.genome_path + " --out=" + self.output_path + "/b/" + " --rev=1"
        self.run_cmd(cmd)

    def run_hmm(self, t, fname):
        if t == "forward":
            cmd = self.run_hmm_cmd + " --dna=" + fname + " --out=" + self.output_path + "/f/" + " --hmmerv=" + self.hmmerv
        elif t == "backward":
            cmd = self.run_hmm_cmd + " --dna=" + fname + " --out=" + self.output_path + "/b/" + " --hmmerv=" + self.hmmerv
        self.run_cmd(cmd)

    def post_process2(self):
        cmd = self.run_post2_cmd + " --data_dir=" + self.output_path + " --hmmerv=" + self.hmmerv
        self.run_cmd(cmd)

    def backward(self):
        if self.nmpi:
            cmd = self._padding("mpirun", self.p_np, self.p_mpi_option,
                    self.p_mgescan_mpi_cmd, self.p_prg, self.p_genome_b,
                    self.p_data_b, self.p_hmmerv)
            self.run_cmd(cmd)
        else:
           from os import listdir
           from os.path import isfile, join
           mypath = self.genome_path + "_b"
           for f in listdir(mypath):
               fpath = join(mypath, f)
               if isfile(fpath):
                   p = Process(target=self.run_hmm, args=("backward",fpath,))
                   p.start()
        self.post_process("backward")

    def _padding(self, *args):
        res = ""
        for i in args:
            res = res + " " + i
        if len(res) > 1:
            return res[1:]
        else:
            return res

    def run_cmd(self, cmd):
        print cmd
        return
        try:
            retcode = check_call(cmd.split())
            if retcode < 0:
                print >>sys.stderr, "%s was terminated by signal" % cmd, -retcode
            else:
                print >>sys.stderr, "Returned", retcode
        except OSError as e:
            print >>sys.stderr, "Failed:", e
        return retcode

    def set_inputs(self):
        self.args = docopt(self.__doc__, version=self.ver)
        self.nmpi = self.args['--mpi']
        self.genome_path = utils.get_abspath(self.args['<input>'])
        self.output_path = utils.get_abspath(self.args['<output>'])

    def run(self):
        p1 = Process(target=self.forward)
        p2 = Process(target=self.backward)
        p1.start()
        p2.start()

        if 'p1' in locals():
            p1.join()
        if 'p2' in locals():
            p2.join()

        self.post_process2()

if __name__ == '__main__':
    obj = NonLTR()
    obj.run()

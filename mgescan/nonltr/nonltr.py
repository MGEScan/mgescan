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
    tag_for_backward = "_b"

    def __init__(self):
        self.set_inputs()
        self.get_env()
        self.set_param()

    def get_env(self):
        self.base_path = os.environ.get("MGESCAN_SRC") + "/mgescan/"
        self.hmmerv = os.environ.get("MGESCAN_HMMER_VERSION") or self.hmmerv

    def set_param(self):
        if self.nmpi:
            self.p_np = "-n " + self.nmpi
        self.p_prg = "--prg " + self.name
        self.p_mgescan_mpi_cmd = self.base_path + self.mpi_cmd
        self.p_genome_f = "--genome " + self.genome_path
        self.p_genome_b = "--genome " + self.genome_path + self.tag_for_backward
        self.p_data = "--data " + self.output_path
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
        if self.nmpi:
            cmd = self._padding("mpirun", self.p_np, self.p_mpi_option,
                    self.p_mgescan_mpi_cmd, self.p_prg, self.p_genome_f,
                    self.p_data, self.p_hmmerv)
            self.run_cmd(cmd)

    def backward(self):
        if self.nmpi:
            cmd = self._padding("mpirun", self.p_np, self.p_mpi_option,
                    self.p_mgescan_mpi_cmd, self.p_prg, self.p_genome_b,
                    self.p_data, self.p_hmmerv)
            self.run_cmd(cmd)

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

if __name__ == '__main__':
    obj = NonLTR()
    obj.run()

from docopt import docopt


class NonLTR(object):
    """MGEScan Non-LTR
    
    Usage:
      nonltr.py <input> [--output=<output>]
      nonltr.py -h | --help
      nonltr.py --version

    Options:
      -h --help     show help message
      --version     show version
      --output=<output>     output directory to store results

    """

    def run(self):
        arguments = docopt(self.__doc__, version='MGEScan NonLTR 2.0')
        print arguments

if __name__ == '__main__':
    obj = NonLTR()
    obj.run()

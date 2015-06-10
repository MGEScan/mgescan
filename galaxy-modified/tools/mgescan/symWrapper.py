"""symWrapper.

Usage:
    symWrapper.py <arg>...

"""
from docopt import docopt

def main():
    arguments = docopt(__doc__, version="symWrapper 0.1")
    print arguments

if __name__ == "__main__":
    main()


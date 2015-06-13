import os
from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg 

class MGEScanInstall(bdist_egg):
    def run(self):
        os.system("cd mgescan/ltr/MER; make clean; make")
        os.system("cd mgescan/nonltr/; make clean; make translate")
        os.system("cd mgescan/nonltr/hmm;make clean; make")
        os.system("cd mgescan;mpicc mpi_mgescan.c -o mpi_mgescan")
        bdist_egg.run(self)

class MGEScanInstallOnly(bdist_egg):
    def run(self):
        bdist_egg.run(self)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(
        name = "MGEScan",
        version = "0.0.2",
        author = "Hyungro Lee",
        author_email = "hroe.lee@gmail.com",
        description = ("MGEScan on Galaxy Workflow System for identifying ltr and "
            "non-ltr in genome sequences"),
        license = "GPLv3",
        keywords = "MGEScan, Galaxy workflow",
        url = "https://github.com/MGEScan/mgescan",
        packages = ['mgescan'],
        install_requires = reqs,
        long_description = read('README.md'),
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Scientific/Engineering",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU GEneral Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux",
            "programming Language :: Python",
            ],
        entry_points='''
            [console_scripts]
            mgescan=mgescan.cmd:main
            nonltr=mgescan.nonltr:main
            ''',

        cmdclass={'bdist_egg': MGEScanInstall},  # override bdist_egg
        )


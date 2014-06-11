import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(
        name = "RetroTMiner",
        version = "0.0.1",
        author = "Hyungro Lee",
        author_email = "hroe.lee@gmail.com",
        description = ("RetroTMiner: Galaxy-based tool for identifying ltr and "
            "non-ltr in genome sequences"),
        license = "GPLv3",
        keywords = "MGEScan, Galaxy workflow, RetroTMiner",
        url = "https://github.com/lee212/retrotminer",
        packages = ['retrotminer'],
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
        )


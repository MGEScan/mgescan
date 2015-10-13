MGEScan on Galaxy Scientific Workflow
===============================================================================

A Galaxy based system for identifying retrotransposons in genome

![mgescan workflow](https://raw.githubusercontent.com/MGEScan/mgescan/master/docs/source/images/rtm-workflow-final.png)

**DEMO Version : [silo.cs.indiana.edu:38080](http://silo.cs.indiana.edu:38080/)**

* [Tutorial](http://mgescan.readthedocs.org/en/latest/tutorial.html)
* [Documentation](http://mgescan.readthedocs.org/en/latest/index.html)
* [Source](https://github.com/MGEScan/mgescan/)
* [Home Page](http://mgescan.github.io/mgescan/)

Prerequisite
-------------------------------------------------------------------------------

### Python

* git
* virtualenv
* python-dev

```sh
sudo apt-get update
sudo apt-get install python-virtualenv -y
sudo apt-get install git -y
sudo apt-get install python-dev -y
```

#### Virtualenv


```sh
mkdir ~/virtualenv
virtualenv ~/virtualenv/mgescan
source ~/virtualenv/mgescan/bin/activate
echo "source ~/virtualenv/mgescan/bin/activate" >> ~/.bash_profile
```

### Tools

* Galaxy
* HMMER
* EMBOSS
* trf (Tandem Repeats Finder)

#### Galaxy
```sh
cd ~/
git clone https://github.com/galaxyproject/galaxy/
```

#### HMMER and EMBOSS

*Ubuntu*

```sh
sudo apt-get install hmmer -y
sudo apt-get install emboss -y
```

#### trf

```sh
wget http://tandem.bu.edu/trf/downloads/trf407b.linux64
mv trf407b.linux64 ~/virtualenv/mgescan/bin/trf
chmod 700 ~/virtualenv/mgescan/bin/trf
```

#### RepeatMasker

```sh
cd ~
wget http://www.repeatmasker.org/RepeatMasker-open-4-0-5.tar.gz
tar xvzf RepeatMasker-open-4-0-5.tar.gz
```

.. note:: Find the latest at: http://www.repeatmasker.org/RMDownload.html

Installation
-------------------------------------------------------------------------------

```sh
git clone https://github.com/MGEScan/mgescan.git
cd mgescan
python setup.py install
```

### virtualenv (optional for individual without sudo)


```sh
virtualenv ~/virtualenv/mgescan
source ~/virtualenv/mgescan/bin/activate
```

### Galaxy modification

```sh
cd ~/
cp -pr ~/mgescan/galaxy-modified/* ~/galaxy
```

### Start Galaxy
```sh
cd ~/galaxy
./run.sh &
```

Default port number : **38080**
http://[IP ADDRESS]:38080

Command Line Tool (mgescan)
-------------------------------------------------------------------------------

```sh
Usage:
    mgescan both <genome_dir> [--output=<data_dir>] [--mpi=<num>]
    mgescan ltr <genome_dir> [--output=<data_dir>] [--mpi=<num>]
    mgescan nonltr <genome_dir> [--output=<data_dir>] [--mpi=<num>]
    mgescan (-h | --help)
    mgescan --version
```

Amazon Cloud Image (EC2)
-------------------------------------------------------------------------------

* US East Region Only
* MGEScan - ami-394ebd52 (latest version)
* retrotminer-alpha - ami-23d9c74a (created at 2014)

Citation
-------------------------------------------------------------------------------

How to cite MGEScan on Galaxy [here]

References
-------------------------------------------------------------------------------

1. M. Rho, S. Schaack, X. Gao, S. Kim, M. Lynch and H. Tang (2010), LTR
   retroelements in the genome of Daphnia pulex, BMC Genomics, 11:425. Pubmed. 

2. M. Rho and H. Tang (2009), MGEScan-nonLTR: computational identification and
   classification of Non-LTR retrotransposons in eukaryotic genomes. Nucleic Acid
   Res, 37(21):e143. Free fulltext at NAR online 

3. M. Rho, J. H. Choi, S. Kim, M. Lynch and H. Tang (2007), De novo
   identification of LTR retrotransposons in eukaryotic genomes. BMC Genomics,
   8:90. Pubmed. 

Web Sites
-------------------------------------------------------------------------------

* [MGEScan-LTR](http://darwin.informatics.indiana.edu/cgi-bin/evolution/daphnia_ltr.pl)
* [MGEScan-nonLTR](http://darwin.informatics.indiana.edu/cgi-bin/evolution/nonltr/nonltr.pl)

License
-------------------------------------------------------------------------------

Copyright (C) 2015. See the LICENSE file for license rights and limitations
(GPL v3).

This program is part of MGEScan.

MGEScan is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.

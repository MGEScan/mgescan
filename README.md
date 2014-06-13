RetroTMiner
===========

A Galaxy based system for identifying retrotransposons in genome
**DEMO Version : [silo.cs.indiana.edu](http://silo.cs.indiana.edu:38080/)**

* [Tutorial](http://retrotminer.readthedocs.org/en/latest/tutorial.html)
* [Documentation](http://retrotminer.readthedocs.org/en/latest/index.html)
* [MGEScan-LTR](http://darwin.informatics.indiana.edu/cgi-bin/evolution/daphnia_ltr.pl)
* [MGEScan-nonLTR](http://darwin.informatics.indiana.edu/cgi-bin/evolution/nonltr/nonltr.pl)
* [Source](https://github.com/MGEScan/retrotminer/)

Installation
------------

```sh
git clone git@github.com:MGEScan/retrotminer.git
cd retrotminer
python setup.py install
```

Command Line Tool (rtm)
-----------------------

```sh
Usage:
    retrotminer.py <genome_dir> [--output=<data_dir>]
    retrotminer.py ltr <genome_dir> [--output=<data_dir>]
    retrotminer.py nonltr <genome_dir> [--output=<data_dir>]
    retrotminer.py (-h | --help)
    retrotminer.py --version
```

On Cloud (Amazon EC2)
---------------------
retrotminer-alpha - ami-23d9c74a

References
-----------

1. M. Rho, S. Schaack, X. Gao, S. Kim, M. Lynch and H. Tang (2010), LTR retroelements in the genome of Daphnia pulex, BMC Genomics, 11:425. Pubmed. 
2. M. Rho and H. Tang (2009), MGEScan-nonLTR: computational identification and classification of Non-LTR retrotransposons in eukaryotic genomes. Nucleic Acid Res, 37(21):e143. Free fulltext at NAR online 
3. M. Rho, J. H. Choi, S. Kim, M. Lynch and H. Tang (2007), De novo identification of LTR retrotransposons in eukaryotic genomes. BMC Genomics, 8:90. Pubmed. 

License
-------
Copyright (C) 2014 Hyungro Lee, Wazim Mohammed Ismail, Mina Rho & Haixu Tang. See the LICENSE file for license rights and limitations (GPL v3).

This program is part of MGEScan.

MGEScan is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

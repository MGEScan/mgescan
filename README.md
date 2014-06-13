retrotminer
===========

A Galaxy based system for identifying retrotransposons in genome

[Tutorial](http://retrotminer.readthedocs.org/en/latest/tutorial.html)
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

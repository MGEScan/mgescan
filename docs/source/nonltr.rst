MGEScan-nonLTR
==============

.. image:: images/rtm-nonltr.png

Running the program
--------------------
To run MGEScan-nonLTR, follow the steps below:

* Select genome files a select box. You can upload your genome files through 'Get Data' at Tools menu bar.
* Click 'Execute' button. This tool reads your genome files and runs the whole process.

Result
------
Upon completion, MGEScan-nonLTR generates output, "info" in the data directory you specified. In this "info" directory, two sub-directories ("full" and "validation") are generated.

The "full" directory is for storing sequences of elements. Each subdirectory in "full" is the name of clade. In each directory of clade, the DNA sequences of nonLTRs identified are listed. Each sequence is in fasta format. The header contains the position information of TEs identified, [genome_file_name]_[start position in the sequence]
For example, >chr1_333 means that this element start at 333bp in the "chr1" file. - The "validation" directory is for storing Q values. In the files "en" and "rt", the first column corresponds to the element name and the last column Q value.

License
-------
Copyright 2014 Mina Rho, Haixu Tang. You may redistribute this software under the terms of the GNU General Public License.

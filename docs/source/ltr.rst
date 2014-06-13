MGEScan-LTR
===========

.. image:: images/rtm-ltr.png

Running the program
-------------------
To run MGEScan-LTR, follow the steps below,

* Specify options that you like to have:
  Check repeatmasker if you want to preprocess
  Check scaffold if the input file has all scaffolds.
* Update values:
  * min_dist: minimum distance(bp) between LTRs.
  * max_dist: maximum distance(bp) between LTRS
  * min_len_ltr: minimum length(bp) of LTR.
  * max_len_ltr: maximum length(bp) of LTR.
  * ltr_sim_condition: minimum similarity(%) for LTRs in an element.
  * cluster_sim_condition: minimum similarity(%) for LTRs in a cluster
  * len_condition: minimum length(bp) for LTRs aligned in local alignment.
* Click 'Execute'

Result
------
Upon completion, MGEScan-LTR generates a file ltr.out. This output file has information about clusters and coordinates of LTR retrotransposons identified. Each cluster of LTR retrotransposons starts with the head line of [cluster_number]---------, followed by the information of LTR retrotransposons in the cluster. The columns for LTR retrotransposons are as follows.

* LTR_id: unique id of LTRs identified. It consist of two components, sequence file name and id in the file. For example, chr1_2 is the second LTR retrotransposon in the chr1 file.
* start position of 5 LTR.
* end position of 5 LTR.
* start position of 3 LTR.
* end position of 3 LTR.
* strand: + or -.
* length of 5 LTR.
* length of 3 LTR.
* length of the LTR retrotransposon.
* TSD on the left side of the LTR retotransposons.
* TSD on the right side of the LTR retrotransposons.
* di(tri)nucleotide on the left side of 5LTR
* di(tri)nucleotide on the right side of 5LTR
* di(tri)nucleotide on the left side of 3LTR
* di(tri)nucleotide on the right side of 3LTR

License
-------
Copyright 2014 Mina Rho, Haixu Tang. You may redistribute this software under the terms of the GNU General Public License.

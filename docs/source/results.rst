Test Results
===============================================================================

Four sample genomes were tested with MGEScan-LTR and MGEScan-nonLTR programs.

* Test Environment: India Cluster on Futuresystems Cloud
* Hardware Spec: Intel Xeon X5550 2.66GHz, 8 vCPUs, 16 GB DDR3 1333 MHz,
  160GB 7200RPM SATA

.. sidebar:: Page Contents

   .. contents::
         :local:

D. melanogaster
-------------------------------------------------------------------------------

* :download:`dm3.gff3 <sample/dm3.gff3.txt>`
* :download:`dm3.ltr.out <sample/dm3.ltr.out.txt>`
* :download:`dm3.en <sample/dm3.en.txt>`
* :download:`dm3.rt <sample/dm3.rt.txt>`

Evaluation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Elapsed time for MGEScan (dm3)
   :header-rows: 1

   * - Program
     - Total
     - nonLTR
     - LTR
     - Options
   * - MGEScan1.3.1
     - 3 hrs 40 mins (13,220 secs)
     - 55 mins (3,320 secs)
     - 2 hrs 45 mins  (9,900 secs)
     - HMMER2, no MPI
   * - MGEScan2
     - 2 hrs 35 mins (9,304 secs)
     - 19 mins (1,170 secs)
     - 2 hrs 35 mins (9,304 secs)
     - HMMER3.1b1, no MPI
   * - MGEScan2 with MPI
     - 1 hr 48 mins (6,502 secs)
     - 15 mins (929 secs)
     - 1 hr 48 mins (6,502 secs)
     - HMMER3.1b1, MPI with 4 processors


Extra Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :download:`en <sample/dm3/data/info/validation/en.txt>`
* :download:`rt <sample/dm3/data/info/validation/rt.txt>`
* :download:`R2.rt.pep <sample/dm3/data/info/full/R2/R2.rt.pep.txt>`
* :download:`R2.rt.dna <sample/dm3/data/info/full/R2/R2.rt.dna.txt>`
* :download:`R2.dna <sample/dm3/data/info/full/R2/R2.dna.txt>`
* :download:`R2.pep <sample/dm3/data/info/full/R2/R2.pep.txt>`
* :download:`I.en.dna <sample/dm3/data/info/full/I/I.en.dna.txt>`
* :download:`I.rt.dna <sample/dm3/data/info/full/I/I.rt.dna.txt>`
* :download:`I.en.pep <sample/dm3/data/info/full/I/I.en.pep.txt>`
* :download:`I.pep <sample/dm3/data/info/full/I/I.pep.txt>`
* :download:`I.dna <sample/dm3/data/info/full/I/I.dna.txt>`
* :download:`I.rt.pep <sample/dm3/data/info/full/I/I.rt.pep.txt>`
* :download:`Jockey.en.dna <sample/dm3/data/info/full/Jockey/Jockey.en.dna.txt>`
* :download:`Jockey.rt.pep <sample/dm3/data/info/full/Jockey/Jockey.rt.pep.txt>`
* :download:`Jockey.dna <sample/dm3/data/info/full/Jockey/Jockey.dna.txt>`
* :download:`Jockey.en.pep <sample/dm3/data/info/full/Jockey/Jockey.en.pep.txt>`
* :download:`Jockey.rt.dna <sample/dm3/data/info/full/Jockey/Jockey.rt.dna.txt>`
* :download:`Jockey.pep <sample/dm3/data/info/full/Jockey/Jockey.pep.txt>`
* :download:`R1.dna <sample/dm3/data/info/full/R1/R1.dna.txt>`
* :download:`R1.en.pep <sample/dm3/data/info/full/R1/R1.en.pep.txt>`
* :download:`R1.pep <sample/dm3/data/info/full/R1/R1.pep.txt>`
* :download:`R1.en.dna <sample/dm3/data/info/full/R1/R1.en.dna.txt>`
* :download:`R1.rt.dna <sample/dm3/data/info/full/R1/R1.rt.dna.txt>`
* :download:`R1.rt.pep <sample/dm3/data/info/full/R1/R1.rt.pep.txt>`
* :download:`CR1.en.dna <sample/dm3/data/info/full/CR1/CR1.en.dna.txt>`
* :download:`CR1.dna <sample/dm3/data/info/full/CR1/CR1.dna.txt>`
* :download:`CR1.pep <sample/dm3/data/info/full/CR1/CR1.pep.txt>`
* :download:`CR1.rt.pep <sample/dm3/data/info/full/CR1/CR1.rt.pep.txt>`
* :download:`CR1.rt.dna <sample/dm3/data/info/full/CR1/CR1.rt.dna.txt>`
* :download:`CR1.en.pep <sample/dm3/data/info/full/CR1/CR1.en.pep.txt>`
* :download:`nonltr.gff3 <sample/dm3/data/info/nonltr.gff3.txt>`

d. pulex        MGEScan1.3.1    No MPI  4 hrs 5mins     14,697 secs     1hr 8mins       4,127 secs      2 hrs 57 mins   10,570 secs
MGEScan2        No MPI  2 hrs 36 mins   9,414 secs      46 mins 2,780 secs      2 hrs 36 mins   9,414 secs
MGEScan2        MPI (4 Proc)    1hr 3mins       3,823 secs      4 mins  222 secs        1 hr 3mins      3,823 secs
c. intestinalis exp1    MGEScan1.3.1    No MPI  3 hrs 34 mins   12,837 secs     21 mins 1,256 secs      3hrs 13 mins    11,581 secs
MGEScan2        No MPI  2 hrs 23 mins   8,604 secs      　      42 secs 2 hrs 23 mins   8,604 secs
MGEScan2        MPI (4 Proc)    50 mins 2,949 secs      　      13 secs 50 mins 2,949 secs
c. intestinalis exp2    MGEScan1.3.1    No MPI  3 hrs 34 mins   12,837 secs     21 mins 1,256 secs      3hrs 13 mins    11,581 secs
MGEScan2        No MPI  4 hrs 5 mins    14,727 secs     9 mins  503 secs        4hrs 5 mins     14,727 secs
MGEScan2        MPI (4 Proc)    1hr 22mins      4,897 secs      3 mins  182 secs        1 hr 22 mins    4,897 secs
s. purpuratus   MGEScan1.3.1    No MPI  45 hrs 12 mins  162,723 secs    6 hrs 34 mins   23,644 secs     38 hrs 37 mins  139,079 secs
MGEScan2        No MPI  67 hrs 13 mins  242,002 secs    7 hrs 53 mins   28,392 secs     67 hrs 13 mins  242,002 secs
MGEScan2        MPI (4 Proc)    12 hrs 55 mins  46,550 secs     2 hrs 36 mins   9,411 secs      12 hrs 55 mins  46,550 secs

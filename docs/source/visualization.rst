Visualization
=============

Galaxy Workflow System helps display results using genome browsers such as UCSC or Ensembl. MGEScan supports gene-finding format (GFF) to describe genes of MGEScan results so both ltr and non-ltr results can be views via UCSC Genome Browser or Ensembl.

UCSC Genome Browser
-------------------

.. image:: images/rtm-ltr-gff3-ensembl.png

Ensembl
-------

.. image:: images/rtm-ltr-gff3-ucsc-browser.png

Source Code
-----------
In RetoTMiner source code, ltr/toGFF.py and nonltr/toGFF.py are used to convert results to GFF format developed by Wazim Mohammmed Ismail.

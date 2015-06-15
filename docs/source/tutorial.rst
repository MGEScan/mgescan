Tutorial: Using MGEScan on Galaxy Workflow
===============================================================================

Galaxy workflow is a web-based system to support data analysis on the web.
MGEScan, identifying LTR and non-LTR in genome sequences are available on the
Galaxy workflow with additional tools.

Overview
-------------------------------------------------------------------------------

This tutorial demonstrates a quick start of using MGEScan on Galaxy workflow
with a sample dataset, D. melanogaster genome. A public server at Indiana
University (http://silo.cs.indiana.edu:38080) provides sample datasets and
MGEScan tools to try MGEScan on Galaxy without installation hassle.

.. tip:: Approximate 30 minutes

Run MGEScan-LTR and MGEScan-nonLTR for D. melanogaster
-------------------------------------------------------------------------------

In this tutorial, we will try to run both MGEScan-LTR and MGEScan-nonLTR with
D. melanogaster genome dataset. You can find the dataset at the ``Shared Data``
menu on top and MGEScan tools on the left frame.

Galaxy/MGEScan Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open Galaxy/MGEScan at your web browser:

* http://silo.cs.indiana.edu:38080

.. image:: images/mgescan-main.png

Login or Register (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can save your work if you have account on Galaxy workflow. The user-based
history in Galaxy/MGEScan stores your data and launched tasks. The guest user
account is able to run the MGEScan tools without the login but results or
history data won't be saved if the web browser session is closed.

Register
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Email address is required to sign up.

* http://silo.cs.indiana.edu:38080/user/create

.. image:: images/galaxy-register.png

Login
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If you already have an account, you can use your user id and password at
the *User > Login* page.

* http://silo.cs.indiana.edu:38080/user/login

.. image:: images/galaxy-login.png

Shared Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find same datasets (e.g. D.melanogaster) at ``Shared Data`` menu on
top. Click "Shared Data" > "Data Libraries" and find "Sample datasets for
MGEScan".

* http://silo.cs.indiana.edu:38080/library/index

Drosophila melanogaster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the Data Library, enable the checkbox for ``d.melanogaster`` and click
"Select datasets for import into selected histories" from the down arrow at
the end.

.. image:: images/galaxy-importing-from-dataset.png

You will find 8 fasta files are available. We need to import all of them, make
them all checked and click "Import library datasets" in the middle of the page.

.. image:: images/galaxy-importing-from-dataset2.png

Once you imported the D. melanogaster datasets into your history, you are ready
to run MGEScan tools on Galaxy. Go to the main page, and checkout imported
datasets (8 files) on the right frame of the page.

.. note:: You can select where datasets to be imported.

.. comment::

        Get Data (Upload input data)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        With a couple of options to upload your genome sequences, MGEScan is ready to
        conduct data analysis.

        Upload file from local (Option I)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        Single file upload from local is available at *Get Data > Upload File*.

        .. image:: images/rtm-upload-file.png

        Get Data from UCSC Table Browser (Option II)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        You can also use UCSC to get input data instead of uploading files from local.
        UCSC Table Browser provides the easy way to download the database to Galaxy.
        Open "Get Data > UCSC Main".

        `Using UCSC Table Browser <http://genome.ucsc.edu/cgi-bin/hgTables?GALAXY_URL=http%3A//silo.cs.indiana.edu%3A38080/tool_runner&tool_id=ucsc_table_direct1&hgta_compressType=none&sendToGalaxy=1&hgta_outputType=bed#Help>`_

        .. image:: images/rtm-upload-ucsc.png

MGEScan for LTR and nonLTR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In our new version of MGEScan, MGEScan-LTR and MGEScan-nonLTR can be executed
concurrently. Open the page at **"MGEScan > MGEScan"**, a simple tool is
available for LTR and nonLTR executions with MPI option to enable parallel
processing. 

.. note:: Find **LTR** or **nonLTR** page if you'd like to choose other options
          to run MGEScan tools in detail.

Create a single link to multiple inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, we have 8 fasta files as parts of d. melanogaster sequences.
To run them all at the same time, we need to create a single link to the files
prior to running MGEScan tool on Galaxy.

FInd "Tools > Create a symlink to multiple datasets" on the left frame.

We will add 8 fasta files each by clicking "Add new Dataset" from "8:
Drosophila_melanogaster.BDGP6.dna.chromosome.dmel_mitochondrion_genome.fa" to
"1: Drosophila_melanogaster.BDGP6.dna.chromosome.2L.fa"

.. image:: images/galaxy-create-a-symlink.png

Make sure you added all of the files without duplication. The added order is
not important though. File(s) will be placed in a same directory without
order.

MGEScan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MGEScan runs both LTR and nonLTR with a selected input genome sequence.
Find "MGEScan > MGEScan" tool on the left frame and confirm that the symlink
dataset we created in the previous step is loaded in "From" select form.

Enable MPI
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

To accelerate processing time, select "Yes" at "Enable MPI" select form and
specify **4** at "Number of MPI Processes".

Our options are:

* From: Create a symlink to multiple datasets on data 2 and data 8, and others
* MGEScan: Both
* Enable MPI: Yes
* Number of MPI Processes: 4

And click "Execute".

.. comment::

   .. image:: images/rtm-mgescan.png

        LTR
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        LTR takes option values from user input. RepeatMasker or scaffold files can be
        selected in this tool. 

        .. image:: images/rtm-ltr.png

        nonLTR
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        nonLTR

        .. image:: images/rtm-nonltr.png

Visualization: UCSC or Ensembl Genome Browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon completion of LTR or nonLTR, the output is generated in a gff3 format as
well. In Galaxy, UCSC or Ensembl Genome Browser link is provided for a gff3
file to support interactive graphical display of genome sequence data.

UCSC Genome Browser
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. image:: images/rtm-ltr-gff3-ucsc-browser.png

Ensembl
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. image:: images/rtm-ltr-gff3-ensembl.png

Download Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Galaxy provides a dowload option to results of tools via a download icon. 

Description of tools
-------------------------------------------------------------------------------

Each tool in Galaxy has its description to explain how to use.

.. image:: images/rtm-description.png


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
D. melanogaster genome dataset. You can find the dataset at the ``Shard Data``
menu to import into your workflow history and MGEScan tools on the left frame.

Galaxy/MGEScan Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the Galaxy/MGEScan web server at your web browser:

http://silo.cs.indiana.edu:38080

.. image:: images/mgescan-main.png

Login or Register (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can save your work if you have account on Galaxy workflow. The user-based
history in Galaxy/MGEScan stores your data and launched tasks. The guest user
account is able to run MGEScan without the login but results or history data
won't be saved if the web browser session is closed.

Register
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

First-time user need to register to the Galaxy system.

http://silo.cs.indiana.edu:38080/user/create

.. image:: images/galaxy-register.png

Login
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If you already have an account, you can use your user id and password at
the *User > Login* page.

http://silo.cs.indiana.edu:38080/user/login

.. image:: images/galaxy-login.png

Shared Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Program Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In our new version of MGEScan, MGEScan-LTR and MGEScan-nonLTR can be executed
concurrently. Open the page at **"MGEScan > MGEScan"**, a simple command is
available for LTR and nonLTR executions. In a separated menu such as **LTR** or
**nonLTR**, you can choose other options to run them separately.

MGEScan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MGEScan runs LTR and nonLTR both with a selected input genome sequences.
Default value settings and configurations are used.

.. image:: images/rtm-mgescan.png

.. comment::

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


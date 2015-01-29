MGEScan
===========

Open a Galaxy/MGEScan web page
-----------------------------------
Galaxy workflow system is a web-based program. With a specialized galaxy tools for MGEScan, identifying LTR and non-LTR in genome sequences are available on the web.

http://silo.cs.indiana.edu:38080

.. image:: images/mgescan-main.png

Login or Register
-----------------
To keep a user-based history, login is required in Galaxy/MGEScan. The guest user account is able to run MGEScan without the login but results or history data can be lost if the web browser session is closed.

Register
^^^^^^^^
First-time user need to register first to the Galaxy system.

.. image:: images/rtm-register.png

Login
^^^^^
If you already have an account, you can provide your user id and password at the *User > Login* page.

.. image:: images/rtm-login.png

Get Data (Upload input data)
-----------------------------
With a couple of options to upload your genome sequences, MGEScan is ready to conduct data analysis.

Upload file from local (Option I)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Single file upload from local is available at *Get Data > Upload File*.

.. image:: images/rtm-upload-file.png

Get Data from UCSC Table Browser (Option II)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also use UCSC to get input data instead of uploading files from local.
UCSC Table Browser provides the easy way to download the database to Galaxy. Open "Get Data > UCSC Main".

`Using UCSC Table Browser <http://genome.ucsc.edu/cgi-bin/hgTables?GALAXY_URL=http%3A//silo.cs.indiana.edu%3A38080/tool_runner&tool_id=ucsc_table_direct1&hgta_compressType=none&sendToGalaxy=1&hgta_outputType=bed#Help>`_

.. image:: images/rtm-upload-ucsc.png

Program Execution
------------------
In our new version of MGEScan, MGEScan-LTR and MGEScan-nonLTR can be executed concurrently. Open the page at **"MGEScan > MGEScan"**, a simple command is available for LTR and nonLTR executions. In a separated menu such as **LTR** or **nonLTR**, you can choose other options to run them separately.

MGEScan
^^^^^^^^

MGEScan runs LTR and nonLTR both with a selected input genome sequences. Default value settings and configurations are used.

.. image:: images/rtm-mgescan.png

LTR
^^^^^^^^

LTR takes option values from user input. RepeatMasker or scaffold files can be selected in this tool. 

.. image:: images/rtm-ltr.png

nonLTR
^^^^^^^^

nonLTR

.. image:: images/rtm-nonltr.png

Visualization via UCSC or Ensembl Genome Browser
--------------------------------------------------------

Upon completion of LTR or nonLTR, the output is generated in a gff3 format as well. In Galaxy, UCSC or Ensembl Genome Browser link is provided for a gff3 file to support interactive graphical display of genome sequence data.

UCSC Genome Browser
^^^^^^^^^^^^^^^^^^^

.. image:: images/rtm-ltr-gff3-ucsc-browser.png

Ensembl
^^^^^^^

.. image:: images/rtm-ltr-gff3-ensembl.png

Download Results
----------------

Galaxy provides a dowload option to results of tools via a download icon. 

Description of tools
--------------------

Each tool in Galaxy has its description to explain how to use.

.. image:: images/rtm-description.png

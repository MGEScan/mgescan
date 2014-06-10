RetroTMiner
===========

Open a Galaxy/RetroTMiner web page
-----------------------------------
Galaxy workflow system is a web-based program. With a specialized galaxy tools for MGEScan, identifying LTR and non-LTR in genome sequences are available on the web.

http://silo.cs.indiana.edu:38080

.. image:: images/rtm-main.png

Login or Register
-----------------
To keep a user-based history, login is required in Galaxy/RetroTMiner. The guest user account is able to run MGEScan without the login but results or history data can be lost if the web browser session is closed.

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

Upload file from local
^^^^^^^^^^^^^^^^^^^^^^^

Single file upload from local is available at *Get Data > Upload File*

.. image:: images/rtm-upload-file.png

Get Data from UCSC Table Browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

UCSC Table Browser provides the easy way to download the database to Galaxy.

`Using UCSC Table Browser <http://genome.ucsc.edu/cgi-bin/hgTables?GALAXY_URL=http%3A//silo.cs.indiana.edu%3A38080/tool_runner&tool_id=ucsc_table_direct1&hgta_compressType=none&sendToGalaxy=1&hgta_outputType=bed#Help>`_

.. image:: images/rtm-upload-ucsc.png

MGEScan
-------

.. image:: images/rtm-mgescan.png

LTR
---

.. image:: images/rtm-ltr.png

nonLTR
------

.. image:: images/rtm-nonltr.png

Genome Browser via UCSC or Ensembl
----------------------------------

UCSC Genome Browser
^^^^^^^^^^^^^^^^^^^

.. image:: images/rtm-ltr-gff3-ucsc-browser.png

Ensembl
^^^^^^^

.. image:: images/rtm-ltr-gff3-ensembl.png

Description of tools
^^^^^^^^^^^^^^^^^^^^
Each tool in Galaxy has its description to explain how to use.

.. image:: images/rtm-description.png

MGEScan Command Line Interface
===============================================================================

MGEScan provides Command Line Interface (CLI) along with Galaxy Web Interface.
You can run MGEScan-LTR and MGEScan-nonLTR programs on your shell terminal.

Installation
-------------------------------------------------------------------------------

If you have installed MGEScan on Galaxy, you have MGEScan CLI tools. 

.. note:: Do you need to install MGEScan? See here: :ref:`Installation <ref-mgescan-installation>`

Usage
-------------------------------------------------------------------------------

Try ``mgescan -h`` on your terminal:

::

  (mgescan)$ mgescan -h
  MGEScan: identifying ltr and non-ltr in genome sequences

  Usage:
          mgescan both <genome_dir> [--output=<data_dir>] [--mpi=<num>]
          mgescan ltr <genome_dir> [--output=<data_dir>] [--mpi=<num>]
          mgescan nonltr <genome_dir> [--output=<data_dir>] [--mpi=<num>]
          mgescan (-h | --help)
          mgescan --version

  Options:
          -h --help   Show this screen.
          --version   Show version.
          --output=<data_dir> Directory results will be saved

MGEScan Programs
-------------------------------------------------------------------------------

``mgescan`` CLI tool provides options to run ``ltr``, ``nonltr`` or both
programs.

How to Run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to run MGEScan program to indentify both LTR and non-LTR for
certain genome sequences, simply specify the path where your input genome files
(FASTA format) exist with ``both`` sub-command.

For example, if you have DNA sequences (FASTA) for Fruitfly (Drosophila
melanogaster) under ``$HOME/dmelanogaster`` directory, and want to save
results in the ``$HOME/mgescan_result_dmelanogaster``, your may run ``mgescan``
command like so::


  (mgescan)$ mgescan both $HOME/dmelanogaster --output=$HOME/mgescan_result_dmelanogaster


The expected output message is like so::

        ltr: starting
        nonltr: starting


MPI Option
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your system supports a MPI program, you can use ``--mpi`` option with a
number of processes.

Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



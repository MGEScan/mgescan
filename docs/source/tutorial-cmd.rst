MGEScan Command Line Interface
===============================================================================

MGEScan provides Command Line Interface (CLI) along with Galaxy Web Interface.
You can run MGEScan-LTR and MGEScan-nonLTR programs on your shell terminal.

.. tip:: Approximate: 20 minutes

Installation
-------------------------------------------------------------------------------

If you have installed MGEScan on Galaxy, you have MGEScan CLI tools. 

.. note:: Do you need to install MGEScan? See here: :ref:`Installation <ref-mgescan-installation>`

git clone mgescan
source virtualenv
python setup.py install

mgescan ltr|nonltr|both genome_dir --output=output_dir --mpi=number_of_process
nonltr

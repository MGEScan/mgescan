MGEScan on Galaxy Installation
===============================================================================

MGEScan on Galaxy provide local installation and cloud installation. 

Local Installation
-------------------------------------------------------------------------------

This installation manual is for Ubuntu 14.04+ distribution. Others are not
tested.

Prerequisite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software packages and system packages are requied to run MGEScan.  You need to
install system packages with ``sudo`` command. An admin ``root`` privilege is
required.

System Packages
*******************************************************************************

If you have ``virtualenv``, ``git``, and ``python-dev``, you can skip this
step.

**Ubuntu**

::

  sudo apt-get update
  sudo apt-get install python-virtualenv -y
  sudo apt-get install git -y
  sudo apt-get install python-dev -y

Environment Variables
*******************************************************************************

MGEScan will be installed on a default directory ``$HOME/mgescan3``. You can
change it if you prefer other location to install MGEScan.

::

  export MGESCAN_HOME=$HOME/mgescan3
  export MGESCAN_SRC=$MGESCAN_HOME/src
  export GALAXY_HOME=$MGESCAN_HOME/galaxy
  export TRF_HOME=$MGESCAN_HOME/trf
  export MGESCAN_VENV=$MGESCAN_HOME/virtualenv/mgescan



Create a MGESCan start file ``.mgescanrc`` 

::

   cat <<EOF > $HOME/.mgescanrc
   export MGESCAN_HOME=\$HOME/mgescan3
   export GALAXY_HOME=\$MGESCAN_HOME/galaxy
   export TRF_HOME=\$MGESCAN_HOME/trf
   export MGESCAN_VENV=\$MGESCAN_HOME/virtualenv/mgescan
   EOF

Then include it to your startup file (i.e. ``.bashrc``).

::

   echo "source ~/.mgescanrc" >> $HOME/.bashrc


Software Packages
*******************************************************************************

Galaxy Workflow, HMMER (3.1b1), EMBOSS Suite and TRF are required.

Galaxy
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. tip:: Make sure that $MGESCAN_HOME is set by ``echo $MGESCAN_HOME`` command.
        If you don't see a path similar to ``/home/.../mgescan3/``, you have to
        define environment variables again.

From Github repository (source code):

::

        cd $MGESCAN_HOME
        git clone https://github.com/galaxyproject/galaxy/
        cd galaxy/
        ./run.sh &

HMMER and EMBOSS
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you have ``HMMER`` and ``EMBOSS`` on your system, you can skip this step.

**Ubuntu**

::

        sudo apt-get install hmmer -y
        sudo apt-get install emboss -y

Virtual Environments (virtualenv)
*******************************************************************************

It is recommended to have an isolated environment for MGEScan Python
libraries. virtualenv creates a separated space for MGEScan, and issues from
dependencies and versions of Python libraries can be avoided. Note that you
have to be in the virtualenv of MGEScan before to run any MGEScan command line
tools. The following commands create a virtualenv for MGEScan and enable it on
your account.

::

  mkdir -p $MGESCAN_VENV
  virtualenv $MGESCAN_VENV
  source $MGESCAN_VENV/bin/activate
  echo "source $MGESCAN_VENV/bin/activate" >> ~/.bash_profile


Tandem Repeats Finder (trf)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

``trf`` is a single binary executable file.

::
 
   mkdir -p $TRF_HOME
   wget http://tandem.bu.edu/trf/downloads/trf407b.linux64 -P $TRF_HOME

MGEScan Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Github repository (source code):

::

  cd $MGESCAN_HOME
  git clone https://github.com/MGEScan/mgescan.git
  ln -s mgescan src 
  cd mgescan
  python setup.py install

Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Virtual Environments (virtualenv)
*******************************************************************************

It is recommended to have an isolated environment for MGEScan Python
libraries. virtualenv creates a separated space for MGEScan, and issues from
dependencies and versions of Python libraries can be avoided. Note that you
have to be in the virtualenv of MGEScan before to run any MGEScan command line
tools. The following commands create a virtualenv for MGEScan and enable it on
your account.

::

  source $MGESCAN_VENV/bin/activate

Make sure that you see ``(mgescan)`` label on your prompt.

Galaxy Configurations for MGEScan
*******************************************************************************

MGEScan github repository contains codes and toolkits for MGEScan on Galaxy.
Prior to run a Galaxy Workflow web server, the codes and toolkits should be
installed in the ``galaxy`` main directory.

::

  cp -pr $MGESCAN_SRC/galaxy-modified/* $GALAXY_HOME

trf
*******************************************************************************

To run ``trf`` anywhere under ``mgescan`` virtualenv, we create a symlink in
the ``bin`` directory.

::

   ln -s $TRF_HOME/trf407b.linux64 $MGESCAN_VENV/bin/trf
   chmod 700 $MGESCAN_VENV/bin/trf


Start Galaxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

        cd $GALAXY_HOME
        nohup sh run.sh &

.. note:: Default port number : 38080 http://[IP ADDRESS]:38080






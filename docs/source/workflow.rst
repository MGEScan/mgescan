.. _ref-mgescan-workflow:

MGEScan Workflow
===============================================================================

With Galaxy Workflow tools, each procedure of MGEScan can be described with
input and output as its steps.

Galaxy Workflow Canvas
-------------------------------------------------------------------------------

In Galaxy > Workflow > Edit, you can modify or update the MGEScan workflow on
Galaxy Workflow Canvas.

.. image:: images/rtm-workflow-final-large.png

Registered Workflow in local
-------------------------------------------------------------------------------

Once you completed composing/updating workflow, you can save your work on local.

.. image:: images/rtm-private-workflow.png

Registered Workflow in public
-------------------------------------------------------------------------------

Through Galaxy Public Workflow Website, your workflow can be shared with other
scientists and researchers. MGEScan workflow has been registed on
https://usegalaxy.org/workflow/list_published.

.. image:: images/rtm-public-workflow.png

Overview of MGEScan Workflow (Draft)
-------------------------------------------------------------------------------

The published MGEScan workflow consists of LTR and non-LTR programs in
parallel. LTR has four components including splitting scaffolds, pre-processing
by repeatmasker, finding LTRs, and converting results in gff3 format.

.. image:: images/rtm-retrotminer-image.svg

:ref:`Quick Start <ref-mgescan-tutorial>`

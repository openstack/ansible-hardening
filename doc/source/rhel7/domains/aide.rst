aide - Advanced Intrusion Detection Environment
===============================================

AIDE provides integrity monitoring for files on a Linux system and can notify
system administrators of changes to critical files and packages.

Overview
--------

By default, AIDE will examine and monitor all of the files on a host unless
directories are added to its exclusion list. The security role sets directories
to exclude from AIDE monitoring via the ``aide_exclude_dirs`` variable. this
list excludes the most common directories that change very often via automated
methods.

The security role skips the AIDE initialization step by default to avoid system
disruption or a reduction in performance. Deployers should determine the best
time to initialize the database that does not interfere with the system's
operations.

To initialize the AIDE database, set the following Ansible variable and
re-apply the role:

.. code-block:: yaml

    security_rhel7_initialize_aide: true

.. warning::

    Even with the excluded directories, the first AIDE initialization can take
    a long time on some systems. During this time, the CPU and disks are **very
    busy**.

To avoid installing and initializing AIDE, set the following Ansible variable:

.. code-block:: yaml

    security_rhel7_enable_aide: false

.. include:: auto_aide.rst

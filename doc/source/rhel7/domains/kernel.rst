kernel - Kernel parameters
==========================

The Linux kernel has many parameters that can improve overall system security
and most of these parameters can be changed while a system is running.

Overview
--------

The security role applies several changes to kernel parameters and each of
these changes are controlled by Ansible variables. Review the ``## Kernel
settings`` section within ``defaults/main.yml`` file for more information on
these changes.

One deviation appears in this section for IP forwarding. Review the
documentation for ``V-72309`` below for more details.

.. include:: auto_kernel.rst

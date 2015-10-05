Security hardening for openstack-ansible
========================================

The openstack-ansible-security role provides security hardening for `OpenStack`_
environments deployed with `openstack-ansible`_.  The role has multiple goals:

* Provide additional security in a highly configurable, integrated way
* Make it easier for organizations to meet the requirements of compliance
  programs, such as `Payment Card Industry Data Security Standard (PCI-DSS)`_
* Document all changes to allow deployers to make educated decisions on which
  security configuration changes to apply.

At this time, the role follows the requirements of the US Government's
`Security Technical Implementation Guide (STIG)`_ for Red Hat Enterprise Linux 6.
Since openstack-ansible only supports Ubuntu 14.04 (as of late 2015), many of
the configuration changes in the STIG will be adapted to fit an Ubuntu 14.04
system.  Those adaptations are noted within the playbook tasks themselves and
also within this documentation.

The easiest method for reviewing the STIG configurations and the relevant
metadata is through the `STIG Viewer`_ service provided by `UCF`_.

.. _OpenStack: http://www.openstack.org/
.. _openstack-ansible: http://docs.openstack.org/developer/openstack-ansible/
.. _Payment Card Industry Data Security Standard (PCI-DSS): https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard
.. _Security Technical Implementation Guide (STIG): https://en.wikipedia.org/wiki/Security_Technical_Implementation_Guide
.. _STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/
.. _UCF: http://www.unifiedcompliance.com/

Table of Contents
=================

.. toctree::
   :maxdepth: 2

   getting-started.rst
   writing-docs.rst
   configurations.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


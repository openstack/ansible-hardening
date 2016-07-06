========================================
Security hardening for OpenStack-Ansible
========================================

Abstract
~~~~~~~~

The openstack-ansible-security role provides security hardening for `OpenStack`_
environments deployed with `openstack-ansible`_.  The role has multiple goals:

* Provide additional security in a highly configurable, integrated way without
  disrupting a production OpenStack environment.
* Make it easier for organizations to meet the requirements of compliance
  programs, such as `Payment Card Industry Data Security Standard (PCI-DSS)`_.
* Document all changes to allow deployers to make educated decisions on which
  security configuration changes to apply.

At this time, the role follows the requirements of the US Government's
`Security Technical Implementation Guide (STIG)`_ for Red Hat Enterprise Linux 6.

The easiest method for reviewing the STIG configurations and the relevant
metadata is through the `STIG Viewer`_ service provided by `UCF`_.

.. _OpenStack: http://www.openstack.org/
.. _openstack-ansible: http://docs.openstack.org/developer/openstack-ansible/
.. _Payment Card Industry Data Security Standard (PCI-DSS): https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard
.. _Security Technical Implementation Guide (STIG): https://en.wikipedia.org/wiki/Security_Technical_Implementation_Guide
.. _STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/
.. _UCF: http://www.unifiedcompliance.com/

Newton: Development
~~~~~~~~~~~~~~~~~~~

The openstack-ansible-security role is currently under development for the
Newton release. The Newton release supports the following Linux distributions:

* Ubuntu 14.04
* Ubuntu 16.04
* CentOS 7
* Red Hat Enterprise Linux 7 `(partial automated test coverage)`

.. toctree::
   :maxdepth: 2

   benefits.rst
   configuration.rst
   getting-started.rst
   controls.rst
   developer-guide.rst

Mitaka: Stable release
~~~~~~~~~~~~~~~~~~~~~~

The Mitaka release of the openstack-ansible-security role was first released
with the 13.0.0 tag on April 1st, 2016.  Refer to the `Mitaka release notes
<http://docs.openstack.org/releasenotes/openstack-ansible-security/mitaka.html>`_
for more details on the improvements and fixes.

Ubuntu 14.04 is supported in the Mitaka release.

* `openstack-ansible-security Mitaka Documentation`_

.. _openstack-ansible-security Mitaka Documentation: http://docs.openstack.org/developer/openstack-ansible-security/mitaka/

Liberty: Previous stable release (EOL: 2016-11-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the `Liberty release notes
<http://docs.openstack.org/releasenotes/openstack-ansible-security/liberty.html>`_
for more details on the improvements and fixes.

Ubuntu 14.04 is supported in the Liberty release.

* `openstack-ansible-security Liberty Documentation`_

.. _openstack-ansible-security Liberty Documentation: http://docs.openstack.org/developer/openstack-ansible-security/liberty/


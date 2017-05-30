============================================
Automated security hardening for Linux hosts
============================================

The ansible-hardening Ansible role uses industry-standard security
hardening guides to secure Linux hosts. Although the role is designed to work
well in OpenStack environments that are deployed with OpenStack-Ansible, it can
be used with almost any Linux system.

What does the role do?
----------------------

It all starts with the `Security Technical Implementation Guide (STIG)`_ from
the `Defense Information Systems Agency (DISA)`_, part of the United States
Department of Defense. The guide is released with a public domain license and
it is commonly used to secure systems at public and private organizations
around the world.

Each configuration from the STIG is analyzed to determine what impact it could
have on a live production environment and how to implement it in Ansible. Tasks
are added to the role that configure a host to meet the configuration
requirement. Each task is documented to explain what was changed, why it was
changed, and what deployers need to understand about the change.

Deployers have the option to pick and choose which configurations are applied
using Ansible variables and tags. Some tasks allow deployers to provide custom
configurations to tighten down or relax certain requirements.

For more details, review the *Documentation* section below.

.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/Pages/index.aspx
.. _Defense Information Systems Agency (DISA): http://www.disa.mil/

Documentation
-------------

The following documentation applies to the Ocata release. Documentation from
previous releases are available in the *Releases* section below.

.. toctree::
   :maxdepth: 2

   faq.rst
   getting-started.rst
   special-notes.rst
   controls-rhel7.rst
   developer-guide.rst

The RHEL 7 STIG content was first added in the Ocata release. The original RHEL
6 STIG content is deprecated in the Ocata release and will be removed in the
Queens OpenStack release (early 2018). The documentation for the RHEL 6 STIG
content is still available:

.. toctree::
   :maxdepth: 2

   controls.rst

Releases
--------

Deployers should use the latest stable release for all production deployments.

Ocata
~~~~~

* **Status:** Stable release

* **Supported Operating Systems:**

  * Ubuntu 14.04 Trusty *(Deprecated)*
  * Ubuntu 16.04 Xenial
  * CentOS 7
  * Red Hat Enterprise Linux 7 *(partial automated test coverage)*

* **Documentation:**

  * `ansible-hardening Ocata Documentation`_
  * `ansible-hardening Ocata Release Notes`_

.. _ansible-hardening Ocata Documentation: http://docs.openstack.org/developer/ansible-hardening/ocata/
.. _ansible-hardening Ocata Release Notes: http://docs.openstack.org/releasenotes/ansible-hardening/ocata.html

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

The following documentation applies to the Pike release. Documentation from
previous releases are available in the *Releases* section below.

.. toctree::
   :maxdepth: 2

   getting-started.rst
   faq.rst
   special-notes.rst
   controls-rhel7.rst
   developer-guide.rst

Special Notes: STIG Content
---------------------------

The RHEL 7 STIG content was first added in the Ocata release using the
pre-release STIG content (version 0.2). The Pike release contains the final
STIG release content which also included a numbering change from the
``RHEL-xx-xxxxxx`` style to the traditional ``V-xxxxx`` style.

The original RHEL 6 STIG content was deprecated in the Ocata release and will
be removed in the Queens release (early 2018). The documentation for the
RHEL 6 STIG content is still available:

.. toctree::
   :maxdepth: 2

   controls.rst

Releases
--------

Deployers should use the latest stable release for all production deployments.

Pike
~~~~

* **Status:** Active development *(anticipated release: September 2017)*

* **Supported Operating Systems:**

  * Ubuntu 14.04 Trusty *(Deprecated)*
  * Ubuntu 16.04 Xenial
  * CentOS 7
  * Red Hat Enterprise Linux 7 *(partial automated test coverage)*

* **Documentation:**

  * `ansible-hardening Pike Release Notes`_

.. _ansible-hardening Pike Release Notes: http://docs.openstack.org/releasenotes/ansible-hardening/unreleased.html

Ocata
~~~~~

* **Status:** Latest stable release *(released February 2017)*

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

Newton
~~~~~~

* **Status:** Previous stable release *(released October 2016)*

* **Supported Operating Systems:**

  * Ubuntu 14.04 Trusty
  * Ubuntu 16.04 Xenial
  * CentOS 7
  * Red Hat Enterprise Linux 7 *(partial automated test coverage)*

* **Documentation:**

  * `ansible-hardening Newton Documentation`_
  * `ansible-hardening Newton Release Notes`_

.. _ansible-hardening Newton Documentation: http://docs.openstack.org/developer/ansible-hardening/newton/
.. _ansible-hardening Newton Release Notes: http://docs.openstack.org/releasenotes/ansible-hardening/newton.html

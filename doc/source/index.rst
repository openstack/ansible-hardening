=========================================================
Automated security hardening for Linux hosts with Ansible
=========================================================

.. image:: _static/ansible-hardening-logo.png
   :alt: ansible-hardening logo

What does the role do?
----------------------

The ansible-hardening Ansible role uses industry-standard security
hardening guides to secure Linux hosts. Although the role is designed to work
well in OpenStack environments that are deployed with OpenStack-Ansible, it can
be used with almost any Linux system.

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

.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/Pages/index.aspx
.. _Defense Information Systems Agency (DISA): http://www.disa.mil/

OpenStack Summit Boston 2017 Talk
---------------------------------

This talk covers the latest updates from the project and a live demo. Slides
from the talk are
`available for download <https://www.slideshare.net/MajorHayden/securing-openstack-and-beyond-with-ansible>`_.

.. raw:: html

    <iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/E67zaS_UZks?rel=0" frameborder="0" allowfullscreen></iframe>

Documentation
-------------

The following documentation applies to the Queens release (currently under
active development). Documentation for the latest stable and previous stable
releases is found within the *Releases* section below.

.. toctree::
   :maxdepth: 2

   getting-started.rst
   deviations.rst
   faq.rst
   domains.rst
   controls-rhel7.rst
   contrib.rst
   developer-guide.rst

Releases
--------

Deployers should use the latest stable release for all production deployments.

Train
~~~~~~

* **Status:** Latest stable release

* **STIG Version:**
  RHEL 7 STIG Version 1, Release 3 *(Published on 2017-10-27)*

* **Supported Operating Systems:**

  * CentOS 7
  * Debian 10 Buster
  * openSUSE Leap 15 and 15.1
  * Red Hat Enterprise Linux 7
  * Ubuntu 18.04 Bionic

Stein
~~~~~~

* **Status:** Latest stable release

* **STIG Version:**
  RHEL 7 STIG Version 1, Release 3 *(Published on 2017-10-27)*

* **Supported Operating Systems:**

  * CentOS 7
  * Debian 9 Stretch and 10 Buster
  * openSUSE Leap 15 and 15.1
  * Red Hat Enterprise Linux 7
  * Ubuntu 18.04 Bionic

Rocky
~~~~~~

* **Status:** Latest stable release

* **STIG Version:**
  RHEL 7 STIG Version 1, Release 3 *(Published on 2017-10-27)*

* **Supported Operating Systems:**

  * CentOS 7
  * openSUSE Leap 42.3
  * Red Hat Enterprise Linux 7
  * Ubuntu 16.04 Xenial and 18.04 Bionic

Queens
~~~~~~

* **Status:** Latest stable release

* **STIG Version:**
  RHEL 7 STIG Version 1, Release 3 *(Published on 2017-10-27)*

* **Supported Operating Systems:**

  * CentOS 7
  * Debian 8 Jessie
  * Fedora 26
  * openSUSE Leap 42.2 and 42.3
  * Red Hat Enterprise Linux 7 *(partial automated test coverage)*
  * SUSE Linux Enterprise 12 (*experimental*)
  * Ubuntu 16.04 Xenial

* **Documentation:**

  * `ansible-hardening Queens Release Notes`_

.. _ansible-hardening Queens Release Notes: https://docs.openstack.org/releasenotes/ansible-hardening/unreleased.html

Pike
~~~~

* **Status:** Latest stable release *(released: September 2017)*

* **STIG Version:**
  RHEL 7 STIG Version 1, Release 1 *(Published on 2017-02-27)*

* **Supported Operating Systems:**

  * CentOS 7
  * Debian 8 Jessie
  * Fedora 26
  * openSUSE Leap 42.2 and 42.3
  * Red Hat Enterprise Linux 7 *(partial automated test coverage)*
  * SUSE Linux Enterprise 12 (*experimental*)
  * Ubuntu 14.04 Trusty *(Deprecated)*
  * Ubuntu 16.04 Xenial

* **Documentation:**

  * `ansible-hardening Pike Documentation`_
  * `ansible-hardening Pike Release Notes`_

.. _ansible-hardening Pike Documentation: https://docs.openstack.org/ansible-hardening/pike/
.. _ansible-hardening Pike Release Notes: https://docs.openstack.org/releasenotes/ansible-hardening/pike.html

Ocata
~~~~~

* **Status:** Latest stable release *(released February 2017)*

* **Supported Operating Systems:**

  * CentOS 7
  * Red Hat Enterprise Linux 7 *(partial automated test coverage)*
  * Ubuntu 14.04 Trusty *(Deprecated)*
  * Ubuntu 16.04 Xenial

* **Documentation:**

  * `ansible-hardening Ocata Documentation`_
  * `ansible-hardening Ocata Release Notes`_

.. _ansible-hardening Ocata Documentation: https://docs.openstack.org/ansible-hardening/ocata/
.. _ansible-hardening Ocata Release Notes: https://docs.openstack.org/releasenotes/ansible-hardening/ocata.html

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

.. _ansible-hardening Newton Documentation: https://docs.openstack.org/ansible-hardening/newton/
.. _ansible-hardening Newton Release Notes: https://docs.openstack.org/releasenotes/ansible-hardening/newton.html

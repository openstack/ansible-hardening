.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Security benefits FAQ
=====================

The openstack-ansible-security role provides hardened security configurations
for the host operating system as well as many common system services.

Why should this role be applied to a system?
--------------------------------------------

First and foremost, this role should be applied to production systems in
environments where security is a priority.  If an OpenStack environment is
exposed to the internet or to large internal corporate networks, applying
this role will reduce the risk of compromised OpenStack infrastructure. The
changes made by the role should also reduce the impact of potential
compromises as well.

Some deployers may be subject to industry compliance programs, such as
PCI-DSS, ISO 27001/27002, or NIST 800-53.  Many of these programs require
hardening standards to be applied to critical systems, such as OpenStack
infrastructure components.

Which systems are covered?
--------------------------------------------------------

The openstack-ansible-security role provides security hardening for physical
servers running the following Linux distributions:

* Ubuntu 14.04
* Ubuntu 16.04
* CentOS 7
* Red Hat Enterprise Linux 7

The OpenStack gating system tests the role against each of these distributions
regularly except for Red Hat Enterprise Linux 7, since it is a non-free
Linux distribution. CentOS 7 is very similar to Red Hat Enterprise Linux 7 and
the existing test coverage for CentOS is very thorough.

Which systems are not covered?
------------------------------

The containers that run various OpenStack services on physical servers in
OpenStack-Ansible deployments are currently out of scope and are not changed
by the role.

Virtual machines that are created within the OpenStack environment are also
not affected by this role, although this role could be applied within those
VM's if a deployer chooses to do so.

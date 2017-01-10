Frequently Asked Questions
==========================

Does this role work only with OpenStack environments?
-----------------------------------------------------

No -- it works on almost any Linux host!

The openstack-ansible-security role first began as a component of the
OpenStack-Ansible project and it was designed to deploy into an existing
OpenStack environment without causing disruptions. However, the role now works
well in OpenStack and non-OpenStack environments.

See *Which systems are covered?* below for more details.

Why should this role be applied to a system?
--------------------------------------------

There are three main reasons to apply this role to production Linux systems:

Improve security posture
  The configurations from the STIG add security and rigor around multiple
  components of a Linux system, including user authentication, service
  configurations, and package management. All of these configurations add up
  to an environment that is more difficult for an attacker to penetrate and use
  for lateral movement.

Meet compliance requirements
  Some deployers may be subject to industry compliance programs, such as
  PCI-DSS, ISO 27001/27002, or NIST 800-53. Many of these programs require
  hardening standards to be applied to critical systems, such as OpenStack
  infrastructure components.

Deployment without disruption
  Security is often at odds with usability. The role provides the greatest
  security benefit without disrupting production systems. Deployers have the
  option to opt out or opt in for most configurations depending on how their
  environments are configured.

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

misc - Miscellaneous security controls
======================================

Some of the security controls provided by the STIG are difficult to group
together. The following documentation includes STIG requirements which do not
easily fit into one of the other hardening domains.

Overview
--------

Reliable time synchronization is a requirement in the STIG and the ``chrony``
package will be installed to handle NTP for systems secured with the openstack-
ansible-security role. The default settings will work for most environments,
but some deployers may prefer to use NTP servers which are geographically
closer to their servers.

The role configures the chrony daemon to listen only on ``localhost``. To allow
chrony to listen on all addresses (the upstream default for chrony),
set the ``security_ntp_bind_local_interfaces_only`` variable to ``False``.

The default configuration allows `RFC1918`_ addresses to reach the NTP server
running on each host. That could be changed by using the
``security_allowed_ntp_subnets`` parameter.

.. _RFC1918: https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces

.. include:: auto_misc.rst

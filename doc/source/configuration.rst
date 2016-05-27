.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Configuration
=============

The openstack-ansible-security role is highly configurable and it ships with
reasonable defaults that provide a balance of enhanced security with limited
interruptions to production environments.  However, some deployers may need to
adjust the default configurations to fit the particular needs of their
OpenStack environment.

All of the default configurations are found within ``defaults/main.yml`` in the
role itself.

*NOTE: Deployers are strongly urged to test this role and any configuration
changes in a non-production, test environment.*

.. contents::
   :local:

AIDE
----

The STIG sets requirements for integrity monitoring of the system and the role
will install AIDE to meet these requirements.  However, Ubuntu's default
configuration will cause AIDE to search through container filesystems and this
will cause a serious performance hit to disk I/O for very long periods.

By default, this role exludes some directories that cause AIDE to spend a very
long time indexing the disk.  Additional directories can be added to the
exclusion list, but the directories currenty listed **should not be removed**.
Deployers can add directories to ``aide_exlude_dirs``.

The first AIDE database initialization can consume lots of CPU time and I/O
resources. By default, the role won't run the database initialization after
the role is applied to avoid causing performance degradation. The database will
be initialized automatically when the AIDE cron job runs the next day. To force
the initialization to run as soon as the role finishes running, change the
the following variable to ``true``:

.. code-block:: yaml

    security_initialize_aide: true

Audit daemon
------------

The `audit daemon`_ is required by the STIG and it provides useful logging of
critical events on a Linux server.

.. _audit daemon: http://people.redhat.com/sgrubb/audit/

Rules for auditd
^^^^^^^^^^^^^^^^

The openstack-ansible-security role creates a file containing audit rules for
hosts.

Each group of rules are controlled by Ansible variables that begin with
``security_audit_``. To omit a set of rules on a host, set the variable to
``no``. To include a set of rules on a host, set the variable to ``yes``.

For example, setting ``security_audit_filesystem_mounts`` to ``yes`` will
ensure that the rules for auditing filesystem mounts are included on each host.
Setting ``security_audit_filesystem_mounts`` to ``no`` will omit that group of
rules on each host.

To review the full list of rules and variables, refer to
``templates/osas-auditd.j2``.

Other auditd configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

There are several configurations for auditd which are critical for deployers
to review in detail.  The options beneath the ``## Auditd configuration``
comment will change how auditd handles log files and what it should do in case
of emergencies.

**NOTE:** Some of these configuration options can cause serious issues on
production systems, ranging from a reduction in security to servers going
offline unexpectedly.  There is extensive documentation in the developer notes
for each STIG requirement.

Authentication
--------------

The STIG sets requirements for various authentication-related security
controls, including password complexity, password aging/locking, and
simultaneous logins.  All of these can cause issues on production systems and
some cannot be met on Ubuntu systems due to the lack of certain packages.

Deployers are urged to review each item under the ``## Authentication`` comment
in ``defaults/main.yml`` as well as the developer notes for each requirement.
The notes explain the potential pitfalls from each configuration item and
they provide alternatives when a configuration isn't directly available.

fail2ban
^^^^^^^^

The fail2ban service is installed to meet some requirements around failed login
attempts.  The STIG requires ``pam_faillock``, but that module isn't available
in Ubuntu 14.04.

To opt-in for the fail2ban service to be installed, set
``security_install_fail2ban`` to ``yes`` and set an appropriate time for bans
with ``security_fail2ban_bantime``.  See the notes for V-38501 for more
details.

Kernel
------

Kernel modules
^^^^^^^^^^^^^^

Certain kernel modules are restricted by the STIG because they can become a
security threat to a server. The Ansible tasks will disable most of these
variables in accordance with the STIG. These changes are controlled by Ansible
variables matching the pattern ``security_disable_module_MODULENAME``. Refer to
``defaults/main.yml`` for a full list of these variables.

A setting of ``yes`` means that the module will be disabled on the next boot
and a setting of ``no`` means that the state of the module will not be changed.

All of the defaults are set in accordance with the STIG's requitements with
the exception of the ``usb_storage`` kernel module.  This module is used
frequently with external hard drives, USB sticks, and with some IPMI
implementations.  Deployers who wish to follow the STIG guidelines will need
to set ``usb_storage`` to ``yes`` so that the ``usb_storage`` module is
disabled on the next boot.

sysctl settings
^^^^^^^^^^^^^^^

The STIG requires that TCP SYN cookies enabled by default to protect against
certain types of attacks, like SYN floods.  This can cause issues in some
environments with busy load balancers.  Deployers should review the notes for
V-38539 for more details.

Also, the STIG requires IPv6 support to be fully disabled, and this could cause
issues for production systems.  The role will not disable IPv6 by default, but
deployers can adjust this by changing ``security_disable_ipv6`` to ``yes``.

Core dumps are also disabled by default in the openstack-ansible-security role.

Linux Security Module (LSM)
---------------------------

The STIG requires that SELinux is in enforcing mode to provide additional
security against attacks. The security role will enable SELinux on CentOS
systems and enable AppArmor on Ubuntu systems.

For more information on how these changes are applied, refer to the
documentation for V-51337.

Mail
----

Deployers are strongly urged to configure an address to receive the ``root``
user's email on various hosts.  This is done with the
``security_root_forward_email`` variable.

The STIG requires that a valid user receives the email in case of errors or a
security issue.

Services and packages
---------------------

The STIG has recommendations for which services shouldn't be running and which
packages shouldn't be installed.  These removals can be configured to meet
the requirements of the deployer.

Disabling services
^^^^^^^^^^^^^^^^^^

By default, the role will disable any services that are recommended to be
disabled by the STIG. These changes are controlled by Ansible variables that
match the ``security_disable_SERVICENAME`` pattern. Review these variables in
``defaults/main.yml`` for more details.

A setting of ``yes`` for a service will cause the service to be disabled in
accordance to the STIG's requirements.

A setting of ``no`` causes the role to ignore the service entirely.  If the
service is running, it will remain running.  If the service is stopped,
it will remain stopped.

Removing services
^^^^^^^^^^^^^^^^^

The STIG requires that some packages are completely removed from the server. By
default, the role will remove the packages in accordance with the STIG's
requirements. These changes are controlled by Ansible variables that match the
``security_remove_SERVICENAME`` pattern. Review these variables in
``defaults/main.yml`` for more details.

A setting of ``yes`` for a service will cause the package that contains the
service to be removed from the system.  If the service happens to be running
at the time, it will be stopped by ``apt``.

A setting of ``no`` for a service will cause the role to ignore the package
that contains the service.  If the package is installed, it will be left
installed.

SSH server
----------

The STIG has some requirements for ssh server configuration and these
requirements are applied by default by the role.  To opt-out or change these
requirements, see the section under the ``## SSH configuration`` comment in
``defaults/main.yml``.

Special note about PermitRootLogin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**NOTE:** There is one deviation from the STIG for the ``PermitRootLogin``
configuration option.  The STIG requires that direct root logins are disabled,
and this is the recommended setting for secure production environments.
However, this can cause problems in some existing environments and the default
for the role is to set it to ``yes`` (direct root logins allowed).

Time synchronization with chrony
--------------------------------

Reliable time synchronization is a requirement in the STIG and the ``chrony``
package will be installed to handle NTP for systems secured with the
openstack-ansible-security role.

The default settings will work for most environments, but some deployers may
prefer to use NTP servers which are geographically closer to their servers.

The role configures the chrony daemon to listen only on localhost. To allow
chrony to listen on all addresses (the upstream default for chrony),
set the ``security_ntp_bind_local_interfaces_only`` variable to ``False``.

The default configuration allows `RFC1918`_ addresses to reach the NTP server
running on each host. That could be changed by using the
``security_allowed_ntp_subnets`` parameter.

.. _RFC1918: https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces

umask adjustments
-----------------

Certain umask adjustments are required by the STIG, but these can cause
problems with production systems.  The requirements are commented out within
``defaults/main.yml`` and can be applied by uncommenting the variables that
start with ``security_umask_*``.  There is extensive documentation available
within the developer notes for each STIG requirement.

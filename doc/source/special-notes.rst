Deviations & Special Notes
==========================

The Security Technical Implementation Guide (STIG) provides over 200 controls
to secure a Linux system, but some of these configurations can cause problems
with production environments.

.. contents::
   :local:
   :backlinks: none
   :depth: 2

Reviewing deviations
--------------------

The openstack-ansible-security role deviates from some of the STIG's
requirements when a security control could cause significant issues with
production systems. The role classifies each control into an implementation
status and provides notes on why a certain control is skipped or altered.

The following provides a brief overview of each implementation status:

Exception
  If a control requires manual intervention outside the host, or if it could
  cause significant harm to a host, it will be skipped and listed as an
  exception. All controls in this category are not implemented in Ansible.

Configuration Required
  These controls require some type of initial configuration before they can
  be applied. Review the notes for each control to determine how to configure
  each of them.

Implemented
  These controls are fully implemented and they may have configurations which
  can be adjusted. The notes for each control will identify which configuration
  options are available.

Opt-In
  The controls in the opt-in list are implemented in Ansible, but are disabled
  by default. They are often disabled because they could cause harm to a subset
  of systems. Each control has notes that explains the caveats of the control
  and how to enable it if needed.

Deployers should review the full list of controls
`sorted by implementation status <auto_controls-by-status.html>`_.

.. note::

   All of the default configurations are found within ``defaults/main.yml``.

AIDE initialization
-------------------

The STIG sets requirements for integrity monitoring of the system and the role
will install AIDE to meet these requirements.

By default AIDE will examine and monitor all of the files on a host unless
directories are added to its exclusion list. The security role sets directories
to exclude from AIDE monitoring via the ``aide_exclude_dirs`` variable. this
list excludes the most common directories that change very often via automated
methods.

Even with the excluded directories, the first AIDE initialization can take a
long time on some systems. During this time, the CPU and disks are **very
busy**.

The security role will skip the AIDE initialization step by default. Deployers
must set the following Ansible variable to initialize the database:

.. code-block:: yaml

    security_initialize_aide: true

auditd
------

The audit daemon (``auditd``) is required by the STIG and it provides useful
logging of critical events on a Linux server. The audit daemon monitors
syscalls on a Linux system and logs alerts based on sets of auditing rules.

Rules for auditd
  Each set of rules is controlled by Ansible variables that begin with
  ``security_audit_``. To omit a set of rules on a host, set the variable to
  ``no``. To include a set of rules on a host, set the variable to ``yes``.

  For example, setting ``security_audit_filesystem_mounts`` to ``yes`` will
  ensure that the rules for auditing filesystem mounts are included on each
  host. Setting ``security_audit_filesystem_mounts`` to ``no`` will omit that
  group of rules on each host.

  To review the full list of rules and variables, refer to
  ``templates/osas-auditd.j2``.

Handling audit emergencies
  There are several configurations for auditd which are critical for deployers
  to review in detail.  The options beneath the ``## Auditd configuration``
  comment will change how auditd handles log files and what it should do in
  case of emergencies.

  .. note::

    Some of these configuration options can cause serious issues on
    production systems, ranging from a reduction in security to servers going
    offline unexpectedly.  There is extensive documentation in the developer notes
    for each STIG requirement.

Authentication
--------------

The STIG sets requirements for various authentication-related security
controls, including password complexity, password aging/locking, and
simultaneous logins.  All of these can cause issues on production systems.

Handling multiple failed login attempts
  The fail2ban service is installed to meet some requirements around failed
  login attempts.  The STIG requires ``pam_faillock``, but that module isn't
  available in the Linux distributions supported by this role.

  To opt-in for the fail2ban service to be installed, set
  ``security_install_fail2ban`` to ``yes`` and set an appropriate time for bans
  with ``security_fail2ban_bantime``.  See the notes for
  :ref:`V-38501 <stig-V-38501>` for more details.

  Note that fail2ban will not take action on failed logins via physical
  consoles or consoles exposed to out of band interfaces, such as DRAC, IPMI,
  or iLO. This will be fixed in a future release.

Deployers are urged to review each item in the ``## PAM and Authentication``
section in ``defaults/main.yml`` as well as the developer notes for each
requirement. The notes explain the potential pitfalls from each configuration
item and they provide alternatives when a configuration isn't directly
available.

Kernel modules
--------------

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

Linux Security Modules (LSM)
----------------------------

The STIG requires that SELinux is in enforcing mode to provide additional
security against attacks. The security role will enable SELinux on CentOS
systems and enable AppArmor on Ubuntu systems.

For more information on how these changes are applied, refer to the
documentation for :ref:`V-51337 <stig-V-51337>`.

Mail
----

Deployers are strongly urged to configure an address to receive the ``root``
user's email on various hosts.  This is done with the
``security_root_forward_email`` variable.

The STIG requires that a valid user receives the email in case of errors or a
security issue.

Removing and disabling services
-------------------------------

The STIG has recommendations for which services shouldn't be running and which
packages shouldn't be installed.  These removals can be configured to meet
the requirements of the deployer.

Disabling services
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
  The STIG requires that some packages are completely removed from the server.
  By default, the role will remove the packages in accordance with the STIG's
  requirements. These changes are controlled by Ansible variables that match
  the ``security_remove_SERVICENAME`` pattern. Review these variables in
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

Deviation for PermitRootLogin
  There is one deviation from the STIG for the ``PermitRootLogin``
  configuration option.  The STIG requires that direct root logins are
  disabled, and this is the recommended setting for secure production
  environments.

  However, this can cause problems in some existing environments and the
  default for the role is to set it to ``yes`` (direct root logins allowed).

sysctl settings
---------------

The STIG requires that TCP SYN cookies enabled by default to protect against
certain types of attacks, like SYN floods.  This can cause issues in some
environments with busy load balancers.  Deployers should review the notes for
:ref:`V-38539 <stig-V-38539>` for more details.

Also, the STIG requires IPv6 support to be fully disabled, and this could cause
issues for production systems.  The role will not disable IPv6 by default, but
deployers can adjust this by changing ``security_disable_ipv6`` to ``yes``.

Core dumps are also disabled by default in the openstack-ansible-security role.

Time synchronization
--------------------

Reliable time synchronization is a requirement in the STIG and the ``chrony``
package will be installed to handle NTP for systems secured with the
openstack-ansible-security role.

The default settings will work for most environments, but some deployers may
prefer to use NTP servers which are geographically closer to their servers.

The role configures the chrony daemon to listen only on ``localhost``. To allow
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

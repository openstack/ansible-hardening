.. _special_notes:

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

    security_rhel7_initialize_aide: true

auditd
------

The audit daemon (``auditd``) is required by the STIG and it provides useful
logging of critical events on a Linux server. The audit daemon monitors
syscalls on a Linux system and logs alerts based on sets of auditing rules.

Rules for auditd
  Each set of rules is controlled by Ansible variables that begin with
  ``security_audit__rhel7``. To omit a set of rules on a host, set the variable
  to ``no``. To include a set of rules on a host, set the variable to ``yes``.

  For example, setting ``security_rhel7_audit_mount`` to ``yes`` will
  ensure that the rules for auditing filesystem mounts are included on each
  host. Setting ``security_rhel7_audit_mount`` to ``no`` will omit that
  group of rules on each host.

  To review the full list of rules and variables, refer to
  ``templates/osas-auditd-rhel7.j2``.

Handling audit emergencies
  There are several configurations for auditd which are critical for deployers
  to review in detail. The options beneath the ``## Audit daemon (auditd)``
  comment will change how auditd handles log files and what it should do in
  case of emergencies.

  .. note::

    Some of these configuration options can cause serious issues on
    production systems, ranging from a reduction in security to servers going
    offline unexpectedly. There is extensive documentation in the developer
    notes for each STIG requirement.

Linux Security Modules (LSM)
----------------------------

The STIG requires that SELinux is in enforcing mode to provide additional
security against attacks. The security role will enable SELinux on CentOS
systems and enable AppArmor on Ubuntu systems.

For more information on how these changes are applied, refer to the
documentation for :ref:`V-71989 <stig-V-71989>`.

SSH server
----------

The STIG has some requirements for ssh server configuration and these
requirements are applied by default by the role. To opt-out or change these
requirements, see the section under the ``## ssh server (sshd)`` comment in
``defaults/main.yml``.

Deviation for PermitRootLogin
  There is one deviation from the STIG for the ``PermitRootLogin``
  configuration option. The STIG requires that direct root logins are
  disabled, and this is the recommended setting for secure production
  environments.

  However, this can cause problems in some existing environments and the
  default for the role is to set it to ``yes`` (direct root logins allowed).

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

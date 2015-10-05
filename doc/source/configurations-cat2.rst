.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Category 2 (Medium) configurations
================================

.. contents::
   :depth: 2


V-38612: The SSH daemon must not allow host-based authentication.
-----------------------------------------------------------------

SSH trust relationships mean a compromise on one host can allow an attacker to
move trivially to other hosts.

Details: `V-38612 in STIG Viewer`_.

.. _V-38612 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38612

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38612.rst

V-38580: The audit system must be configured to audit the loading and unloading of dynamic kernel modules.
----------------------------------------------------------------------------------------------------------

The addition/removal of kernel modules can be used to alter the behavior of
the kernel and potentially introduce malicious code into kernel space. It is
important to have an audit trail of modules that have been introduced into the
kernel.

Details: `V-38580 in STIG Viewer`_.

.. _V-38580 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38580

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38580.rst

V-38459: The /etc/group file must be group-owned by root.
---------------------------------------------------------

The "/etc/group" file contains information regarding groups that are
configured on the system. Protection of this file is important for system
security.

Details: `V-38459 in STIG Viewer`_.

.. _V-38459 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38459

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38459.rst

V-38643: There must be no world-writable files on the system.
-------------------------------------------------------------

Data in world-writable files can be modified by any user on the system. In
almost all circumstances, files can be configured using a combination of user
and group permissions to support whatever legitimate access is needed without
the risk caused by world-writable files.

Details: `V-38643 in STIG Viewer`_.

.. _V-38643 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38643

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38643.rst

V-38551: The operating system must connect to external networks or information systems only through managed IPv6 interfaces consisting of boundary protection devices arranged in accordance with an organizational security architecture.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The "ip6tables" service provides the system's host-based firewalling
capability for IPv6 and ICMPv6.

Details: `V-38551 in STIG Viewer`_.

.. _V-38551 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38551

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38551.rst

V-51363: The system must use a Linux Security Module configured to enforce limits on system services.
-----------------------------------------------------------------------------------------------------

Setting the SELinux state to enforcing ensures SELinux is able to confine
potentially compromised processes to the security policy, which is designed to
prevent them from causing damage to the system or further elevating their
privileges.

Details: `V-51363 in STIG Viewer`_.

.. _V-51363 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-51363

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-51363.rst

V-38499: The /etc/passwd file must not contain password hashes.
---------------------------------------------------------------

The hashes for all user account passwords should be stored in the file
"/etc/shadow" and never in "/etc/passwd", which is readable by all users.

Details: `V-38499 in STIG Viewer`_.

.. _V-38499 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38499

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38499.rst

V-38450: The /etc/passwd file must be owned by root.
----------------------------------------------------

The "/etc/passwd" file contains information about the users that are
configured on the system. Protection of this file is critical for system
security.

Details: `V-38450 in STIG Viewer`_.

.. _V-38450 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38450

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38450.rst

V-38581: The system boot loader configuration file(s) must be group-owned by root.
----------------------------------------------------------------------------------

The "root" group is a highly-privileged group. Furthermore, the group-owner of
this file should not have any access privileges anyway.

Details: `V-38581 in STIG Viewer`_.

.. _V-38581 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38581

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38581.rst

V-38451: The /etc/passwd file must be group-owned by root.
----------------------------------------------------------

The "/etc/passwd" file contains information about the users that are
configured on the system. Protection of this file is critical for system
security.

Details: `V-38451 in STIG Viewer`_.

.. _V-38451 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38451

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38451.rst

V-38458: The /etc/group file must be owned by root.
---------------------------------------------------

The "/etc/group" file contains information regarding groups that are
configured on the system. Protection of this file is important for system
security.

Details: `V-38458 in STIG Viewer`_.

.. _V-38458 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38458

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38458.rst

V-38658: The system must prohibit the reuse of passwords within twenty-four iterations.
---------------------------------------------------------------------------------------

Preventing reuse of previous passwords helps ensure that a compromised
password is not reused by a user.

Details: `V-38658 in STIG Viewer`_.

.. _V-38658 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38658

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38658.rst

V-38582: The xinetd service must be disabled if no network services utilizing it are enabled.
---------------------------------------------------------------------------------------------

The xinetd service provides a dedicated listener service for some programs,
which is no longer necessary for commonly-used network services. Disabling it
ensures that these uncommon services are not running, and also prevents
attacks against xinetd itself.

Details: `V-38582 in STIG Viewer`_.

.. _V-38582 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38582

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38582.rst

V-38652: Remote file systems must be mounted with the nodev option.
-------------------------------------------------------------------

Legitimate device files should only exist in the /dev directory. NFS mounts
should not present device files to users.

Details: `V-38652 in STIG Viewer`_.

.. _V-38652 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38652

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38652.rst

V-38654: Remote file systems must be mounted with the nosuid option.
--------------------------------------------------------------------

NFS mounts should not present suid binaries to users. Only vendor-supplied
suid executables should be installed to their default location on the local
filesystem.

Details: `V-38654 in STIG Viewer`_.

.. _V-38654 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38654

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38654.rst

V-38490: The operating system must enforce requirements for the connection of mobile devices to operating systems.
------------------------------------------------------------------------------------------------------------------

USB storage devices such as thumb drives can be used to introduce unauthorized
software and other vulnerabilities. Support for these devices should be
disabled and the devices themselves should be tightly controlled.

Details: `V-38490 in STIG Viewer`_.

.. _V-38490 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38490

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38490.rst

V-38443: The /etc/gshadow file must be owned by root.
-----------------------------------------------------

The "/etc/gshadow" file contains group password hashes. Protection of this
file is critical for system security.

Details: `V-38443 in STIG Viewer`_.

.. _V-38443 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38443

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38443.rst

V-38526: The system must not accept ICMPv4 secure redirect packets on any interface.
------------------------------------------------------------------------------------

Accepting "secure" ICMP redirects (from those gateways listed as default
gateways) has few legitimate uses. It should be disabled unless it is
absolutely required.

Details: `V-38526 in STIG Viewer`_.

.. _V-38526 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38526

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38526.rst

V-38524: The system must not accept ICMPv4 redirect packets on any interface.
-----------------------------------------------------------------------------

Accepting ICMP redirects has few legitimate uses. It should be disabled unless
it is absolutely required.

Details: `V-38524 in STIG Viewer`_.

.. _V-38524 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38524

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38524.rst

V-38488: The operating system must conduct backups of user-level information contained in the operating system per organization defined frequency to conduct backups consistent with recovery time and recovery point objectives.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Operating system backup is a critical step in maintaining data assurance and
availability. User-level information is data generated by information system
and/or application users. Backups shall be consistent with organizational
recovery time and recovery point objectives.

Details: `V-38488 in STIG Viewer`_.

.. _V-38488 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38488

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38488.rst

V-38520: The operating system must back up audit records on an organization defined frequency onto a different system or media than the system being audited.
-------------------------------------------------------------------------------------------------------------------------------------------------------------

A log server (loghost) receives syslog messages from one or more systems. This
data can be used as an additional log source in the event a system is
compromised and its local logs are suspect. Forwarding log messages to a
remote loghost also provides system administrators with a centralized place to
view the status of multiple hosts within the enterprise.

Details: `V-38520 in STIG Viewer`_.

.. _V-38520 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38520

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38520.rst

V-38521: The operating system must support the requirement to centrally manage the content of audit records generated by organization defined information system components.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A log server (loghost) receives syslog messages from one or more systems. This
data can be used as an additional log source in the event a system is
compromised and its local logs are suspect. Forwarding log messages to a
remote loghost also provides system administrators with a centralized place to
view the status of multiple hosts within the enterprise.

Details: `V-38521 in STIG Viewer`_.

.. _V-38521 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38521

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38521.rst

V-38484: The operating system, upon successful logon, must display to the user the date and time of the last logon or access via ssh.
-------------------------------------------------------------------------------------------------------------------------------------

Users need to be aware of activity that occurs regarding their account.
Providing users with information regarding the date and time of their last
successful login allows the user to determine if any unauthorized activity has
occurred and gives them an opportunity to notify administrators.  At ssh
login, a user must be presented with the last successful login date and time.

Details: `V-38484 in STIG Viewer`_.

.. _V-38484 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38484

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38484.rst

V-38486: The operating system must conduct backups of system-level information contained in the information system per organization defined frequency to conduct backups that are consistent with recovery time and recovery point objectives.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Operating system backup is a critical step in maintaining data assurance and
availability. System-level information includes system-state information,
operating system and application software, and licenses. Backups must be
consistent with organizational recovery time and recovery point objectives.

Details: `V-38486 in STIG Viewer`_.

.. _V-38486 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38486

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38486.rst

V-38481: System security patches and updates must be installed and up-to-date.
------------------------------------------------------------------------------

Installing software updates is a fundamental mitigation against the
exploitation of publicly-known vulnerabilities.

Details: `V-38481 in STIG Viewer`_.

.. _V-38481 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38481

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38481.rst

V-38529: The system must not accept IPv4 source-routed packets by default.
--------------------------------------------------------------------------

Accepting source-routed packets in the IPv4 protocol has few legitimate uses.
It should be disabled unless it is absolutely required.

Details: `V-38529 in STIG Viewer`_.

.. _V-38529 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38529

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38529.rst

V-38665: The system package management tool must verify group-ownership on all files and directories associated with the audit package.
---------------------------------------------------------------------------------------------------------------------------------------

Group-ownership of audit binaries and configuration files that is incorrect
could allow an unauthorized user to gain privileges that they should not have.
The group-ownership set by the vendor should be maintained. Any deviations
from this baseline should be investigated.

Details: `V-38665 in STIG Viewer`_.

.. _V-38665 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38665

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38665.rst

V-38664: The system package management tool must verify ownership on all files and directories associated with the audit package.
---------------------------------------------------------------------------------------------------------------------------------

Ownership of audit binaries and configuration files that is incorrect could
allow an unauthorized user to gain privileges that they should not have. The
ownership set by the vendor should be maintained. Any deviations from this
baseline should be investigated.

Details: `V-38664 in STIG Viewer`_.

.. _V-38664 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38664

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38664.rst

V-38667: The system must have a host-based intrusion detection tool installed.
------------------------------------------------------------------------------

Adding host-based intrusion detection tools can provide the capability to
automatically take actions in response to malicious behavior, which can
provide additional agility in reacting to network threats. These tools also
often include a reporting capability to provide network awareness of system,
which may not otherwise exist in an organization's systems management regime.

Details: `V-38667 in STIG Viewer`_.

.. _V-38667 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38667

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38667.rst

V-38660: The snmpd service must use only SNMP protocol version 3 or newer.
--------------------------------------------------------------------------

Earlier versions of SNMP are considered insecure, as they potentially allow
unauthorized access to detailed system management information.

Details: `V-38660 in STIG Viewer`_.

.. _V-38660 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38660

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38660.rst

V-38663: The system package management tool must verify permissions on all files and directories associated with the audit package.
-----------------------------------------------------------------------------------------------------------------------------------

Permissions on audit binaries and configuration files that are too generous
could allow an unauthorized user to gain privileges that they should not have.
The permissions set by the vendor should be maintained. Any deviations from
this baseline should be investigated.

Details: `V-38663 in STIG Viewer`_.

.. _V-38663 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38663

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38663.rst

V-38446: The mail system must forward all mail for root to one or more system administrators.
---------------------------------------------------------------------------------------------

A number of system services utilize email messages sent to the root user to
notify system administrators of active or impending issues.  These messages
must be forwarded to at least one monitored email address.

Details: `V-38446 in STIG Viewer`_.

.. _V-38446 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38446

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38446.rst

V-38466: Library files must be owned by root.
---------------------------------------------

Files from shared library directories are loaded into the address space of
processes (including privileged ones) or of the kernel itself at runtime.
Proper ownership is necessary to protect the integrity of the system.

Details: `V-38466 in STIG Viewer`_.

.. _V-38466 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38466

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38466.rst

V-38465: Library files must have mode 0755 or less permissive.
--------------------------------------------------------------

Files from shared library directories are loaded into the address space of
processes (including privileged ones) or of the kernel itself at runtime.
Restrictive permissions are necessary to protect the integrity of the system.

Details: `V-38465 in STIG Viewer`_.

.. _V-38465 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38465

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38465.rst

V-38464: The audit system must take appropriate action when there are disk errors on the audit storage volume.
--------------------------------------------------------------------------------------------------------------

Taking appropriate action in case of disk errors will minimize the possibility
of losing audit records.

Details: `V-38464 in STIG Viewer`_.

.. _V-38464 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38464

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38464.rst

V-38461: The /etc/group file must have mode 0644 or less permissive.
--------------------------------------------------------------------

The "/etc/group" file contains information regarding groups that are
configured on the system. Protection of this file is important for system
security.

Details: `V-38461 in STIG Viewer`_.

.. _V-38461 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38461

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38461.rst

V-38492: The system must prevent the root account from logging in from virtual consoles.
----------------------------------------------------------------------------------------

Preventing direct root login to virtual console devices helps ensure
accountability for actions taken on the system using the root account.

Details: `V-38492 in STIG Viewer`_.

.. _V-38492 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38492

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38492.rst

V-38469: All system command files must have mode 755 or less permissive.
------------------------------------------------------------------------

System binaries are executed by privileged users, as well as system services,
and restrictive permissions are necessary to ensure execution of these
programs cannot be co-opted.

Details: `V-38469 in STIG Viewer`_.

.. _V-38469 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38469

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38469.rst

V-38468: The audit system must take appropriate action when the audit storage volume is full.
---------------------------------------------------------------------------------------------

Taking appropriate action in case of a filled audit storage volume will
minimize the possibility of losing audit records.

Details: `V-38468 in STIG Viewer`_.

.. _V-38468 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38468

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38468.rst

V-38553: The operating system must prevent public IPv6 access into an organizations internal networks, except as appropriately mediated by managed interfaces employing boundary protection devices.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The "ip6tables" service provides the system's host-based firewalling
capability for IPv6 and ICMPv6.

Details: `V-38553 in STIG Viewer`_.

.. _V-38553 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38553

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38553.rst

V-38498: Audit log files must have mode 0640 or less permissive.
----------------------------------------------------------------

If users can write to audit logs, audit trails can be modified or destroyed.

Details: `V-38498 in STIG Viewer`_.

.. _V-38498 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38498

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38498.rst

V-38555: The system must employ a local IPv4 firewall.
------------------------------------------------------

The "iptables" service provides the system's host-based firewalling capability
for IPv4 and ICMP.

Details: `V-38555 in STIG Viewer`_.

.. _V-38555 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38555

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38555.rst

V-51875: The operating system, upon successful logon/access, must display to the user the number of unsuccessful logon/access attempts since the last successful logon/access.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Users need to be aware of activity that occurs regarding their account.
Providing users with information regarding the number of unsuccessful attempts
that were made to login to their account allows the user to determine if any
unauthorized activity has occurred and gives them an opportunity to notify
administrators.

Details: `V-51875 in STIG Viewer`_.

.. _V-51875 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-51875

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-51875.rst

V-38493: Audit log directories must have mode 0755 or less permissive.
----------------------------------------------------------------------

If users can delete audit logs, audit trails can be modified or destroyed.

Details: `V-38493 in STIG Viewer`_.

.. _V-38493 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38493

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38493.rst

V-38496: Default operating system accounts, other than root, must be locked.
----------------------------------------------------------------------------

Disabling authentication for default system accounts makes it more difficult
for attackers to make use of them to compromise a system.

Details: `V-38496 in STIG Viewer`_.

.. _V-38496 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38496

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38496.rst

V-38523: The system must not accept IPv4 source-routed packets on any interface.
--------------------------------------------------------------------------------

Accepting source-routed packets in the IPv4 protocol has few legitimate uses.
It should be disabled unless it is absolutely required.

Details: `V-38523 in STIG Viewer`_.

.. _V-38523 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38523

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38523.rst

V-38673: The operating system must ensure unauthorized, security-relevant configuration changes detected are tracked.
---------------------------------------------------------------------------------------------------------------------

By default, AIDE does not install itself for periodic execution. Periodically
running AIDE may reveal unexpected changes in installed files.

Details: `V-38673 in STIG Viewer`_.

.. _V-38673 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38673

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38673.rst

V-38670: The operating system must detect unauthorized changes to software and information. 
--------------------------------------------------------------------------------------------

By default, AIDE does not install itself for periodic execution. Periodically
running AIDE may reveal unexpected changes in installed files.

Details: `V-38670 in STIG Viewer`_.

.. _V-38670 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38670

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38670.rst

V-38671: The sendmail package must be removed.
----------------------------------------------

The sendmail software was not developed with security in mind and its design
prevents it from being effectively contained by SELinux. Postfix should be
used instead.

Details: `V-38671 in STIG Viewer`_.

.. _V-38671 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38671

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38671.rst

V-38674: X Windows must not be enabled unless required.
-------------------------------------------------------

Unnecessary services should be disabled to decrease the attack surface of the
system.

Details: `V-38674 in STIG Viewer`_.

.. _V-38674 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38674

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38674.rst

V-38630: The graphical desktop environment must automatically lock after 15 minutes of inactivity and the system must require user reauthentication to unlock the environment.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enabling idle activation of the screen saver ensures the screensaver will be
activated after the idle delay. Applications requiring continuous, real-time
screen display (such as network management products) require the login session
does not have administrator rights and the display station is located in a
controlled-access area.

Details: `V-38630 in STIG Viewer`_.

.. _V-38630 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38630

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38630.rst

V-38678: The audit system must provide a warning when allocated audit record storage volume reaches a documented percentage of maximum audit record storage capacity.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Notifying administrators of an impending disk space problem may allow them to
take corrective action prior to any disruption.

Details: `V-38678 in STIG Viewer`_.

.. _V-38678 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38678

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38678.rst

V-58901: The sudo command must require authentication.
------------------------------------------------------

The "sudo" command allows authorized users to run programs (including shells)
as other users, system users, and root. The "/etc/sudoers" file is used to
configure authorized "sudo" users as well as the programs they are allowed to
run. Some configuration options in the "/etc/sudoers" file allow configured
users to run programs without re-authenticating. Use of these configuration
options makes it easier for one compromised account to be used to compromise
other accounts.

Details: `V-58901 in STIG Viewer`_.

.. _V-58901 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-58901

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-58901.rst

V-38475: The system must require passwords to contain a minimum of 14 characters.
---------------------------------------------------------------------------------

Requiring a minimum password length makes password cracking attacks more
difficult by ensuring a larger search space. However, any security benefit
from an onerous requirement must be carefully weighed against usability
problems, support costs, or counterproductive behavior that may result.  While
it does not negate the password length requirement, it is preferable to
migrate from a password-based authentication scheme to a stronger one based on
PKI (public key infrastructure).

Details: `V-38475 in STIG Viewer`_.

.. _V-38475 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38475

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38475.rst

V-38477: Users must not be able to change passwords more than once every 24 hours.
----------------------------------------------------------------------------------

Setting the minimum password age protects against users cycling back to a
favorite password after satisfying the password reuse requirement.

Details: `V-38477 in STIG Viewer`_.

.. _V-38477 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38477

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38477.rst

V-38470: The audit system must alert designated staff members when the audit storage volume approaches capacity.
----------------------------------------------------------------------------------------------------------------

Notifying administrators of an impending disk space problem may allow them to
take corrective action prior to any disruption.

Details: `V-38470 in STIG Viewer`_.

.. _V-38470 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38470

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38470.rst

V-38679: The DHCP client must be disabled if not needed.
--------------------------------------------------------

DHCP relies on trusting the local network. If the local network is not
trusted, then it should not be used. However, the automatic configuration
provided by DHCP is commonly used and the alternative, manual configuration,
presents an unacceptable burden in many circumstances.

Details: `V-38679 in STIG Viewer`_.

.. _V-38679 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38679

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38679.rst

V-38479: User passwords must be changed at least every 60 days.
---------------------------------------------------------------

Setting the password maximum age ensures users are required to periodically
change their passwords. This could possibly decrease the utility of a stolen
password. Requiring shorter password lifetimes increases the risk of users
writing down the password in a convenient location subject to physical
compromise.

Details: `V-38479 in STIG Viewer`_.

.. _V-38479 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38479

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38479.rst

V-54381: The audit system must switch the system to single-user mode when available audit storage volume becomes dangerously low.
---------------------------------------------------------------------------------------------------------------------------------

Administrators should be made aware of an inability to record audit records.
If a separate partition or logical volume of adequate size is used, running
low on space for audit records should never occur.

Details: `V-54381 in STIG Viewer`_.

.. _V-54381 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-54381

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-54381.rst

V-38445: Audit log files must be group-owned by root.
-----------------------------------------------------

If non-privileged users can write to audit logs, audit trails can be modified
or destroyed.

Details: `V-38445 in STIG Viewer`_.

.. _V-38445 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38445

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38445.rst

V-38542: The system must use a reverse-path filter for IPv4 network traffic when possible on all interfaces.
------------------------------------------------------------------------------------------------------------

Enabling reverse path filtering drops packets with source addresses that
should not have been able to be received on the interface they were received
on. It should not be used on systems which are routers for complicated
networks, but is helpful for end hosts and routers serving small networks.

Details: `V-38542 in STIG Viewer`_.

.. _V-38542 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38542

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38542.rst

V-38544: The system must use a reverse-path filter for IPv4 network traffic when possible by default.
-----------------------------------------------------------------------------------------------------

Enabling reverse path filtering drops packets with source addresses that
should not have been able to be received on the interface they were received
on. It should not be used on systems which are routers for complicated
networks, but is helpful for end hosts and routers serving small networks.

Details: `V-38544 in STIG Viewer`_.

.. _V-38544 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38544

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38544.rst

V-38546: The IPv6 protocol handler must not be bound to the network stack unless needed.
----------------------------------------------------------------------------------------

Any unnecessary network stacks - including IPv6 - should be disabled, to
reduce the vulnerability to exploitation.

Details: `V-38546 in STIG Viewer`_.

.. _V-38546 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38546

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38546.rst

V-38548: The system must ignore ICMPv6 redirects by default.
------------------------------------------------------------

An illicit ICMP redirect message could result in a man-in-the-middle attack.

Details: `V-38548 in STIG Viewer`_.

.. _V-38548 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38548

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38548.rst

V-38549: The system must employ a local IPv6 firewall.
------------------------------------------------------

The "ip6tables" service provides the system's host-based firewalling
capability for IPv6 and ICMPv6.

Details: `V-38549 in STIG Viewer`_.

.. _V-38549 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38549

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38549.rst

V-38472: All system command files must be owned by root.
--------------------------------------------------------

System binaries are executed by privileged users as well as system services,
and restrictive permissions are necessary to ensure that their execution of
these programs cannot be co-opted.

Details: `V-38472 in STIG Viewer`_.

.. _V-38472 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38472

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38472.rst

V-38689: The Department of Defense (DoD) login banner must be displayed immediately prior to, or as part of, graphical desktop environment login prompts.
---------------------------------------------------------------------------------------------------------------------------------------------------------

An appropriate warning message reinforces policy awareness during the logon
process and facilitates possible legal action against attackers.

Details: `V-38689 in STIG Viewer`_.

.. _V-38689 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38689

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38689.rst

V-38688: A login banner must be displayed immediately prior to, or as part of, graphical desktop environment login prompts.
---------------------------------------------------------------------------------------------------------------------------

An appropriate warning message reinforces policy awareness during the logon
process and facilitates possible legal action against attackers.

Details: `V-38688 in STIG Viewer`_.

.. _V-38688 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38688

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38688.rst

V-38686: The systems local firewall must implement a deny-all, allow-by-exception policy for forwarded packets.
---------------------------------------------------------------------------------------------------------------

In "iptables" the default policy is applied only after all the applicable
rules in the table are examined for a match. Setting the default policy to
"DROP" implements proper design for a firewall, i.e., any packets which are
not explicitly permitted should not be accepted.

Details: `V-38686 in STIG Viewer`_.

.. _V-38686 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38686

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38686.rst

V-38682: The Bluetooth kernel module must be disabled.
------------------------------------------------------

If Bluetooth functionality must be disabled, preventing the kernel from
loading the kernel module provides an additional safeguard against its
activation.

Details: `V-38682 in STIG Viewer`_.

.. _V-38682 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38682

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38682.rst

V-38680: The audit system must identify staff members to receive notifications of audit log storage volume capacity issues.
---------------------------------------------------------------------------------------------------------------------------

Email sent to the root account is typically aliased to the administrators of
the system, who can take appropriate action.

Details: `V-38680 in STIG Viewer`_.

.. _V-38680 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38680

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38680.rst

V-38606: The tftp-server package must not be installed unless required.
-----------------------------------------------------------------------

Removing the "tftp-server" package decreases the risk of the accidental (or
intentional) activation of tftp services.

Details: `V-38606 in STIG Viewer`_.

.. _V-38606 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38606

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38606.rst

V-38605: The cron service must be running.
------------------------------------------

Due to its usage for maintenance and security-supporting tasks, enabling the
cron daemon is essential.

Details: `V-38605 in STIG Viewer`_.

.. _V-38605 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38605

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38605.rst

V-38604: The ypbind service must not be running.
------------------------------------------------

Disabling the "ypbind" service ensures the system is not acting as a client in
a NIS or NIS+ domain.

Details: `V-38604 in STIG Viewer`_.

.. _V-38604 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38604

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38604.rst

V-38603: The ypserv package must not be installed.
--------------------------------------------------

Removing the "ypserv" package decreases the risk of the accidental (or
intentional) activation of NIS or NIS+ services.

Details: `V-38603 in STIG Viewer`_.

.. _V-38603 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38603

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38603.rst

V-38601: The system must not send ICMPv4 redirects from any interface.
----------------------------------------------------------------------

Sending ICMP redirects permits the system to instruct other systems to update
their routing information. The ability to send ICMP redirects is only
appropriate for systems acting as routers.

Details: `V-38601 in STIG Viewer`_.

.. _V-38601 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38601

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38601.rst

V-38600: The system must not send ICMPv4 redirects by default.
--------------------------------------------------------------

Sending ICMP redirects permits the system to instruct other systems to update
their routing information. The ability to send ICMP redirects is only
appropriate for systems acting as routers.

Details: `V-38600 in STIG Viewer`_.

.. _V-38600 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38600

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38600.rst

V-38449: The /etc/gshadow file must have mode 0000.
---------------------------------------------------

The /etc/gshadow file contains group password hashes. Protection of this file
is critical for system security.

Details: `V-38449 in STIG Viewer`_.

.. _V-38449 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38449

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38449.rst

V-38448: The /etc/gshadow file must be group-owned by root.
-----------------------------------------------------------

The "/etc/gshadow" file contains group password hashes. Protection of this
file is critical for system security.

Details: `V-38448 in STIG Viewer`_.

.. _V-38448 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38448

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38448.rst

V-38609: The TFTP service must not be running.
----------------------------------------------

Disabling the "tftp" service ensures the system is not acting as a tftp
server, which does not provide encryption or authentication.

Details: `V-38609 in STIG Viewer`_.

.. _V-38609 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38609

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38609.rst

V-51391: A file integrity baseline must be created.
---------------------------------------------------

For AIDE to be effective, an initial database of "known-good" information
about files must be captured and it should be able to be verified against the
installed files.

Details: `V-51391 in STIG Viewer`_.

.. _V-51391 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-51391

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-51391.rst

V-38632: The operating system must produce audit records containing sufficient information to establish what type of events occurred.
-------------------------------------------------------------------------------------------------------------------------------------

Ensuring the "auditd" service is active ensures audit records generated by the
kernel can be written to disk, or that appropriate actions will be taken if
other obstacles exist.

Details: `V-38632 in STIG Viewer`_.

.. _V-38632 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38632

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38632.rst

V-38579: The system boot loader configuration file(s) must be owned by root.
----------------------------------------------------------------------------

Only root should be able to modify important boot parameters.

Details: `V-38579 in STIG Viewer`_.

.. _V-38579 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38579

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38579.rst

V-38613: The system must not permit root logins using remote access programs such as ssh.
-----------------------------------------------------------------------------------------

Permitting direct root login reduces auditable information about who ran
privileged commands on the system and also allows direct attack attempts on
root's password.

Details: `V-38613 in STIG Viewer`_.

.. _V-38613 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38613

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38613.rst

V-38574: The system must use a FIPS 140-2 approved cryptographic hashing algorithm for generating account password hashes (system-auth).
----------------------------------------------------------------------------------------------------------------------------------------

Using a stronger hashing algorithm makes password cracking attacks more
difficult.

Details: `V-38574 in STIG Viewer`_.

.. _V-38574 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38574

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38574.rst

V-38577: The system must use a FIPS 140-2 approved cryptographic hashing algorithm for generating account password hashes (libuser.conf).
-----------------------------------------------------------------------------------------------------------------------------------------

Using a stronger hashing algorithm makes password cracking attacks more
difficult.

Details: `V-38577 in STIG Viewer`_.

.. _V-38577 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38577

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38577.rst

V-38576: The system must use a FIPS 140-2 approved cryptographic hashing algorithm for generating account password hashes (login.defs).
---------------------------------------------------------------------------------------------------------------------------------------

Using a stronger hashing algorithm makes password cracking attacks more
difficult.

Details: `V-38576 in STIG Viewer`_.

.. _V-38576 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38576

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38576.rst

V-38489: A file integrity tool must be installed.
-------------------------------------------------

The AIDE package must be installed if it is to be available for integrity
checking.

Details: `V-38489 in STIG Viewer`_.

.. _V-38489 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38489

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38489.rst

V-38573: The system must disable accounts after three consecutive unsuccessful logon attempts.
----------------------------------------------------------------------------------------------

Locking out user accounts after a number of incorrect attempts prevents direct
password guessing attacks.

Details: `V-38573 in STIG Viewer`_.

.. _V-38573 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38573

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38573.rst

V-38698: The operating system must employ automated mechanisms to detect the presence of unauthorized software on organizational information systems and notify designated organizational officials in accordance with the organization defined frequency.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, AIDE does not install itself for periodic execution. Periodically
running AIDE may reveal unexpected changes in installed files.

Details: `V-38698 in STIG Viewer`_.

.. _V-38698 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38698

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38698.rst

V-38519: All rsyslog-generated log files must be group-owned by root.
---------------------------------------------------------------------

The log files generated by rsyslog contain valuable information regarding
system configuration, user authentication, and other such information. Log
files should be protected from unauthorized access.

Details: `V-38519 in STIG Viewer`_.

.. _V-38519 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38519

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38519.rst

V-38518: All rsyslog-generated log files must be owned by root.
---------------------------------------------------------------

The log files generated by rsyslog contain valuable information regarding
system configuration, user authentication, and other such information. Log
files should be protected from unauthorized access.

Details: `V-38518 in STIG Viewer`_.

.. _V-38518 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38518

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38518.rst

V-38517: The Transparent Inter-Process Communication (TIPC) protocol must be disabled unless required.
------------------------------------------------------------------------------------------------------

Disabling TIPC protects the system against exploitation of any flaws in its
implementation.

Details: `V-38517 in STIG Viewer`_.

.. _V-38517 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38517

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38517.rst

V-38515: The Stream Control Transmission Protocol (SCTP) must be disabled unless required.
------------------------------------------------------------------------------------------

Disabling SCTP protects the system against exploitation of any flaws in its
implementation.

Details: `V-38515 in STIG Viewer`_.

.. _V-38515 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38515

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38515.rst

V-38514: The Datagram Congestion Control Protocol (DCCP) must be disabled unless required.
------------------------------------------------------------------------------------------

Disabling DCCP protects the system against exploitation of any flaws in its
implementation.

Details: `V-38514 in STIG Viewer`_.

.. _V-38514 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38514

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38514.rst

V-38691: The Bluetooth service must be disabled.
------------------------------------------------

Disabling the "bluetooth" service prevents the system from attempting
connections to Bluetooth devices, which entails some security risk.
Nevertheless, variation in this risk decision may be expected due to the
utility of Bluetooth connectivity and its limited range.

Details: `V-38691 in STIG Viewer`_.

.. _V-38691 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38691

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38691.rst

V-38511: IP forwarding for IPv4 must not be enabled, unless the system is a router.
-----------------------------------------------------------------------------------

IP forwarding permits the kernel to forward packets from one network interface
to another. The ability to forward packets between two networks is only
appropriate for systems acting as routers.

Details: `V-38511 in STIG Viewer`_.

.. _V-38511 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38511

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38511.rst

V-38597: The system must limit the ability of processes to have simultaneous write and execute access to memory.
----------------------------------------------------------------------------------------------------------------

ExecShield uses the segmentation feature on all x86 systems to prevent
execution in memory higher than a certain address. It writes an address as a
limit in the code segment descriptor, to control where code can be executed,
on a per-process basis. When the kernel places a process's memory regions such
as the stack and heap higher than this address, the hardware prevents
execution in that address range.

Details: `V-38597 in STIG Viewer`_.

.. _V-38597 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38597

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38597.rst

V-38596: The system must implement virtual address space randomization.
-----------------------------------------------------------------------

Address space layout randomization (ASLR) makes it more difficult for an
attacker to predict the location of attack code he or she has introduced into
a process's address space during an attempt at exploitation. Additionally,
ASLR also makes it more difficult for an attacker to know the location of
existing code in order to repurpose it using return oriented programming (ROP)
techniques.

Details: `V-38596 in STIG Viewer`_.

.. _V-38596 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38596

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38596.rst

V-38595: The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication.
----------------------------------------------------------------------------------------------------------------------------------------------------

Smart card login provides two-factor authentication stronger than that
provided by a username/password combination. Smart cards leverage a PKI
(public key infrastructure) in order to provide and verify credentials.

Details: `V-38595 in STIG Viewer`_.

.. _V-38595 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38595

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38595.rst

V-38593: The Department of Defense (DoD) login banner must be displayed immediately prior to, or as part of, console login prompts.
-----------------------------------------------------------------------------------------------------------------------------------

An appropriate warning message reinforces policy awareness during the logon
process and facilitates possible legal action against attackers.

Details: `V-38593 in STIG Viewer`_.

.. _V-38593 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38593

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38593.rst

V-38592: The system must require administrator action to unlock an account locked by excessive failed login attempts.
---------------------------------------------------------------------------------------------------------------------

Locking out user accounts after a number of incorrect attempts prevents direct
password guessing attacks. Ensuring that an administrator is involved in
unlocking locked accounts draws appropriate attention to such situations.

Details: `V-38592 in STIG Viewer`_.

.. _V-38592 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38592

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38592.rst

V-38457: The /etc/passwd file must have mode 0644 or less permissive.
---------------------------------------------------------------------

If the "/etc/passwd" file is writable by a group-owner or the world the risk
of its compromise is increased. The file contains the list of accounts on the
system and associated information, and protection of this file is critical for
system security.

Details: `V-38457 in STIG Viewer`_.

.. _V-38457 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38457

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38457.rst

V-38495: Audit log files must be owned by root.
-----------------------------------------------

If non-privileged users can write to audit logs, audit trails can be modified
or destroyed.

Details: `V-38495 in STIG Viewer`_.

.. _V-38495 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38495

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38495.rst

V-38619: There must be no .netrc files on the system.
-----------------------------------------------------

Unencrypted passwords for remote FTP servers may be stored in ".netrc" files.
DoD policy requires passwords be encrypted in storage and not used in access
scripts.

Details: `V-38619 in STIG Viewer`_.

.. _V-38619 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38619

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38619.rst

V-38599: The FTPS/FTP service on the system must be configured with the Department of Defense (DoD) login banner.
-----------------------------------------------------------------------------------------------------------------

This setting will cause the system greeting banner to be used for FTP
connections as well.

Details: `V-38599 in STIG Viewer`_.

.. _V-38599 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38599

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38599.rst

V-51337: The system must use a Linux Security Module at boot time.
------------------------------------------------------------------

Disabling a major host protection feature, such as SELinux, at boot time
prevents it from confining system services at boot time. Further, it increases
the chances that it will remain off during system operation.

Details: `V-51337 in STIG Viewer`_.

.. _V-51337 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-51337

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-51337.rst

V-38585: The system boot loader must require authentication.
------------------------------------------------------------

Password protection on the boot loader configuration ensures users with
physical access cannot trivially alter important bootloader settings. These
include which kernel to use, and whether to enter single-user mode.

Details: `V-38585 in STIG Viewer`_.

.. _V-38585 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38585

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38585.rst

V-43150: The login user list must be disabled.
----------------------------------------------

Leaving the user list enabled is a security risk since it allows anyone with
physical access to the system to quickly enumerate known user accounts without
logging in.

Details: `V-43150 in STIG Viewer`_.

.. _V-43150 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-43150

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-43150.rst

V-57569: The noexec option must be added to the /tmp partition.
---------------------------------------------------------------

Allowing users to execute binaries from world-writable directories such as
"/tmp" should never be necessary in normal operation and can expose the system
to potential compromise.

Details: `V-57569 in STIG Viewer`_.

.. _V-57569 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-57569

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-57569.rst

V-38560: The operating system must connect to external networks or information systems only through managed IPv4 interfaces consisting of boundary protection devices arranged in accordance with an organizational security architecture.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The "iptables" service provides the system's host-based firewalling capability
for IPv4 and ICMP.

Details: `V-38560 in STIG Viewer`_.

.. _V-38560 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38560

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38560.rst

V-38444: The systems local IPv6 firewall must implement a deny-all, allow-by-exception policy for inbound packets.
------------------------------------------------------------------------------------------------------------------

In "ip6tables" the default policy is applied only after all the applicable
rules in the table are examined for a match. Setting the default policy to
"DROP" implements proper design for a firewall, i.e., any packets which are
not explicitly permitted should not be accepted.

Details: `V-38444 in STIG Viewer`_.

.. _V-38444 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38444

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38444.rst

V-38504: The /etc/shadow file must have mode 0000.
--------------------------------------------------

The "/etc/shadow" file contains the list of local system accounts and stores
password hashes. Protection of this file is critical for system security.
Failure to give ownership of this file to root provides the designated owner
with access to sensitive information which could weaken the system security
posture.

Details: `V-38504 in STIG Viewer`_.

.. _V-38504 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38504

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38504.rst

V-38583: The system boot loader configuration file(s) must have mode 0600 or less permissive.
---------------------------------------------------------------------------------------------

Proper permissions ensure that only the root user can modify important boot
parameters.

Details: `V-38583 in STIG Viewer`_.

.. _V-38583 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38583

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38583.rst

V-38500: The root account must be the only account having a UID of 0.
---------------------------------------------------------------------

An account has root authority if it has a UID of 0. Multiple accounts with a
UID of 0 afford more opportunity for potential intruders to guess a password
for a privileged account. Proper configuration of sudo is recommended to
afford multiple system administrators access to root privileges in an
accountable manner.

Details: `V-38500 in STIG Viewer`_.

.. _V-38500 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38500

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38500.rst

V-38501: The system must disable accounts after excessive login failures within a 15-minute interval.
-----------------------------------------------------------------------------------------------------

Locking out user accounts after a number of incorrect attempts within a
specific period of time prevents direct password guessing attacks.

Details: `V-38501 in STIG Viewer`_.

.. _V-38501 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38501

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38501.rst

V-38502: The /etc/shadow file must be owned by root.
----------------------------------------------------

The "/etc/shadow" file contains the list of local system accounts and stores
password hashes. Protection of this file is critical for system security.
Failure to give ownership of this file to root provides the designated owner
with access to sensitive information which could weaken the system security
posture.

Details: `V-38502 in STIG Viewer`_.

.. _V-38502 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38502

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38502.rst

V-38503: The /etc/shadow file must be group-owned by root.
----------------------------------------------------------

The "/etc/shadow" file stores password hashes. Protection of this file is
critical for system security.

Details: `V-38503 in STIG Viewer`_.

.. _V-38503 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38503

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38503.rst

V-38621: The system clock must be synchronized to an authoritative DoD time source.
-----------------------------------------------------------------------------------

Synchronizing with an NTP server makes it possible to collate system logs from
multiple sources or correlate computer events with real time events. Using a
trusted NTP server provided by your organization is recommended.

Details: `V-38621 in STIG Viewer`_.

.. _V-38621 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38621

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38621.rst

V-38620: The system clock must be synchronized continuously, or at least daily.
-------------------------------------------------------------------------------

Enabling the "ntpd" service ensures that the "ntpd" service will be running
and that the system will synchronize its time to any servers specified. This
is important whether the system is configured to be a client (and synchronize
only its own clock) or it is also acting as an NTP server to other systems.
Synchronizing time is essential for authentication services such as Kerberos,
but it is also important for maintaining accurate logs and auditing possible
security breaches.

Details: `V-38620 in STIG Viewer`_.

.. _V-38620 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38620

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38620.rst

V-38623: All rsyslog-generated log files must have mode 0600 or less permissive.
--------------------------------------------------------------------------------

Log files can contain valuable information regarding system configuration. If
the system log files are not protected, unauthorized users could change the
logged data, eliminating their forensic value.

Details: `V-38623 in STIG Viewer`_.

.. _V-38623 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38623

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38623.rst

V-38625: If the system is using LDAP for authentication or account information, the system must use a TLS connection using FIPS 140-2 approved cryptographic algorithms.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The ssl directive specifies whether to use ssl or not. If not specified it
will default to "no". It should be set to "start_tls" rather than doing LDAP
over SSL.

Details: `V-38625 in STIG Viewer`_.

.. _V-38625 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38625

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38625.rst

V-38626: The LDAP client must use a TLS connection using trust certificates signed by the site CA.
--------------------------------------------------------------------------------------------------

The tls_cacertdir or tls_cacertfile directives are required when tls_checkpeer
is configured (which is the default for openldap versions 2.1 and up). These
directives define the path to the trust certificates signed by the site CA.

Details: `V-38626 in STIG Viewer`_.

.. _V-38626 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38626

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38626.rst

V-38629: The graphical desktop environment must set the idle timeout to no more than 15 minutes.
------------------------------------------------------------------------------------------------

Setting the idle delay controls when the screensaver will start, and can be
combined with screen locking to prevent access from passersby.

Details: `V-38629 in STIG Viewer`_.

.. _V-38629 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38629

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38629.rst

V-38628: The operating system must produce audit records containing sufficient information to establish the identity of any user/subject associated with the event.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ensuring the "auditd" service is active ensures audit records generated by the
kernel can be written to disk, or that appropriate actions will be taken if
other obstacles exist.

Details: `V-38628 in STIG Viewer`_.

.. _V-38628 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38628

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38628.rst

V-38588: The system must not permit interactive boot.
-----------------------------------------------------

Using interactive boot, the console user could disable auditing, firewalls, or
other services, weakening system security.

Details: `V-38588 in STIG Viewer`_.

.. _V-38588 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38588

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38588.rst

V-38700: The operating system must provide a near real-time alert when any of the organization defined list of compromise or potential compromise indicators occurs. 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, AIDE does not install itself for periodic execution. Periodically
running AIDE may reveal unexpected changes in installed files.

Details: `V-38700 in STIG Viewer`_.

.. _V-38700 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38700

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38700.rst

V-38695: A file integrity tool must be used at least weekly to check for unauthorized file changes, particularly the addition of unauthorized system libraries or binaries, or for unauthorized modification to authorized system libraries or binaries.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, AIDE does not install itself for periodic execution. Periodically
running AIDE may reveal unexpected changes in installed files.

Details: `V-38695 in STIG Viewer`_.

.. _V-38695 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38695

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38695.rst

V-38483: The system package management tool must cryptographically verify the authenticity of system software packages during installation.
-------------------------------------------------------------------------------------------------------------------------------------------

Ensuring the validity of packages' cryptographic signatures prior to
installation ensures the provenance of the software and protects against
malicious tampering.

Details: `V-38483 in STIG Viewer`_.

.. _V-38483 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38483

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38483.rst

V-38539: The system must be configured to use TCP syncookies when experiencing a TCP SYN flood.
-----------------------------------------------------------------------------------------------

A TCP SYN flood attack can cause a denial of service by filling a system's TCP
connection table with connections in the SYN_RCVD state. Syncookies can be
used to track a connection when a subsequent ACK is received, verifying the
initiator is attempting a valid connection and is not a flood source. This
feature is activated when a flood condition is detected, and enables the
system to continue servicing valid connection requests.

Details: `V-38539 in STIG Viewer`_.

.. _V-38539 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38539

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38539.rst

V-38513: The systems local IPv4 firewall must implement a deny-all, allow-by-exception policy for inbound packets.
------------------------------------------------------------------------------------------------------------------

In "iptables" the default policy is applied only after all the applicable
rules in the table are examined for a match. Setting the default policy to
"DROP" implements proper design for a firewall, i.e., any packets which are
not explicitly permitted should not be accepted.

Details: `V-38513 in STIG Viewer`_.

.. _V-38513 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38513

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38513.rst

V-38532: The system must not accept ICMPv4 secure redirect packets by default.
------------------------------------------------------------------------------

Accepting "secure" ICMP redirects (from those gateways listed as default
gateways) has few legitimate uses. It should be disabled unless it is
absolutely required.

Details: `V-38532 in STIG Viewer`_.

.. _V-38532 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38532

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38532.rst

V-38512: The operating system must prevent public IPv4 access into an organizations internal networks, except as appropriately mediated by managed interfaces employing boundary protection devices.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The "iptables" service provides the system's host-based firewalling capability
for IPv4 and ICMP.

Details: `V-38512 in STIG Viewer`_.

.. _V-38512 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38512

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38512.rst

V-38439: The system must provide automated support for account management functions.
------------------------------------------------------------------------------------

A comprehensive account management process that includes automation helps to
ensure the accounts designated as requiring attention are consistently and
promptly addressed. Enterprise environments make user account management
challenging and complex. A user management process requiring administrators to
manually address account management functions adds risk of potential
oversight.

Details: `V-38439 in STIG Viewer`_.

.. _V-38439 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38439

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38439.rst

V-38638: The graphical desktop environment must have automatic lock enabled.
----------------------------------------------------------------------------

Enabling the activation of the screen lock after an idle period ensures
password entry will be required in order to access the system, preventing
access by passersby.

Details: `V-38638 in STIG Viewer`_.

.. _V-38638 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38638

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38638.rst

V-38636: The system must retain enough rotated audit logs to cover the required log retention period.
-----------------------------------------------------------------------------------------------------

The total storage for audit log files must be large enough to retain log
information over the period required. This is a function of the maximum log
file size and the number of logs retained.

Details: `V-38636 in STIG Viewer`_.

.. _V-38636 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38636

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38636.rst

V-38637: The system package management tool must verify contents of all files associated with the audit package.
----------------------------------------------------------------------------------------------------------------

The hash on important files like audit system executables should match the
information given by the RPM database. Audit executables  with erroneous
hashes could be a sign of nefarious activity on the system.

Details: `V-38637 in STIG Viewer`_.

.. _V-38637 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38637

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38637.rst

V-38634: The system must rotate audit log files that reach the maximum file size.
---------------------------------------------------------------------------------

Automatically rotating logs (by setting this to "rotate") minimizes the
chances of the system unexpectedly running out of disk space by being
overwhelmed with log data. However, for systems that must never discard log
data, or which use external processes to transfer it and reclaim space,
"keep_logs" can be employed.

Details: `V-38634 in STIG Viewer`_.

.. _V-38634 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38634

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38634.rst

V-38696: The operating system must employ automated mechanisms, per organization defined frequency, to detect the addition of unauthorized components/devices into the operating system.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, AIDE does not install itself for periodic execution. Periodically
running AIDE may reveal unexpected changes in installed files.

Details: `V-38696 in STIG Viewer`_.

.. _V-38696 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38696

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38696.rst

V-38633: The system must set a maximum audit log file size.
-----------------------------------------------------------

The total storage for audit log files must be large enough to retain log
information over the period required. This is a function of the maximum log
file size and the number of logs retained.

Details: `V-38633 in STIG Viewer`_.

.. _V-38633 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38633

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38633.rst

V-38586: The system must require authentication upon booting into single-user and maintenance modes.
----------------------------------------------------------------------------------------------------

This prevents attackers with physical access from trivially bypassing security
on the machine and gaining root access. Such accesses are further prevented by
configuring the bootloader password.

Details: `V-38586 in STIG Viewer`_.

.. _V-38586 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38586

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38586.rst

V-38631: The operating system must employ automated mechanisms to facilitate the monitoring and control of remote access methods.
---------------------------------------------------------------------------------------------------------------------------------

Ensuring the "auditd" service is active ensures audit records generated by the
kernel can be written to disk, or that appropriate actions will be taken if
other obstacles exist.

Details: `V-38631 in STIG Viewer`_.

.. _V-38631 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38631

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38631.rst

V-38615: The SSH daemon must be configured with the Department of Defense (DoD) login banner.
---------------------------------------------------------------------------------------------

The warning message reinforces policy awareness during the logon process and
facilitates possible legal action against attackers. Alternatively, systems
whose ownership should not be obvious should ensure usage of a banner that
does not provide easy attribution.

Details: `V-38615 in STIG Viewer`_.

.. _V-38615 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38615

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38615.rst

V-38622: Mail relaying must be restricted.
------------------------------------------

This ensures "postfix" accepts mail messages (such as cron job reports) from
the local system only, and not from the network, which protects it from
network attack.

Details: `V-38622 in STIG Viewer`_.

.. _V-38622 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38622

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38622.rst

V-38617: The SSH daemon must be configured to use only FIPS 140-2 approved ciphers.
-----------------------------------------------------------------------------------

Approved algorithms should impart some level of confidence in their
implementation. These are also required for compliance.

Details: `V-38617 in STIG Viewer`_.

.. _V-38617 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38617

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38617.rst

V-38611: The SSH daemon must ignore .rhosts files.
--------------------------------------------------

SSH trust relationships mean a compromise on one host can allow an attacker to
move trivially to other hosts.

Details: `V-38611 in STIG Viewer`_.

.. _V-38611 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38611

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38611.rst

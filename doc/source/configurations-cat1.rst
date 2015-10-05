.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Category 1 (Low) configurations
================================

.. contents::
   :depth: 2


V-38649: The system default umask for the csh shell must be 077.
----------------------------------------------------------------

The umask value influences the permissions assigned to files when they are
created. A misconfigured umask value could result in files with excessive
permissions that can be read and/or written to by unauthorized users.

Details: `V-38649 in STIG Viewer`_.

.. _V-38649 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38649

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38649.rst

V-38648: The qpidd service must not be running.
-----------------------------------------------

The qpidd service is automatically installed when the "base" package selection
is selected during installation. The qpidd service listens for network
connections which increases the attack surface of the system. If the system is
not intended to receive AMQP traffic then the "qpidd" service is not needed
and should be disabled or removed.

Details: `V-38648 in STIG Viewer`_.

.. _V-38648 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38648

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38648.rst

V-38642: The system default umask for daemons must be 027 or 022.
-----------------------------------------------------------------

The umask influences the permissions assigned to files created by a process at
run time. An unnecessarily permissive umask could result in files being
created with insecure permissions.

Details: `V-38642 in STIG Viewer`_.

.. _V-38642 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38642

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38642.rst

V-38641: The atd service must be disabled.
------------------------------------------

The "atd" service could be used by an unsophisticated insider to carry out
activities outside of a normal login session, which could complicate
accountability. Furthermore, the need to schedule tasks with "at" or "batch"
is not common.

Details: `V-38641 in STIG Viewer`_.

.. _V-38641 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38641

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38641.rst

V-38640: The Automatic Bug Reporting Tool (abrtd) service must not be running.
------------------------------------------------------------------------------

Mishandling crash data could expose sensitive information about
vulnerabilities in software executing on the local machine, as well as
sensitive information from within a process's address space or registers.

Details: `V-38640 in STIG Viewer`_.

.. _V-38640 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38640

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38640.rst

V-38647: The system default umask in /etc/profile must be 077.
--------------------------------------------------------------

The umask value influences the permissions assigned to files when they are
created. A misconfigured umask value could result in files with excessive
permissions that can be read and/or written to by unauthorized users.

Details: `V-38647 in STIG Viewer`_.

.. _V-38647 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38647

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38647.rst

V-38646: The oddjobd service must not be running.
-------------------------------------------------

The "oddjobd" service may provide necessary functionality in some environments
but it can be disabled if it is not needed. Execution of tasks by privileged
programs, on behalf of unprivileged ones, has traditionally been a source of
privilege escalation security issues.

Details: `V-38646 in STIG Viewer`_.

.. _V-38646 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38646

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38646.rst

V-38645: The system default umask in /etc/login.defs must be 077.
-----------------------------------------------------------------

The umask value influences the permissions assigned to files when they are
created. A misconfigured umask value could result in files with excessive
permissions that can be read and/or written to by unauthorized users.

Details: `V-38645 in STIG Viewer`_.

.. _V-38645 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38645

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38645.rst

V-38644: The ntpdate service must not be running.
-------------------------------------------------

The "ntpdate" service may only be suitable for systems which are rebooted
frequently enough that clock drift does not cause problems between reboots. In
any event, the functionality of the ntpdate service is now available in the
ntpd program and should be considered deprecated.

Details: `V-38644 in STIG Viewer`_.

.. _V-38644 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38644

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38644.rst

V-51369: The system must use a Linux Security Module configured to limit the privileges of system services.
-----------------------------------------------------------------------------------------------------------

Setting the SELinux policy to "targeted" or a more specialized policy ensures
the system will confine processes that are likely to be targeted for
exploitation, such as network or system services.

Details: `V-51369 in STIG Viewer`_.

.. _V-51369 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-51369

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-51369.rst

V-38452: The system package management tool must verify permissions on all files and directories associated with packages.
--------------------------------------------------------------------------------------------------------------------------

Permissions on system binaries and configuration files that are too generous
could allow an unauthorized user to gain privileges that they should not have.
The permissions set by the vendor should be maintained. Any deviations from
this baseline should be investigated.

Details: `V-38452 in STIG Viewer`_.

.. _V-38452 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38452

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38452.rst

V-38453: The system package management tool must verify group-ownership on all files and directories associated with packages.
------------------------------------------------------------------------------------------------------------------------------

Group-ownership of system binaries and configuration files that is incorrect
could allow an unauthorized user to gain privileges that they should not have.
The group-ownership set by the vendor should be maintained. Any deviations
from this baseline should be investigated.

Details: `V-38453 in STIG Viewer`_.

.. _V-38453 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38453

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38453.rst

V-38608: The SSH daemon must set a timeout interval on idle sessions.
---------------------------------------------------------------------

Causing idle users to be automatically logged out guards against compromises
one system leading trivially to compromises on another.

Details: `V-38608 in STIG Viewer`_.

.. _V-38608 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38608

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38608.rst

V-38447: The system package management tool must verify contents of all files associated with packages.
-------------------------------------------------------------------------------------------------------

The hash on important files like system executables should match the
information given by the RPM database. Executables with erroneous hashes could
be a sign of nefarious activity on the system.

Details: `V-38447 in STIG Viewer`_.

.. _V-38447 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38447

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38447.rst

V-38659: The operating system must employ cryptographic mechanisms to protect information in storage.
-----------------------------------------------------------------------------------------------------

The risk of a system's physical compromise, particularly mobile systems such
as laptops, places its data at risk of compromise. Encrypting this data
mitigates the risk of its loss if the system is lost.

Details: `V-38659 in STIG Viewer`_.

.. _V-38659 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38659

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38659.rst

V-38650: The rdisc service must not be running.
-----------------------------------------------

General-purpose systems typically have their network and routing information
configured statically by a system administrator. Workstations or some special-
purpose systems often use DHCP (instead of IRDP) to retrieve dynamic network
configuration information.

Details: `V-38650 in STIG Viewer`_.

.. _V-38650 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38650

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38650.rst

V-38651: The system default umask for the bash shell must be 077.
-----------------------------------------------------------------

The umask value influences the permissions assigned to files when they are
created. A misconfigured umask value could result in files with excessive
permissions that can be read and/or written to by unauthorized users.

Details: `V-38651 in STIG Viewer`_.

.. _V-38651 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38651

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38651.rst

V-38656: The system must use SMB client signing for connecting to samba servers using smbclient.
------------------------------------------------------------------------------------------------

Packet signing can prevent man-in-the-middle attacks which modify SMB packets
in transit.

Details: `V-38656 in STIG Viewer`_.

.. _V-38656 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38656

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38656.rst

V-38657: The system must use SMB client signing for connecting to samba servers using mount.cifs.
-------------------------------------------------------------------------------------------------

Packet signing can prevent man-in-the-middle attacks which modify SMB packets
in transit.

Details: `V-38657 in STIG Viewer`_.

.. _V-38657 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38657

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38657.rst

V-38437: Automated file system mounting tools must not be enabled unless needed.
--------------------------------------------------------------------------------

All filesystems that are required for the successful operation of the system
should be explicitly listed in "/etc/fstab" by an administrator. New
filesystems should not be arbitrarily introduced via the automounter.  The
"autofs" daemon mounts and unmounts filesystems, such as user home directories
shared via NFS, on demand. In addition, autofs can be used to handle removable
media, and the default configuration provides the cdrom device as "/misc/cd".
However, this method of providing access to removable media is not common, so
autofs can almost always be disabled if NFS is not in use. Even if NFS is
required, it is almost always possible to configure filesystem mounts
statically by editing "/etc/fstab" rather than relying on the automounter.

Details: `V-38437 in STIG Viewer`_.

.. _V-38437 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38437

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38437.rst

V-51379: All device files must be monitored by the system Linux Security Module.
--------------------------------------------------------------------------------

If a device file carries the SELinux type "unlabeled_t", then SELinux cannot
properly restrict access to the device file.

Details: `V-51379 in STIG Viewer`_.

.. _V-51379 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-51379

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-51379.rst

V-38527: The audit system must be configured to audit all attempts to alter system time through clock_settime.
--------------------------------------------------------------------------------------------------------------

Arbitrary changes to the system time can be used to obfuscate nefarious
activities in log files, as well as to confuse network services that are
highly dependent upon an accurate system time (such as sshd). All changes to
the system time should be audited.

Details: `V-38527 in STIG Viewer`_.

.. _V-38527 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38527

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38527.rst

V-38525: The audit system must be configured to audit all attempts to alter system time through stime.
------------------------------------------------------------------------------------------------------

Arbitrary changes to the system time can be used to obfuscate nefarious
activities in log files, as well as to confuse network services that are
highly dependent upon an accurate system time (such as sshd). All changes to
the system time should be audited.

Details: `V-38525 in STIG Viewer`_.

.. _V-38525 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38525

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38525.rst

V-38522: The audit system must be configured to audit all attempts to alter system time through settimeofday.
-------------------------------------------------------------------------------------------------------------

Arbitrary changes to the system time can be used to obfuscate nefarious
activities in log files, as well as to confuse network services that are
highly dependent upon an accurate system time (such as sshd). All changes to
the system time should be audited.

Details: `V-38522 in STIG Viewer`_.

.. _V-38522 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38522

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38522.rst

V-38487: The system package management tool must cryptographically verify the authenticity of all software packages during installation.
----------------------------------------------------------------------------------------------------------------------------------------

Ensuring all packages' cryptographic signatures are valid prior to
installation ensures the provenance of the software and protects against
malicious tampering.

Details: `V-38487 in STIG Viewer`_.

.. _V-38487 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38487

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38487.rst

V-38480: Users must be warned 7 days in advance of password expiration.
-----------------------------------------------------------------------

Setting the password warning age enables users to make the change at a
practical time.

Details: `V-38480 in STIG Viewer`_.

.. _V-38480 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38480

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38480.rst

V-38528: The system must log Martian packets.
---------------------------------------------

The presence of "martian" packets (which have impossible addresses) as well as
spoofed packets, source-routed packets, and redirects could be a sign of
nefarious network activity. Logging these packets enables this activity to be
detected.

Details: `V-38528 in STIG Viewer`_.

.. _V-38528 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38528

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38528.rst

V-38661: The operating system must protect the confidentiality and integrity of data at rest. 
----------------------------------------------------------------------------------------------

The risk of a system's physical compromise, particularly mobile systems such
as laptops, places its data at risk of compromise. Encrypting this data
mitigates the risk of its loss if the system is lost.

Details: `V-38661 in STIG Viewer`_.

.. _V-38661 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38661

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38661.rst

V-38662: The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of data at rest unless otherwise protected by alternative physical measures.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The risk of a system's physical compromise, particularly mobile systems such
as laptops, places its data at risk of compromise. Encrypting this data
mitigates the risk of its loss if the system is lost.

Details: `V-38662 in STIG Viewer`_.

.. _V-38662 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38662

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38662.rst

V-38669: The postfix service must be enabled for mail delivery.
---------------------------------------------------------------

Local mail delivery is essential to some system maintenance and notification
tasks.

Details: `V-38669 in STIG Viewer`_.

.. _V-38669 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38669

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38669.rst

V-38467: The system must use a separate file system for the system audit data path.
-----------------------------------------------------------------------------------

Placing "/var/log/audit" in its own partition enables better separation
between audit files and other files, and helps ensure that auditing cannot be
halted due to the partition running out of space.

Details: `V-38467 in STIG Viewer`_.

.. _V-38467 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38467

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38467.rst

V-38463: The system must use a separate file system for /var/log.
-----------------------------------------------------------------

Placing "/var/log" in its own partition enables better separation between log
files and other files in "/var/".

Details: `V-38463 in STIG Viewer`_.

.. _V-38463 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38463

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38463.rst

V-38460: The NFS server must not have the all_squash option enabled.
--------------------------------------------------------------------

The "all_squash" option maps all client requests to a single anonymous uid/gid
on the NFS server, negating the ability to track file access by user ID.

Details: `V-38460 in STIG Viewer`_.

.. _V-38460 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38460

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38460.rst

V-38702: The FTP daemon must be configured for logging or verbose mode.
-----------------------------------------------------------------------

To trace malicious activity facilitated by the FTP service, it must be
configured to ensure that all commands sent to the ftp server are logged using
the verbose vsftpd log format. The default vsftpd log file is
/var/log/vsftpd.log.

Details: `V-38702 in STIG Viewer`_.

.. _V-38702 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38702

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38702.rst

V-38552: The audit system must be configured to audit all discretionary access control permission modifications using fchown.
-----------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38552 in STIG Viewer`_.

.. _V-38552 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38552

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38552.rst

V-38550: The audit system must be configured to audit all discretionary access control permission modifications using fchmodat.
-------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38550 in STIG Viewer`_.

.. _V-38550 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38550

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38550.rst

V-38557: The audit system must be configured to audit all discretionary access control permission modifications using fsetxattr.
--------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38557 in STIG Viewer`_.

.. _V-38557 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38557

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38557.rst

V-38556: The audit system must be configured to audit all discretionary access control permission modifications using fremovexattr.
-----------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38556 in STIG Viewer`_.

.. _V-38556 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38556

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38556.rst

V-38554: The audit system must be configured to audit all discretionary access control permission modifications using fchownat.
-------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38554 in STIG Viewer`_.

.. _V-38554 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38554

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38554.rst

V-38559: The audit system must be configured to audit all discretionary access control permission modifications using lremovexattr.
-----------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38559 in STIG Viewer`_.

.. _V-38559 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38559

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38559.rst

V-38558: The audit system must be configured to audit all discretionary access control permission modifications using lchown.
-----------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38558 in STIG Viewer`_.

.. _V-38558 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38558

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38558.rst

V-38494: The system must prevent the root account from logging in from serial consoles.
---------------------------------------------------------------------------------------

Preventing direct root login to serial port interfaces helps ensure
accountability for actions taken on the systems using the root account.

Details: `V-38494 in STIG Viewer`_.

.. _V-38494 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38494

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38494.rst

V-38672: The netconsole service must be disabled unless required.
-----------------------------------------------------------------

The "netconsole" service is not necessary unless there is a need to debug
kernel panics, which is not common.

Details: `V-38672 in STIG Viewer`_.

.. _V-38672 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38672

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38672.rst

V-38676: The xorg-x11-server-common (X Windows) package must not be installed, unless required.
-----------------------------------------------------------------------------------------------

Unnecessary packages should not be installed to decrease the attack surface of
the system.

Details: `V-38676 in STIG Viewer`_.

.. _V-38676 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38676

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38676.rst

V-38675: Process core dumps must be disabled unless needed.
-----------------------------------------------------------

A core dump includes a memory image taken at the time the operating system
terminates an application. The memory image could contain sensitive data and
is generally useful only for developers trying to debug problems.

Details: `V-38675 in STIG Viewer`_.

.. _V-38675 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38675

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38675.rst

V-38474: The system must allow locking of graphical desktop sessions.
---------------------------------------------------------------------

The ability to lock graphical desktop sessions manually allows users to easily
secure their accounts should they need to depart from their workstations
temporarily.

Details: `V-38474 in STIG Viewer`_.

.. _V-38474 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38474

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38474.rst

V-38471: The system must forward audit records to the syslog service.
---------------------------------------------------------------------

The auditd service does not include the ability to send audit records to a
centralized server for management directly.  It does, however, include an
audit event multiplexor plugin (audispd) to pass audit records to the local
syslog server.

Details: `V-38471 in STIG Viewer`_.

.. _V-38471 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38471

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38471.rst

V-38473: The system must use a separate file system for user home directories.
------------------------------------------------------------------------------

Ensuring that "/home" is mounted on its own partition enables the setting of
more restrictive mount options, and also helps ensure that users cannot
trivially fill partitions used for log or audit data storage.

Details: `V-38473 in STIG Viewer`_.

.. _V-38473 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38473

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38473.rst

V-38536: The operating system must automatically audit account disabling actions.
---------------------------------------------------------------------------------

In addition to auditing new user and group accounts, these watches will alert
the system administrator(s) to any modifications. Any unexpected users,
groups, or modifications should be investigated for legitimacy.

Details: `V-38536 in STIG Viewer`_.

.. _V-38536 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38536

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38536.rst

V-38478: The Red Hat Network Service (rhnsd) service must not be running, unless using RHN or an RHN Satellite.
---------------------------------------------------------------------------------------------------------------

Although systems management and patching is extremely important to system
security, management by a system outside the enterprise enclave is not
desirable for some environments. However, if the system is being managed by
RHN or RHN Satellite Server the "rhnsd" daemon can remain on.

Details: `V-38478 in STIG Viewer`_.

.. _V-38478 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38478

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38478.rst

V-38540: The audit system must be configured to audit modifications to the systems network configuration.
---------------------------------------------------------------------------------------------------------

The network environment should not be modified by anything other than
administrator action. Any change to network parameters should be audited.

Details: `V-38540 in STIG Viewer`_.

.. _V-38540 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38540

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38540.rst

V-38541: The audit system must be configured to audit modifications to the systems Mandatory Access Control (MAC) configuration (SELinux).
------------------------------------------------------------------------------------------------------------------------------------------

The system's mandatory access policy (SELinux) should not be arbitrarily
changed by anything other than administrator action. All changes to MAC policy
should be audited.

Details: `V-38541 in STIG Viewer`_.

.. _V-38541 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38541

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38541.rst

V-38543: The audit system must be configured to audit all discretionary access control permission modifications using chmod.
----------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38543 in STIG Viewer`_.

.. _V-38543 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38543

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38543.rst

V-38547: The audit system must be configured to audit all discretionary access control permission modifications using fchmod.
-----------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38547 in STIG Viewer`_.

.. _V-38547 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38547

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38547.rst

V-38482: The system must require passwords to contain at least one numeric character.
-------------------------------------------------------------------------------------

Requiring digits makes password guessing attacks more difficult by ensuring a
larger search space.

Details: `V-38482 in STIG Viewer`_.

.. _V-38482 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38482

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38482.rst

V-38454: The system package management tool must verify ownership on all files and directories associated with packages.
------------------------------------------------------------------------------------------------------------------------

Ownership of system binaries and configuration files that is incorrect could
allow an unauthorized user to gain privileges that they should not have. The
ownership set by the vendor should be maintained. Any deviations from this
baseline should be investigated.

Details: `V-38454 in STIG Viewer`_.

.. _V-38454 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38454

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38454.rst

V-38687: The system must provide VPN connectivity for communications over untrusted networks.
---------------------------------------------------------------------------------------------

Providing the ability for remote users or systems to initiate a secure VPN
connection protects information when it is transmitted over a wide area
network.

Details: `V-38687 in STIG Viewer`_.

.. _V-38687 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38687

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38687.rst

V-38685: Temporary accounts must be provisioned with an expiration date.
------------------------------------------------------------------------

When temporary accounts are created, there is a risk they may remain in place
and active after the need for them no longer exists. Account expiration
greatly reduces the risk of accounts being misused or hijacked.

Details: `V-38685 in STIG Viewer`_.

.. _V-38685 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38685

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38685.rst

V-38684: The system must limit users to 10 simultaneous system logins, or a site-defined number, in accordance with operational requirements.
---------------------------------------------------------------------------------------------------------------------------------------------

Limiting simultaneous user logins can insulate the system from denial of
service problems caused by excessive logins. Automated login processes
operating improperly or maliciously may result in an exceptional number of
simultaneous login sessions.

Details: `V-38684 in STIG Viewer`_.

.. _V-38684 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38684

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38684.rst

V-38683: All accounts on the system must have unique user or account names
--------------------------------------------------------------------------

Unique usernames allow for accountability on the system.

Details: `V-38683 in STIG Viewer`_.

.. _V-38683 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38683

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38683.rst

V-38681: All GIDs referenced in /etc/passwd must be defined in /etc/group
-------------------------------------------------------------------------

Inconsistency in GIDs between /etc/passwd and /etc/group could lead to a user
having unintended rights.

Details: `V-38681 in STIG Viewer`_.

.. _V-38681 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38681

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38681.rst

V-38530: The audit system must be configured to audit all attempts to alter system time through /etc/localtime.
---------------------------------------------------------------------------------------------------------------

Arbitrary changes to the system time can be used to obfuscate nefarious
activities in log files, as well as to confuse network services that are
highly dependent upon an accurate system time (such as sshd). All changes to
the system time should be audited.

Details: `V-38530 in STIG Viewer`_.

.. _V-38530 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38530

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38530.rst

V-38578: The audit system must be configured to audit changes to the /etc/sudoers file.
---------------------------------------------------------------------------------------

The actions taken by system administrators should be audited to keep a record
of what was executed on the system, as well as, for accountability purposes.

Details: `V-38578 in STIG Viewer`_.

.. _V-38578 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38578

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38578.rst

V-38575: The audit system must be configured to audit user deletions of files and programs.
-------------------------------------------------------------------------------------------

Auditing file deletions will create an audit trail for files that are removed
from the system. The audit trail could aid in system troubleshooting, as well
as detecting malicious processes that attempt to delete log files to conceal
their presence.

Details: `V-38575 in STIG Viewer`_.

.. _V-38575 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38575

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38575.rst

V-38571: The system must require passwords to contain at least one lowercase alphabetic character.
--------------------------------------------------------------------------------------------------

Requiring a minimum number of lowercase characters makes password guessing
attacks more difficult by ensuring a larger search space.

Details: `V-38571 in STIG Viewer`_.

.. _V-38571 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38571

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38571.rst

V-38572: The system must require at least four characters be changed between the old and new passwords during a password change.
--------------------------------------------------------------------------------------------------------------------------------

Requiring a minimum number of different characters during password changes
ensures that newly changed passwords should not resemble previously
compromised ones. Note that passwords which are changed on compromised systems
will still be compromised, however.

Details: `V-38572 in STIG Viewer`_.

.. _V-38572 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38572

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38572.rst

V-38699: All public directories must be owned by a system account.
------------------------------------------------------------------

Allowing a user account to own a world-writable directory is undesirable
because it allows the owner of that directory to remove or replace any files
that may be placed in the directory by other users.

Details: `V-38699 in STIG Viewer`_.

.. _V-38699 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38699

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38699.rst

V-38516: The Reliable Datagram Sockets (RDS) protocol must be disabled unless required.
---------------------------------------------------------------------------------------

Disabling RDS protects the system against exploitation of any flaws in its
implementation.

Details: `V-38516 in STIG Viewer`_.

.. _V-38516 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38516

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38516.rst

V-38690: Emergency accounts must be provisioned with an expiration date.

-------------------------------------------------------------------------

When emergency accounts are created, there is a risk they may remain in place
and active after the need for them no longer exists. Account expiration
greatly reduces the risk of accounts being misused or hijacked.

Details: `V-38690 in STIG Viewer`_.

.. _V-38690 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38690

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38690.rst

V-38693: The system must require passwords to contain no more than three consecutive repeating characters.
----------------------------------------------------------------------------------------------------------

Passwords with excessive repeating characters may be more vulnerable to
password-guessing attacks.

Details: `V-38693 in STIG Viewer`_.

.. _V-38693 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38693

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38693.rst

V-38590: The system must allow locking of the console screen in text mode.
--------------------------------------------------------------------------

Installing "screen" ensures a console locking capability is available for
users who may need to suspend console logins.

Details: `V-38590 in STIG Viewer`_.

.. _V-38590 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38590

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38590.rst

V-38456: The system must use a separate file system for /var.
-------------------------------------------------------------

Ensuring that "/var" is mounted on its own partition enables the setting of
more restrictive mount options. This helps protect system services such as
daemons or other programs which use it. It is not uncommon for the "/var"
directory to contain world-writable directories, installed by other software
packages.

Details: `V-38456 in STIG Viewer`_.

.. _V-38456 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38456

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38456.rst

V-38455: The system must use a separate file system for /tmp.
-------------------------------------------------------------

The "/tmp" partition is used as temporary storage by many programs. Placing
"/tmp" in its own partition enables the setting of more restrictive mount
options, which can help protect programs which use it.

Details: `V-38455 in STIG Viewer`_.

.. _V-38455 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38455

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38455.rst

V-38618: The avahi service must be disabled.
--------------------------------------------

Because the Avahi daemon service keeps an open network port, it is subject to
network attacks. Its functionality is convenient but is only appropriate if
the local network can be trusted.

Details: `V-38618 in STIG Viewer`_.

.. _V-38618 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38618

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38618.rst

V-38570: The system must require passwords to contain at least one special character.
-------------------------------------------------------------------------------------

Requiring a minimum number of special characters makes password guessing
attacks more difficult by ensuring a larger search space.

Details: `V-38570 in STIG Viewer`_.

.. _V-38570 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38570

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38570.rst

V-38568: The audit system must be configured to audit successful file system mounts.
------------------------------------------------------------------------------------

The unauthorized exportation of data to external media could result in an
information leak where classified information, Privacy Act information, and
intellectual property could be lost. An audit trail should be created each
time a filesystem is mounted to help identify and guard against information
loss.

Details: `V-38568 in STIG Viewer`_.

.. _V-38568 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38568

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38568.rst

V-38569: The system must require passwords to contain at least one uppercase alphabetic character.
--------------------------------------------------------------------------------------------------

Requiring a minimum number of uppercase characters makes password guessing
attacks more difficult by ensuring a larger search space.

Details: `V-38569 in STIG Viewer`_.

.. _V-38569 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38569

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38569.rst

V-38561: The audit system must be configured to audit all discretionary access control permission modifications using lsetxattr.
--------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38561 in STIG Viewer`_.

.. _V-38561 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38561

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38561.rst

V-38566: The audit system must be configured to audit failed attempts to access files and programs.
---------------------------------------------------------------------------------------------------

Unsuccessful attempts to access files could be an indicator of malicious
activity on a system. Auditing these events could serve as evidence of
potential system compromise.

Details: `V-38566 in STIG Viewer`_.

.. _V-38566 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38566

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38566.rst

V-38567: The audit system must be configured to audit all use of setuid and setgid programs.
--------------------------------------------------------------------------------------------

Privileged programs are subject to escalation-of-privilege attacks, which
attempt to subvert their normal role of providing some necessary but limited
capability. As such, motivation exists to monitor these programs for unusual
activity.

Details: `V-38567 in STIG Viewer`_.

.. _V-38567 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38567

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38567.rst

V-38565: The audit system must be configured to audit all discretionary access control permission modifications using setxattr.
-------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38565 in STIG Viewer`_.

.. _V-38565 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38565

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38565.rst

V-38537: The system must ignore ICMPv4 bogus error responses.
-------------------------------------------------------------

Ignoring bogus ICMP error responses reduces log size, although some activity
would not be logged.

Details: `V-38537 in STIG Viewer`_.

.. _V-38537 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38537

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38537.rst

V-38624: System logs must be rotated daily.
-------------------------------------------

Log files that are not properly rotated run the risk of growing so large that
they fill up the /var/log partition. Valuable logging information could be
lost if the /var/log partition becomes full.

Details: `V-38624 in STIG Viewer`_.

.. _V-38624 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38624

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38624.rst

V-38627: The openldap-servers package must not be installed unless required.
----------------------------------------------------------------------------

Unnecessary packages should not be installed to decrease the attack surface of
the system.

Details: `V-38627 in STIG Viewer`_.

.. _V-38627 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38627

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38627.rst

V-38584: The xinetd service must be uninstalled if no network services utilizing it are enabled.
------------------------------------------------------------------------------------------------

Removing the "xinetd" package decreases the risk of the xinetd service's
accidental (or intentional) activation.

Details: `V-38584 in STIG Viewer`_.

.. _V-38584 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38584

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38584.rst

V-38694: The operating system must manage information system identifiers for users and devices by disabling the user identifier after an organization defined time period of inactivity.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Disabling inactive accounts ensures that accounts which may not have been
responsibly removed are not available to attackers who may have compromised
their credentials.

Details: `V-38694 in STIG Viewer`_.

.. _V-38694 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38694

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38694.rst

V-38545: The audit system must be configured to audit all discretionary access control permission modifications using chown.
----------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38545 in STIG Viewer`_.

.. _V-38545 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38545

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38545.rst

V-38538: The operating system must automatically audit account termination.
---------------------------------------------------------------------------

In addition to auditing new user and group accounts, these watches will alert
the system administrator(s) to any modifications. Any unexpected users,
groups, or modifications should be investigated for legitimacy.

Details: `V-38538 in STIG Viewer`_.

.. _V-38538 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38538

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38538.rst

V-38697: The sticky bit must be set on all public directories.
--------------------------------------------------------------

Failing to set the sticky bit on public directories allows unauthorized users
to delete files in the directory structure.   The only authorized public
directories are those temporary directories supplied with the system, or those
designed to be temporary file repositories. The setting is normally reserved
for directories used by the system, and by users for temporary file storage -
such as /tmp - and for directories requiring global read/write access.

Details: `V-38697 in STIG Viewer`_.

.. _V-38697 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38697

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38697.rst

V-38531: The operating system must automatically audit account creation.
------------------------------------------------------------------------

In addition to auditing new user and group accounts, these watches will alert
the system administrator(s) to any modifications. Any unexpected users,
groups, or modifications should be investigated for legitimacy.

Details: `V-38531 in STIG Viewer`_.

.. _V-38531 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38531

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38531.rst

V-38533: The system must ignore ICMPv4 redirect messages by default.
--------------------------------------------------------------------

This feature of the IPv4 protocol has few legitimate uses. It should be
disabled unless it is absolutely required.

Details: `V-38533 in STIG Viewer`_.

.. _V-38533 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38533

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38533.rst

V-38535: The system must not respond to ICMPv4 sent to a broadcast address.
---------------------------------------------------------------------------

Ignoring ICMP echo requests (pings) sent to broadcast or multicast addresses
makes the system slightly more difficult to enumerate on the network.

Details: `V-38535 in STIG Viewer`_.

.. _V-38535 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38535

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38535.rst

V-38534: The operating system must automatically audit account modification.
----------------------------------------------------------------------------

In addition to auditing new user and group accounts, these watches will alert
the system administrator(s) to any modifications. Any unexpected users,
groups, or modifications should be investigated for legitimacy.

Details: `V-38534 in STIG Viewer`_.

.. _V-38534 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38534

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38534.rst

V-38655: The noexec option must be added to removable media partitions.
-----------------------------------------------------------------------

Allowing users to execute binaries from removable media such as USB keys
exposes the system to potential compromise.

Details: `V-38655 in STIG Viewer`_.

.. _V-38655 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38655

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38655.rst

V-38438: Auditing must be enabled at boot by setting a kernel parameter.
------------------------------------------------------------------------

Each process on the system carries an "auditable" flag which indicates whether
its activities can be audited. Although "auditd" takes care of enabling this
for all processes which launch after it does, adding the kernel argument
ensures it is set for every process during boot.

Details: `V-38438 in STIG Viewer`_.

.. _V-38438 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38438

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38438.rst

V-38692: Accounts must be locked upon 35 days of inactivity.
------------------------------------------------------------

Disabling inactive accounts ensures that accounts which may not have been
responsibly removed are not available to attackers who may have compromised
their credentials.

Details: `V-38692 in STIG Viewer`_.

.. _V-38692 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38692

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38692.rst

V-38639: The system must display a publicly-viewable pattern during a graphical desktop environment session lock.
-----------------------------------------------------------------------------------------------------------------

Setting the screensaver mode to blank-only conceals the contents of the
display from passersby.

Details: `V-38639 in STIG Viewer`_.

.. _V-38639 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38639

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38639.rst

V-38635: The audit system must be configured to audit all attempts to alter system time through adjtimex.
---------------------------------------------------------------------------------------------------------

Arbitrary changes to the system time can be used to obfuscate nefarious
activities in log files, as well as to confuse network services that are
highly dependent upon an accurate system time (such as sshd). All changes to
the system time should be audited.

Details: `V-38635 in STIG Viewer`_.

.. _V-38635 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38635

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38635.rst

V-38616: The SSH daemon must not permit user environment settings.
------------------------------------------------------------------

SSH environment options potentially allow users to bypass access restriction
in some configurations.

Details: `V-38616 in STIG Viewer`_.

.. _V-38616 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38616

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38616.rst

V-38563: The audit system must be configured to audit all discretionary access control permission modifications using removexattr.
----------------------------------------------------------------------------------------------------------------------------------

The changing of file permissions could indicate that a user is attempting to
gain access to information that would otherwise be disallowed. Auditing DAC
modifications can facilitate the identification of patterns of abuse among
both authorized and unauthorized users.

Details: `V-38563 in STIG Viewer`_.

.. _V-38563 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38563

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38563.rst

V-38610: The SSH daemon must set a timeout count on idle sessions.
------------------------------------------------------------------

This ensures a user login will be terminated as soon as the
"ClientAliveCountMax" is reached.

Details: `V-38610 in STIG Viewer`_.

.. _V-38610 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38610

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38610.rst

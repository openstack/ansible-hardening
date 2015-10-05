.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Category 3 (High) configurations
================================

.. contents::
   :depth: 2


V-38653: The snmpd service must not use a default password.
-----------------------------------------------------------

Presence of the default SNMP password enables querying of different system
aspects and could result in unauthorized knowledge of the system.

Details: `V-38653 in STIG Viewer`_.

.. _V-38653 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38653

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38653.rst

V-38666: The system must use and update a DoD-approved virus scan program.
--------------------------------------------------------------------------

Virus scanning software can be used to detect if a system has been compromised
by computer viruses, as well as to limit their spread to other systems.

Details: `V-38666 in STIG Viewer`_.

.. _V-38666 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38666

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38666.rst

V-38668: The x86 Ctrl-Alt-Delete key sequence must be disabled.
---------------------------------------------------------------

A locally logged-in user who presses Ctrl-Alt-Delete, when at the console, can
reboot the system. If accidentally pressed, as could happen in the case of
mixed OS environment, this can create the risk of short-term loss of
availability of systems due to unintentional reboot. In the GNOME graphical
environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is
reduced because the user will be prompted before any action is taken.

Details: `V-38668 in STIG Viewer`_.

.. _V-38668 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38668

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38668.rst

V-38462: The RPM package management tool must cryptographically verify the authenticity of all software packages during installation.
-------------------------------------------------------------------------------------------------------------------------------------

Ensuring all packages' cryptographic signatures are valid prior to
installation ensures the provenance of the software and protects against
malicious tampering.

Details: `V-38462 in STIG Viewer`_.

.. _V-38462 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38462

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38462.rst

V-38497: The system must not have accounts configured with blank or null passwords.
-----------------------------------------------------------------------------------

If an account has an empty password, anyone could log in and run commands with
the privileges of that account. Accounts with empty passwords should never be
used in operational environments.

Details: `V-38497 in STIG Viewer`_.

.. _V-38497 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38497

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38497.rst

V-38677: The NFS server must not have the insecure file locking option enabled.
-------------------------------------------------------------------------------

Allowing insecure file locking could allow for sensitive data to be viewed or
edited by an unauthorized user.

Details: `V-38677 in STIG Viewer`_.

.. _V-38677 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38677

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38677.rst

V-38476: Vendor-provided cryptographic certificates must be installed to verify the integrity of system software.
-----------------------------------------------------------------------------------------------------------------

The Red Hat GPG keys are necessary to cryptographically verify packages are
from Red Hat.

Details: `V-38476 in STIG Viewer`_.

.. _V-38476 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38476

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38476.rst

V-38491: There must be no .rhosts or hosts.equiv files on the system.
---------------------------------------------------------------------

Trust files are convenient, but when used in conjunction with the R-services,
they can allow unauthenticated access to a system.

Details: `V-38491 in STIG Viewer`_.

.. _V-38491 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38491

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38491.rst

V-38607: The SSH daemon must be configured to use only the SSHv2 protocol.
--------------------------------------------------------------------------

SSH protocol version 1 suffers from design flaws that result in security
vulnerabilities and should not be used.

Details: `V-38607 in STIG Viewer`_.

.. _V-38607 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38607

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38607.rst

V-38602: The rlogind service must not be running.
-------------------------------------------------

The rlogin service uses unencrypted network communications, which means that
data from the login session, including passwords and all other information
transmitted during the session, can be stolen by eavesdroppers on the network.

Details: `V-38602 in STIG Viewer`_.

.. _V-38602 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38602

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38602.rst

V-38594: The rshd service must not be running.
----------------------------------------------

The rsh service uses unencrypted network communications, which means that data
from the login session, including passwords and all other information
transmitted during the session, can be stolen by eavesdroppers on the network.

Details: `V-38594 in STIG Viewer`_.

.. _V-38594 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38594

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38594.rst

V-38591: The rsh-server package must not be installed.
------------------------------------------------------

The "rsh-server" package provides several obsolete and insecure network
services. Removing it decreases the risk of those services' accidental (or
intentional) activation.

Details: `V-38591 in STIG Viewer`_.

.. _V-38591 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38591

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38591.rst

V-38598: The rexecd service must not be running.
------------------------------------------------

The rexec service uses unencrypted network communications, which means that
data from the login session, including passwords and all other information
transmitted during the session, can be stolen by eavesdroppers on the network.

Details: `V-38598 in STIG Viewer`_.

.. _V-38598 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38598

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38598.rst

V-38587: The telnet-server package must not be installed.
---------------------------------------------------------

Removing the "telnet-server" package decreases the risk of the unencrypted
telnet service's accidental (or intentional) activation.  Mitigation:  If the
telnet-server package is configured to only allow encrypted sessions, such as
with Kerberos or the use of encrypted network tunnels, the risk of exposing
sensitive information is mitigated.

Details: `V-38587 in STIG Viewer`_.

.. _V-38587 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38587

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38587.rst

V-38589: The telnet daemon must not be running.
-----------------------------------------------

The telnet protocol uses unencrypted network communication, which means that
data from the login session, including passwords and all other information
transmitted during the session, can be stolen by eavesdroppers on the network.
The telnet protocol is also subject to man-in-the-middle attacks.  Mitigation:
If an enabled telnet daemon is configured to only allow encrypted sessions,
such as with Kerberos or the use of encrypted network tunnels, the risk of
exposing sensitive information is mitigated.

Details: `V-38589 in STIG Viewer`_.

.. _V-38589 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38589

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38589.rst

V-38701: The TFTP daemon must operate in secure mode which provides access only to a single directory on the host file system.
------------------------------------------------------------------------------------------------------------------------------

Using the "-s" option causes the TFTP service to only serve files from the
given directory. Serving files from an intentionally specified directory
reduces the risk of sharing files which should remain private.

Details: `V-38701 in STIG Viewer`_.

.. _V-38701 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38701

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38701.rst

V-38614: The SSH daemon must not allow authentication using an empty password.
------------------------------------------------------------------------------

Configuring this setting for the SSH daemon provides additional assurance that
remote login via SSH will require a password, even in the event of
misconfiguration elsewhere.

Details: `V-38614 in STIG Viewer`_.

.. _V-38614 in STIG Viewer: https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2015-05-26/finding/V-38614

Developer Notes
~~~~~~~~~~~~~~~
.. include:: developer-notes/V-38614.rst

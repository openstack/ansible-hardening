sshd - SSH daemon
=================

The SSH daemon, ``sshd``, provides secure, encrypted access to Linux servers.

Overview
--------

The STIG has several requirements for ssh server configuration and these
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

.. include:: auto_sshd.rst

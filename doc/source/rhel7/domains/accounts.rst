accounts - User account security controls
=========================================

Security controls for user accounts on Linux systems are a crucial barrier to
prevent unauthorized access.

Overview
--------

Many of the STIG requirements for user account controls are already included in
many Linux distributions or they can be applied without disruptions. However,
some requirements can cause problems with user authentication without
coordination.

Deployers should consider an authentication solution that uses centralized
authentication, such as LDAP, Active Directory, or Kerberos, for the best
security posture.

.. include:: auto_accounts.rst

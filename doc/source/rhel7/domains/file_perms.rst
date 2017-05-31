file_perms - Filesystem permissions
===================================

One of the first layers of defense against attacks on a Linux system is
Discretionary Access Control (DAC), which is managed through filesystem
permissions.

Overview
--------

Some of the STIG requirements for file permissions could cause disruptions on
production systems if the permissions were adjusted to meet the needs of a
particular application. These configurations are applied on an opt-in basis.
Deployers must verify that these changes work well with their systems before
applying the changes.

.. include:: auto_file_perms.rst

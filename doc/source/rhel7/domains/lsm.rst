lsm - Linux Security Modules
============================

Linux Security Modules, such as AppArmor and SELinux, provide an extra level of
security controls on a Linux system. They provide Mandatory Access Control
(MAC) that checks system activities against security policy. These policies
apply to all users, including root.

Overview
--------

The STIG requires that SELinux is in enforcing mode to provide additional
security against attacks. The security role will enable SELinux on CentOS
systems and enable AppArmor on Ubuntu and Debian systems.

.. include:: auto_lsm.rst

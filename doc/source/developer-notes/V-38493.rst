Ubuntu 14.04, Ubuntu 16.04, and CentOS 7 set the mode of ``/var/log/audit/`` to
``0750`` by default. The Ansible task for this requirement ensures that the
mode is ``0750`` (which is more strict than the STIG requirement).

When auditd notices that free disk space on its logging partition is low, it
will trigger the ``security_space_left_action``. The threshold of remaining
disk space is configured by ``security_space_left`` in
``/etc/audit/auditd.conf``.

By default, Ubuntu 14.04, Ubuntu 16.04 and CentOS 7 set this value to 75
megabytes. The STIG doesn't set a specific requirement for the exact size, so
the Ansible task will ensure that the default of 75 megabytes is set.

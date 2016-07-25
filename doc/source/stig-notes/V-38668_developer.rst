In Ubuntu 14.04, the Ansible tasks disable the control-alt-delete keyboard
sequence via a configuration in ``/etc/init/control-alt-delete.conf``.  A
reboot is recommended to apply the change.

Linux distributions that use systemd, such as Ubuntu 16.04 and CentOS 7,
disable the key sequence by masking the ``ctrl-alt-del.target`` with
``systemctl``.

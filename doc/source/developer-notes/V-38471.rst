An Ansible task will adjust ``active`` from `no` to `yes` in
``/etc/audisp/plugins.d/syslog.conf`` so that auditd records are forwarded to
syslog automatically. The auditd daemon will be restarted if the configuration
file is changed.

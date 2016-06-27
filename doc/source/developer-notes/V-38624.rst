The STIG requires that system logs are rotate daily, but the check only
involves verifying that logrotate is installed and activated by cron. The
openstack-ansible project already configures weekly log rotation with
compression. For high-traffic logging environments, changing the frequency
to weekly in ``/etc/logrotate.conf`` may help.

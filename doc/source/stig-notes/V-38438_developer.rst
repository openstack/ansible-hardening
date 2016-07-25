**Exception**

Adjusting the bootloader configuration can cause issues with reboots and this
work is left up to the deployer.  Enabling auditing at boot time is helpful,
but the risk may not be worth the change in most environments.

The ``auditd`` process starts very early during the boot process to catch
events already, and this should be sufficient for most environments.

Ubuntu and CentOS set the current audit log (the one that is actively being
written to) to ``0600`` so that only the root user can read and write to it.
The older, rotated logs are set to ``0400`` since they should not receive
any more writes.

The STIG requirement states that log files must have mode ``0640`` or less. The
security role will remove any permissions that are not allowed by the STIG
(``u-x,g-wx,o-rwx``).

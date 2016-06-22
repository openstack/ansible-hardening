**Exception**

Although Ubuntu provides the ``debsums`` command for checking the contents of
files installed from packages, it cannot perform a detailed level of checking
sufficient to meet the STIG requirement. Some packages are not shipped with MD5
checksums for all files. Deployers are encouraged to use ``debsums -c``
regularly to check for alterations in as many packages as possible.

Ubuntu does not currently have a capability to check file permissions,
ownership, or group ownership against the permissions that were originally set
when the package was installed.

In CentOS, the ``rpm`` command can verify package contents, ownership, group
ownership, and permissions after the package has been installed. However, many
configuration files are changed by the security role and this will cause the
verification to fail.

Deployers should utilize the monitoring capabilities of the ``aide`` package
(which is installed by other Ansible tasks in this role) to determine which
configuration files, libraries or binaries may have been changed.

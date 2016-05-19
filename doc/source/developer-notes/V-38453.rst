**Exception for Ubuntu**

Verifying ownership and permissions of installed packages isn't possible in the
current version of ``dpkg`` as it is with ``rpm``. This security configuration
is skipped for Ubuntu. For CentOS, this check is done as part of V-38637.

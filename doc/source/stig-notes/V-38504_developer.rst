Ubuntu 14.04 and Ubuntu 16.04 set the mode of ``/etc/shadow`` to ``0640``, but
CentOS 7 sets it to ``000``. The STIG requires the mode to be ``000`` and the
Ansible tasks in the security role ensure that the mode meets the requirement.

**Special note for Ubuntu:** This change doesn't affect how the system operates
since root is the only user that should be able to read from and write to
``/etc/shadow``. Allowing users to read the file could open up the system to
attacks since the password hashes can be dumped and brute forced.

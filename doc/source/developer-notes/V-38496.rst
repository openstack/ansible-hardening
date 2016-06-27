**Exception**

The Ansible tasks will check for default system accounts (other than root)
that are not locked. The tasks won't take any action, however, because
any action could cause authorized users to be unable to access the system.
However, if any unlocked default system accounts are found, the playbook will
fail with an error message until the user accounts are locked.

Deployers who intentionally want to skip this step should use
``--skip-tags V-38496`` to avoid a playbook failure on this check.

Deployers are urged to audit the accounts on their systems and lock any users
that don't need to log in via consoles or via ssh.

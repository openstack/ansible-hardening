**Opt-in required**

Changing the umask for the bash shell is an opt-in setting. Deployers that
want to set the umask for bash sessions to match the STIG requirement must
set the Ansible variable ``security_umask_bash`` to ``077``.

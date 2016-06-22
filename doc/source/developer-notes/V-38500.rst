The Ansible tasks will search for accounts in ``/etc/passwd`` that have UID 0
that aren't the normal root account. If any matching accounts are found, a
warning is printed to stdout and the Ansible play will fail.

No action is taken on those accounts as that action may disrupt a production
environment.  Deployers are strongly urged to use ``sudo`` for these types of
actions.

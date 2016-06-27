The Ansible task will use the ``pwck`` command to search for non-unique
usernames on the system. If any matching usernames are found, an error
will be printed and the playbook will fail.

**NOTE:** The ``pwck`` command will find other abnormalities on the system,
including users that exist in ``/etc/passwd`` but not in ``/etc/shadow``, and
vice versa. If the playbook fails on this task, try to run this command
on the system as root to find out what caused the failure:

.. code-block:: bash

    pwck -rq

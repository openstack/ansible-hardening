The Ansible tasks will run ``pwck`` to find any groups that are defined in
``/etc/passwd`` but not in ``/etc/group``. This could be a sign of an
accidental misconfiguration or a more serious security problem. If the command
returns output about missing groups, the playbook will fail.

To see the exact problems on the system when the playbook fails, run this
command as root:

.. code-block:: bash

    pwck -r | grep 'no group'

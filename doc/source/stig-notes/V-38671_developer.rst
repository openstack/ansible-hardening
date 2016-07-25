The security role will remove the sendmail package if it exists on the system.
To opt-out of this change, adjust the following Ansible variable to ``no``:

.. code-block:: yaml

    security_remove_sendmail: no

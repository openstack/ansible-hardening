The Ansible tasks in the security role will disable the atd service and stop
the service immediately. To opt-out of this change, set the following Ansible
variable:

.. code-block:: yaml

    security_disable_atd: no

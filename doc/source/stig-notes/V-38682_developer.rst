The Ansible task will disable the bluetooth kernel modules to meet the STIG
requirements. To opt-out of this change, adjust the following Ansible variable
to ``no``:

.. code-block:: yaml

    disable_bluetooth_module: no

**NOTE:** The module will be disabled on the next system reboot.

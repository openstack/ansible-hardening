The STIG recommends setting ``ClientAliveCountMax`` to ensure that ssh
connections will close after reaching the ``ClientAliveInterval`` one
time. To change this setting, simply change this configuration option
to something other than ``0``:

.. code-block:: yaml

    security_ssh_client_alive_count_max: 0

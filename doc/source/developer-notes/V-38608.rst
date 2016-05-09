The ``ClientAliveInterval`` in the ssh configuration will be set to 15 minutes
as recommended by the STIG.  However, this time is configurable by setting
``security_ssh_client_alive_interval`` to another value, in seconds.

To change to 10 minutes, adjust the configuration item to 600 seconds:

.. code-block:: yaml

    security_ssh_client_alive_interval: 600

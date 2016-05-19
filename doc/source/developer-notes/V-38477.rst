**Configuration required**

The STIG recommends setting a limit of one password change per day. To enable
this configuration, use this Ansible variable:

.. code-block:: yaml

    security_password_minimum_days: 14

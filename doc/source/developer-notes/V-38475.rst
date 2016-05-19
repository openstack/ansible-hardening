**Configuration required**

The STIG recommends passwords to be a minimum of 14 characters in length. To
apply this setting, set the following Ansible variable:

.. code-block:: yaml

    security_password_minimum_length: 14

Deployers are urged to avoid the use of passwords and rely upon SSH keys if
possible.

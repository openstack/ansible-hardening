**Configuration required**

After enabling password age limits in V-38479, be sure to configure
warnings for users so they know when their password is approaching expiration.
STIG's recommendation is seven days prior to the expiration. Use an Ansible
variable to configure the warning:

.. code-block:: yaml

    security_password_warn_age: 7

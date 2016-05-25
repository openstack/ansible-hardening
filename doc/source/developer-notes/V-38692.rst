**Opt-in required**

Deployers must opt-in for this change by setting the following Ansible
variable:

.. code-block:: yaml

    security_inactive_account_lock_days: 35

The STIG requires this to be set to 35 days at a maximum. The Ansible tasks
will not make any changes to ``/etc/default/useradd`` unless
``security_inactive_account_lock_days`` is set.

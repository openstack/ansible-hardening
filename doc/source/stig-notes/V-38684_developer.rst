**Opt-in required**

Ubuntu does not set a limit on the maximum number of active sessions that
a single user can have at one time. The STIG requires setting a limit of
``10``.

To opt-in for this change, set the following Ansible variable:

.. code-block:: yaml

    security_max_simultaneous_logins: 10

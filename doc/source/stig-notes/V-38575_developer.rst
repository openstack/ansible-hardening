**Exception**

The audit rules for monitoring deleted files can cause very high system load
during OpenStack-Ansible deployments and during package updates using apt.
It's recommended that deployers keep these rules disabled unless they're
explicitly required.

These rules are disabled by default, but they can be enabled by setting the
following Ansible variable:

.. code-block:: yaml

    security_audit_deletions: yes

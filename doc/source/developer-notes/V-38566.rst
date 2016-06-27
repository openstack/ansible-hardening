**Exception**

The audit rules for logging failed access attempts can generate significant
amounts of log traffic in some environments. These rules are disabled by
default.

To opt-in for this change and enable audit logging for these events, adjust
the following Ansible variable:

.. code-block:: yaml

    security_auditd_failed_access: yes

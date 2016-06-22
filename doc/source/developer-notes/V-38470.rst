The default configuration for ``security_space_left_action`` is ``SUSPEND``,
which actually only suspends audit logging. Suspending audit logging can lead
to security problems because the system is no longer keeping track of which
syscalls were made.

The security role sets the configuration to  ``SYSLOG`` so that messages are
sent to syslog when the available disk space reaches a low level. If syslog
messages are being sent to remote servers, these log messages should alert an
administrator about the disk being almost full. There are additional options
available, like ``EXEC``, ``SINGLE`` or ``HALT``.

To configure a different ``space_left_action``, set the following
Ansible variable:

.. code-block:: yaml

    security_space_left_action: SYSLOG

For details on available settings and what they do, run ``man auditd.conf``.
Some options can cause the host to go offline until the issue is fixed.
Deployers are urged to **carefully read the auditd documentation** prior to
changing the ``space_left_action`` setting from the default.

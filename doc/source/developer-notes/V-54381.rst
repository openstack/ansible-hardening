**Exception**

The STIG requires that the audit system must switch the entire system into
single-user mode when the space for logging becomes dangerously low.

.. note::

    **This will cause serious service disruptions for any environment and
    should only be enabled for extremely high security environments.**

The ``security_admin_space_left_action`` configuration is set to ``SUSPEND`` by
default, and this will cause logging to be temporarily suspended until disk
space is freed.

For extremely high security environments, this Ansible variable can be
provided to meet the requirements of the STIG:

.. code-block:: yaml

    security_admin_space_left_action: SINGLE

Additional hardening configurations
===================================

Although the Security Technical Implementation Guide (STIG) contains a very
comprehensive set of security configurations, some ansible-hardening
contributors want to add extra security configurations to the role. The
*contrib* portion of the ansible-hardening role is designed to implement those
configurations as an optional set of tasks.

The *contrib* hardening configurations are disabled by default, but they can
be enabled by setting the following Ansible variable:

.. code-block:: yaml

    security_contrib_enabled: yes

The individual tasks are controlled by Ansible variables in
``defaults/main.yml`` that begin with ``security_contrib_``.

Kernel
------

C-00001 - Disable IPv6
~~~~~~~~~~~~~~~~~~~~~~

Some systems do not require IPv6 connectivity and the presence of link local
IPv6 addresses can present an additional attack surface for lateral movement.
Deployers can set the following variable to disable IPv6 on all network
interfaces:

.. code-block:: yaml

    security_contrib_disable_ipv6: yes

.. warning::

    Deployers should test this change in a test environment before applying it
    in a production deployment. Applying this change to a production system
    that relies on IPv6 connectivity will cause unexpected downtime.

**Opt-in required**

Operating system patching policies vary from organization to organization and
are typically established based on business requirements and risk tolerance.

.. note::

    Automatically upgrading packages can provide significant security benefits,
    but they can reduce availability and reliability. Updating packages can
    cause daemons to restart on some systems and they can cause local
    customizations of configuration files to be lost.

    Deployers are **strongly urged** to understand the nature of this change
    and the associated risks prior to enabling automatic upgrades.

Deployers can enable automatic updates by setting
``security_unattended_upgrades`` to ``True``:

.. code-block:: yaml

    security_unattended_upgrades: true

In Ubuntu, the ``unattended-upgrades`` package is installed and enabled. This
will apply updates that are made available to the trusty-security (Ubuntu
14.04) or xenial-security (Ubuntu 16.04) repositories.

In CentOS, the ``yum-cron`` package is installed and configured to
automatically apply updates.

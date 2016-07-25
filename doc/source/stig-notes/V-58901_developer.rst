This STIG requires that ``NOPASSWD`` and ``!authenticate`` are not used within
the sudoers configuration files. Using these directives reduces the security
of the system.

``NOPASSWD`` allows users to run commands as root without providing a password
first. Using ``!authenticate`` with the ``Defaults`` directive will disable
password usage for any users which use ``sudo``.

There are two configuration options for handling these changes. By default,
both of these options are set to ``no``, which means that the sudoers
configuration files will not be altered:

.. code-block:: yaml

    security_sudoers_remove_nopasswd: no
    security_sudoers_remove_authenticate: no

Setting ``security_sudoers_remove_nopasswd`` to ``yes`` will cause the Ansible
tasks to search for any lines containing ``NOPASSWD`` and comment them out of
the configuration. Setting ``security_sudoers_remove_authenticate`` will do the
same actions on lines containing ``!authenticate``. Lines that are already
commented will be left unaltered.

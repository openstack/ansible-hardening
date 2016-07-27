Ubuntu 14.04, Ubuntu 16.04, and CentOS 7 allow accounts with null passwords to
authenticate via PAM by default. This STIG requires that those login attempts
are blocked.

For Ubuntu, the ``nullok_secure`` option will be removed from ``/etc/pam.d
/common-auth``.

For CentOS, the ``nullok`` option will be removed from ``/etc/pam.d/system-
auth``.

The effects of the change are **immediate** and no service restarts are
required.

Deployers can opt-out of this change by adjusting an Ansible variable:

.. code-block:: yaml

    security_pam_remove_nullok: no

Setting the variable to ``yes`` (the default) will cause the Ansible tasks to
remove the ``nullok_secure`` parameter while setting the variable to ``no``
will leave the PAM configuration unchanged.

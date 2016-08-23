The role will add ``audit=1`` to the ``GRUB_CMDLINE_LINUX_DEFAULT`` variable
in the GRUB configuration within ``/etc/default/grub.d/`` and it will also
update the active ``grub.cfg`` so that the change takes effect on the next
boot.

To opt-out of the change, set the following variable:

.. code-block:: yaml

   security_enable_audit_during_boot: no

Deployers may opt-in for the change without automatically updating the active
``grub.cfg`` file by setting the following Ansible variables:

.. code-block:: yaml

   security_enable_audit_during_boot: yes
   security_enable_grub_update: no

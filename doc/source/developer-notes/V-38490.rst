**Exception**

Disabling the ``usb-storage`` module can add extra security, but it's not
necessary on most systems. To disable the ``usb-storage`` module on hosts,
set the following variable to ``yes``:

.. code-block:: yaml

    security_disable_module_usb_storage: yes

**NOTE:** The module will be disabled on the next reboot.

The Ansible tasks will remove the ``xserver-xorg`` package if it is present.

To opt-out of the change, set the following Ansible variable to ``no``:

.. code-block:: yaml

    security_remove_xorg: no

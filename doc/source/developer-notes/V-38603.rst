This packages is named differently depending on the Linux distribution:

* Ubuntu 14.04: ``nis``
* Ubuntu 16.04: ``nis``
* CentOS 7: ``ypserv``

The Ansible tasks will remove the appropriate package if it is installed. To
opt-out of this change, adjust the following configuration variable to ``no``:

.. code-block:: yaml

    security_remove_ypserv: no

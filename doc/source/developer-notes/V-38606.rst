The package containing the tftp daemon has different names depending on the
Linux distribution:

* Ubuntu 14.04: ``tftpd``
* Ubuntu 16.04: ``tftpd``
* CentOS 7: ``tftp-server``

The Ansible tasks will select the appropriate package for the Linux
distribution and remove the package. To opt-out, adjust the following
configuration variable to ``no``:

.. code-block:: yaml

    security_remove_tftp_server: no

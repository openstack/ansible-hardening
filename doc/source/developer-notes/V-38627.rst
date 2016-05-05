The STIG requires that any LDAP server packages on the system are removed.
The Ansible role will remove ``slapd`` from the server if it is present.

To opt-out of this change, set the following Ansible variable to ``no``:

.. code-block:: yaml

   security_remove_ldap_server: no

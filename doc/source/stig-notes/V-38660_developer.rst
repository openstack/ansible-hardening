The Ansible tasks will check to see if the SNMP configuration file is present.
If the file is present, and the file contains configurations for insecure SNMP
protocols, an error will be printed and the playbook will fail.

The task specifically looks for uncommented configuration lines containing:

* ``v1``
* ``v2c``
* ``com2sec``
* ``community``

`Red Hat's guide to SNMP`_ has some example configurations that deployers
can use to enable SNMPv3.

.. _Red Hat's guide to SNMP: https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/sect-System_Monitoring_Tools-Net-SNMP-Configuring.html

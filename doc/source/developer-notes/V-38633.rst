The default setting for ``security_max_log_file`` in Ubuntu 14.04, Ubuntu
16.04, and CentOS 7 matches the STIG requirement of rotating logs when they
reach 6MB. The Ansible task for this STIG requirement ensures that the secure
default is maintained.

Deployers who want to exceed the STIG guideline can increase the size of logs
by adjusting the following Ansible variable:

.. code-block:: yaml

    security_max_log_file: 6

**Exception**

Running a ``find`` command on the system during the playbook run is
time-consuming and will also slow down disk I/O while it runs. Deployers
are urged to review public directories to ensure the sticky bit is
configured.

Further reading: `sticky bit on Wikipedia`_

.. _sticky bit on Wikipedia: https://en.wikipedia.org/wiki/Sticky_bit

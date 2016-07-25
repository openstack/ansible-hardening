The STIG recommends enabling TCP SYN cookies to deal with TCP SYN floods.
Ubuntu 14.04 already enables SYN cookies by default, and this role will ensure
that the default is maintained.

Keep in mind, however, that high-traffic environments may require TCP
SYN cookies to be disabled. Certain load balancers may forward requests in such
a way that web servers may think they're being SYN flooded during peak traffic
events. Putting well-configured hardware network devices in front of OpenStack
environments is always recommended and this may allow some deployers to turn
off SYN cookies within their environment.

Deployers can disable TCP SYN cookies by setting an Ansible variable:

.. code-block:: yaml

    security_sysctl_tcp_syncookies: 0

For more information on TCP SYN cookies and TCP SYN floods, refer to these
links:

* `Wikipedia: SYN flood <https://en.wikipedia.org/wiki/SYN_flood>`_
* `Wikipedia: SYN cookies <https://en.wikipedia.org/wiki/SYN_cookies>`_

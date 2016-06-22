The STIG requires that postfix only listens on the localhost so that it isn't
abused as a mail relay. The Ansible task will adjust the ``inet_interfaces``
line in the Postfix configuration and restart postfix if the line is changed.

Although it's not common, some deployers may need to configure hosts so they
can receive email over the network. In that case, deployers would need to set
the following Ansible variable:

.. code-block:: yaml

    security_postfix_inet_interfaces: all

Note that postfix can have ``inet_interfaces`` set to ``localhost`` and it can
still send email on the network. The ``inet_interfaces`` directive only
controls where postfix **listens** for incoming email.

For more information, review the postfix documentation for `inet_interfaces`_.

.. _inet_interfaces: http://www.postfix.org/postconf.5.html#inet_interfaces

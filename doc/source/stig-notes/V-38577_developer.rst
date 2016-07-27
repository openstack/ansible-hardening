The STIG requires SHA512 to be used for hashing password since it is
in the list of FIPS 140-2 approved hashing algorithms. This is also the
default in Ubuntu 14.04, Ubuntu 16.04, and CentOS 7.

The ``libuser`` package isn't installed by default in Ubuntu or via
openstack-ansible. The Ansible tasks will do the following:

* Check to see if libuser is installed
* If it's installed, it will check for the password hashing algorithm in
  ``/etc/libuser.conf``
* If libuser is installed **and** the password hashing algorithm isn't SHA512,
  an error will be printed and the playbook will fail

Further reading:

* `FIPS 140-2 on Wikipedia`_
* `FIPS 140-2 from NIST`_

.. _FIPS 140-2 on Wikipedia: https://en.wikipedia.org/wiki/FIPS_140-2
.. _FIPS 140-2 from NIST: http://csrc.nist.gov/groups/STM/cmvp/standards.html

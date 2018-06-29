ansible-hardening
=================

![ansible-hardening-logo](doc/source/_static/ansible-hardening-logo.png)

The ansible-hardening role applies security hardening configurations
from the [Security Technical Implementation Guide (STIG)](http://iase.disa.mil/stigs/Pages/index.aspx)
to systems running the following distributions:

* CentOS 7
* Debian Jessie
* Fedora 27
* openSUSE Leap 42.2 and 42.3
* Red Hat Enterprise Linux 7
* SUSE Linux Enterprise 12 (*experimental*)
* Ubuntu 16.04

For more details, review the
[ansible-hardening documentation](http://docs.openstack.org/developer/ansible-hardening/).

Release notes for the project can be found at:
  https://docs.openstack.org/releasenotes/ansible-hardening

Requirements
------------

This role can be used with or without OpenStack-Ansible. It requires
Ansible 2.3 or later.

Role Variables
--------------

All of the variables for this role are in `defaults/main.yml`.

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

Using the role is fairly straightforward:

    - hosts: servers
      roles:
         - ansible-hardening

Running with Vagrant
--------------------

This role can be tested easily on multiple platforms using Vagrant.

The `Vagrantfile` supports testing on:
 * Ubuntu 16.04
 * CentOS 7

To test on all platforms:

```shell
vagrant destroy --force && vagrant up
```

To test on Ubuntu 14.04 only:

```shell
vagrant destroy ubuntu1404 --force && vagrant up ubuntu1404
```

To test on Ubuntu 16.04 only:
```shell
vagrant destroy ubuntu1604 --force && vagrant up ubuntu1604
```

To test on CentOS 7 only:

```shell
vagrant destroy centos7 --force && vagrant up centos7
```

License
-------

Apache 2.0

Author Information
------------------

For more information, join `#openstack-ansible` on Freenode.

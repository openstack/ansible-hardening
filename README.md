openstack-ansible-security
==========================

The openstack-ansible security role applies security hardening configurations
from the [Security Technical Implementation Guide(STIG)](http://iase.disa.mil/stigs/Pages/index.aspx)
to systems running Ubuntu 14.04, Ubuntu 16.04, CentOS 7, and Red Hat
Enterprise Linux 7.

The role is part of the
[OpenStack-Ansible project](https://git.openstack.org/cgit/openstack/openstack-ansible),
which deploys enterprise-grade OpenStack clouds using Ansible.  However, the
role can easily be used outside of an OpenStack environment to secure hosts,
virtual machines, and containers.

For more details, review the
[openstack-ansible-security documentation](http://docs.openstack.org/developer/openstack-ansible-security/).

Requirements
------------

This role can be used with or without the OpenStack-Ansible role. It requires
Ansible 1.9.1 or later.

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
         - openstack-ansible-security

Running with Vagrant
--------------------

This role can be tested easily on multiple platforms using Vagrant.

The `Vagrantfile` supports testing on:
 * Ubuntu 14.04
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

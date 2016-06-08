openstack-ansible-security
==========================

The goal of the openstack-ansible-security role is to improve security within [openstack-ansible](https://github.com/openstack/openstack-ansible) deployments. The role is based on the [Security Technical Implementation Guide (STIG)](http://iase.disa.mil/stigs/Pages/index.aspx) for [Red Hat Enterprise Linux 6](https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/).

Requirements
------------

This role can be used with or without the openstack-ansible role. It requires
Ansible 1.8.3 at a minimum.

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

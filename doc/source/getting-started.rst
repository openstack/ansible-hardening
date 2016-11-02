Getting started
===============

The openstack-ansible-security role can be used along with the
`OpenStack-Ansible`_ project or as a standalone role that can be used along
with other Ansible playbooks.

.. _OpenStack-Ansible: https://git.openstack.org/cgit/openstack/openstack-ansible/

.. contents::
   :local:
   :backlinks: none

Prepare your system
-------------------

Start by installing ansible and then install the role itself using
``ansible-galaxy``:

.. code-block:: console

   pip install ansible
   ansible-galaxy install git+https://git.openstack.org/openstack/openstack-ansible-security

The role will be installed into
``/etc/ansible/roles/openstack-ansible-security``.

Initial configuration
---------------------

Some of the security configurations need initial configuration or they may
require you to opt-in for a change to be applied.  Start by reviewing the list
of STIG controls that
:ref:`require initial configuration <implementation-status-configuration-required>`
or :ref:`require opt-in <implementation-status-opt-in>`.

An example of a STIG requiring initial configuration is
:ref:`V-38446 <stig-V-38446>`, which requires an email address for a person
who can receive email sent to ``root``.

Many of the STIG configurations are in an *opt-in* status because they can be
helpful for some systems and harmful to others. A good example of this is
:ref`V-38481 <stig-V-38481>`, which requires that automatic package updates are
configured on a host. In some environments, this isn't a problem, but this
could cause disruptions in environments with low tolerance for changes.

Using as a standalone role
--------------------------

Adding the openstack-ansible-security role to existing playbooks is
straightforward. Here is an example of an existing role for deploying web
servers with the security hardening role added:

.. code-block:: yaml

   ---

   - name: Deploy web servers
     hosts: webservers
     become: yes
     roles:
       - common
       - webserver
       - openstack-ansible-security

Using with OpenStack-Ansible
----------------------------

The openstack-ansible-security role is automatically enabled and applied in the
Newton release of OpenStack-Ansible. In the Liberty and Mitaka releases, the
role is easily enabled by adjusting the following Ansible variable:

.. code-block:: yaml

     apply_security_hardening: true

For more information, refer to the OpenStack-Ansible documentation on
`configuring security hardening`_.

.. _configuring security hardening: http://docs.openstack.org/developer/openstack-ansible/install-guide/app-advanced-config-security.html#security-hardening

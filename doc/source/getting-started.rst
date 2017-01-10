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

The role's default configuration is suitable for most Linux hosts. Deployers
should review the :ref:`special_notes` section to learn more about how to
provide custom configuration for the Ansible tasks in the role.

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
Newton release of OpenStack-Ansible. Set the following Ansible variable to
enable the role in the Mitaka release of OpenStack-Ansible:

.. code-block:: yaml

     apply_security_hardening: true

For more information, refer to the OpenStack-Ansible documentation on
`configuring security hardening`_.

.. _configuring security hardening: http://docs.openstack.org/project-deploy-guide/openstack-ansible/draft/app-advanced-config-security.html#security-hardening

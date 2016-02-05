.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for OpenStack-Ansible

Getting started
===============

The openstack-ansible-security role can be used along with the
`OpenStack-Ansible`_ project or as a standalone role that can be used along
with other Ansible playbooks.

.. _OpenStack-Ansible: https://github.com/openstack/openstack-ansible/

Using with OpenStack-Ansible
----------------------------

Starting with the Mitaka release, OpenStack-Ansible installs the
openstack-ansible-security role automatically. It's disabled by default for
deployments and can be enabled with an Ansible variable:

.. code-block:: yaml

     apply_security_hardening: true

If the variable is set, the security hardening configurations will be applied
automatically on new builds that use the ``scripts/run_playbooks.sh`` script
provided with OpenStack-Ansible. However, the role can be applied anytime by
using the playbook provided with OpenStack-Ansible:

.. code-block:: bash

     cd /opt/openstack-ansible/playbooks/
     openstack-ansible -e "apply_security_hardening=true" security-hardening.yml

For more information, refer to the OpenStack-Ansible documentation on
`configuring security hardening`_.

.. _configuring security hardening: http://docs.openstack.org/developer/openstack-ansible/install-guide/configure-initial.html

Using as a standalone role
--------------------------

There are several options for using openstack-ansible-security as a standalone
role or along with another existing project. Here are two fairly easy methods:

* Add openstack-ansible-security as a git submodule in the roles directory
  of an existing Ansible project
* Clone the role into ``/etc/ansible/roles/`` on any system and write a custom
  playbook and hosts inventory file

The playbook for openstack-ansible-security can be fairly simple, depending
on the configuration of the systems:

.. code-block:: yaml

    ---

    - name: Run openstack-ansible-security
      hosts: webservers
      user: root
      roles:
        - openstack-ansible-security

This playbook will run the tasks in the openstack-ansible-security role against
all hosts in the ``webservers`` group (as defined in an inventory file).

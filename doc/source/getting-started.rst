.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Getting started
===============

`This role is still a work in progress.  These instructions are subject to
change frequently until the development work is feature complete.`

The openstack-ansible-security role can be used along with the
`openstack-ansible`_ project or as a standalone role that can be used along
with other Ansible playbooks.

Using with openstack-ansible
----------------------------

This portion of the guide assumes that openstack-ansible is already cloned
into ``/opt/openstack-ansible`` and it has been properly configured.  Start by
cloning openstack-ansible-security into Ansible's default role location::

    git clone https://github.com/openstack/openstack-ansible-security \
        /etc/ansible/roles/openstack-ansible-security

Before getting started, review the ``defaults/main.yml`` file from the
openstack-ansible-security repository.  There are some documented options there
for changes which may require opt-in or opt-out configuration.  Some options
can be adjusted depending on the security level of a particular environment.

Create a directory to hold an Ansible configuration file and a small playbook::

    mkdir /opt/openstack-ansible-security
    cd /opt/openstack-ansible-security

Create a small Ansible playbook at
``/opt/openstack-ansible-security/os-security.yml``:

.. code-block:: yaml

    ---

    - name: Run openstack-ansible-security
      hosts: "{{ host_group|default('hosts') }}"
      user: root
      roles:
        - openstack-ansible-security

Add an Ansible configuration file so that your playbook can use
openstack-ansible's dynamic inventory.  Create a new file at
``/opt/openstack-ansible-security/ansible.cfg``::

    [defaults]
    gathering = smart
    host_key_checking = False

    # SSH timeout
    timeout = 120

    # Set the path to the folder in openstack-ansible which holds the dynamic
    # inventory script - new config setting for ansible v1.9 and above
    inventory = ../openstack-ansible/playbooks/inventory/

    # Set the path to the folder in openstack-ansible which holds the dynamic
    # inventory script - uncomment if using ansible below v1.9
    #hostfile = ../openstack-ansible/playbooks/inventory/

    # Set the path to the folder in openstack-ansible which holds the
    # libraries required
    library = ../openstack-ansible/playbooks/library/

    # Set the path to the folder in openstack-ansible which holds the
    # lookup plugins required
    lookup_plugins = ../openstack-ansible/playbooks/plugins/lookups/

    # Set the path to the folder in openstack-ansible which holds the filter
    # plugins required
    filter_plugins = ../openstack-ansible/playbooks/plugins/filters/

    # Set the path to the folder in openstack-ansible which holds the action
    # plugins required
    action_plugins = ../openstack-ansible/playbooks/plugins/actions/

    [ssh_connection]
    pipelining = True

Run the playbook::

    cd /opt/openstack-ansible-security/
    openstack-ansible os-security.yml

There are lots of tags throughout the tasks in the role that will allow
deployers to select certain tasks or groups of tasks to run.  For example, just
the ``auditd`` improvements can be deployed by using the appropriate tag::

    openstack-ansible os-security.yml -t auditd

.. _openstack-ansible: https://github.com/openstack/openstack-ansible/

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

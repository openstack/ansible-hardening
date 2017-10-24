Getting started
===============

The ansible-hardening role can be used along with the `OpenStack-Ansible`_
project or as a standalone role that can be used along with other Ansible
playbooks. This documentation assumes that the reader has completed the steps
within the
`Ansible installation guide <http://docs.ansible.com/ansible/intro_installation.html>`_.

.. _OpenStack-Ansible: https://git.openstack.org/cgit/openstack/openstack-ansible/

.. contents::
   :local:
   :backlinks: none

Installing the ansible-hardening role
-------------------------------------

The recommended installation methods for the ansible-hardening role are
``ansible-galaxy`` (recommended) or ``git``.

Using ``ansible-galaxy``
~~~~~~~~~~~~~~~~~~~~~~~~

The easiest installation method is to use the ``ansible-galaxy`` command that
is provided with your Ansible installation:

.. code-block:: console

   ansible-galaxy install git+https://github.com/openstack/ansible-hardening

The ``ansible-galaxy`` command will install the role into
``/etc/ansible/roles/ansible-hardening`` and this makes it easy to use with
Ansible playbooks.

Using ``git``
~~~~~~~~~~~~~

Start by cloning the role into a directory of your choice:

.. code-block:: console

   mkdir -p ~/.ansible/roles/
   git clone https://github.com/openstack/ansible-hardening ~/.ansible/roles/ansible-hardening

Ansible looks for roles in ``~/.ansible/roles`` by default.

If the role is cloned into a different directory, that directory must be
provided with the ``roles_path`` option in ``ansible.cfg``. The following is
an example of a ``ansible.cfg`` file that uses a custom path for roles:

.. code-block:: ini

   [DEFAULTS]
   roles_path = /etc/ansible/roles:/home/myuser/custom/roles

With this configuration, Ansible looks for roles in ``/etc/ansible/roles`` and
``~/custom/roles``.

Usage
-----

The ansible-hardening role works well with existing playbooks. The following
is an example of a basic playbook that uses the ansible-hardening role:

.. code-block:: yaml

    ---

    - name: Harden all systems
      hosts: all
      become: yes
      vars:
        security_enable_firewalld: no
        security_rhel7_initialize_aide: no
        security_ntp_servers:
          - 1.example.com
          - 2.example.com
      roles:
        - ansible-hardening

The variables provided in the ``vars`` section can enable, disable, or alter
configuration for various tasks in the ansible-hardening role. For more details
on the available variables, refer to the :ref:`hardening_domains_label`
section.

.. note::

    The role must be run as the root user or as a user with ``sudo`` access.
    The example above uses the ``become`` option, which causes Ansible to use
    sudo before running tasks. If the role is running as root, this option can
    be changed to ``user: root``.

.. warning::

    It is strongly recommended to run the role in check mode (often called a
    `dry run`) first before making any modifications. This gives the deployer
    the opportunity to review all of the proposed changes before applying the
    role to the system. Use the ``--check`` parameter with ``ansible-playbook``
    to use check mode.

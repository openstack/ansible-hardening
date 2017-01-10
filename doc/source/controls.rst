Security hardening controls in detail (RHEL 6 STIG)
===================================================

The Security Technical Implementation Guide (STIG) for Red Hat Enterprise Linux
6 contains over 200 security controls. The links below will allow you to review
each control based on a certain set of criteria.

Controls are divided into groups based on certain properties:

* **Severity:** Normally high, medium and low. High severity items are the ones
  which should be completed first, since they pose the greatest threat to the
  security of a system.
  *(These severity levels are set within the STIG.)*

* **Implementation status:** Each control is assessed thoroughly before Ansible
  tasks are written. Some controls may be listed as *exceptions* since they
  can't be implemented with automation, or they could cause damage to an
  existing system. Other controls are listed as *opt-in* when they are
  implemented, but they require a deployer to enable them.
  *(This categorization comes from openstack-ansible-security, not the STIG.)*

* **Tag:** The controls are also separated based on which parts of the system
  they act upon. Something that secures ``grub`` would be tagged with *boot*
  while controls for ``sshd`` would be tagged with *auth*.
  *(This categorization comes from openstack-ansible-security, not the STIG.)*

You can also review the STIG controls in one very large page. This can be
helpful when you need to search using your web browser.

.. note::

    The RHEL 6 STIG content is deprecated in the Ocata release and will be
    removed in a future release. Deployers can choose to deploy the RHEL 6
    STIG content by setting the ``stig_version`` Ansible variable:

    .. code-block:: console

        ansible-playbook -i hosts playbook.yml -e stig_version=rhel7

.. toctree::
   :maxdepth: 2

   auto_controls-by-severity.rst
   auto_controls-by-status.rst
   auto_controls-by-tag.rst
   auto_controls-all.rst

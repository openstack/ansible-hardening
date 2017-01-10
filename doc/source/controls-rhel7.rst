Security hardening controls in detail (RHEL 7 STIG)
===================================================

The openstack-ansible-security role follows the Red Hat Enteprise Linux 7
`Security Technical Implementation Guide (STIG)`_. The guide has over 200
controls that apply to various parts of a Linux system, and it is updated
regularly by the Defense Information Systems Agency (DISA). DISA is part of the
United States Department of Defense. The current version of the openstack-
ansible-security role is based on release 1, version 0.2 of the Red Hat
Enterprise Linux 7 STIG.

Controls are divided into groups based on the following properties:

* **Severity:**

  * *High severity* controls have a large impact on the security of a
    system. They also have the largest operational impact to a system and
    deployers should test them thoroughly in non-production environments.

  * *Low severity* controls have a smaller impact on overall security, but they
    are generally easier to implement with a much lower operational impact.

* **Implementation Status:**

  * *Implemented* controls are automatically implemented with automated tasks.
    Deployers can often opt out of these controls by adjusting Ansible
    variables. These variables are documented with each control below.

  * *Exceptions* denote controls that cannot be completed via automated tasks.
    Some of these controls must be applied during the initial provisioning
    process for new servers while others require manual inspection of the
    system.

  * *Opt in* controls have automated tasks written, but these tasks are
    disabled by default. These controls are often disabled because they could
    cause disruptions on a production system, or they do not provide a
    significant security benefit. Each control can be enabled with Ansible
    variables and these variables are documented with each control below.

  * *Verification only* controls have tasks that verify that a control is met.
    These tasks do not take any action on the system, but they often display
    debug output with additional instructions for deployers.

* **Tag:**

  * Each control has a tag applied, and the tags allow deployers to select
    specific groups of controls to apply. For example, deployers can apply the
    controls for the ssh daemon by using ``--tags sshd`` on the Ansible command
    line.

  * Tags also make it easier to navigate through the Ansible tasks in the code
    itself. For example, all tasks tagged with ``auditd`` are found within
    ``tasks/rhel7stig/auditd.yml``.

.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/os/unix-linux/Pages/red-hat.aspx

Although the STIG is specific to Red Hat Enterprise Linux 7, it also applies to
CentOS 7 systems. In addition, almost all of the controls are easily translated
for Ubuntu 16.04. Any deviations during translation are noted within the
documentation below.

.. toctree::
   :maxdepth: 2

   rhel7/auto_controls-by-severity.rst
   rhel7/auto_controls-by-status.rst
   rhel7/auto_controls-by-tag.rst
   rhel7/auto_controls-all.rst

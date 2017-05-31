auditd - audit daemon
=====================

The STIG requires all systems to have the audit daemon, ``auditd``, running to
monitor system calls and other critical events. The daemon has rules that
define which events are noteworthy on the system and it can generate alerts
based on the events it finds.

Overview
--------

Audit daemon rules
  The auditd rules are deployed in a single task via a template
  (``templates/osas-auditd-rhel7.j2``). Each rule or set of similar rules are
  controlled by an Ansible variable that starts with ``security_audit_rhel7``.
  Refer to ``defaults/main.yml`` for a list of these variables.

  Example:

  .. code-block:: yaml

    # Add audit rules for commands/syscalls.
    security_rhel7_audit_chsh: yes                               # V-72167
    security_rhel7_audit_chage: yes                              # V-72155
    security_rhel7_audit_chcon: yes                              # V-72139
    security_rhel7_audit_chmod: no                               # V-72105
    security_rhel7_audit_chown: no                               # V-72097

  For example, setting ``security_rhel7_audit_chown`` to ``yes`` will
  ensure that the rule for auditing the usage of the ``chown`` are included
  on each host. Setting ``security_rhel7_audit_chown`` to ``no`` will omit that
  rule on each host.

Handling audit emergencies
  There are several configurations for auditd which are critical for deployers
  to review in detail. The options beneath the ``## Audit daemon (auditd)``
  comment will change how auditd handles log files and what it should do in
  case of emergencies.

  .. warning::

    Deployers should thoroughly test all changes to auditd emergency
    configurations. Some of these configuration options can cause serious
    issues on production systems, ranging from a reduction in security to
    servers going offline unexpectedly. There is extensive documentation in the
    developer notes below for each STIG requirement.

.. include:: auto_auditd.rst

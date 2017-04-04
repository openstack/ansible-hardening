.. contents::
   :local:
   :backlinks: none

Developer Guide
===============

Building a development environment
----------------------------------

The OpenStack gate runs the tox tests found within ``tox.ini``. Developers
should use these tox tests to verify that their changes will work when the gate
jobs run. Some systems may need additional packages for these tests to run
properly.

To install all of the prerequisites and run the functional tests, use the
``run_tests.sh`` script:

.. code-block:: console

    ./run_tests.sh

.. note::

   This script will apply the default security hardening configurations to the
   local host. Avoid running this script on production servers which have not
   been properly tested with the security role.

Writing documentation
---------------------

Documentation consists of two parts: metadata and deployer notes. The metadata
exists as `YAML frontmatter <https://jekyllrb.com/docs/frontmatter/>`_ for each
STIG configuration. The frontmatter is followed by the text of the deployer
note itself.

All of the notes are found within ``doc/metadata/rhel7``. Here is an example
of V-71989:

.. literalinclude:: ../metadata/rhel7/V-71989.rst
   :language: yaml

The block after the first three dashes (``---``) is the metadata. The metadata
must include:

* ``id``: The ID of the STIG configuration item.
* ``status``: The implementation status of the STIG configuration, such as
  ``implemented``, ``exception``, or ``opt-in``.
* ``tag``: The Ansible tag associated with the task(s) that make changes based
  on the STIG requirement, such as ``auditd``, ``kernel``, or ``lsm``.

The next block is the deployer note. The note should be brief, but it must
answer a few critical questions:

* What does the change do to a system?
* What is the value of making this change?
* How can a deployer opt out or opt in for a particular change?
* Is there additional documentation available online that may help a deployer
  decide whether or not this change is valuable to them?

Run ``tox -e docs`` to rebuild the documentation from the metadata and review
your changes.

Release notes
-------------

Adding release notes helps deployers and other developers discover the new
additions to the role in a concise format. Release notes should be added to
incoming patches if they would change something noticeable in the role, such as
bug fixes, new functionality, or variable name changes.

To add a release note, use ``reno``:

.. code-block:: console

    reno new i-made-a-new-feature-that-does-something-awesome

Once you run the ``reno new`` command with a release note slug, a new file
appears in ``releasenotes/notes``. Edit that file and adjust the relevant
section to explain the changes found within your patch. Delete any unused
sections and submit the release note with your patch.

For more details, refer to the documentation on release notes found in the
`OpenStack-Ansible developer documentation <http://docs.openstack.org/developer/openstack-ansible/developer-docs/contribute.html#release-notes>`_

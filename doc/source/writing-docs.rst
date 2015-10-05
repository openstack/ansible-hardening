.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Writing docs for openstack-ansible-security
===========================================

The configurations-cat[number].rst files are automatically generated with the
``stigcsv-to-rst.py`` script and the ``rhel6stig.csv``.

Each hardening configuration does an import from the developer-notes directory
and looks for a file called ``[STIG_ID].rst``.  As an example, the
documentation for V-38476 would live in ``developer-notes/V-38476.rst``.

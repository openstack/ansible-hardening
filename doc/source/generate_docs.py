#!/usr/bin/env python
# Copyright 2015, Rackspace US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Generates the documentation scaffolding."""
import csv
from jinja2 import Template
from textwrap import fill


def reindent(string_to_indent, numSpaces):
    """Indent strings with spaces."""
    s = string_to_indent.splitlines()
    s = [(numSpaces * ' ') + line.lstrip() for line in s]
    return '\n'.join(s)


stigviewer_url = ("https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/"
                  "2015-05-26/finding/{0}")

stig_note_template = """{{ title }}
{{ '-' * title | length }}

{{ desc }}

Details: `{{ id }} in STIG Viewer`_.

.. _{{ id }} in STIG Viewer: {{ stigviewer }}

Notes for deployers
~~~~~~~~~~~~~~~~~~~

.. include:: developer-notes/{{ id }}.rst

"""

stigs = []

with open('rhel6stig.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        metadata = {
            'id': row[0],
            'title': "{0}: {1}".format(row[0], row[2]),
            'desc': fill(row[3], width=78),
            'fixtext': row[7],
            'checktext': row[9],
            'severity': row[1],
            'stigviewer': stigviewer_url.format(row[0]),
        }
        template = Template(stig_note_template)
        with open("stig-notes/{0}.rst".format(metadata['id']), 'w') as rstfile:
            rstfile.write(template.render(metadata))

        stigs.append(metadata)


category_template = """.. include:: <xhtml1-lat1.txt>
`Home <index.html>`__ |raquo| Security hardening for openstack-ansible

Category {{ level }} ({{ name | capitalize }}) controls
================================

.. toctree::
   :maxdepth: 1


"""


categories = {
    'low': 1,
    'medium': 2,
    'high': 3,
}

for category_name, category_level in categories.items():
    matching_stigs = [x for x in stigs if x['severity'] == category_name]
    cat_file = open("controls-cat{0}.rst".format(category_level), 'w')
    template = Template(category_template)
    cat_file.write(template.render(name=category_name,
                                   level=category_level))

    include_template = ".. include:: stig-notes/{0}.rst\n\n"
    for matching_stig in sorted(matching_stigs, key=lambda k: k['id']):
        cat_file.write(include_template.format(matching_stig['id']))

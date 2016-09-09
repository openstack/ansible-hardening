#!/usr/bin/env python
# Copyright 2016, Rackspace US, Inc.
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
"""Import existing developer notes into base YAML format."""
import os


import jinja2


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
METADATA_DIR = "{0}/rhel6".format(SCRIPT_DIR)
NOTES_DIR = "{0}/../source/stig-notes".format(SCRIPT_DIR)

yaml_tmp = """---
id: {{ note_data['id'] }}
status: {{ note_data['status'] }}
tag: {{ note_data['tag'] }}
---

{{ note_data['deployer_notes'] }}
"""


note_files = [x for x in os.listdir(NOTES_DIR) if 'developer' in x]
for note_file in note_files:
    stig_id = note_file[0:7]

    with open("{0}/{1}".format(NOTES_DIR, note_file), 'r') as f:
        content = f.read()

    first_line = content.splitlines()[0]
    print(first_line)
    if 'exception' in first_line.lower():
        status = 'exception'
    elif 'opt-in' in first_line.lower():
        status = 'opt-in'
    else:
        status = 'implemented'

    note_data = {
        'id': stig_id,
        'status': status,
        'tag': 'misc',
        'deployer_notes': content
    }

    with open("{0}/{1}.rst".format(METADATA_DIR, stig_id), 'w') as f:
        template = jinja2.Template(yaml_tmp)
        f.write(template.render(note_data=note_data))

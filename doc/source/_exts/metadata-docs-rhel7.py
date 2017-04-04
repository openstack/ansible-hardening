#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
"""Build documentation from STIG and deployer notes."""
from __future__ import print_function, unicode_literals
import os
import re

from collections import OrderedDict, defaultdict

import jinja2
from lxml import etree
import yaml


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
METADATA_DIR = "{0}/../../metadata".format(SCRIPT_DIR)
DOC_SOURCE_DIR = "{0}/..".format(SCRIPT_DIR)
XCCDF_FILE = 'U_Red_Hat_Enterprise_Linux_7_STIG_V1R1_Manual-xccdf.xml'
XCCDF_NAMESPACE = {'x': 'http://checklists.nist.gov/xccdf/1.1'}


def add_monospace(text):
    """Add monospace formatting to RST."""
    paragraphs = text.split('\n\n')
    for key, value in enumerate(paragraphs):

        # Replace all quotes "" with backticks `` for monospacing
        paragraphs[key] = re.sub(u'\u201c(.*?)\u201d',
                                 r'``\1``',
                                 value)

        # If our paragraph ends with a colon and the next line isn't a special
        # note, let's make sure the next paragraph is monospaced.
        if value.endswith(":"):

            if paragraphs[key + 1].startswith('Note:'):

                # Indent the paragraph AFTER the note.
                paragraphs[key + 2] = '::\n\n    ' + '\n    '.join(
                    paragraphs[key + 2].split('\n')
                )

            else:
                # Ensure the paragraph ends with double colon (::).
                paragraphs[key] = re.sub(r':$', '::', value)

                # Indent the next paragraph.
                paragraphs[key + 1] = '    ' + '\n    '.join(
                    paragraphs[key + 1].split('\n')
                )

        # If we found a note in the description, let's format it like a note.
        if value.startswith('Note:'):
            paragraphs[key] = ".. note::\n\n    {0}".format(value[6:])

        # If we have a line that starts with a pound sign, this probably needs
        # to be pre-formatted as well.
        if value.startswith('#'):
            paragraphs[key] = '::\n\n    ' + '\n    '.join(value.split('\n'))

        # If there's a command on a line by itself, we probably need to merge
        # it with the next line. The STIG has terrible formatting in some
        # places.
        monospace_strings = ['grep', 'more']
        if (
            key + 1 < len(paragraphs) and
            any(x in value for x in monospace_strings) and
            '\n' not in value and
            not paragraphs[key + 1].startswith('Password')
        ):
            value = "{0}\n{1}".format(
                value,
                '\n    '.join(paragraphs[key + 1].split('\n'))
            )
            del(paragraphs[key + 1])

    return '\n\n'.join(paragraphs)

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(METADATA_DIR),
    trim_blocks=True,
    keep_trailing_newline=False,
)
JINJA_ENV.filters['addmonospace'] = add_monospace


def element_flatten(element):
    """Flatten the element into a single item if it's a single item list."""
    # If there's only one result in the list, then return that single result.
    if isinstance(element, list) and len(element) == 1:
        return element[0]
    else:
        return element


def filter_xpath(tree, xpath_string):
    """Apply an xpath filter to the XML and return data."""
    element = tree.xpath(xpath_string, namespaces=XCCDF_NAMESPACE)
    return element_flatten(element)


def filter_find(tree, xpath_string):
    """Do a find on the tree to get specific data."""
    element = tree.find(xpath_string, namespaces=XCCDF_NAMESPACE)
    return element_flatten(element)


def filter_findall(tree, xpath_string):
    """Do a find on the tree to get specific data."""
    element = tree.findall(xpath_string, namespaces=XCCDF_NAMESPACE)
    return element_flatten(element)


def get_deployer_notes(stig_id):
    """Read deployer notes based on the STIG ID."""
    filename = "{0}/rhel7/{1}.rst".format(METADATA_DIR, stig_id)

    # Does this deployer note exist?
    if not os.path.isfile(filename):
        return False

    # Read the note and parse it with YAML
    with open(filename, 'r') as f:
        rst_file = f.read()

    # Split the RST into frontmatter and text
    # NOTE(mhayden): Can't use the standard yaml.load_all() here at it will
    #                have scanner errors in documents that have colons (:).
    yaml_boundary = re.compile(r'^-{3,}$', re.MULTILINE)
    _, metadata, text = yaml_boundary.split(rst_file, 2)

    # Assemble the metadata and the text from the deployer note.
    post = yaml.safe_load(metadata)
    post['content'] = text

    return post


def read_xml():
    """Read XCCDF XML file and parse it into an etree."""
    with open("{0}/{1}".format(METADATA_DIR, XCCDF_FILE), 'r') as f:
        tree = etree.parse(f)
    return tree


def render_all(stig_ids, all_deployer_notes):
    """Generate documentation RST for each STIG configuration."""
    template = JINJA_ENV.get_template('template_all_rhel7.j2')
    return template.render(
        stig_ids=stig_ids,
        all_deployer_notes=all_deployer_notes,
    )


def render_doc(stig_rule, deployer_notes):
    """Generate documentation RST for each STIG configuration."""
    template = JINJA_ENV.get_template('template_doc_rhel7.j2')
    return template.render(
        rule=stig_rule,
        notes=deployer_notes
    )


def render_toc(toc_type, stig_dict, all_deployer_notes):
    """Generate documentation RST for each STIG configuration."""
    template = JINJA_ENV.get_template('template_toc_rhel7.j2')
    return template.render(
        toc_type=toc_type,
        stig_dict=stig_dict,
        all_deployer_notes=all_deployer_notes,
    )


def write_file(filename, content):
    """Write contents to files."""
    file_path = "{0}/{1}".format(DOC_SOURCE_DIR, filename)

    if not os.path.isdir(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'w') as f:
        f.write(content.encode('utf-8'))

    return True


def generate_docs():
    """The main function."""
    tree = read_xml()

    # Create a simple list to capture all of the STIGs
    stig_ids = []

    # Create defaultdicts to hold information to build our table of
    # contents files for sphinx.
    all_deployer_notes = defaultdict(list)
    severity = defaultdict(list)
    tag = defaultdict(list)
    status = defaultdict(list)

    # Loop through the groups and extract rules
    group_elements = filter_xpath(tree, "/x:Benchmark/x:Group")
    for group_element in group_elements:
        rule_element = filter_find(group_element, 'x:Rule')

        # Build a dictionary with all of our rule data.
        rule = {
            'id': group_element.attrib['id'],
            'title': filter_find(rule_element, 'x:title').text,
            'severity': rule_element.attrib['severity'],
            'fix': filter_find(rule_element, 'x:fixtext').text,
            'check': filter_find(rule_element,
                                 'x:check/x:check-content').text,
            'ident': [x.text for x in filter_find(rule_element, 'x:ident')],
        }

        # The description has badly formed XML in it, so we need to hack it up
        # and turn those tags into a dictionary.
        description = filter_find(rule_element, 'x:description').text
        parser = etree.XMLParser(recover=True)
        temp = etree.fromstring("<root>{0}</root>".format(description), parser)
        rule['description'] = {x.tag: x.text for x in temp.iter()}

        # Get the deployer notes from YAML
        print(rule['id'])
        deployer_notes = get_deployer_notes(rule['id'])
        rule['deployer_notes'] = deployer_notes

        all_deployer_notes[rule['id']] = rule
        stig_ids.append(rule['id'])
        severity[rule['severity']].append(rule['id'])
        status[deployer_notes['status']].append(rule['id'])
        tag[deployer_notes['tag']].append(rule['id'])

    keyorder = ['high', 'medium', 'low']
    severity = OrderedDict(sorted(severity.items(),
                                  key=lambda x: keyorder.index(x[0])))
    status = OrderedDict(sorted(status.items(), key=lambda x: x[0]))
    tag = OrderedDict(sorted(tag.items(), key=lambda x: x[0]))

    all_toc = render_all(stig_ids, all_deployer_notes)
    severity_toc = render_toc('severity',
                              severity,
                              all_deployer_notes)
    status_toc = render_toc('implementation status',
                            status,
                            all_deployer_notes)
    tag_toc = render_toc('tag',
                         tag,
                         all_deployer_notes)

    write_file("rhel7/auto_controls-all.rst", all_toc)
    write_file("rhel7/auto_controls-by-severity.rst", severity_toc)
    write_file("rhel7/auto_controls-by-status.rst", status_toc)
    write_file("rhel7/auto_controls-by-tag.rst", tag_toc)


def setup(app):
    """Set up the Sphinx extension."""
    print("Generating RHEL7 STIG documentation...")
    generate_docs()

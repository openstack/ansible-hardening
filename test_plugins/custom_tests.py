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
"""Extra tests for jinja2 templates in Ansible."""

# NOTE(mhayden): Remove this file when jinja 2.9.5 is available for use within
# OpenStack.


def greaterthan(value, reference_value):
    """Return true if value > reference_value."""
    return value > reference_value


def lessthan(value, reference_value):
    """Return true if value < reference_value."""
    return value < reference_value


class TestModule:
    """Main test class from Ansible."""

    def tests(self):
        """Add these tests to the list of tests available to Ansible."""
        return {
            'greaterthan': greaterthan,
            'lessthan': lessthan,
        }

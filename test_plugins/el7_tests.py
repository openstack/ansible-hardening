# Copyright 2017, Rackspace US, Inc.
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
"""Additional Jinja2 tests for CentOS/RHEL7."""

# NOTE(mhayden): CentOS and RHEL7 ship with Jinja2 2.7.2 and it doesn't have
# some of the newer tests. This snippet adds those tests so that the tasks that
# use them will work properly.


def test_equalto(value, other):
    """Test to see if two values are the same."""
    return value == other


def test_greaterthan(value, other):
    """Check if value is greater than other."""
    return value > other


def test_lessthan(value, other):
    """Check if value is less than other."""
    return value < other


class TestModule:
    """Main test class from Ansible."""

    def tests(self):
        """Add these tests to the list of tests available to Ansible."""
        return {
            'equalto': test_equalto,
            'greaterthan': test_greaterthan,
            'lessthan': test_lessthan,
        }

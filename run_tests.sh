#!/usr/bin/env bash
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

set -euov

FUNCTIONAL_TEST=${FUNCTIONAL_TEST:-true}

# Install pip
if [ ! "$(which pip)" ]; then
  curl --silent --show-error --retry 5 \
    https://bootstrap.pypa.io/get-pip.py | sudo python2.7
fi

# Install bindep and tox
pip install bindep tox

# CentOS 7 requires two additional packages:
#   redhat-lsb-core - for bindep profile support
#   epel-release    - required to install python-ndg_httpsclient/python2-pyasn1
if [ "$(which yum)" ]; then
    yum -y install redhat-lsb-core epel-release
fi

# Install OS packages using bindep
if apt-get -v >/dev/null 2>&1 ; then
    apt-get update
    DEBIAN_FRONTEND=noninteractive \
      apt-get -q --option "Dpkg::Options::=--force-confold" \
      --assume-yes install `bindep -b -f bindep.txt test`
else
    yum install -y `bindep -b -f bindep.txt test`
fi

# run through each tox env and execute the test
for tox_env in $(awk -F= '/envlist/ {print $2}' tox.ini | sed 's/,/ /g'); do
  if [ "${tox_env}" != "ansible-functional" ]; then
    tox -e ${tox_env}
  elif [ "${tox_env}" == "ansible-functional" ]; then
    if ${FUNCTIONAL_TEST}; then
      tox -e ${tox_env}
    fi
  fi
done

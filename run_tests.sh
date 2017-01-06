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

set -xeuo pipefail

FUNCTIONAL_TEST=${FUNCTIONAL_TEST:-true}

# Install pip.
if ! which pip; then
  curl --silent --show-error --retry 5 \
    https://bootstrap.pypa.io/get-pip.py | sudo python2.7
fi

# Install bindep and tox with pip.
sudo pip install bindep tox

# CentOS 7 requires two additional packages:
#   redhat-lsb-core - for bindep profile support
#   epel-release    - required to install python-ndg_httpsclient/python2-pyasn1
if which yum; then
    sudo yum -y install redhat-lsb-core epel-release
fi

# Get a list of packages to install with bindep. If packages need to be
# installed, bindep exits with an exit code of 1.
BINDEP_PKGS=$(bindep -b -f bindep.txt test || true)
echo "Packages to install: ${BINDEP_PKGS}"

# Install a list of OS packages provided by bindep.
if which apt-get; then
    sudo apt-get update
    DEBIAN_FRONTEND=noninteractive \
      sudo apt-get -q --option "Dpkg::Options::=--force-confold" \
      --assume-yes install $BINDEP_PKGS
elif which yum; then
    # Don't run yum with an empty list of packages.
    # It will fail and cause the script to exit with an error.
    if [[ ${#BINDEP_PKGS} > 0 ]]; then
      sudo yum install -y $BINDEP_PKGS
    fi
fi

# Loop through each tox environment and run tests.
for tox_env in $(awk -F= '/envlist/ { gsub(",", " "); print $2 }' tox.ini); do
  echo "Executing tox environment: ${tox_env}"
  if [[ ${tox_env} == ansible-functional ]]; then
    if ${FUNCTIONAL_TEST}; then
      tox -e ${tox_env}
    fi
  else
    tox -e ${tox_env}
  fi
done

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
#
# Note:
# This file is maintained in the openstack-ansible-tests repository.
# https://git.openstack.org/cgit/openstack/openstack-ansible-tests/tree/run_tests.sh
# If you need to modify this file, update the one in the openstack-ansible-tests
# repository and then update this file as well. The purpose of this file is to
# prepare the host and then execute all the tox tests.
#

## Shell Opts ----------------------------------------------------------------
set -xeu

## Vars ----------------------------------------------------------------------

export WORKING_DIR=${WORKING_DIR:-$(pwd)}

## Main ----------------------------------------------------------------------

source /etc/os-release || source /usr/lib/os-release

install_pkg_deps() {
    pkg_deps="git"

    case ${ID,,} in
        centos|rhel) pkg_mgr_cmd="yum install -y" ;;
        fedora) pkg_mgr_cmd="dnf -y install" ;;
        ubuntu|debian) pkg_mgr_cmd="apt-get install -y" ;;
        *) echo "unsupported distribution: ${ID,,}"; exit 1 ;;
    esac

    eval sudo $pkg_mgr_cmd $pkg_deps
}

git_clone_repo() {
    if [[ ! -d tests/common ]]; then
        # The tests repo doesn't need a clone, we can just
        # symlink it.
        if [[ "$(basename ${WORKING_DIR})" == "openstack-ansible-tests" ]]; then
            ln -s ${WORKING_DIR} ${WORKING_DIR}/tests/common
        else
            git clone -b stable/newton \
                https://git.openstack.org/openstack/openstack-ansible-tests \
                tests/common
        fi
    fi
}

install_pkg_deps

git_clone_repo

# start executing the main test script
source tests/common/run_tests_common.sh


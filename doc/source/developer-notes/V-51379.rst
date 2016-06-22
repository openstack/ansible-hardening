**Exception for Ubuntu**

The security role will search for unlabeled devices on CentOS and the playbook
will fail with an error message if any unlabeled devices are found.

Although SELinux works through a labeling system where every file (including
devices) receives a label, AppArmor on Ubuntu works purely through policies
without labels. However, OpenStack-Ansible does configure several AppArmor
policies to reduce the chances and impact of LXC container breakouts on
OpenStack hosts.

Although SELinux is available on Ubuntu 14.04, the policies aren't maintained
as well as they are on Red Hat-based systems.  The openstack-ansible project
has chosen to use the more Ubuntu-compatible Linux security module, AppArmor.

AppArmor roles are configured in openstack-ansible to limit the chances of
container breakout and the potential damage done in case it does occur.

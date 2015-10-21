**Exception**

Searching for world-writable files on a host deployed with openstack-ansible
can be very time consuming and it can create unneccessary I/O load on hosts.
Deployers are urged to check for world-writable files on a regular basis in
directories where those files might be a concern (especially web accessible
directories).

The command provided with the STIG is helpful for finding these types of files:

.. code-block:: bash

    find ${MOUNT_POINT} -xdev -type f -perm -002

Running ``find /`` isn't recommended on systems without LVM storage for
containers since it will eventually search through the filesystems of the LXC
containers that are deployed by openstack-ansible. The ``-xdev`` option
prevents ``find`` from wandering into other mounted filesystems and will
prevent it from searching through containers in logical volumes.

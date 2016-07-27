**Fixed by V-38591**

On Ubuntu, the ``rexecd`` daemon is part of the package that contains the
``rsh`` daemon. CentOS 7 doesn't provide the ``rexecd`` daemon in any packages.

Running a rsh daemon isn't recommended under most situations, so the rsh server
package will be removed from the system if it is installed. The rsh server is
removed by the Ansible tasks for V-38591, so no action is required here.

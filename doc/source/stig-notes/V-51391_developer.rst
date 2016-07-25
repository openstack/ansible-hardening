When AIDE is first installed for V-38429, a new database will be created.
The creation process takes some time because AIDE needs to review each file
in its list of monitored files to get timestamps and hashes. The
initialization will be forked into the background so that it doesn't slow
down the playbook run.

Some directories are excluded from AIDE runs to prevent AIDE from wandering
into directories where it shouldn't be hashing/monitoring files. The
``defaults/main.yml`` file has some recommended directories as part of the
``security_aide_exclude_dirs`` variable.

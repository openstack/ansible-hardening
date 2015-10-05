**Exception**

Installing AIDE on Ubuntu isn't an issue, but there's a bug that causes AIDE
to wander into individual LXC infrastructure container filesystems. This
causes AIDE runs to take an extremely long time to complete and also adds
files into AIDE's database that shouldn't be included.

This security configuration will be revisited at a later date.

**Exception**

Filtering IPv6 traffic is left up to the deployer to implement. The
openstack-ansible roles don't configure IPv6 (at this time) and adding
persistent ip6tables rules could harm a running system.

However, deployers are strongly recommended to implement IPv6 filtering at the
edges of the network via network devices.  In addition, deployers should be
aware that link-local IPv6 addresses are configured automatcally by the system
and those addresses could open up new network paths for future attacks.

For example, if IPv4 access was tightly controlled and segmented, hosts and/or
containers could possibly communicate across these boundaries using IPv6
link-local addresses.  For more detailed information on this security topic,
review Cisco's documentation titled `IPv6 Security Brief`_ that is available
on their website.

.. _IPv6 Security Brief: http://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/enterprise-ipv6-solution/white_paper_c11-678658.html

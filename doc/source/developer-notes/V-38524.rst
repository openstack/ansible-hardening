This patch disables ICMPv4 redirects feature on the host.
Accepting ICMP redirects has few legitimate uses.
It should be disabled unless it is absolutely required.

It is configurable by ``security_disable_icmpv4_redirects`` variable.
This feature is disabled by default as it can disrupt ``LXC`` deployments.

Deployers can skip or enable this task by setting
``security_disable_icmpv4_redirects`` to ``no``  or ``yes``,  respectively.

__doc__ = """ifconfig
ifconfig maps a linux ifconfig command to the interfaces relation.
"""

from Products.DataCollector.plugins.zenoss.cmd.linux.ifconfig import ifconfig as ifconfig_old
class ifconfig(ifconfig_old):
    command = '/sbin/ifconfig -a 2>/dev/null && echo __COMMAND__ && /bin/dmesg'

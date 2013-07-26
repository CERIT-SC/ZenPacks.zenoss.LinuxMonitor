##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2009, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


__doc__ = """ip
ip maps a linux ip command to the interfaces relation.
"""

import re

from Products.DataCollector.plugins.CollectorPlugin import LinuxCommandPlugin

class ip(LinuxCommandPlugin):
    command = '/sbin/ip address show'
    compname = "os"
    relname = "interfaces"
    modname = "Products.ZenModel.IpInterface"
    deviceProperties = LinuxCommandPlugin.deviceProperties + (
           'zInterfaceMapIgnoreNames', 'zInterfaceMapIgnoreTypes')

    addr = re.compile(r"(?P<type>inet6?) (?P<ip>\S+)/(?P<mask>\S+)")
    mac = re.compile(r"link/(?P<type>\S+) (?P<mac>[0-9a-fA-F:]+)")
    ifstart  = re.compile(r"^(?P<id>\d+):\s+(?P<name>\S+):\s*"
        "<(?P<flags>[^>]+)> mtu (?P<mtu>\d+) .*state (?P<state>\S+)")

    def process(self, device, results, log):
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        rm = self.relMap()
        iface = None
        for line in results.splitlines():
            matchIface = self.ifstart.match(line)
            if matchIface:
                # add previous interface
                if iface:
                  rm.append(iface)

                iface = self.objectMap()
                iface.interfaceName = matchIface.group('name')
                iface.id = self.prepId(iface.interfaceName)
                iface.ifindex = matchIface.group('id')
                iface.mtu = int(matchIface.group('mtu'))
                iface.operStatus = int("UP" not in matchIface.group('flags'))+1
                # TODO: speed, duplex

                # for loopback we usually get "state UNKNOWN"
                iface.adminStatus = {'UP':1,'DOWN':2}.get(matchIface.group('state'),0)
                if "LOOPBACK" in matchIface.group('flags') and not iface.adminStatus:
                  iface.adminStatus = iface.operStatus

                dontCollectIntNames = getattr(device, 'zInterfaceMapIgnoreNames', None)
                if dontCollectIntNames and re.search(dontCollectIntNames, iface.interfaceName):
                    log.debug("Interface %s matched the zInterfaceMapIgnoreNames zprop '%s'",
                              iface.interfaceName, dontCollectIntNames)
                    iface = None

            if not iface:
                continue

            # get the IP addresses of an interface
            matchAddr = self.addr.search(line)
            if matchAddr:
                ip, netmask = matchAddr.group('ip'), matchAddr.group('mask')
                netmask = self.maskToBits(netmask)
                if not hasattr(iface, 'setIpAddresses'):
                    iface.setIpAddresses = []
                iface.setIpAddresses.append("%s/%s" % (ip, netmask))

            # get MAC address and network type
            matchMac = self.mac.search(line)
            if matchMac:
                iface.macaddress=matchMac.group("mac").upper()
                iface.type = matchMac.group("type")
                if iface.type == "ether":
                  iface.type = "ethernetCsmacd"

                dontCollectIntTypes = getattr(device, 'zInterfaceMapIgnoreTypes', None)
                if dontCollectIntTypes and re.search(dontCollectIntTypes, iface.type):
                    log.debug("Interface %s type %s matched the zInterfaceMapIgnoreTypes zprop '%s'",
                      iface.interfaceName, iface.type, dontCollectIntTypes)
                    iface = None

        # add last interface
        if iface:
          rm.append(iface)

        return rm

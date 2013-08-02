import re

from Products.DataCollector.plugins.CollectorPlugin import LinuxCommandPlugin
from ZenPacks.zenoss.LinuxMonitor.lib.parse import parse_mdstat
from Products.DataCollector.plugins.DataMaps import MultiArgs

class lspci(LinuxCommandPlugin):
    maptype = "ExpansionCardMap"
    modname = "ZenPacks.zenoss.LinuxMonitor.LinuxExpansionCard"
    relname = "cards"
    compname = "hw"
    command = 'PATH="$PATH:/sbin:/usr/sbin" lspci -vmm'
    deviceProperties = LinuxCommandPlugin.deviceProperties + (
      'zLinuxExpansionCardMapMatchIgnoreTypes', )

    sectionPattern = re.compile(r"\n\s*\n")

    attributeMap = {
        'Slot':     'slot',
        'Class':    'type',
        'Driver':   'driver',
        'Module':   'module',
        'SVendor':  'subVendor',
        'SDevice':  'subModel',
        'Rev':      'revision',
        'ProgIf':   'progIface',
    }

    def process(self, device, results, log):
        log.info('Collecting expansion cards for device %s' % device.id)
        skiptypes = getattr(device, 'zLinuxExpansionCardMapMatchIgnoreTypes', [])
        rm = self.relMap()

        for section in self.sectionPattern.split(results.strip()):
            om = self.objectMap({'type':'Unknown'})
            vendor, model = ('Unknown', 'Unknown')

            for l in section.splitlines():
                match=re.match('(?P<tag>[^:]+):\s+(?P<value>.*)',l)
                if match:
                    omAttr = self.attributeMap.get(match.group('tag'))
                    if omAttr:
                        setattr(om, omAttr, match.group('value'))
                    elif match.group('tag') == 'PhySlot':
                        om.physicalSlot = int(match.group('value'))
                    elif match.group('tag') == 'Vendor':
                        vendor = match.group('value')
                    elif match.group('tag') == 'Device':
                        model = match.group('value')

            om.id = self.prepId('pci_%s' % (om.slot,))
            om.title = "%s: %s %s" % (om.type, vendor, model)
            om.setProductKey = MultiArgs(model, vendor)

            skip=False
            for regex in skiptypes:
                if re.search(regex,om.type,re.I):
                    log.info("Skipping '%s' as it matches zLinuxExpansionCardMapMatchIgnoreTypes.",
                        om.title)
                    skip=True
                    break

            if not skip:
                rm.append(om)

        return rm

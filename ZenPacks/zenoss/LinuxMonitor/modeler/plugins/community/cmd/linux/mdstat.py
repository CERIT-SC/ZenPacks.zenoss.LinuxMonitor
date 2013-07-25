from Products.DataCollector.plugins.CollectorPlugin import LinuxCommandPlugin
from ZenPacks.zenoss.LinuxMonitor.lib.parse import parse_mdstat

class mdstat(LinuxCommandPlugin):
    maptype = "LogicalDiskMap"
    modname = "ZenPacks.zenoss.LinuxMonitor.LogicalDiskMD"
    relname = "logicaldisks"
    compname = "hw"
    command = '/bin/cat /proc/mdstat'

    def process(self, device, results, log):
        log.info('Collecting Linux software raids for device %s' % device.id)
        rm = self.relMap()
        for device in parse_mdstat(results):
            om = self.objectMap()
            om.id = self.prepId('md%s' % device['id'])
            om.description = '/dev/md%s' % device['id']
            om.hostresindex = int(device['id'])
            om.diskType = device['type']
            om.size = device.get('blocks',0)
            om.stripesize = device.get('stripesize',0)
            rm.append(om)
        return rm

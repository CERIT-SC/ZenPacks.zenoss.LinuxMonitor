from Products.ZenRRD.CommandParser import CommandParser
from Products.ZenUtils.Utils import prepId as globalPrepId
from ZenPacks.zenoss.LinuxMonitor.lib.parse import parse_mdstat

class mdstat(CommandParser):
    componentScanValue = 'id'

    def prepId(self, id, subchar='_'):
        return globalPrepId(id, subchar)

    def dataForParser(self, context, dp):
        # This runs in the zenhub service, so it has access to the actual ZODB object
        print "Tady!?????"
        return dict(componentScanValue = getattr(context, self.componentScanValue))

    def processResults(self, cmd, result):
        """
        Process the results of "cat /proc/mdstat".
        """
        ifs = {}
        for dp in cmd.points:
            dp.component = dp.data['componentScanValue']
            points = ifs.setdefault(dp.component, {})
            points[dp.id] = dp

        for device in parse_mdstat(cmd.result.output):
            component = self.prepId('md%s' % device['id'])
            points = ifs.get(component, None)
            if points:
                for name,value in device.items():
                    dp = points.get(name, None)
                    if dp is not None:
                        if value in ('-',''): value = 0
                        result.values.append((dp, float(value)))

        print result
        return result

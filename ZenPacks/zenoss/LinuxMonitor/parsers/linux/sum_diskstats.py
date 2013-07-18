from Products.ZenRRD.CommandParser import CommandParser
import re

class sum_diskstats(CommandParser):
    def processResults(self, cmd, result):
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])

        names=[
            'rTotal','rMerged','rSectors','rTime',
            'wTotal','wMerged','wSectors','wTime',
            'ioPending','ioTime','ioTimeWeigh']

        values=[0]*len(names)
        for l in cmd.result.output.splitlines():
            data=l.split()

            # take only whole disks, match:
            # hd*, sd*, vd*, xvd*, cciss/cXdY, sr*
            if re.match('^((hd|sd|vd|xvd)[a-z]+|cciss/c\d+d\d+|sr\d+)$',data[2]):
                for i in range(len(names)):
                    values[i] += long(data[3+i])

        for (name,value) in zip(names,values):
            if datapointMap.has_key(name):
                result.values.append((datapointMap[name], long(value)))
        
        return result

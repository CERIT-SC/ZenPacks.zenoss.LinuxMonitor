##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2010, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from Products.ZenRRD.CommandParser import CommandParser

MULTIPLIER = {
    'kB' : 1024,
    'MB' : 1024 * 1024,
    'b' : 1
}

class mem(CommandParser):

    def processResults(self, cmd, result):
        """
        Process the results of "cat /proc/meminfo".
        """
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        data = [line.split(':', 1) for line in cmd.result.output.splitlines()]
        dataMap = dict()
        
        for id, vals in data:
            try:
                value, unit = vals.strip().split()
            except:
                value = vals
                unit = 1
            size = int(value) * MULTIPLIER.get(unit, 1)
            dataMap[id]=size

        # count additional data
        if ('MemTotal' in dataMap) and ('MemFree' in dataMap) and \
                ('Buffers' in dataMap) and ('Cached' in dataMap):
            dataMap['MemAllocated']=dataMap['MemTotal'] \
                - dataMap['MemFree'] \
                - dataMap['Buffers'] \
                - dataMap['Cached'] \

        if ('SwapTotal' in dataMap) and ('SwapFree' in dataMap):
            dataMap['SwapAllocated']=dataMap['SwapTotal']-dataMap['SwapFree']

        for id,size in dataMap.items():
            if id in datapointMap:
                result.values.append((datapointMap[id], size))
        
        return result

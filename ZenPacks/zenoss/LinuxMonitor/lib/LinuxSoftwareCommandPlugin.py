from Products.DataCollector.plugins.CollectorPlugin import SoftwareCommandPlugin
import Products.DataCollector.CommandPluginUtils as utils
import time
import re

class LinuxSoftwareCommandPlugin(SoftwareCommandPlugin):
    matchOS = ''
    vendor = 'Unknown Linux'

    def __init__(self):
        super(LinuxSoftwareCommandPlugin,self).__init__(self.parse)

    def condition(self, device, log):
        """
        If matchOS is specified, check device OS name and
        manufacturer for match.
        """
        if self.matchOS:
            match=re.compile(self.matchOS,re.I)
            return match.search(device.getOSManufacturerName()) or \
                match.search(device.getOSProductKey())
        else:
            return true

    def parse(self,results):
        """
        Read command output with each software package on line and
        convert into list of software dictionaries.
        """
        sw=[]
        t=time.localtime()
        for n in results.splitlines():
            sw.append(utils.createSoftwareDict(n,self.vendor,n,t))
        return sw

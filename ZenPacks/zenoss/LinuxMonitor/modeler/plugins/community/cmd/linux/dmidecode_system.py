import re
from ZenPacks.zenoss.LinuxMonitor.lib.DMICommandPlugin import DMICommandPlugin
from Products.DataCollector.plugins.DataMaps import MultiArgs

class dmidecode_system(DMICommandPlugin):
    maptype  = "DeviceMap" 
    compname = ""
    command  = 'sudo -n /usr/sbin/dmidecode --type 1'

    def check_number(self, v):
        return (not v in (None,'','Not Specified') and \
            v.find('O.E.M.')<0 and \
            v.find('123456')<0)

    def process(self, device, results, log):
        """Collect command-line information from this device"""
        log.info("Processing the dmidecode system info for device %s" % device.id)
        system=[results[x]['data'] for x in results if results[x]['type'] == '1']
        if len(system)==1:
            om=self.objectMap()

            # set only valid S/N
            sn=system[0].get('Serial Number',None)
            if self.check_number(sn):
                om.setHWSerialNumber=sn
                log.debug("setHWSerialNumber=%s" % (om.setHWSerialNumber))

            # set only valid Tag
            tag=system[0].get('SKU Number',None)
            if self.check_number(tag):
                om.setHWTag=tag
                log.debug("setHWTag=%s" % (om.setHWTag))

            # normalize product name (remove part number?)
            product=system[0].get('Product Name','None')
            if product:
                # IBM: "PRODUCT -[SKU]-"
                result=re.match('^(.+)\s+-\[(.+)\]-$',product)
                if result:
                    product=result.group(1)
                    om.setHWTag=result.group(2)

            om.setHWProductKey=MultiArgs(
                product,
                system[0].get('Manufacturer',None))

            log.debug("setHWProductKey=%s" % (om.setHWProductKey))
            return om

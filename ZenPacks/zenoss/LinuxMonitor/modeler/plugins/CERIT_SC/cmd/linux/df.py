##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2009, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


__doc__ = """df
Determine the filesystems to monitor
"""

import re

from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin

class df(CommandPlugin):
    """
    Run df -k to model filesystem information. Should work on most *nix.
    """
    maptype = "FilesystemMap" 
    command = '/bin/df -PkT 2>/dev/null'
    compname = "os"
    relname = "filesystems"
    modname = "Products.ZenModel.FileSystem"
    deviceProperties = CommandPlugin.deviceProperties + (
      'zFileSystemMapIgnoreNames', 'zFileSystemMapIgnoreTypes')

    oses = ['Linux']

    def condition(self, device, log):
        return device.os.uname == '' or device.os.uname in self.oses


    def process(self, device, results, log):
        log.info('Collecting filesystems for device %s' % device.id)
        skipfsnames = getattr(device, 'zFileSystemMapIgnoreNames', None)
        skipfstypes = getattr(device, 'zFileSystemMapIgnoreTypes', None)
        rm = self.relMap()
        rlines = results.split("\n")
        bline = ""
        for line in rlines:
            if line.startswith("Filesystem"): continue
            om = self.objectMap()
            spline = line.split()
            if len(spline) == 1:
                bline = spline[0]
                continue
            if bline: 
                spline.insert(0,bline)
                bline = None
            if len(spline) != 7: continue
            (om.storageDevice, fs, tblocks, u, a, p, om.mount) = spline

            if re.search('^(root|[xj]|btr|reiser)fs|ext[234]$',fs):
                om.type = "fixedDisk"
            elif fs in ['fat','vfat','msdos']:
                om.type = "removableDisk"
            elif fs in ['iso9660','udf']:
                om.types = "compactDisk"
            elif fs in ['nfs','afs','gpfs','cifs','ceph','coda','9p']: #gfs2, ocfs
                om.type = "networkDisk"
            elif re.search('(hugetlb|ram|tmp)fs$',fs):
                om.type = "ramDisk"
            else:
                om.type = "other"

            if skipfsnames and re.search(skipfsnames,om.mount):
                log.info("Skipping %s as it matches zFileSystemMapIgnoreNames.",
                    om.mount)
                continue

            if skipfstypes and om.type in skipfstypes:
                log.info("Skipping %s (%s) as it matches zFileSystemMapIgnoreTypes.",
                    om.mount, om.type)
                continue

            if tblocks == "-":
                om.totalBlocks = 0
            else:
                try:
                    om.totalBlocks = long(tblocks)
                except ValueError:
                    # Ignore this filesystem if what we thought was total
                    # blocks isn't a number.
                    continue

            om.blockSize = 1024
            om.id = self.prepId(om.mount)
            om.title = om.mount
            rm.append(om)
        return rm

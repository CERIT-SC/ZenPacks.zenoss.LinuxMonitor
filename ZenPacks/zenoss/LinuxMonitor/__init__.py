##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2009, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


import logging
import Globals
import os.path
from Products.ZenModel.ZenPack import ZenPackBase

log = logging.getLogger('zen.LinuxMonitor')

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

class ZenPack(ZenPackBase):
    packZProperties = [
        ('zThresholdMemoryCrit', 95, 'int'),
        ('zThresholdSwapCrit', 85, 'int'),
        ('zThresholdFilesystemLow', 90, 'int'),
        ('zThresholdFilesystemCrit', 99, 'int'),
        ('zThresholdLoadOffset', 1.3, 'float'),
        ('zLinuxExpansionCardMapMatchIgnoreTypes',[
            'bridge$',
            'smbus',
            'system peripheral',
            'performance counters',
            '(signal processing|usb) controller',
            'ram memory',
            '^pic$'
        ],'lines'),
    ]
    
    def install(self, app):
        """
        Set the collector plugins for Server/SSH/Linux.
        """
        linux = app.dmd.Devices.createOrganizer('/Server/SSH/Linux')
        linux.setZenProperty( 'zCollectorPlugins', 
                              ['zenoss.cmd.uname',
                               'zenoss.cmd.uname_a',
                               'zenoss.cmd.linux.cpuinfo', 
                               'zenoss.cmd.linux.memory', 
                               'community.cmd.linux.ip', 
                               'community.cmd.linux.netstat_an', 
                               'zenoss.cmd.linux.netstat_rn', 
                               'zenoss.cmd.linux.process',
                               'community.cmd.linux.df',
                               'community.cmd.linux.lsb_release',
                               'community.cmd.linux.dmidecode',
                               'community.cmd.linux.sys_block',
                               'community.cmd.linux.mdstat',
                               'community.cmd.linux.lspci',
                               'community.cmd.linux.sw.dpkg',
                               'community.cmd.linux.sw.rpm' ] ) 
        
        linux.register_devtype('Linux Server', 'SSH')
        ZenPackBase.install(self, app)
                                   
    def remove(self, app, leaveObjects=False):
        """
        Remove the collector plugins.
        """
        ZenPackBase.remove(self, app, leaveObjects)
        if not leaveObjects:
            try:
                # Using findChild here to avoid finding /Server/Linux
                # accidentally via acquisition.
                linux = app.dmd.findChild('Devices/Server/SSH/Linux')
                linux.zCollectorPlugins = []
            except AttributeError:
                # No /Server/SSH/Linux device class to remove.
                pass

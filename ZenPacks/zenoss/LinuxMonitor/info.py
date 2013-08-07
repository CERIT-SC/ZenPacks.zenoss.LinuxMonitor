###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/#
###########################################################################

from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from Products.ZenUtils.Utils import convToUnits

from ZenPacks.zenoss.LinuxMonitor.interfaces import *

class LinuxExpansionCardInfo(ComponentInfo):
    implements(ILinuxExpansionCardInfo)

    serialNumber = ProxyProperty("serialNumber")
    slot = ProxyProperty("slot")
    physicalSlot = ProxyProperty("physicalSlot")
    subVendor = ProxyProperty("subVendor")
    subModel = ProxyProperty("subModel")
    revision = ProxyProperty("revision")
    progIface = ProxyProperty("progIface")
    driver = ProxyProperty("driver")
    module = ProxyProperty("module")

    @property
    @info
    def manufacturer(self):
        pc = self._object.productClass()
        if (pc):
            return pc.manufacturer()

    @property
    @info
    def product(self):
        return self._object.productClass()

    @property
    def status(self):
        if not hasattr(self._object, 'statusString'): return 'Unknown'
        else: return self._object.statusString()


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

from Products.Zuul.form import schema
from Products.Zuul.infos.component import IComponentInfo

class ILinuxExpansionCardInfo(IComponentInfo):
    """
    Info adapter for ILinuxExpansionCardInfo components.
    """
    status = schema.Text(title=u"Status", readonly=True, group='Overview')
    slot = schema.Int(title=u"Slot", readonly=True, group='Details')
    physicalSlot = schema.Int(title=u"Physical slot", readonly=True, group='Details')
    manufacturer = schema.Entity(title=u"Manufacturer", readonly=True, group='Details')
    product = schema.Entity(title=u"Model", readonly=True, group='Details')
    subVendor = schema.Text(title=u"Subsystem manufacturer", readonly=True, group='Details')
    subModel = schema.Text(title=u"Subsystem model", readonly=True, group='Details')
    revision = schema.Text(title=u"Revision", readonly=True, group='Details')
    progIface = schema.Text(title=u"Programming interface", readonly=True, group='Details')
    driver = schema.List(title=u"Kernel driver(s)", readonly=True, group='Details')
    module = schema.List(title=u"Kernel module(s)", readonly=True, group='Details')

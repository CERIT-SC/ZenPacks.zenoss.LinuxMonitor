# ZenPacks.zenoss.LinuxMonitor

## About

This is a [Zenoss](http://www.zenoss.com) monitoring system extension (ZenPack)
for advanced Linux monitoring **based on original Zenoss Core**
[LinuxMonitor](https://github.com/zenoss/ZenPacks.zenoss.LinuxMonitor) plugin.
Features:

* NEW: system load graph
* memory and swap utilization graphs with allocated space
* filesystem two-level thresholds and support for `zFileSystemMapIgnoreTypes`

## Installation

Requirements:

* Zenoss 3.2 or later

### Normal Installation (packaged egg)

No prebuilt packages yet.

### Developer Installation (link mode)

    git clone git://github.com/CERIT-SC/ZenPacks.zenoss.LinuxMonitor.git
    zenpack --link --install ZenPacks.zenoss.LinuxMonitor
    zenoss restart

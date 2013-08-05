# ZenPacks.zenoss.LinuxMonitor

## About

This is a [Zenoss](http://www.zenoss.com) monitoring system extension (ZenPack)
for advanced Linux monitoring **based on original Zenoss Core's**
[LinuxMonitor](https://github.com/zenoss/ZenPacks.zenoss.LinuxMonitor) plugin.
This module is a drop-in replacement of existing module by Zenoss,
*original module must be uninstalled first*.

Features:

* **NEW:** system load graph
* **NEW:** total system disk I/O activity graph
* **NEW:** modeler community.cmd.linux.lbs_release to get OS name/version
* **NEW:** modeler community.cmd.linux.dmidecode to get hardware
 * name and manufacturer
 * serial number
 * tag (SKU Number)
 * rack chassis size
* **NEW:** software RAID (md) monitoring via `/proc/mdstat`
 * detect RAID type, size, stripe size
 * status monitoring
 * I/O activity graph per device
* **NEW:** very simple hard disks modeling via `/sys/block/`
 * detect vendor and type only
 * I/O activity graph per device
* **NEW:** collect installed software
 * Red Hat via `rpm`
 * Debian and Ubuntu via `dpkg-query`
* **NEW:** modeler community.cmd.linux.lspci to get expansion cards
 * configurable types to ignore via `zLinuxExpansionCardMapMatchIgnoreTypes`
* improved memory and swap utilization graphs
  * graph allocated space
  * nice event texts (e.g.: `memory threshold: 97.0% used (3.8GB free)`)
* improved filesystem monitoring
  * per filesystem monitoring to avoid hangups on e.g. NFS problems
  * model only last filesystem mounted on each mount point
  * two-level thresholds (warning, critical)
  * nice event texts (e.g.: `disk space threshold: 99.3% used (1.7MB free)`)
  * support for `zFileSystemMapIgnoreTypes`
* improved CPU utilization graph
  * show time spent in nice, I/O wait, steal, IRQ, soft IRQ
  * all graph points are now stacked area
* improved network interfaces monitoring
  * **NEW:** modeler community.cmd.linux.ip using `ip address show`
  * interface graphs: throughput, packets, errors
* improved IP service monitoring
  * **NEW:** inherited community.cmd.linux.netstat_an
  * do not model services listening on 127.* or ::1
  * identify IPv6 protocols: tcp6, udp6
* improved process monitoring
  * added graphs for process CPU time, RSS, count
* improved processor modeling
  * added shortened manufacturer

## Installation

Requirements:

* Zenoss 3.2 or later
* [Advanced Device Details ZenPack](http://wiki.zenoss.org/ZenPack:Advanced_Device_Details)
* uninstall existing Zenoss Core's [LinuxMonitor](https://github.com/zenoss/ZenPacks.zenoss.LinuxMonitor)

### Normal Installation (packaged egg)

No prebuilt packages yet.

### Developer Installation (link mode)

    git clone git://github.com/CERIT-SC/ZenPacks.zenoss.LinuxMonitor.git
    zenpack --link --install ZenPacks.zenoss.LinuxMonitor
    zenoss restart

## Screenshots

* Overview
* Performance graphs
* Hard Disks
* Logical Disks
* Interfaces
* OS Processes
* File Systems
* Processors
* Software

## Bug reports

Please report your problems or feature requests via [GitHub issues tracker](https://github.com/CERIT-SC/ZenPacks.zenoss.LinuxMonitor/issues)

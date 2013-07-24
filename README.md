# ZenPacks.zenoss.LinuxMonitor

## About

This is a [Zenoss](http://www.zenoss.com) monitoring system extension (ZenPack)
for advanced Linux monitoring **based on original Zenoss Core's**
[LinuxMonitor](https://github.com/zenoss/ZenPacks.zenoss.LinuxMonitor) plugin.

Features:

* **NEW:** system load graph
* **NEW:** total system disk I/O activity graph
* **NEW:** modeler community.cmd.linux.lbs_release to get OS name/version
* **NEW:** modeler community.cmd.linux.dmidecode to get hardware
 * name and manufacturer
 * serial number
 * tag (SKU Number)
 * rack chassis size
* **NEW:** software RAID (md) monitoring
* **NEW:** collect installed software
 * Red Hat via `rpm'
 * Debian and Ubuntu via `dpkg-query'
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
  * **NEW:** inherited community.cmd.linux.ifconfig supress error messages

## Installation

Requirements:

* Zenoss 3.2 or later

### Normal Installation (packaged egg)

No prebuilt packages yet.

### Developer Installation (link mode)

    git clone git://github.com/CERIT-SC/ZenPacks.zenoss.LinuxMonitor.git
    zenpack --link --install ZenPacks.zenoss.LinuxMonitor
    zenoss restart

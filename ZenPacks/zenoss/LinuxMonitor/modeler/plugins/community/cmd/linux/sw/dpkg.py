from ZenPacks.zenoss.LinuxMonitor.lib.LinuxSoftwareCommandPlugin import LinuxSoftwareCommandPlugin

class dpkg(LinuxSoftwareCommandPlugin):
    command = 'dpkg-query -W --showformat \'${Package}_${Version}_${Architecture}\n\''
    matchOS = '(Debian|Ubuntu)'

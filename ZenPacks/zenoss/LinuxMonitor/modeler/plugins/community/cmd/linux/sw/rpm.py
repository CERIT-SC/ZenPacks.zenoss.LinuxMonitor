from ZenPacks.zenoss.LinuxMonitor.lib.LinuxSoftwareCommandPlugin import LinuxSoftwareCommandPlugin

class rpm(LinuxSoftwareCommandPlugin):
    command = 'rpm -qa --qf \'%{NAME}_%{RELEASE}_%{ARCH}\\n\''
    matchOS = '(RedHat|CentOS|Fedora)'

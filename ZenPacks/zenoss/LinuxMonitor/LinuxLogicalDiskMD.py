from ZenPacks.community.deviceAdvDetail.LogicalDisk import *
from ZenPacks.community.deviceAdvDetail.HWStatus import *

class LinuxLogicalDiskMD(LogicalDisk,HWStatus):
    """LogicalDisk object MD"""

    statusmap = {
        0:  (DOT_GREY,   SEV_WARNING,  'Unknown'),
        1:  (DOT_GREY,   SEV_WARNING,  'Unknown'),
        2:  (DOT_GREEN,  SEV_CLEAN,    'Online'),
        3:  (DOT_RED,    SEV_CRITICAL, 'Offline'),
        4:  (DOT_YELLOW, SEV_WARNING,  'Non-degraded w/ failed disks'),
        5:  (DOT_ORANGE, SEV_ERROR,    'Degraded'),
        6:  (DOT_RED,    SEV_CRITICAL, 'Failed'),

        10: (DOT_YELLOW, SEV_WARNING,  'Resync pending'),
        11: (DOT_BLUE,   SEV_INFO,     'Resync delayed'),
        12: (DOT_ORANGE, SEV_WARNING,  'Resync unknown'),
        13: (DOT_BLUE,   SEV_INFO,     'Resyncing'),

        15: (DOT_GREEN,  SEV_WARNING,  'Check pending'),
        16: (DOT_BLUE,   SEV_INFO,     'Check delayed'),
        17: (DOT_YELLOW, SEV_WARNING,  'Check unknown'),
        18: (DOT_BLUE,   SEV_INFO,     'Checking'),

        20: (DOT_ORANGE, SEV_ERROR,    'Recovery pending'),
        21: (DOT_YELLOW, SEV_WARNING,  'Recovery delayed'),
        22: (DOT_ORANGE, SEV_ERROR,    'Recovery unknown'),
        23: (DOT_YELLOW, SEV_WARNING,  'Recovering'),

        30: (DOT_RED,    SEV_CRITICAL, 'Unknown task'),
    }

    factory_type_information = ({   
        'id'             : 'HardDisk',
        'meta_type'      : 'HardDisk',
        'description'    : 'Linux Software RAID Logical Disks',
        'icon'           : 'HardDisk_icon.gif',
        'product'        : 'ZenModel',
        'immediate_view' : 'viewLinuxLogicalDiskMD',
        'actions'        : ({
            'id'            : 'status',
            'name'          : 'Status',
            'action'        : 'viewLinuxLogicalDiskMD',
            'permissions'   : (ZEN_VIEW, ),
        },{
            'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE, ),
        },),
    },)

    def getRRDTemplates(self):
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates


InitializeClass(LinuxLogicalDiskMD)

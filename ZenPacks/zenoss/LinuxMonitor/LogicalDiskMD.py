from ZenPacks.community.deviceAdvDetail.LogicalDisk import *
from ZenPacks.community.deviceAdvDetail.HWStatus import *

class LogicalDiskMD(LogicalDisk,HWStatus):
    """LogicalDisk objectMD"""

    statusmap = {
        0:  (DOT_GREY,   SEV_WARNING,  'Unknown'),
        1:  (DOT_GREY,   SEV_WARNING,  'Unknown'),
        2:  (DOT_GREEN,  SEV_CLEAN,    'Online'),
        3:  (DOT_RED,    SEV_CRITICAL, 'Offline'),
        4:  (DOT_YELLOW, SEV_WARNING,  'Non-degraded w/ failed disks'),
        5:  (DOT_ORANGE, SEV_ERROR,    'Degraded'),
        6:  (DOT_RED,    SEV_CRITICAL, 'Failed'),

        10: (DOT_GREEN,  SEV_WARNING,  'Resync pending'),
        11: (DOT_GREEN,  SEV_INFO,     'Resyncing'),
        12: (DOT_GREEN,  SEV_INFO,     'Check pending'),
        13: (DOT_GREEN,  SEV_INFO,     'Checking'),
        14: (DOT_ORANGE, SEV_ERROR,    'Recovery pending'),
        15: (DOT_YELLOW, SEV_WARNING,  'Recovering'),
        16: (DOT_RED,    SEV_CRITICAL, 'Unknown task'),
    }

    factory_type_information = ({   
        'id'             : 'HardDisk',
        'meta_type'      : 'HardDisk',
        'description'    : 'Linux Software RAID Logical Disks',
        'icon'           : 'HardDisk_icon.gif',
        'product'        : 'ZenModel',
        'immediate_view' : 'viewLogicalDiskMD',
        'actions'        : ({
            'id'            : 'status',
            'name'          : 'Status',
            'action'        : 'viewLogicalDiskMD',
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


InitializeClass(LogicalDiskMD)

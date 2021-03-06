from Globals import InitializeClass
from Products.ZenModel.ExpansionCard import ExpansionCard
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_DEVICE

class LinuxExpansionCard(ExpansionCard):
    """Linux Expansion Card"""

    type = ''
    subVendor = ''
    subModel = ''
    physicalSlot = None
    revision = ''
    progIface = ''
    driver = []
    module = []

    monitor = False

    _properties = ExpansionCard._properties + (
        {'id':'type',         'type':'string', 'mode':'w'},
        {'id':'subVendor',    'type':'string', 'mode':'w'},
        {'id':'subModel',     'type':'string', 'mode':'w'},
        {'id':'physicalSlot', 'type':'int',    'mode':'w'},
        {'id':'driver',       'type':'lines',  'mode':'w'},
        {'id':'module',       'type':'lines',  'mode':'w'},
        {'id':'revision',     'type':'string', 'mode':'w'},
        {'id':'progIface',    'type':'string', 'mode':'w'},
    )

    factory_type_information = ({   
        'id'             : 'ExpansionCard',
        'meta_type'      : 'ExpansionCard',
        'description'    : 'Linux Expansion Card',
        'icon'           : 'ExpansionCard_icon.gif',
        'product'        : 'ZenModel',
        'factory'        : 'manage_addExpansionCard',
        'immediate_view' : 'viewLinuxExpansionCard',
        'actions'        : ({
            'id'            : 'status',
            'name'          : 'Status',
            'action'        : 'viewLinuxExpansionCard',
            'permissions'   : (ZEN_VIEW, ),
        },),
    },)


InitializeClass(LinuxExpansionCard)

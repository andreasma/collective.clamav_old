from plone.app.registry.browser import controlpanel

from plone.z3cform import layout

from collective.ClamAV import _
from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IContextSourceBinder
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapts
from zope.interface import implements


from collective.ClamAV import _
from collective.ClamAV.interfaces import IAVScannerSettings





class ClamAVControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IAVScannerSettings)


    def __init__(self, context):
        super(ClamAVControlPanelAdapter, self).__init__(context)
        properties = getToolByName(context, 'portal_properties')
        self.context = properties.clamav_properties

    # Connection type
    def get_clamav_connection(self):
        return getattr(self.context, 'clamav_connection', "socket")

    def set_clamav_connection(self, value):
        self.context._updateProperty('clamav_connection', value)

    clamav_connection = property(get_clamav_connection, set_clamav_connection)

    # Socket path
    def get_clamav_socket(self):
        return getattr(self.context, 'clamav_socket', '/var/run/clamd')

    def set_clamav_socket(self, value):
        self.context._updateProperty('clamav_socket', value)

    clamav_socket = property(get_clamav_socket, set_clamav_socket)

    # Host
    def get_clamav_host(self):
        return getattr(self.context, 'clamav_host', 'localhost')

    def set_clamav_host(self, value):
        self.context._updateProperty('clamav_host', value)

    clamav_host = property(get_clamav_host, set_clamav_host)

    # Port
    def get_clamav_port(self):
        return int(getattr(self.context, 'clamav_port', '3310'))

    def set_clamav_port(self, value):
        self.context._updateProperty('clamav_port', value)

    clamav_port = property(get_clamav_port, set_clamav_port)

    # Timeout
    def get_clamav_timeout(self):
        return int(getattr(self.context, 'clamav_timeout', '120'))

    def set_clamav_timeout(self, value):
        self.context._updateProperty('clamav_timeout', value)

    clamav_timeout = property(get_clamav_timeout, set_clamav_timeout)




class ClamAVControlPanelForm(controlpanel.RegistryEditForm):
    schema= IAVScannerSettings
    label = _(u'ClamAV Plone Settings')
    description = _(u"""""")

    def updateFields(self):
            super(ClamAVControlPanelForm, self).updateFields()

    def updateWidgets(self):
            super(ClamAVControlPanelForm, self).updateWidgets()



class ClamAVControlPanelView(controlpanel.ControlPanelFormWrapper):
    form = ClamAVControlPanelForm

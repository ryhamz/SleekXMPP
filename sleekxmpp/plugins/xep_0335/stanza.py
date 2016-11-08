from sleekxmpp.xmlstream import ElementBase


class JsonContainers(ElementBase):

    name = 'json'
    namespace = 'urn:xmpp:json:0'
    plugin_attrib = 'json'
    interfaces = set(['json'])
    is_extension = True
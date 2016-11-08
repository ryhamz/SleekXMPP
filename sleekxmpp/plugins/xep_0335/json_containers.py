
import logging

from sleekxmpp import Message
from sleekxmpp.plugins import BasePlugin
from sleekxmpp.xmlstream.handler import Callback
from sleekxmpp.xmlstream.matcher import StanzaPath
from sleekxmpp.xmlstream import register_stanza_plugin, JID
from sleekxmpp.plugins.xep_0335 import JsonContainers, stanza


log = logging.getLogger(__name__)


class XEP_0335(BasePlugin):

    name = 'xep_0335'
    description = 'XEP-0335: JSON Containers'
    dependencies = set()
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Message, JsonContainers)

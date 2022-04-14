from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AtmAAL5Frame(Base):
    __slots__ = ()
    _SDM_NAME = "atmAAL5Frame"
    _SDM_ATT_MAP = {
        "HeaderLlcHeader": "atmAAL5Frame.header.llcHeader-1",
        "HeaderAal5OUI": "atmAAL5Frame.header.aal5OUI-2",
        "HeaderProtocolType": "atmAAL5Frame.header.protocolType-3",
    }

    def __init__(self, parent, list_op=False):
        super(AtmAAL5Frame, self).__init__(parent, list_op)

    @property
    def HeaderLlcHeader(self):
        """
        Display Name: LLC Header
        Default Value: 0xAAAA03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLlcHeader"])
        )

    @property
    def HeaderAal5OUI(self):
        """
        Display Name: AAL5 OUI
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAal5OUI"]))

    @property
    def HeaderProtocolType(self):
        """
        Display Name: Protocol Type
        Default Value: 0x0800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

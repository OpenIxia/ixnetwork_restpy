from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CiscoHDLC(Base):
    __slots__ = ()
    _SDM_NAME = "ciscoHDLC"
    _SDM_ATT_MAP = {
        "HeaderAddress": "ciscoHDLC.header.address-1",
        "HeaderControl": "ciscoHDLC.header.control-2",
        "HeaderProtocolType": "ciscoHDLC.header.protocolType-3",
        "ClnsPadPad": "ciscoHDLC.header.clnsPad.pad-4",
    }

    def __init__(self, parent, list_op=False):
        super(CiscoHDLC, self).__init__(parent, list_op)

    @property
    def HeaderAddress(self):
        """
        Display Name: Cisco HDLC Address
        Default Value: 0x0F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAddress"]))

    @property
    def HeaderControl(self):
        """
        Display Name: Cisco HDLC Control
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderControl"]))

    @property
    def HeaderProtocolType(self):
        """
        Display Name: Cisco HDLC Protocol Type
        Default Value: 0x0800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolType"])
        )

    @property
    def ClnsPadPad(self):
        """
        Display Name: Cisco Pad
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClnsPadPad"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

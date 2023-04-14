from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NFapiP7P19sHeader(Base):
    __slots__ = ()
    _SDM_NAME = "nFapiP7P19sHeader"
    _SDM_ATT_MAP = {
        "HeaderSn": "nFapiP7P19sHeader.header.sn-1",
        "HeaderTotalSduLength": "nFapiP7P19sHeader.header.totalSduLength-2",
        "HeaderByteOffset": "nFapiP7P19sHeader.header.byteOffset-3",
        "HeaderTransmitTimeStamp": "nFapiP7P19sHeader.header.transmitTimeStamp-4",
    }

    def __init__(self, parent, list_op=False):
        super(NFapiP7P19sHeader, self).__init__(parent, list_op)

    @property
    def HeaderSn(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSn"]))

    @property
    def HeaderTotalSduLength(self):
        """
        Display Name: Total SDU Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTotalSduLength"])
        )

    @property
    def HeaderByteOffset(self):
        """
        Display Name: Byte Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderByteOffset"])
        )

    @property
    def HeaderTransmitTimeStamp(self):
        """
        Display Name: Transmit Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTransmitTimeStamp"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

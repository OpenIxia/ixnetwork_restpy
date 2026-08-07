from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcRequestorTimestampExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcRequestorTimestampExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "TsethTxTimestamp": "mrcRequestorTimestampExtendedTransportHeader.tseth.txTimestamp-1",
        "TsethTsr": "mrcRequestorTimestampExtendedTransportHeader.tseth.tsr-2",
        "TsethReserved": "mrcRequestorTimestampExtendedTransportHeader.tseth.reserved-3",
        "TsethFtype": "mrcRequestorTimestampExtendedTransportHeader.tseth.ftype-4",
    }

    def __init__(self, parent, list_op=False):
        super(MrcRequestorTimestampExtendedTransportHeader, self).__init__(
            parent, list_op
        )

    @property
    def TsethTxTimestamp(self):
        """
        Display Name: Requestor Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsethTxTimestamp"])
        )

    @property
    def TsethTsr(self):
        """
        Display Name: Timestamp Resolution
        Default Value: 0
        Value Format: decimal
        Available enum values: 128ns, 0, Implementation defined, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TsethTsr"]))

    @property
    def TsethReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TsethReserved"]))

    @property
    def TsethFtype(self):
        """
        Display Name: TSETH Type
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TsethFtype"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

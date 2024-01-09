from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Roe(Base):
    __slots__ = ()
    _SDM_NAME = "roe"
    _SDM_ATT_MAP = {
        "Subtype": "roe.header.subtype-1",
        "FlowID": "roe.header.flowID-2",
        "Length": "roe.header.length-3",
        "OrderInfoSeqNumber": "roe.header.orderInfo.seqNumber-4",
        "OrderInfoTimeStamp": "roe.header.orderInfo.timeStamp-5",
    }

    def __init__(self, parent, list_op=False):
        super(Roe, self).__init__(parent, list_op)

    @property
    def Subtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        Available enum values: RoE control subtype, 0, Reserved1, 1, RoE structure-agnostic data subtype, 2, RoE structure-aware CPRI data subtype, 3, RoE Slow C and M CPRI subtype, 4, Reserved2, 5, RoE native time domain data subtype, 16, RoE native frequency domain data subtype, 17, RoE native PRACH data subtype, 18, Reserved3, 19, Mapped subTypes, 128, Reserved4, 192, Experimental, 252
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Subtype"]))

    @property
    def FlowID(self):
        """
        Display Name: FlowID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlowID"]))

    @property
    def Length(self):
        """
        Display Name: Length
        Default Value: 0x0000
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Length"]))

    @property
    def OrderInfoSeqNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OrderInfoSeqNumber"])
        )

    @property
    def OrderInfoTimeStamp(self):
        """
        Display Name: Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OrderInfoTimeStamp"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

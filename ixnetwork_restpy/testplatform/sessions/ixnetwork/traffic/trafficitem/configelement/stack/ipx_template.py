from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipx(Base):
    __slots__ = ()
    _SDM_NAME = "ipx"
    _SDM_ATT_MAP = {
        "Checksum": "ipx.header.checksum-1",
        "Length": "ipx.header.length-2",
        "TransportControl": "ipx.header.transportControl-3",
        "Type": "ipx.header.type-4",
        "DstNetwork": "ipx.header.dstNetwork-5",
        "DstNode": "ipx.header.dstNode-6",
        "DstSocket": "ipx.header.dstSocket-7",
        "SrcNetwork": "ipx.header.srcNetwork-8",
        "SrcNode": "ipx.header.srcNode-9",
        "SrcSocket": "ipx.header.srcSocket-10",
    }

    def __init__(self, parent, list_op=False):
        super(Ipx, self).__init__(parent, list_op)

    @property
    def Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Checksum"]))

    @property
    def Length(self):
        """
        Display Name: Packet length
        Default Value: 43
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Length"]))

    @property
    def TransportControl(self):
        """
        Display Name: Transport control
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TransportControl"])
        )

    @property
    def Type(self):
        """
        Display Name: Packet type
        Default Value: 4
        Value Format: decimal
        Available enum values: Hello or SAP, 0, Routing Information Protocol, 1, Echo Packet, 2, Error Packet, 3, PEP: Packet Exchange Protocol, 4, SPX: Sequenced Packet Exchange, 5, NCP: Netware Core Protocol, 17
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def DstNetwork(self):
        """
        Display Name: Destination network
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DstNetwork"]))

    @property
    def DstNode(self):
        """
        Display Name: Destination node
        Default Value: 0x000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DstNode"]))

    @property
    def DstSocket(self):
        """
        Display Name: Destination socket
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DstSocket"]))

    @property
    def SrcNetwork(self):
        """
        Display Name: Source network
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcNetwork"]))

    @property
    def SrcNode(self):
        """
        Display Name: Source node
        Default Value: 0x000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcNode"]))

    @property
    def SrcSocket(self):
        """
        Display Name: Source socket
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcSocket"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

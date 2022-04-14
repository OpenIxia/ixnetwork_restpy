from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PppLCP(Base):
    __slots__ = ()
    _SDM_NAME = "pppLCP"
    _SDM_ATT_MAP = {
        "HeaderOpcode": "pppLCP.header.opcode-1",
        "HeaderIdentifier": "pppLCP.header.identifier-2",
        "HeaderLength": "pppLCP.header.length-3",
        "OptionsType": "pppLCP.header.data.options.type-4",
        "OptionsLength": "pppLCP.header.data.options.length-5",
        "TlvLength": "pppLCP.header.data.options.tlv.length-6",
        "TlvData": "pppLCP.header.data.options.tlv.data-7",
        "MagicNumberNumber": "pppLCP.header.data.magicNumber.number-8",
        "LcpDataLength": "pppLCP.header.data.lcpData.length-9",
        "LcpDataData": "pppLCP.header.data.lcpData.data-10",
        "RejectedProtocolId": "pppLCP.header.data.rejectedProtocol.id-11",
    }

    def __init__(self, parent, list_op=False):
        super(PppLCP, self).__init__(parent, list_op)

    @property
    def HeaderOpcode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        Available enum values: Configure-Request, 1, Configure-Ack, 2, Configure-Nak, 3, Configure-Reject, 4, Terminate-Request, 5, Terminate-Ack, 6, Code-Reject, 7, Protocol-Reject, 8, Echo-Request, 9, Echo-Reply, 10, Discard-Request, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOpcode"]))

    @property
    def HeaderIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderIdentifier"])
        )

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def OptionsType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        Available enum values: RESERVED, 0, Maximum-Receive-Unit, 1, Authentication-Protocol, 3, Quality-Protocol, 4, Magic-Number, 5, Protocol-Field-Compression, 7, Address-and-Control-Field-Compression, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionsType"]))

    @property
    def OptionsLength(self):
        """
        Display Name: Length of TLV
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionsLength"]))

    @property
    def TlvLength(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TlvLength"]))

    @property
    def TlvData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TlvData"]))

    @property
    def MagicNumberNumber(self):
        """
        Display Name: Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MagicNumberNumber"])
        )

    @property
    def LcpDataLength(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpDataLength"]))

    @property
    def LcpDataData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpDataData"]))

    @property
    def RejectedProtocolId(self):
        """
        Display Name: Protocol Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RejectedProtocolId"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TDSResponse(Base):
    __slots__ = ()
    _SDM_NAME = "TDS_Response"
    _SDM_ATT_MAP = {
        "HeaderType": "TDS_Response.header.Type-1",
        "HeaderStatus": "TDS_Response.header.Status-2",
        "HeaderLength": "TDS_Response.header.Length-3",
        "HeaderChannel": "TDS_Response.header.Channel-4",
        "HeaderPacket number": "TDS_Response.header.Packet number-5",
        "HeaderWindow": "TDS_Response.header.Window-6",
        "Token 0xff Done in Proc0xff": "TDS_Response.header.Token 0xff Done in Proc.0xff-7",
        "Token 0xff Done in ProcStatus flags": "TDS_Response.header.Token 0xff Done in Proc.Status flags-8",
        "Token 0xff Done in ProcOperation": "TDS_Response.header.Token 0xff Done in Proc.Operation-9",
        "Token 0xff Done in ProcRow count": "TDS_Response.header.Token 0xff Done in Proc.Row count-10",
        "Token 0x00 Unknown Token Type0x00": "TDS_Response.header.Token 0x00 Unknown Token Type.0x00-11",
        "Token 0x00 Unknown Token TypeLength": "TDS_Response.header.Token 0x00 Unknown Token Type.Length-12",
        "Token 0x00 Unknown Token Type 20x00": "TDS_Response.header.Token 0x00 Unknown Token Type 2.0x00-13",
        "Token 0x00 Unknown Token Type 2Length": "TDS_Response.header.Token 0x00 Unknown Token Type 2.Length-14",
        "Token 0x00 Unknown Token Type 2Unknown": "TDS_Response.header.Token 0x00 Unknown Token Type 2.Unknown-15",
    }

    def __init__(self, parent, list_op=False):
        super(TDSResponse, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderStatus(self):
        """
        Display Name: Status
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderStatus"]))

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0x0039
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderChannel(self):
        """
        Display Name: Channel
        Default Value: 0x0033
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderChannel"]))

    @property
    def HeaderPacketnumber(self):
        """
        Display Name: Packet number
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPacket number"])
        )

    @property
    def HeaderWindow(self):
        """
        Display Name: Window
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderWindow"]))

    @property
    def Token0xffDoneinProc0xff(self):
        """
        Display Name: 0xff
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Token 0xff Done in Proc0xff"])
        )

    @property
    def Token0xffDoneinProcStatusflags(self):
        """
        Display Name: Status flags
        Default Value: 0x0100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Token 0xff Done in ProcStatus flags"]
            ),
        )

    @property
    def Token0xffDoneinProcOperation(self):
        """
        Display Name: Operation
        Default Value: 0xC700
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Token 0xff Done in ProcOperation"]),
        )

    @property
    def Token0xffDoneinProcRowcount(self):
        """
        Display Name: Row count
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Token 0xff Done in ProcRow count"]),
        )

    @property
    def Token0x00UnknownTokenType0x00(self):
        """
        Display Name: 0x00
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Token 0x00 Unknown Token Type0x00"]),
        )

    @property
    def Token0x00UnknownTokenTypeLength(self):
        """
        Display Name: Length
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Token 0x00 Unknown Token TypeLength"]
            ),
        )

    @property
    def Token0x00UnknownTokenType20x00(self):
        """
        Display Name: 0x00
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Token 0x00 Unknown Token Type 20x00"]
            ),
        )

    @property
    def Token0x00UnknownTokenType2Length(self):
        """
        Display Name: Length
        Default Value: 0x7900
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Token 0x00 Unknown Token Type 2Length"]
            ),
        )

    @property
    def Token0x00UnknownTokenType2Unknown(self):
        """
        Display Name: Unknown
        Default Value: 0xAC0000000100000000000026040404000000FE0000E0000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Token 0x00 Unknown Token Type 2Unknown"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

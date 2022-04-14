from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TDSRemoteProcedureCall(Base):
    __slots__ = ()
    _SDM_NAME = "TDS_Remote_Procedure_Call"
    _SDM_ATT_MAP = {
        "HeaderType": "TDS_Remote_Procedure_Call.header.Type-1",
        "HeaderStatus": "TDS_Remote_Procedure_Call.header.Status-2",
        "HeaderLength": "TDS_Remote_Procedure_Call.header.Length-3",
        "HeaderChannel": "TDS_Remote_Procedure_Call.header.Channel-4",
        "HeaderPacket number": "TDS_Remote_Procedure_Call.header.Packet number-5",
        "HeaderWindow": "TDS_Remote_Procedure_Call.header.Window-6",
        "Packet data stream headersTotal length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Packet data stream headers.Total length-7",
        "Packet data stream headersHeaderLength": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Packet data stream headers.Header.Length-8",
        "Packet data stream headersHeaderType": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Packet data stream headers.Header.Type-9",
        "HeaderTransaction descriptor": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Packet data stream headers.Header.Transaction descriptor-10",
        "HeaderField0": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Packet data stream headers.Header.field0-11",
        "Remote Procedure CallProcedure name length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Procedure name length-12",
        "Remote Procedure CallStored procedure ID": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Stored procedure ID-13",
        "Option flagsWith recompile": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Option flags.With recompile-14",
        "Option flagsNo metadata": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Option flags.No metadata-15",
        "Option flagsReuse metadata": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Option flags.Reuse metadata-16",
        "Parameter1Field1": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter1.field1-17",
        "Parameter1Name length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter1.Name length-18",
        "Type info (INTNTYPE)Type": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter1.Type info (INTNTYPE).Type-19",
        "Type info (INTNTYPE)Maximal length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter1.Type info (INTNTYPE).Maximal length-20",
        "ValueLength": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter1.Value.Length-21",
        "ValueData": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter1.Value.Data-22",
        "Parameter2Name length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Name length-23",
        "Parameter2Status flags": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Status flags-24",
        "Type info (NVARCHARTYPE - NVarChar)Type": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Type info (NVARCHARTYPE - NVarChar).Type-25",
        "Type info (NVARCHARTYPE - NVarChar)Maximal length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Type info (NVARCHARTYPE - NVarChar).Maximal length-26",
        "CollationCollation bits": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Type info (NVARCHARTYPE - NVarChar).Collation.Collation bits-27",
        "CollationSortId": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Type info (NVARCHARTYPE - NVarChar).Collation.SortId-28",
        "Parameter2ValueLength": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Value.Length-29",
        "Parameter2ValueData": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter2.Value.Data-30",
        "Parameter3Name length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Name length-31",
        "Parameter3Status flags": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Status flags-32",
        "Parameter3Type info (NVARCHARTYPE - NVarChar)Type": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Type info (NVARCHARTYPE - NVarChar).Type-33",
        "Parameter3Type info (NVARCHARTYPE - NVarChar)Maximal length": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Type info (NVARCHARTYPE - NVarChar).Maximal length-34",
        "CollationCollation Bits": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Type info (NVARCHARTYPE - NVarChar).Collation.Collation Bits-35",
        "Type info (nvarchartype - nvarchar)CollationSortId": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Type info (NVARCHARTYPE - NVarChar).Collation.SortId-36",
        "Parameter3ValueLength": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Value.Length-37",
        "Parameter3ValueData": "TDS_Remote_Procedure_Call.header.Remote Procedure Call.Parameter3.Value.Data-38",
    }

    def __init__(self, parent, list_op=False):
        super(TDSRemoteProcedureCall, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x03
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
        Default Value: 0x0067
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderChannel(self):
        """
        Display Name: Channel
        Default Value: 0
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
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderWindow"]))

    @property
    def PacketdatastreamheadersTotallength(self):
        """
        Display Name: Total length
        Default Value: 0x16000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Packet data stream headersTotal length"]
            ),
        )

    @property
    def PacketdatastreamheadersHeaderLength(self):
        """
        Display Name: Length
        Default Value: 0x12000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Packet data stream headersHeaderLength"]
            ),
        )

    @property
    def PacketdatastreamheadersHeaderType(self):
        """
        Display Name: Type
        Default Value: 0x0200
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Packet data stream headersHeaderType"]
            ),
        )

    @property
    def HeaderTransactiondescriptor(self):
        """
        Display Name: Transaction descriptor
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTransaction descriptor"])
        )

    @property
    def HeaderField0(self):
        """
        Display Name: Outstanding request count
        Default Value: 0x01000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderField0"]))

    @property
    def RemoteProcedureCallProcedurenamelength(self):
        """
        Display Name: Procedure name length
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Remote Procedure CallProcedure name length"]
            ),
        )

    @property
    def RemoteProcedureCallStoredprocedureID(self):
        """
        Display Name: Stored procedure ID
        Default Value: 0x0D00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Remote Procedure CallStored procedure ID"]
            ),
        )

    @property
    def OptionflagsWithrecompile(self):
        """
        Display Name: With recompile
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Option flagsWith recompile"])
        )

    @property
    def OptionflagsNometadata(self):
        """
        Display Name: No metadata
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Option flagsNo metadata"])
        )

    @property
    def OptionflagsReusemetadata(self):
        """
        Display Name: Reuse metadata
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Option flagsReuse metadata"])
        )

    @property
    def Parameter1Field1(self):
        """
        Display Name: Field0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter1Field1"])
        )

    @property
    def Parameter1Namelength(self):
        """
        Display Name: Name length
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter1Name length"])
        )

    @property
    def TypeinfoINTNTYPEType(self):
        """
        Display Name: Type
        Default Value: 0x26
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Type info (INTNTYPE)Type"])
        )

    @property
    def TypeinfoINTNTYPEMaximallength(self):
        """
        Display Name: Maximal length
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type info (INTNTYPE)Maximal length"]
            ),
        )

    @property
    def ValueLength(self):
        """
        Display Name: Length
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueLength"]))

    @property
    def ValueData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueData"]))

    @property
    def Parameter2Namelength(self):
        """
        Display Name: Name length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter2Name length"])
        )

    @property
    def Parameter2Statusflags(self):
        """
        Display Name: Status flags
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter2Status flags"])
        )

    @property
    def TypeinfoNVARCHARTYPENVarCharType(self):
        """
        Display Name: Type
        Default Value: 0xE7
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type info (NVARCHARTYPE - NVarChar)Type"]
            ),
        )

    @property
    def TypeinfoNVARCHARTYPENVarCharMaximallength(self):
        """
        Display Name: Maximal length
        Default Value: 0x401F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type info (NVARCHARTYPE - NVarChar)Maximal length"]
            ),
        )

    @property
    def CollationCollationbits(self):
        """
        Display Name: Collation bits
        Default Value: 0x0904D000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollationCollation bits"])
        )

    @property
    def CollationSortId(self):
        """
        Display Name: SortId
        Default Value: 0x34
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollationSortId"])
        )

    @property
    def Parameter2ValueLength(self):
        """
        Display Name: Length
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter2ValueLength"])
        )

    @property
    def Parameter2ValueData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter2ValueData"])
        )

    @property
    def Parameter3Namelength(self):
        """
        Display Name: Name length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter3Name length"])
        )

    @property
    def Parameter3Statusflags(self):
        """
        Display Name: Status flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter3Status flags"])
        )

    @property
    def Parameter3TypeinfoNVARCHARTYPENVarCharType(self):
        """
        Display Name: Type
        Default Value: 0xE7
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Parameter3Type info (NVARCHARTYPE - NVarChar)Type"]
            ),
        )

    @property
    def Parameter3TypeinfoNVARCHARTYPENVarCharMaximallength(self):
        """
        Display Name: Maximal length
        Default Value: 0x401F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Parameter3Type info (NVARCHARTYPE - NVarChar)Maximal length"
                ]
            ),
        )

    @property
    def CollationCollationBits(self):
        """
        Display Name: Collation Bits
        Default Value: 0x0904D000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollationCollation Bits"])
        )

    @property
    def TypeinfonvarchartypenvarcharCollationSortId(self):
        """
        Display Name: SortId
        Default Value: 0x34
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type info (nvarchartype - nvarchar)CollationSortId"]
            ),
        )

    @property
    def Parameter3ValueLength(self):
        """
        Display Name: Length
        Default Value: 0x2200
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter3ValueLength"])
        )

    @property
    def Parameter3ValueData(self):
        """
        Display Name: Data
        Default Value: 0x640072006F00700020007400610062006C00650020006E0065007700730079006200
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Parameter3ValueData"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

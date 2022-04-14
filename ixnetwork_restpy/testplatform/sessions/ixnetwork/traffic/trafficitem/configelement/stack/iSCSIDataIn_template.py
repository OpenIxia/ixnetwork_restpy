from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ISCSIDataIn(Base):
    __slots__ = ()
    _SDM_NAME = "iSCSI_Data_In"
    _SDM_ATT_MAP = {
        "HeaderOpcode": "iSCSI_Data_In.header.Opcode-1",
        "HeaderFlags": "iSCSI_Data_In.header.Flags-2",
        "HeaderTotalAHSLength": "iSCSI_Data_In.header.TotalAHSLength-3",
        "HeaderUnknown": "iSCSI_Data_In.header.Unknown-4",
        "HeaderDataSegmentLength": "iSCSI_Data_In.header.DataSegmentLength-5",
        "HeaderLUN": "iSCSI_Data_In.header.LUN-6",
        "HeaderInitiatorTaskTag": "iSCSI_Data_In.header.InitiatorTaskTag-7",
        "HeaderTargetTransferTag": "iSCSI_Data_In.header.TargetTransferTag-8",
        "HeaderStatSN": "iSCSI_Data_In.header.StatSN-9",
        "HeaderExpCmdSN": "iSCSI_Data_In.header.ExpCmdSN-10",
        "HeaderMaxCmdSN": "iSCSI_Data_In.header.MaxCmdSN-11",
        "HeaderDataSN": "iSCSI_Data_In.header.DataSN-12",
        "HeaderBufferoffset": "iSCSI_Data_In.header.Bufferoffset-13",
        "HeaderResidualCount": "iSCSI_Data_In.header.ResidualCount-14",
        "HeaderHeaderDigest": "iSCSI_Data_In.header.HeaderDigest-15",
    }

    def __init__(self, parent, list_op=False):
        super(ISCSIDataIn, self).__init__(parent, list_op)

    @property
    def HeaderOpcode(self):
        """
        Display Name: Opcode
        Default Value: 0x25
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOpcode"]))

    @property
    def HeaderFlags(self):
        """
        Display Name: Flags
        Default Value: 0x80
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlags"]))

    @property
    def HeaderTotalAHSLength(self):
        """
        Display Name: TotalAHSLength
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTotalAHSLength"])
        )

    @property
    def HeaderUnknown(self):
        """
        Display Name: Unknown
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderUnknown"]))

    @property
    def HeaderDataSegmentLength(self):
        """
        Display Name: DataSegmentLength
        Default Value: 0x000016
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDataSegmentLength"])
        )

    @property
    def HeaderLUN(self):
        """
        Display Name: LUN
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLUN"]))

    @property
    def HeaderInitiatorTaskTag(self):
        """
        Display Name: InitiatorTaskTag
        Default Value: 0x00000010
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderInitiatorTaskTag"])
        )

    @property
    def HeaderTargetTransferTag(self):
        """
        Display Name: TargetTransferTag
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTargetTransferTag"])
        )

    @property
    def HeaderStatSN(self):
        """
        Display Name: StatSN
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderStatSN"]))

    @property
    def HeaderExpCmdSN(self):
        """
        Display Name: ExpCmdSN
        Default Value: 0x00000010
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderExpCmdSN"])
        )

    @property
    def HeaderMaxCmdSN(self):
        """
        Display Name: MaxCmdSN
        Default Value: 0x00000051
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMaxCmdSN"])
        )

    @property
    def HeaderDataSN(self):
        """
        Display Name: DataSN
        Default Value: 0x00000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDataSN"]))

    @property
    def HeaderBufferoffset(self):
        """
        Display Name: Bufferoffset
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBufferoffset"])
        )

    @property
    def HeaderResidualCount(self):
        """
        Display Name: ResidualCount
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderResidualCount"])
        )

    @property
    def HeaderHeaderDigest(self):
        """
        Display Name: HeaderDigest
        Default Value: 0x5F7F4CAE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHeaderDigest"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

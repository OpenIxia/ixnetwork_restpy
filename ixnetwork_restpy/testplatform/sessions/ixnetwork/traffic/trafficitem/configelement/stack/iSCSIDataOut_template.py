from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ISCSIDataOut(Base):
    __slots__ = ()
    _SDM_NAME = "iSCSI_Data_Out"
    _SDM_ATT_MAP = {
        "HeaderOpcode": "iSCSI_Data_Out.header.Opcode-1",
        "HeaderFlags": "iSCSI_Data_Out.header.Flags-2",
        "HeaderTotalAHSLength": "iSCSI_Data_Out.header.TotalAHSLength-3",
        "HeaderUnknown ": "iSCSI_Data_Out.header.Unknown -4",
        "HeaderDataSegmentLength": "iSCSI_Data_Out.header.DataSegmentLength-5",
        "HeaderLUN": "iSCSI_Data_Out.header.LUN-6",
        "HeaderInitiatorTaskTag": "iSCSI_Data_Out.header.InitiatorTaskTag-7",
        "HeaderTargetTransferTag": "iSCSI_Data_Out.header.TargetTransferTag-8",
        "HeaderField0": "iSCSI_Data_Out.header.field0-9",
        "HeaderDataSN": "iSCSI_Data_Out.header.DataSN-10",
        "HeaderBufferOffset": "iSCSI_Data_Out.header.BufferOffset-11",
        "HeaderHeaderDigest": "iSCSI_Data_Out.header.HeaderDigest-12",
    }

    def __init__(self, parent, list_op=False):
        super(ISCSIDataOut, self).__init__(parent, list_op)

    @property
    def HeaderOpcode(self):
        """
        Display Name: Opcode
        Default Value: 0x05
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

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderUnknown "])
        )

    @property
    def HeaderDataSegmentLength(self):
        """
        Display Name: DataSegmentLength
        Default Value: 0x00000C
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
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTargetTransferTag"])
        )

    @property
    def HeaderField0(self):
        """
        Display Name: ExpStatSN
        Default Value: 0x00000011
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderField0"]))

    @property
    def HeaderDataSN(self):
        """
        Display Name: DataSN
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDataSN"]))

    @property
    def HeaderBufferOffset(self):
        """
        Display Name: BufferOffset
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBufferOffset"])
        )

    @property
    def HeaderHeaderDigest(self):
        """
        Display Name: HeaderDigest
        Default Value: 0x586ACAAD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHeaderDigest"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

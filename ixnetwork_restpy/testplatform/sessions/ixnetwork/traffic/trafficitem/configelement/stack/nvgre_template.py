from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Nvgre(Base):
    __slots__ = ()
    _SDM_NAME = "nvgre"
    _SDM_ATT_MAP = {
        "ChecksumPresent": "nvgre.header.checksumPresent-1",
        "Reserved1": "nvgre.header.reserved1-2",
        "KeyPresent": "nvgre.header.keyPresent-3",
        "SequencePresent": "nvgre.header.sequencePresent-4",
        "Reserved2": "nvgre.header.reserved2-5",
        "Version": "nvgre.header.version-6",
        "Protocol": "nvgre.header.protocol-7",
        "WithChecksumChecksum": "nvgre.header.checksumHolder.withChecksum.checksum-8",
        "WithChecksumReserved": "nvgre.header.checksumHolder.withChecksum.reserved-9",
        "ChecksumHolderNoChecksum": "nvgre.header.checksumHolder.noChecksum-10",
        "Vsid": "nvgre.header.vsid-11",
        "FlowId": "nvgre.header.flowId-12",
        "SequenceHolderSequenceNum": "nvgre.header.sequenceHolder.sequenceNum-13",
        "SequenceHolderNoSequenceNum": "nvgre.header.sequenceHolder.noSequenceNum-14",
    }

    def __init__(self, parent, list_op=False):
        super(Nvgre, self).__init__(parent, list_op)

    @property
    def ChecksumPresent(self):
        """
        Display Name: Checksum Present
        Default Value: 0
        Value Format: decimal
        Available enum values: 0:No Checksum, 0, 1:Has Checksum, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChecksumPresent"])
        )

    @property
    def Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved1"]))

    @property
    def KeyPresent(self):
        """
        Display Name: Key Present
        Default Value: 1
        Value Format: decimal
        Available enum values: 0:No Key field, 0, 1:Has Key field, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyPresent"]))

    @property
    def SequencePresent(self):
        """
        Display Name: Sequence Number Present
        Default Value: 0
        Value Format: decimal
        Available enum values: 0:No sequence number field, 0, 1:Has sequence number field, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequencePresent"])
        )

    @property
    def Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved2"]))

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Protocol(self):
        """
        Display Name: Protocol
        Default Value: 0x6558
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Protocol"]))

    @property
    def WithChecksumChecksum(self):
        """
        Display Name: NVGRE Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["WithChecksumChecksum"])
        )

    @property
    def WithChecksumReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["WithChecksumReserved"])
        )

    @property
    def ChecksumHolderNoChecksum(self):
        """
        Display Name: No Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChecksumHolderNoChecksum"])
        )

    @property
    def Vsid(self):
        """
        Display Name: Virtual Subnet ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Vsid"]))

    @property
    def FlowId(self):
        """
        Display Name: Flow ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlowId"]))

    @property
    def SequenceHolderSequenceNum(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceHolderSequenceNum"])
        )

    @property
    def SequenceHolderNoSequenceNum(self):
        """
        Display Name: No Sequence Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceHolderNoSequenceNum"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

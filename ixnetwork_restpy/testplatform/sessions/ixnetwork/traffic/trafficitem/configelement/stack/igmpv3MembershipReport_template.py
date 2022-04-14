from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Igmpv3MembershipReport(Base):
    __slots__ = ()
    _SDM_NAME = "igmpv3MembershipReport"
    _SDM_ATT_MAP = {
        "HeaderType": "igmpv3MembershipReport.header.type-1",
        "HeaderReserved": "igmpv3MembershipReport.header.reserved-2",
        "HeaderChecksum": "igmpv3MembershipReport.header.checksum-3",
        "HeaderReserved": "igmpv3MembershipReport.header.reserved-4",
        "HeaderNumberOfGroupRecords": "igmpv3MembershipReport.header.numberOfGroupRecords-5",
        "GroupRecordRecordType": "igmpv3MembershipReport.header.groupRecords.groupRecord.recordType-6",
        "GroupRecordAuxiliaryDataLength": "igmpv3MembershipReport.header.groupRecords.groupRecord.auxiliaryDataLength-7",
        "GroupRecordNumberOfSources": "igmpv3MembershipReport.header.groupRecords.groupRecord.numberOfSources-8",
        "GroupRecordMulticastAddress": "igmpv3MembershipReport.header.groupRecords.groupRecord.multicastAddress-9",
        "MulticastSourcesMulticastSource": "igmpv3MembershipReport.header.groupRecords.groupRecord.multicastSources.multicastSource-10",
        "AuxiliaryDataLength": "igmpv3MembershipReport.header.groupRecords.groupRecord.auxiliaryData.length-11",
        "AuxiliaryDataData": "igmpv3MembershipReport.header.groupRecords.groupRecord.auxiliaryData.data-12",
    }

    def __init__(self, parent, list_op=False):
        super(Igmpv3MembershipReport, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderChecksum"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderNumberOfGroupRecords(self):
        """
        Display Name: Number of group records
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNumberOfGroupRecords"])
        )

    @property
    def GroupRecordRecordType(self):
        """
        Display Name: Record type
        Default Value: 1
        Value Format: decimal
        Available enum values: MODE_IS_INCLUDE, 1, MODE_IS_EXCLUDE, 2, CHANGE_TO_INCLUDE_MODE, 3, CHANGE_TO_EXCLUDE_MODE, 4, ALLOW_NEW_SOURCES, 5, BLOCK_OLD_SOURCES, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordRecordType"])
        )

    @property
    def GroupRecordAuxiliaryDataLength(self):
        """
        Display Name: Auxiliary data length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupRecordAuxiliaryDataLength"]),
        )

    @property
    def GroupRecordNumberOfSources(self):
        """
        Display Name: Number of sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordNumberOfSources"])
        )

    @property
    def GroupRecordMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordMulticastAddress"])
        )

    @property
    def MulticastSourcesMulticastSource(self):
        """
        Display Name: Multicast source
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastSourcesMulticastSource"]),
        )

    @property
    def AuxiliaryDataLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuxiliaryDataLength"])
        )

    @property
    def AuxiliaryDataData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuxiliaryDataData"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

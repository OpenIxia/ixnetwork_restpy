from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mldv2Report(Base):
    __slots__ = ()
    _SDM_NAME = "mldv2Report"
    _SDM_ATT_MAP = {
        "Mldv2ListenerReportType": "mldv2Report.mldv2ListenerReport.type-1",
        "Mldv2ListenerReportReserved": "mldv2Report.mldv2ListenerReport.reserved-2",
        "Mldv2ListenerReportMldv2Checksum": "mldv2Report.mldv2ListenerReport.mldv2Checksum-3",
        "Mldv2ListenerReportReserved": "mldv2Report.mldv2ListenerReport.reserved-4",
        "Mldv2ListenerReportNrOfMcastAddresses": "mldv2Report.mldv2ListenerReport.nrOfMcastAddresses-5",
        "Mldv2AddressRecordRecordType": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.recordType-6",
        "Mldv2AddressRecordAuxDataLen": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.auxDataLen-7",
        "Mldv2AddressRecordNrOfSourceAddresses": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.nrOfSourceAddresses-8",
        "Mldv2AddressRecordMulticastAddress": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.multicastAddress-9",
        "SourceAddressRecordSourceAddress": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.sourceAddressRecord.sourceAddress-10",
        "AuxiliaryDataLength": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.auxiliaryData.length-11",
        "AuxiliaryDataData": "mldv2Report.mldv2ListenerReport.mldv2AddressRecord.auxiliaryData.data-12",
    }

    def __init__(self, parent, list_op=False):
        super(Mldv2Report, self).__init__(parent, list_op)

    @property
    def Mldv2ListenerReportType(self):
        """
        Display Name: Type
        Default Value: 143
        Value Format: decimal
        Available enum values: Type 143, 143, Type 206, 206
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerReportType"])
        )

    @property
    def Mldv2ListenerReportReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerReportReserved"])
        )

    @property
    def Mldv2ListenerReportMldv2Checksum(self):
        """
        Display Name: MLDv2 checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerReportMldv2Checksum"]),
        )

    @property
    def Mldv2ListenerReportReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerReportReserved"])
        )

    @property
    def Mldv2ListenerReportNrOfMcastAddresses(self):
        """
        Display Name: Nr. of mcast addresses
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Mldv2ListenerReportNrOfMcastAddresses"]
            ),
        )

    @property
    def Mldv2AddressRecordRecordType(self):
        """
        Display Name: Record Type
        Default Value: 1
        Value Format: decimal
        Available enum values: IS_IN, 1, IS_EX, 2, TO_IN, 3, TO_EX, 4, ALLOW, 5, BLOCK, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2AddressRecordRecordType"])
        )

    @property
    def Mldv2AddressRecordAuxDataLen(self):
        """
        Display Name: Aux Data Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2AddressRecordAuxDataLen"])
        )

    @property
    def Mldv2AddressRecordNrOfSourceAddresses(self):
        """
        Display Name: Nr. of source addresses
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Mldv2AddressRecordNrOfSourceAddresses"]
            ),
        )

    @property
    def Mldv2AddressRecordMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Mldv2AddressRecordMulticastAddress"]
            ),
        )

    @property
    def SourceAddressRecordSourceAddress(self):
        """
        Display Name: Source address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SourceAddressRecordSourceAddress"]),
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

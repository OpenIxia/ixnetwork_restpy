from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Iec618831(Base):
    __slots__ = ()
    _SDM_NAME = "iec61883-1"
    _SDM_ATT_MAP = {
        "CIP-1Cip1firstBit": "iec61883-1.header.CIP-1.cip1firstBit-1",
        "CIP-1Cip1secondBit": "iec61883-1.header.CIP-1.cip1secondBit-2",
        "CIP-1SourceIdentifier": "iec61883-1.header.CIP-1.sourceIdentifier-3",
        "CIP-1DataBlockSize": "iec61883-1.header.CIP-1.dataBlockSize-4",
        "CIP-1QuadletPaddingCount": "iec61883-1.header.CIP-1.quadletPaddingCount-5",
        "CIP-1FractionNumber": "iec61883-1.header.CIP-1.fractionNumber-6",
        "CIP-1SourcePacketHeader": "iec61883-1.header.CIP-1.sourcePacketHeader-7",
        "CIP-1Reserved": "iec61883-1.header.CIP-1.Reserved-8",
        "CIP-1DataBlockCount": "iec61883-1.header.CIP-1.dataBlockCount-9",
        "CIP-2Cip2firstBit": "iec61883-1.header.CIP-2.cip2firstBit-10",
        "CIP-2Cip2secondBit": "iec61883-1.header.CIP-2.cip2secondBit-11",
        "CIP-2StreamFormat": "iec61883-1.header.CIP-2.streamFormat-12",
        "8BitFDFFormatDependentField": "iec61883-1.header.selectFDF.8BitFDF.formatDependentField-13",
        "8BitFDFSynchronisationTiming": "iec61883-1.header.selectFDF.8BitFDF.synchronisationTiming-14",
        "24BitFDFFormatDependentField": "iec61883-1.header.selectFDF.24BitFDF.formatDependentField-15",
        "24BitFDFAvtpSourcePacketHeader": "iec61883-1.header.selectFDF.24BitFDF.avtpSourcePacketHeader-16",
    }

    def __init__(self, parent, list_op=False):
        super(Iec618831, self).__init__(parent, list_op)

    @property
    def CIP1Cip1firstBit(self):
        """
        Display Name: CIP 1 First Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1Cip1firstBit"])
        )

    @property
    def CIP1Cip1secondBit(self):
        """
        Display Name: CIP 1 Second Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1Cip1secondBit"])
        )

    @property
    def CIP1SourceIdentifier(self):
        """
        Display Name: SID
        Default Value: 63
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1SourceIdentifier"])
        )

    @property
    def CIP1DataBlockSize(self):
        """
        Display Name: DBS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1DataBlockSize"])
        )

    @property
    def CIP1QuadletPaddingCount(self):
        """
        Display Name: QPC
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1QuadletPaddingCount"])
        )

    @property
    def CIP1FractionNumber(self):
        """
        Display Name: FN
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1FractionNumber"])
        )

    @property
    def CIP1SourcePacketHeader(self):
        """
        Display Name: SPH
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1SourcePacketHeader"])
        )

    @property
    def CIP1Reserved(self):
        """
        Display Name: RSV
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CIP-1Reserved"]))

    @property
    def CIP1DataBlockCount(self):
        """
        Display Name: DBC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-1DataBlockCount"])
        )

    @property
    def CIP2Cip2firstBit(self):
        """
        Display Name: CIP 2 First Bit
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-2Cip2firstBit"])
        )

    @property
    def CIP2Cip2secondBit(self):
        """
        Display Name: CIP 2 Second bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-2Cip2secondBit"])
        )

    @property
    def CIP2StreamFormat(self):
        """
        Display Name: FMT
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CIP-2StreamFormat"])
        )

    @property
    def _8BitFDFFormatDependentField(self):
        """
        Display Name: FDF
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["8BitFDFFormatDependentField"])
        )

    @property
    def _8BitFDFSynchronisationTiming(self):
        """
        Display Name: SYT
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["8BitFDFSynchronisationTiming"])
        )

    @property
    def _24BitFDFFormatDependentField(self):
        """
        Display Name: FDF
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["24BitFDFFormatDependentField"])
        )

    @property
    def _24BitFDFAvtpSourcePacketHeader(self):
        """
        Display Name: AVTP SourcePacketHeader Timestamp
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["24BitFDFAvtpSourcePacketHeader"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

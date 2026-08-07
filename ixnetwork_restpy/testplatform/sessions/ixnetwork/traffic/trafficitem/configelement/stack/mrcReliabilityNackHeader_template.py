from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcReliabilityNackHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcReliabilityNackHeader"
    _SDM_ATT_MAP = {
        "ReliabilityNackHeaderNethType": "mrcReliabilityNackHeader.header.reliabilityNackHeader.nethType-1",
        "ReliabilityNackHeaderNxt": "mrcReliabilityNackHeader.header.reliabilityNackHeader.nxt-2",
        "ReliabilityNackHeaderRes1": "mrcReliabilityNackHeader.header.reliabilityNackHeader.res1-3",
        "ReliabilityNackHeaderNackReason": "mrcReliabilityNackHeader.header.reliabilityNackHeader.nackReason-4",
        "ReliabilityNackHeaderVendorInfo": "mrcReliabilityNackHeader.header.reliabilityNackHeader.vendorInfo-5",
        "ReliabilityNackHeaderEntropy": "mrcReliabilityNackHeader.header.reliabilityNackHeader.entropy-6",
        "ReliabilityNackHeaderSpdcid": "mrcReliabilityNackHeader.header.reliabilityNackHeader.spdcid-7",
        "ReliabilityNackHeaderDpdcid": "mrcReliabilityNackHeader.header.reliabilityNackHeader.dpdcid-8",
        "ReliabilityNackHeaderRes2": "mrcReliabilityNackHeader.header.reliabilityNackHeader.res2-9",
        "ReliabilityNackHeaderNackPsn": "mrcReliabilityNackHeader.header.reliabilityNackHeader.nackPsn-10",
        "CcStateCcType": "mrcReliabilityNackHeader.header.ccState.ccType-11",
        "CcStateCcFl": "mrcReliabilityNackHeader.header.ccState.ccFl-12",
        "CcStateCcRes": "mrcReliabilityNackHeader.header.ccState.ccRes-13",
        "CcStateCcTxTimestamp": "mrcReliabilityNackHeader.header.ccState.ccTxTimestamp-14",
    }

    def __init__(self, parent, list_op=False):
        super(MrcReliabilityNackHeader, self).__init__(parent, list_op)

    @property
    def ReliabilityNackHeaderNethType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderNethType"]),
        )

    @property
    def ReliabilityNackHeaderNxt(self):
        """
        Display Name: Next Header
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderNxt"])
        )

    @property
    def ReliabilityNackHeaderRes1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderRes1"])
        )

    @property
    def ReliabilityNackHeaderNackReason(self):
        """
        Display Name: NACK Reason
        Default Value: 1
        Value Format: decimal
        Available enum values: TRIMMED, 1, TRIMMED_LASTHOP, 2, NO_BITMAP, 6, NO_PKT_BUFFER, 7, NO_RESOURCE, 10, PSN_OOR_WINDOW, 11, UNEXP_EVENT, 25
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderNackReason"]),
        )

    @property
    def ReliabilityNackHeaderVendorInfo(self):
        """
        Display Name: Vendor Info
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderVendorInfo"]),
        )

    @property
    def ReliabilityNackHeaderEntropy(self):
        """
        Display Name: Entropy
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderEntropy"])
        )

    @property
    def ReliabilityNackHeaderSpdcid(self):
        """
        Display Name: Source PDCID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderSpdcid"])
        )

    @property
    def ReliabilityNackHeaderDpdcid(self):
        """
        Display Name: Destination PDCID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderDpdcid"])
        )

    @property
    def ReliabilityNackHeaderRes2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderRes2"])
        )

    @property
    def ReliabilityNackHeaderNackPsn(self):
        """
        Display Name: NACK PSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilityNackHeaderNackPsn"])
        )

    @property
    def CcStateCcType(self):
        """
        Display Name: CC Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CcStateCcType"]))

    @property
    def CcStateCcFl(self):
        """
        Display Name: CC Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CcStateCcFl"]))

    @property
    def CcStateCcRes(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CcStateCcRes"]))

    @property
    def CcStateCcTxTimestamp(self):
        """
        Display Name: TX Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CcStateCcTxTimestamp"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

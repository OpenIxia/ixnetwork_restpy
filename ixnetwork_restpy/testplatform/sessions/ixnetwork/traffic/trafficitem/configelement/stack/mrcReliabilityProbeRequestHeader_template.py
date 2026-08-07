from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcReliabilityProbeRequestHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcReliabilityProbeRequestHeader"
    _SDM_ATT_MAP = {
        "ReliabilityProbeRequestHeaderPethType": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.pethType-1",
        "ReliabilityProbeRequestHeaderNxt": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.nxt-2",
        "ReliabilityProbeRequestHeaderRes1": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.res1-3",
        "ReliabilityProbeRequestHeaderRes2": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.res2-4",
        "ReliabilityProbeRequestHeaderVendorInfo": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.vendorInfo-5",
        "ReliabilityProbeRequestHeaderProbeId": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.probeId-6",
        "ReliabilityProbeRequestHeaderRes3": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.res3-7",
        "ReliabilityProbeRequestHeaderSpdcid": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.spdcid-8",
        "ReliabilityProbeRequestHeaderDpdcid": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.dpdcid-9",
        "ReliabilityProbeRequestHeaderTxTimestamp": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.txTimestamp-10",
        "ReliabilityProbeRequestHeaderTsr": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.tsr-11",
        "ReliabilityProbeRequestHeaderRes4": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.res4-12",
        "ReliabilityProbeRequestHeaderFtype": "mrcReliabilityProbeRequestHeader.reliabilityProbeRequestHeader.ftype-13",
    }

    def __init__(self, parent, list_op=False):
        super(MrcReliabilityProbeRequestHeader, self).__init__(parent, list_op)

    @property
    def ReliabilityProbeRequestHeaderPethType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderPethType"]
            ),
        )

    @property
    def ReliabilityProbeRequestHeaderNxt(self):
        """
        Display Name: Next Header
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderNxt"]),
        )

    @property
    def ReliabilityProbeRequestHeaderRes1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderRes1"]),
        )

    @property
    def ReliabilityProbeRequestHeaderRes2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderRes2"]),
        )

    @property
    def ReliabilityProbeRequestHeaderVendorInfo(self):
        """
        Display Name: Vendor Info
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderVendorInfo"]
            ),
        )

    @property
    def ReliabilityProbeRequestHeaderProbeId(self):
        """
        Display Name: Probe ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderProbeId"]
            ),
        )

    @property
    def ReliabilityProbeRequestHeaderRes3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderRes3"]),
        )

    @property
    def ReliabilityProbeRequestHeaderSpdcid(self):
        """
        Display Name: Source PDCID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderSpdcid"]
            ),
        )

    @property
    def ReliabilityProbeRequestHeaderDpdcid(self):
        """
        Display Name: Destination PDCID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderDpdcid"]
            ),
        )

    @property
    def ReliabilityProbeRequestHeaderTxTimestamp(self):
        """
        Display Name: TX Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderTxTimestamp"]
            ),
        )

    @property
    def ReliabilityProbeRequestHeaderTsr(self):
        """
        Display Name: Timestamp Resolution
        Default Value: 0
        Value Format: decimal
        Available enum values: 128ns, 0, Implementation defined, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderTsr"]),
        )

    @property
    def ReliabilityProbeRequestHeaderRes4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderRes4"]),
        )

    @property
    def ReliabilityProbeRequestHeaderFtype(self):
        """
        Display Name: TSETH Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReliabilityProbeRequestHeaderFtype"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

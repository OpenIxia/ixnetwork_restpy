from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcReliabilitySackHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcReliabilitySackHeader"
    _SDM_ATT_MAP = {
        "ReliabilitySackHeaderSethType": "mrcReliabilitySackHeader.header.reliabilitySackHeader.sethType-1",
        "ReliabilitySackHeaderNxt": "mrcReliabilitySackHeader.header.reliabilitySackHeader.nxt-2",
        "ReliabilitySackHeaderMBit": "mrcReliabilitySackHeader.header.reliabilitySackHeader.mBit-3",
        "ReliabilitySackHeaderRes1": "mrcReliabilitySackHeader.header.reliabilitySackHeader.res1-4",
        "ReliabilitySackHeaderRes2": "mrcReliabilitySackHeader.header.reliabilitySackHeader.res2-5",
        "ReliabilitySackHeaderRes3": "mrcReliabilitySackHeader.header.reliabilitySackHeader.res3-6",
        "ReliabilitySackHeaderPr": "mrcReliabilitySackHeader.header.reliabilitySackHeader.pr-7",
        "ReliabilitySackHeaderRes4": "mrcReliabilitySackHeader.header.reliabilitySackHeader.res4-8",
        "ReliabilitySackHeaderAckPsnOffset": "mrcReliabilitySackHeader.header.reliabilitySackHeader.ackPsnOffset-9",
        "ReliabilitySackHeaderEntropy": "mrcReliabilitySackHeader.header.reliabilitySackHeader.entropy-10",
        "ReliabilitySackHeaderSpdcid": "mrcReliabilitySackHeader.header.reliabilitySackHeader.spdcid-11",
        "ReliabilitySackHeaderDpdcid": "mrcReliabilitySackHeader.header.reliabilitySackHeader.dpdcid-12",
        "ReliabilitySackHeaderRes": "mrcReliabilitySackHeader.header.reliabilitySackHeader.res-13",
        "ReliabilitySackHeaderCackPsn": "mrcReliabilitySackHeader.header.reliabilitySackHeader.cackPsn-14",
        "ReliabilitySackHeaderCcType": "mrcReliabilitySackHeader.header.reliabilitySackHeader.ccType-15",
        "ReliabilitySackHeaderCcFl": "mrcReliabilitySackHeader.header.reliabilitySackHeader.ccFl-16",
        "ReliabilitySackHeaderMpr": "mrcReliabilitySackHeader.header.reliabilitySackHeader.mpr-17",
        "ReliabilitySackHeaderSackOffset": "mrcReliabilitySackHeader.header.reliabilitySackHeader.sackOffset-18",
        "ReliabilitySackHeaderSackBitmap": "mrcReliabilitySackHeader.header.reliabilitySackHeader.sackBitmap-19",
        "CcStateCcTxTimestamp": "mrcReliabilitySackHeader.header.ccState.ccTxTimestamp-20",
        "CcStateCcRes": "mrcReliabilitySackHeader.header.ccState.ccRes-21",
        "CcStateOooCount": "mrcReliabilitySackHeader.header.ccState.oooCount-22",
        "CcStateRestoreCwnd": "mrcReliabilitySackHeader.header.ccState.restoreCwnd-23",
        "CcStateRcvCwndPen": "mrcReliabilitySackHeader.header.ccState.rcvCwndPen-24",
        "CcStateRcvdBytes": "mrcReliabilitySackHeader.header.ccState.rcvdBytes-25",
    }

    def __init__(self, parent, list_op=False):
        super(MrcReliabilitySackHeader, self).__init__(parent, list_op)

    @property
    def ReliabilitySackHeaderSethType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderSethType"]),
        )

    @property
    def ReliabilitySackHeaderNxt(self):
        """
        Display Name: Next Header
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderNxt"])
        )

    @property
    def ReliabilitySackHeaderMBit(self):
        """
        Display Name: M-bit
        Default Value: 0
        Value Format: decimal
        Available enum values: None, 0, Skip once, 1, Always skip, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderMBit"])
        )

    @property
    def ReliabilitySackHeaderRes1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderRes1"])
        )

    @property
    def ReliabilitySackHeaderRes2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderRes2"])
        )

    @property
    def ReliabilitySackHeaderRes3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderRes3"])
        )

    @property
    def ReliabilitySackHeaderPr(self):
        """
        Display Name: Probe Response
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderPr"])
        )

    @property
    def ReliabilitySackHeaderRes4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderRes4"])
        )

    @property
    def ReliabilitySackHeaderAckPsnOffset(self):
        """
        Display Name: ACK PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderAckPsnOffset"]),
        )

    @property
    def ReliabilitySackHeaderEntropy(self):
        """
        Display Name: Entropy
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderEntropy"])
        )

    @property
    def ReliabilitySackHeaderSpdcid(self):
        """
        Display Name: Source PDCID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderSpdcid"])
        )

    @property
    def ReliabilitySackHeaderDpdcid(self):
        """
        Display Name: Destination PDCID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderDpdcid"])
        )

    @property
    def ReliabilitySackHeaderRes(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderRes"])
        )

    @property
    def ReliabilitySackHeaderCackPsn(self):
        """
        Display Name: Cumulative ACK PSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderCackPsn"])
        )

    @property
    def ReliabilitySackHeaderCcType(self):
        """
        Display Name: CC Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderCcType"])
        )

    @property
    def ReliabilitySackHeaderCcFl(self):
        """
        Display Name: CC Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderCcFl"])
        )

    @property
    def ReliabilitySackHeaderMpr(self):
        """
        Display Name: Max PSN Range
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderMpr"])
        )

    @property
    def ReliabilitySackHeaderSackOffset(self):
        """
        Display Name: SACK Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderSackOffset"]),
        )

    @property
    def ReliabilitySackHeaderSackBitmap(self):
        """
        Display Name: SACK Bitmap
        Default Value: 0xFFFFFFFFFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReliabilitySackHeaderSackBitmap"]),
        )

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
    def CcStateOooCount(self):
        """
        Display Name: Out-of-Order Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CcStateOooCount"])
        )

    @property
    def CcStateRestoreCwnd(self):
        """
        Display Name: Restore CWND
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CcStateRestoreCwnd"])
        )

    @property
    def CcStateRcvCwndPen(self):
        """
        Display Name: Receiver CWND Penalty
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CcStateRcvCwndPen"])
        )

    @property
    def CcStateRcvdBytes(self):
        """
        Display Name: Received Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CcStateRcvdBytes"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OranDataMsgs(Base):
    __slots__ = ()
    _SDM_NAME = "oranDataMsgs"
    _SDM_ATT_MAP = {
        "PcidDuPortId": "oranDataMsgs..iqDataHeader.pcid.duPortId-1",
        "PcidBandSectorId": "oranDataMsgs..iqDataHeader.pcid.bandSectorId-2",
        "PcidCcId": "oranDataMsgs..iqDataHeader.pcid.ccId-3",
        "PcidRuPortId": "oranDataMsgs..iqDataHeader.pcid.ruPortId-4",
        "SequenceidSeqId": "oranDataMsgs..iqDataHeader.sequenceid.seqId-5",
        "SequenceidEBit": "oranDataMsgs..iqDataHeader.sequenceid.eBit-6",
        "SequenceidSubSeqId": "oranDataMsgs..iqDataHeader.sequenceid.subSeqId-7",
        "RadioCommonHeaderDataDirection": "oranDataMsgs..radioCommonHeader.dataDirection-8",
        "RadioCommonHeaderPayloadVersion": "oranDataMsgs..radioCommonHeader.payloadVersion-9",
        "RadioCommonHeaderFilterIndex": "oranDataMsgs..radioCommonHeader.filterIndex-10",
        "RadioCommonHeaderFrameId": "oranDataMsgs..radioCommonHeader.frameId-11",
        "RadioCommonHeaderSubframeId": "oranDataMsgs..radioCommonHeader.subframeId-12",
        "RadioCommonHeaderSlotId": "oranDataMsgs..radioCommonHeader.slotId-13",
        "RadioCommonHeaderStartSymbolId": "oranDataMsgs..radioCommonHeader.startSymbolId-14",
        "DataHeaderSectionId": "oranDataMsgs..section.dataHeader.sectionId-15",
        "DataHeaderRb": "oranDataMsgs..section.dataHeader.rb-16",
        "DataHeaderSymInc": "oranDataMsgs..section.dataHeader.symInc-17",
        "DataHeaderStartPrbu": "oranDataMsgs..section.dataHeader.startPrbu-18",
        "DataHeaderNumPrbu": "oranDataMsgs..section.dataHeader.numPrbu-19",
        "CompHdrIqBitWidth": "oranDataMsgs..section.dataHeader.compHdr.iqBitWidth-20",
        "CompHdrUdCompMethod": "oranDataMsgs..section.dataHeader.compHdr.udCompMethod-21",
        "DataHeaderReserved": "oranDataMsgs..section.dataHeader.reserved-22",
        "DataPayloadUdCompParam": "oranDataMsgs..section.dataPayload.udCompParam-23",
        "IqDataLength": "oranDataMsgs..section.dataPayload.iqData.length-24",
        "IqDataData": "oranDataMsgs..section.dataPayload.iqData.data-25",
    }

    def __init__(self, parent, list_op=False):
        super(OranDataMsgs, self).__init__(parent, list_op)

    @property
    def PcidDuPortId(self):
        """
        Display Name: DU Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PcidDuPortId"]))

    @property
    def PcidBandSectorId(self):
        """
        Display Name: Band Sector ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PcidBandSectorId"])
        )

    @property
    def PcidCcId(self):
        """
        Display Name: CC ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PcidCcId"]))

    @property
    def PcidRuPortId(self):
        """
        Display Name: RU Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PcidRuPortId"]))

    @property
    def SequenceidSeqId(self):
        """
        Display Name: Seq ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceidSeqId"])
        )

    @property
    def SequenceidEBit(self):
        """
        Display Name: E bit(last fragement)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceidEBit"])
        )

    @property
    def SequenceidSubSeqId(self):
        """
        Display Name: Subsequence ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceidSubSeqId"])
        )

    @property
    def RadioCommonHeaderDataDirection(self):
        """
        Display Name: Data Direction
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderDataDirection"]),
        )

    @property
    def RadioCommonHeaderPayloadVersion(self):
        """
        Display Name: Payload Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderPayloadVersion"]),
        )

    @property
    def RadioCommonHeaderFilterIndex(self):
        """
        Display Name: Filter Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderFilterIndex"])
        )

    @property
    def RadioCommonHeaderFrameId(self):
        """
        Display Name: Frame Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderFrameId"])
        )

    @property
    def RadioCommonHeaderSubframeId(self):
        """
        Display Name: Subframe Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderSubframeId"])
        )

    @property
    def RadioCommonHeaderSlotId(self):
        """
        Display Name: Slot Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderSlotId"])
        )

    @property
    def RadioCommonHeaderStartSymbolId(self):
        """
        Display Name: SymbolId
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderStartSymbolId"]),
        )

    @property
    def DataHeaderSectionId(self):
        """
        Display Name: Section Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderSectionId"])
        )

    @property
    def DataHeaderRb(self):
        """
        Display Name: rb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderRb"]))

    @property
    def DataHeaderSymInc(self):
        """
        Display Name: symInc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderSymInc"])
        )

    @property
    def DataHeaderStartPrbu(self):
        """
        Display Name: Start Prbu
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderStartPrbu"])
        )

    @property
    def DataHeaderNumPrbu(self):
        """
        Display Name: Num Prbu
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderNumPrbu"])
        )

    @property
    def CompHdrIqBitWidth(self):
        """
        Display Name: Bit width of IQ Data
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompHdrIqBitWidth"])
        )

    @property
    def CompHdrUdCompMethod(self):
        """
        Display Name: Compression Method
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompHdrUdCompMethod"])
        )

    @property
    def DataHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderReserved"])
        )

    @property
    def DataPayloadUdCompParam(self):
        """
        Display Name: Compression Param
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataPayloadUdCompParam"])
        )

    @property
    def IqDataLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IqDataLength"]))

    @property
    def IqDataData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IqDataData"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

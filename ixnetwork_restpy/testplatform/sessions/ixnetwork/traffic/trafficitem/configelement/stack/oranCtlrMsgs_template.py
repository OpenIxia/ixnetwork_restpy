from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OranCtlrMsgs(Base):
    __slots__ = ()
    _SDM_NAME = "oranCtlrMsgs"
    _SDM_ATT_MAP = {
        "RtcIdDuPortId": "oranCtlrMsgs..iqDataHeader.rtcId.duPortId-1",
        "RtcIdBandSectorId": "oranCtlrMsgs..iqDataHeader.rtcId.bandSectorId-2",
        "RtcIdCcId": "oranCtlrMsgs..iqDataHeader.rtcId.ccId-3",
        "RtcIdRuPortId": "oranCtlrMsgs..iqDataHeader.rtcId.ruPortId-4",
        "SequenceidSeqId": "oranCtlrMsgs..iqDataHeader.sequenceid.seqId-5",
        "SequenceidEBit": "oranCtlrMsgs..iqDataHeader.sequenceid.eBit-6",
        "SequenceidSubSeqId": "oranCtlrMsgs..iqDataHeader.sequenceid.subSeqId-7",
        "RadioCommonHeaderDataDirection": "oranCtlrMsgs..radioCommonHeader.dataDirection-8",
        "RadioCommonHeaderPayloadVersion": "oranCtlrMsgs..radioCommonHeader.payloadVersion-9",
        "RadioCommonHeaderFilterIndex": "oranCtlrMsgs..radioCommonHeader.filterIndex-10",
        "RadioCommonHeaderFrameId": "oranCtlrMsgs..radioCommonHeader.frameId-11",
        "RadioCommonHeaderSubframeId": "oranCtlrMsgs..radioCommonHeader.subframeId-12",
        "RadioCommonHeaderSlotId": "oranCtlrMsgs..radioCommonHeader.slotId-13",
        "RadioCommonHeaderStartSymbolId": "oranCtlrMsgs..radioCommonHeader.startSymbolId-14",
        "RadioCommonHeaderNumberofSections": "oranCtlrMsgs..radioCommonHeader.numberofSections-15",
        "Section0SectionType": "oranCtlrMsgs..sections.section.section0.sectionType-16",
        "SectionSectionId": "oranCtlrMsgs..sections.section.section0.section.sectionId-17",
        "SectionRb": "oranCtlrMsgs..sections.section.section0.section.rb-18",
        "SectionSymInc": "oranCtlrMsgs..sections.section.section0.section.symInc-19",
        "SectionStartPrbc": "oranCtlrMsgs..sections.section.section0.section.startPrbc-20",
        "SectionNumPrbc": "oranCtlrMsgs..sections.section.section0.section.numPrbc-21",
        "SectionReMask": "oranCtlrMsgs..sections.section.section0.section.reMask-22",
        "SectionNumSymbol": "oranCtlrMsgs..sections.section.section0.section.numSymbol-23",
        "SectionReserved": "oranCtlrMsgs..sections.section.section0.section.reserved-24",
        "Section1SectionType": "oranCtlrMsgs..sections.section.section1.sectionType-25",
        "CompHdrIqBitWidth": "oranCtlrMsgs..sections.section.section1.section1Header.compHdr.iqBitWidth-26",
        "CompHdrUdCompMethod": "oranCtlrMsgs..sections.section.section1.section1Header.compHdr.udCompMethod-27",
        "Section1HeaderReserved": "oranCtlrMsgs..sections.section.section1.section1Header.reserved-28",
        "Section1SectionSectionId": "oranCtlrMsgs..sections.section.section1.section.sectionId-29",
        "Section1SectionRb": "oranCtlrMsgs..sections.section.section1.section.rb-30",
        "Section1SectionSymInc": "oranCtlrMsgs..sections.section.section1.section.symInc-31",
        "Section1SectionStartPrbc": "oranCtlrMsgs..sections.section.section1.section.startPrbc-32",
        "Section1SectionNumPrbc": "oranCtlrMsgs..sections.section.section1.section.numPrbc-33",
        "Section1SectionReMask": "oranCtlrMsgs..sections.section.section1.section.reMask-34",
        "Section1SectionNumSymbol": "oranCtlrMsgs..sections.section.section1.section.numSymbol-35",
        "SectionEf": "oranCtlrMsgs..sections.section.section1.section.ef-36",
        "SectionBeamId": "oranCtlrMsgs..sections.section.section1.section.beamId-37",
        "Section3SectionType": "oranCtlrMsgs..sections.section.section3.sectionType-38",
        "Section3HeaderTimeOffset": "oranCtlrMsgs..sections.section.section3.section3Header.timeOffset-39",
        "Section3HeaderFrameStructure": "oranCtlrMsgs..sections.section.section3.section3Header.frameStructure-40",
        "Section3HeaderCpLength": "oranCtlrMsgs..sections.section.section3.section3Header.cpLength-41",
        "Section3headerCompHdrIqBitWidth": "oranCtlrMsgs..sections.section.section3.section3Header.compHdr.iqBitWidth-42",
        "Section3headerCompHdrUdCompMethod": "oranCtlrMsgs..sections.section.section3.section3Header.compHdr.udCompMethod-43",
        "Section3SectionSectionId": "oranCtlrMsgs..sections.section.section3.section.sectionId-44",
        "Section3SectionRb": "oranCtlrMsgs..sections.section.section3.section.rb-45",
        "Section3SectionSymInc": "oranCtlrMsgs..sections.section.section3.section.symInc-46",
        "Section3SectionStartPrbc": "oranCtlrMsgs..sections.section.section3.section.startPrbc-47",
        "Section3SectionNumPrbc": "oranCtlrMsgs..sections.section.section3.section.numPrbc-48",
        "Section3SectionReMask": "oranCtlrMsgs..sections.section.section3.section.reMask-49",
        "Section3SectionNumSymbol": "oranCtlrMsgs..sections.section.section3.section.numSymbol-50",
        "Section3SectionEf": "oranCtlrMsgs..sections.section.section3.section.ef-51",
        "Section3SectionBeamId": "oranCtlrMsgs..sections.section.section3.section.beamId-52",
        "SectionFrequencyOffset": "oranCtlrMsgs..sections.section.section3.section.frequencyOffset-53",
        "Section3SectionReserved": "oranCtlrMsgs..sections.section.section3.section.reserved-54",
        "ExtensionLength": "oranCtlrMsgs..sections.section.section3.section.extensions.extension.length-55",
        "ExtensionData": "oranCtlrMsgs..sections.section.section3.section.extensions.extension.data-56",
    }

    def __init__(self, parent, list_op=False):
        super(OranCtlrMsgs, self).__init__(parent, list_op)

    @property
    def RtcIdDuPortId(self):
        """
        Display Name: DU Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RtcIdDuPortId"]))

    @property
    def RtcIdBandSectorId(self):
        """
        Display Name: Band Sector ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcIdBandSectorId"])
        )

    @property
    def RtcIdCcId(self):
        """
        Display Name: CC ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RtcIdCcId"]))

    @property
    def RtcIdRuPortId(self):
        """
        Display Name: RU Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RtcIdRuPortId"]))

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
        Display Name: Start SymbolId
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderStartSymbolId"]),
        )

    @property
    def RadioCommonHeaderNumberofSections(self):
        """
        Display Name: Number of Sections
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RadioCommonHeaderNumberofSections"]),
        )

    @property
    def Section0SectionType(self):
        """
        Display Name: Section Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section0SectionType"])
        )

    @property
    def SectionSectionId(self):
        """
        Display Name: Section Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SectionSectionId"])
        )

    @property
    def SectionRb(self):
        """
        Display Name: rb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SectionRb"]))

    @property
    def SectionSymInc(self):
        """
        Display Name: symInc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SectionSymInc"]))

    @property
    def SectionStartPrbc(self):
        """
        Display Name: Start Prbc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SectionStartPrbc"])
        )

    @property
    def SectionNumPrbc(self):
        """
        Display Name: Num Prbc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SectionNumPrbc"])
        )

    @property
    def SectionReMask(self):
        """
        Display Name: ReMask
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SectionReMask"]))

    @property
    def SectionNumSymbol(self):
        """
        Display Name: Num Symbol
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SectionNumSymbol"])
        )

    @property
    def SectionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SectionReserved"])
        )

    @property
    def Section1SectionType(self):
        """
        Display Name: Section Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionType"])
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
    def Section1HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1HeaderReserved"])
        )

    @property
    def Section1SectionSectionId(self):
        """
        Display Name: Section Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionSectionId"])
        )

    @property
    def Section1SectionRb(self):
        """
        Display Name: rb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionRb"])
        )

    @property
    def Section1SectionSymInc(self):
        """
        Display Name: symInc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionSymInc"])
        )

    @property
    def Section1SectionStartPrbc(self):
        """
        Display Name: Start Prbc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionStartPrbc"])
        )

    @property
    def Section1SectionNumPrbc(self):
        """
        Display Name: Num Prbc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionNumPrbc"])
        )

    @property
    def Section1SectionReMask(self):
        """
        Display Name: ReMask
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionReMask"])
        )

    @property
    def Section1SectionNumSymbol(self):
        """
        Display Name: Num Symbol
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section1SectionNumSymbol"])
        )

    @property
    def SectionEf(self):
        """
        Display Name: ef
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SectionEf"]))

    @property
    def SectionBeamId(self):
        """
        Display Name: Beam id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SectionBeamId"]))

    @property
    def Section3SectionType(self):
        """
        Display Name: Section Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionType"])
        )

    @property
    def Section3HeaderTimeOffset(self):
        """
        Display Name: Time Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3HeaderTimeOffset"])
        )

    @property
    def Section3HeaderFrameStructure(self):
        """
        Display Name: Frame Structure
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3HeaderFrameStructure"])
        )

    @property
    def Section3HeaderCpLength(self):
        """
        Display Name: cpLength
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3HeaderCpLength"])
        )

    @property
    def Section3headerCompHdrIqBitWidth(self):
        """
        Display Name: Bit width of IQ Data
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Section3headerCompHdrIqBitWidth"]),
        )

    @property
    def Section3headerCompHdrUdCompMethod(self):
        """
        Display Name: Compression Method
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Section3headerCompHdrUdCompMethod"]),
        )

    @property
    def Section3SectionSectionId(self):
        """
        Display Name: Section Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionSectionId"])
        )

    @property
    def Section3SectionRb(self):
        """
        Display Name: rb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionRb"])
        )

    @property
    def Section3SectionSymInc(self):
        """
        Display Name: symInc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionSymInc"])
        )

    @property
    def Section3SectionStartPrbc(self):
        """
        Display Name: Start Prbc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionStartPrbc"])
        )

    @property
    def Section3SectionNumPrbc(self):
        """
        Display Name: Num Prbc
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionNumPrbc"])
        )

    @property
    def Section3SectionReMask(self):
        """
        Display Name: ReMask
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionReMask"])
        )

    @property
    def Section3SectionNumSymbol(self):
        """
        Display Name: Num Symbol
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionNumSymbol"])
        )

    @property
    def Section3SectionEf(self):
        """
        Display Name: ef
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionEf"])
        )

    @property
    def Section3SectionBeamId(self):
        """
        Display Name: Beam id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionBeamId"])
        )

    @property
    def SectionFrequencyOffset(self):
        """
        Display Name: Frequency Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SectionFrequencyOffset"])
        )

    @property
    def Section3SectionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Section3SectionReserved"])
        )

    @property
    def ExtensionLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionLength"])
        )

    @property
    def ExtensionData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExtensionData"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

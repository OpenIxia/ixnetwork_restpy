from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Elmi(Base):
    __slots__ = ()
    _SDM_NAME = "elmi"
    _SDM_ATT_MAP = {
        "ElmiHeaderProtoVersion": "elmi.elmiHeader.protoVersion-1",
        "ElmiHeaderMsgType": "elmi.elmiHeader.msgType-2",
        "ReportTypeIeReportType": "elmi.elmiHeader.selectInformationElement.reportTypeIe.reportType-3",
        "ReportTypeIeLength": "elmi.elmiHeader.selectInformationElement.reportTypeIe.length-4",
        "ReportTypeIeReportTypeValue": "elmi.elmiHeader.selectInformationElement.reportTypeIe.reportTypeValue-5",
        "SequenceNumberIeSequenceNumbers": "elmi.elmiHeader.selectInformationElement.sequenceNumberIe.sequenceNumbers-6",
        "SequenceNumberIeLength": "elmi.elmiHeader.selectInformationElement.sequenceNumberIe.length-7",
        "SequenceNumberIeSendSequenceNumber": "elmi.elmiHeader.selectInformationElement.sequenceNumberIe.sendSequenceNumber-8",
        "SequenceNumberIeReceiveSequenceNumber": "elmi.elmiHeader.selectInformationElement.sequenceNumberIe.receiveSequenceNumber-9",
        "DataInstanceIeDataInstance": "elmi.elmiHeader.selectInformationElement.dataInstanceIe.dataInstance-10",
        "DataInstanceIeLength": "elmi.elmiHeader.selectInformationElement.dataInstanceIe.length-11",
        "DataInstanceIeReserved": "elmi.elmiHeader.selectInformationElement.dataInstanceIe.reserved-12",
        "DataInstanceIeDataInstance": "elmi.elmiHeader.selectInformationElement.dataInstanceIe.dataInstance-13",
        "UniStatusIeUniStatus": "elmi.elmiHeader.selectInformationElement.uniStatusIe.uniStatus-14",
        "UniStatusIeLength": "elmi.elmiHeader.selectInformationElement.uniStatusIe.length-15",
        "UniStatusIeMapType": "elmi.elmiHeader.selectInformationElement.uniStatusIe.mapType-16",
        "BandwidthProfileBwProfileSubIeId": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.bwProfileSubIeId-17",
        "BandwidthProfileLength": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.length-18",
        "BandwidthProfileReserve": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.reserve-19",
        "BandwidthProfileCm": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.cm-20",
        "BandwidthProfileCf": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.cf-21",
        "BandwidthProfilePerCos": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.perCos-22",
        "BandwidthProfileCirMagnitude": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.cirMagnitude-23",
        "BandwidthProfileCirMultiplier": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.cirMultiplier-24",
        "BandwidthProfileCbsMagnitude": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.cbsMagnitude-25",
        "BandwidthProfileCbsMultiplier": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.cbsMultiplier-26",
        "BandwidthProfileEirMagnitude": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.eirMagnitude-27",
        "BandwidthProfileEirMultiplier": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.eirMultiplier-28",
        "BandwidthProfileEbsMagnitude": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.ebsMagnitude-29",
        "BandwidthProfileEbsMultiplier": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.ebsMultiplier-30",
        "BandwidthProfileUserPriorityBits": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.bandwidthProfile.userPriorityBits-31",
        "UniIdentifierUniIdentifierSubIeId": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.uniIdentifier.uniIdentifierSubIeId-32",
        "UniIdentifierLength": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.uniIdentifier.length-33",
        "UniIdentifierAsciiOctet": "elmi.elmiHeader.selectInformationElement.uniStatusIe.selectSubIe.uniIdentifier.asciiOctet-34",
        "EvcStatusIeEvcStatus": "elmi.elmiHeader.selectInformationElement.evcStatusIe.evcStatus-35",
        "EvcStatusIeLength": "elmi.elmiHeader.selectInformationElement.evcStatusIe.length-36",
        "EvcStatusIeEvcReferenceId": "elmi.elmiHeader.selectInformationElement.evcStatusIe.evcReferenceId-37",
        "EvcStatusTypeReserve1": "elmi.elmiHeader.selectInformationElement.evcStatusIe.evcStatusType.reserve1-38",
        "EvcStatusTypeReserve2": "elmi.elmiHeader.selectInformationElement.evcStatusIe.evcStatusType.reserve2-39",
        "EvcStatusTypeEvcStatus": "elmi.elmiHeader.selectInformationElement.evcStatusIe.evcStatusType.evcStatus-40",
        "EvcParametersEvcParametersSubIeId": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcParameters.evcParametersSubIeId-41",
        "EvcParametersLength": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcParameters.length-42",
        "EvcParametersReserve": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcParameters.reserve-43",
        "EvcParametersEvcType": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcParameters.evcType-44",
        "EvcIdentifierEvcIdentifierSubIeId": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcIdentifier.evcIdentifierSubIeId-45",
        "EvcIdentifierLength": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcIdentifier.length-46",
        "EvcIdentifierAsciiOctet": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.evcIdentifier.asciiOctet-47",
        "SelectsubieBandwidthProfileBwProfileSubIeId": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.bwProfileSubIeId-48",
        "SelectsubieBandwidthProfileLength": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.length-49",
        "SelectsubieBandwidthProfileReserve": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.reserve-50",
        "SelectsubieBandwidthProfileCm": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.cm-51",
        "SelectsubieBandwidthProfileCf": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.cf-52",
        "SelectsubieBandwidthProfilePerCos": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.perCos-53",
        "SelectsubieBandwidthProfileCirMagnitude": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.cirMagnitude-54",
        "SelectsubieBandwidthProfileCirMultiplier": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.cirMultiplier-55",
        "SelectsubieBandwidthProfileCbsMagnitude": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.cbsMagnitude-56",
        "SelectsubieBandwidthProfileCbsMultiplier": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.cbsMultiplier-57",
        "SelectsubieBandwidthProfileEirMagnitude": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.eirMagnitude-58",
        "SelectsubieBandwidthProfileEirMultiplier": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.eirMultiplier-59",
        "SelectsubieBandwidthProfileEbsMagnitude": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.ebsMagnitude-60",
        "SelectsubieBandwidthProfileEbsMultiplier": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.ebsMultiplier-61",
        "SelectsubieBandwidthProfileUserPriorityBits": "elmi.elmiHeader.selectInformationElement.evcStatusIe.selectSubIe.bandwidthProfile.userPriorityBits-62",
        "CeVlanIdEvcMapIeCeVlanIdEvcMapIeId": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.ceVlanIdEvcMapIeId-63",
        "CeVlanIdEvcMapIeLength": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.length-64",
        "CeVlanIdEvcMapIeEvcReferenceId": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.evcReferenceId-65",
        "CeVlanIdEvcMapIeReserve1": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.reserve1-66",
        "CeVlanIdEvcMapIeLastIe": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.lastIe-67",
        "CeVlanIdEvcMapIeMapSequence": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.mapSequence-68",
        "CeVlanIdEvcMapIeReserve2": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.reserve2-69",
        "CeVlanIdEvcMapIeUntaggedPriorityTagged": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.untaggedPriorityTagged-70",
        "CeVlanIdEvcMapIeDefaultEVC": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.defaultEVC-71",
        "EvcMapEntryEvcMapEntrySubIeId": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.evcMapEntry.evcMapEntrySubIeId-72",
        "EvcMapEntryLength": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.evcMapEntry.length-73",
        "EvcMapEntryCeVlanId": "elmi.elmiHeader.selectInformationElement.ceVlanIdEvcMapIe.evcMapEntry.ceVlanId-74",
    }

    def __init__(self, parent, list_op=False):
        super(Elmi, self).__init__(parent, list_op)

    @property
    def ElmiHeaderProtoVersion(self):
        """
        Display Name: Protocol Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElmiHeaderProtoVersion"])
        )

    @property
    def ElmiHeaderMsgType(self):
        """
        Display Name: Message Type
        Default Value: 117
        Value Format: decimal
        Available enum values: Status Enquiry, 117, Status, 125
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElmiHeaderMsgType"])
        )

    @property
    def ReportTypeIeReportType(self):
        """
        Display Name: Report Type IE Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReportTypeIeReportType"])
        )

    @property
    def ReportTypeIeLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReportTypeIeLength"])
        )

    @property
    def ReportTypeIeReportTypeValue(self):
        """
        Display Name: Report Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Full Status, 0, E-LMI Check, 1, Single EVC Async Status, 2, Full Status Continued, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReportTypeIeReportTypeValue"])
        )

    @property
    def SequenceNumberIeSequenceNumbers(self):
        """
        Display Name: Sequence Numbers IE Identifier
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SequenceNumberIeSequenceNumbers"]),
        )

    @property
    def SequenceNumberIeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceNumberIeLength"])
        )

    @property
    def SequenceNumberIeSendSequenceNumber(self):
        """
        Display Name: Send Sequence Number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SequenceNumberIeSendSequenceNumber"]
            ),
        )

    @property
    def SequenceNumberIeReceiveSequenceNumber(self):
        """
        Display Name: Receive Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SequenceNumberIeReceiveSequenceNumber"]
            ),
        )

    @property
    def DataInstanceIeDataInstance(self):
        """
        Display Name: Data Instance IE Identifier
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataInstanceIeDataInstance"])
        )

    @property
    def DataInstanceIeLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataInstanceIeLength"])
        )

    @property
    def DataInstanceIeReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataInstanceIeReserved"])
        )

    @property
    def DataInstanceIeDataInstance(self):
        """
        Display Name: Data Instance
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataInstanceIeDataInstance"])
        )

    @property
    def UniStatusIeUniStatus(self):
        """
        Display Name: UNI Status IE Identifier
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniStatusIeUniStatus"])
        )

    @property
    def UniStatusIeLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniStatusIeLength"])
        )

    @property
    def UniStatusIeMapType(self):
        """
        Display Name: Map Type
        Default Value: 1
        Value Format: decimal
        Available enum values: All to one bundling, 1, Service Multiplexing with no bundling, 2, Bundling, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniStatusIeMapType"])
        )

    @property
    def BandwidthProfileBwProfileSubIeId(self):
        """
        Display Name: Bandwidth Profile Sub IE Identifier
        Default Value: 113
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileBwProfileSubIeId"]),
        )

    @property
    def BandwidthProfileLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileLength"])
        )

    @property
    def BandwidthProfileReserve(self):
        """
        Display Name: Reserve
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileReserve"])
        )

    @property
    def BandwidthProfileCm(self):
        """
        Display Name: CM
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileCm"])
        )

    @property
    def BandwidthProfileCf(self):
        """
        Display Name: CF
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileCf"])
        )

    @property
    def BandwidthProfilePerCos(self):
        """
        Display Name: Per CoS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfilePerCos"])
        )

    @property
    def BandwidthProfileCirMagnitude(self):
        """
        Display Name: CIR Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileCirMagnitude"])
        )

    @property
    def BandwidthProfileCirMultiplier(self):
        """
        Display Name: CIR Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileCirMultiplier"]),
        )

    @property
    def BandwidthProfileCbsMagnitude(self):
        """
        Display Name: CBS Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileCbsMagnitude"])
        )

    @property
    def BandwidthProfileCbsMultiplier(self):
        """
        Display Name: CBS Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileCbsMultiplier"]),
        )

    @property
    def BandwidthProfileEirMagnitude(self):
        """
        Display Name: EIR Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileEirMagnitude"])
        )

    @property
    def BandwidthProfileEirMultiplier(self):
        """
        Display Name: EIR Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileEirMultiplier"]),
        )

    @property
    def BandwidthProfileEbsMagnitude(self):
        """
        Display Name: EBS Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileEbsMagnitude"])
        )

    @property
    def BandwidthProfileEbsMultiplier(self):
        """
        Display Name: EBS Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileEbsMultiplier"]),
        )

    @property
    def BandwidthProfileUserPriorityBits(self):
        """
        Display Name: User Priority Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BandwidthProfileUserPriorityBits"]),
        )

    @property
    def UniIdentifierUniIdentifierSubIeId(self):
        """
        Display Name: UNI Identifier Sub IE Identifier
        Default Value: 81
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UniIdentifierUniIdentifierSubIeId"]),
        )

    @property
    def UniIdentifierLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniIdentifierLength"])
        )

    @property
    def UniIdentifierAsciiOctet(self):
        """
        Display Name: ASCII Octet
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniIdentifierAsciiOctet"])
        )

    @property
    def EvcStatusIeEvcStatus(self):
        """
        Display Name: EVC Status IE Identifier
        Default Value: 33
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcStatusIeEvcStatus"])
        )

    @property
    def EvcStatusIeLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcStatusIeLength"])
        )

    @property
    def EvcStatusIeEvcReferenceId(self):
        """
        Display Name: EVC Reference ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcStatusIeEvcReferenceId"])
        )

    @property
    def EvcStatusTypeReserve1(self):
        """
        Display Name: Reserve1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcStatusTypeReserve1"])
        )

    @property
    def EvcStatusTypeReserve2(self):
        """
        Display Name: Reserve2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcStatusTypeReserve2"])
        )

    @property
    def EvcStatusTypeEvcStatus(self):
        """
        Display Name: EVC Status
        Default Value: 3
        Value Format: decimal
        Available enum values: Not Active, 0, New and Not Active, 1, Active, 2, New and Active, 3, Partially Active, 4, New and Partially Active, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcStatusTypeEvcStatus"])
        )

    @property
    def EvcParametersEvcParametersSubIeId(self):
        """
        Display Name: EVC Parameters Sub IE Identifier
        Default Value: 97
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EvcParametersEvcParametersSubIeId"]),
        )

    @property
    def EvcParametersLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcParametersLength"])
        )

    @property
    def EvcParametersReserve(self):
        """
        Display Name: Reserve
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcParametersReserve"])
        )

    @property
    def EvcParametersEvcType(self):
        """
        Display Name: EVC Type
        Default Value: 0
        Value Format: decimal
        Available enum values: Point-to-Point EVC, 0, Multipoint-to-Multipoint EVC, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcParametersEvcType"])
        )

    @property
    def EvcIdentifierEvcIdentifierSubIeId(self):
        """
        Display Name: EVC Identifier Sub IE Identifier
        Default Value: 98
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EvcIdentifierEvcIdentifierSubIeId"]),
        )

    @property
    def EvcIdentifierLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcIdentifierLength"])
        )

    @property
    def EvcIdentifierAsciiOctet(self):
        """
        Display Name: ASCII Octet
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcIdentifierAsciiOctet"])
        )

    @property
    def SelectsubieBandwidthProfileBwProfileSubIeId(self):
        """
        Display Name: Bandwidth Profile Sub IE Identifier
        Default Value: 113
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileBwProfileSubIeId"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SelectsubieBandwidthProfileLength"]),
        )

    @property
    def SelectsubieBandwidthProfileReserve(self):
        """
        Display Name: Reserve
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileReserve"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileCm(self):
        """
        Display Name: CM
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SelectsubieBandwidthProfileCm"]),
        )

    @property
    def SelectsubieBandwidthProfileCf(self):
        """
        Display Name: CF
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SelectsubieBandwidthProfileCf"]),
        )

    @property
    def SelectsubieBandwidthProfilePerCos(self):
        """
        Display Name: Per CoS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SelectsubieBandwidthProfilePerCos"]),
        )

    @property
    def SelectsubieBandwidthProfileCirMagnitude(self):
        """
        Display Name: CIR Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileCirMagnitude"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileCirMultiplier(self):
        """
        Display Name: CIR Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileCirMultiplier"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileCbsMagnitude(self):
        """
        Display Name: CBS Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileCbsMagnitude"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileCbsMultiplier(self):
        """
        Display Name: CBS Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileCbsMultiplier"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileEirMagnitude(self):
        """
        Display Name: EIR Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileEirMagnitude"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileEirMultiplier(self):
        """
        Display Name: EIR Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileEirMultiplier"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileEbsMagnitude(self):
        """
        Display Name: EBS Magnitude
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileEbsMagnitude"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileEbsMultiplier(self):
        """
        Display Name: EBS Multiplier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileEbsMultiplier"]
            ),
        )

    @property
    def SelectsubieBandwidthProfileUserPriorityBits(self):
        """
        Display Name: User Priority Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SelectsubieBandwidthProfileUserPriorityBits"]
            ),
        )

    @property
    def CeVlanIdEvcMapIeCeVlanIdEvcMapIeId(self):
        """
        Display Name: CE-VLAN ID/EVC Map IE Identifier
        Default Value: 34
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CeVlanIdEvcMapIeCeVlanIdEvcMapIeId"]
            ),
        )

    @property
    def CeVlanIdEvcMapIeLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeLength"])
        )

    @property
    def CeVlanIdEvcMapIeEvcReferenceId(self):
        """
        Display Name: EVC Reference ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeEvcReferenceId"]),
        )

    @property
    def CeVlanIdEvcMapIeReserve1(self):
        """
        Display Name: Reserve
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeReserve1"])
        )

    @property
    def CeVlanIdEvcMapIeLastIe(self):
        """
        Display Name: Last IE
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeLastIe"])
        )

    @property
    def CeVlanIdEvcMapIeMapSequence(self):
        """
        Display Name: CE-VLAN ID/EVC Map Sequence
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeMapSequence"])
        )

    @property
    def CeVlanIdEvcMapIeReserve2(self):
        """
        Display Name: Reserve
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeReserve2"])
        )

    @property
    def CeVlanIdEvcMapIeUntaggedPriorityTagged(self):
        """
        Display Name: Untagged/Priority Tagged
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CeVlanIdEvcMapIeUntaggedPriorityTagged"]
            ),
        )

    @property
    def CeVlanIdEvcMapIeDefaultEVC(self):
        """
        Display Name: Default EVC
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CeVlanIdEvcMapIeDefaultEVC"])
        )

    @property
    def EvcMapEntryEvcMapEntrySubIeId(self):
        """
        Display Name: EVC Map Entry Sub IE Identifier
        Default Value: 99
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EvcMapEntryEvcMapEntrySubIeId"]),
        )

    @property
    def EvcMapEntryLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcMapEntryLength"])
        )

    @property
    def EvcMapEntryCeVlanId(self):
        """
        Display Name: CE-VLAN ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvcMapEntryCeVlanId"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

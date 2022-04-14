from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PTPv2udp(Base):
    __slots__ = ()
    _SDM_NAME = "PTPv2_udp"
    _SDM_ATT_MAP = {
        "HeaderTransportSpecific": "PTPv2_udp.header.header.transportSpecific-1",
        "HeaderMessageType": "PTPv2_udp.header.header.messageType-2",
        "HeaderReserved_4": "PTPv2_udp.header.header.reserved_4-3",
        "HeaderVersionPTP": "PTPv2_udp.header.header.versionPTP-4",
        "HeaderMessageLength": "PTPv2_udp.header.header.messageLength-5",
        "HeaderDomainNumber": "PTPv2_udp.header.header.domainNumber-6",
        "HeaderReserved": "PTPv2_udp.header.header.reserved-7",
        "HeaderFlagField": "PTPv2_udp.header.header.flagField-8",
        "HeaderCorrectionField": "PTPv2_udp.header.header.correctionField-9",
        "HeaderReserved_4bytes": "PTPv2_udp.header.header.reserved_4bytes-10",
        "HeaderSourcePortIdentity": "PTPv2_udp.header.header.sourcePortIdentity-11",
        "HeaderSequenceId": "PTPv2_udp.header.header.sequenceId-12",
        "HeaderControlField": "PTPv2_udp.header.header.controlField-13",
        "HeaderLogMessageInterval": "PTPv2_udp.header.header.logMessageInterval-14",
        "AnnounceOriginTimestamp": "PTPv2_udp.header.messageTypes.announce.originTimestamp-15",
        "AnnounceCurrentUTCOffset": "PTPv2_udp.header.messageTypes.announce.currentUTCOffset-16",
        "AnnounceReserved": "PTPv2_udp.header.messageTypes.announce.reserved-17",
        "AnnounceGrandMasterPriority1": "PTPv2_udp.header.messageTypes.announce.grandMasterPriority1-18",
        "AnnounceGrandMasterClockQuality": "PTPv2_udp.header.messageTypes.announce.grandMasterClockQuality-19",
        "AnnounceGrandMasterPriority2": "PTPv2_udp.header.messageTypes.announce.grandMasterPriority2-20",
        "AnnounceGrandMasterIdentity": "PTPv2_udp.header.messageTypes.announce.grandMasterIdentity-21",
        "AnnounceStepsRemoved": "PTPv2_udp.header.messageTypes.announce.stepsRemoved-22",
        "AnnounceTimeSource": "PTPv2_udp.header.messageTypes.announce.timeSource-23",
        "SyncOriginTimestamp": "PTPv2_udp.header.messageTypes.sync.originTimestamp-24",
        "FollowUpPreciseOriginTimestamp": "PTPv2_udp.header.messageTypes.followUp.preciseOriginTimestamp-25",
        "DelayRequestOriginTimestamp": "PTPv2_udp.header.messageTypes.delayRequest.originTimestamp-26",
        "DelayResponseReceiveTimestamp": "PTPv2_udp.header.messageTypes.delayResponse.receiveTimestamp-27",
        "DelayResponseRequestingPortIdentity": "PTPv2_udp.header.messageTypes.delayResponse.requestingPortIdentity-28",
        "PDelayReqOriginTimestamp": "PTPv2_udp.header.messageTypes.pDelayReq.originTimestamp-29",
        "PDelayReqReserved": "PTPv2_udp.header.messageTypes.pDelayReq.reserved-30",
        "PDelayResponseRequestReceiptTimestamp": "PTPv2_udp.header.messageTypes.pDelayResponse.requestReceiptTimestamp-31",
        "PDelayResponseRequestPortIdentity": "PTPv2_udp.header.messageTypes.pDelayResponse.requestPortIdentity-32",
        "PDelayResponseFollowUpResponseOriginTimestamp": "PTPv2_udp.header.messageTypes.pDelayResponseFollowUp.responseOriginTimestamp-33",
        "PDelayResponseFollowUpRequestingPortIdentity": "PTPv2_udp.header.messageTypes.pDelayResponseFollowUp.requestingPortIdentity-34",
        "SignallingTargetPortIdentity": "PTPv2_udp.header.messageTypes.signalling.targetPortIdentity-35",
        "ManagementTargetPortIdentity": "PTPv2_udp.header.messageTypes.management.targetPortIdentity-36",
        "ManagementStartingBoundaryHops": "PTPv2_udp.header.messageTypes.management.startingBoundaryHops-37",
        "ManagementBoundaryHops": "PTPv2_udp.header.messageTypes.management.boundaryHops-38",
        "ManagementReserved_1": "PTPv2_udp.header.messageTypes.management.reserved_1-39",
        "ManagementActionField": "PTPv2_udp.header.messageTypes.management.actionField-40",
        "ManagementReserved": "PTPv2_udp.header.messageTypes.management.reserved-41",
        "TlvNone": "PTPv2_udp.header.tlvs.tlv.none-42",
        "Request_unicast_transmissionType": "PTPv2_udp.header.tlvs.tlv.request_unicast_transmission.type-43",
        "Request_unicast_transmissionLength": "PTPv2_udp.header.tlvs.tlv.request_unicast_transmission.length-44",
        "Request_unicast_transmissionMessage_type": "PTPv2_udp.header.tlvs.tlv.request_unicast_transmission.message_type-45",
        "Request_unicast_transmissionReserved": "PTPv2_udp.header.tlvs.tlv.request_unicast_transmission.reserved-46",
        "Request_unicast_transmissionLogInterMessagePeriod": "PTPv2_udp.header.tlvs.tlv.request_unicast_transmission.logInterMessagePeriod-47",
        "Request_unicast_transmissionDuration_field": "PTPv2_udp.header.tlvs.tlv.request_unicast_transmission.duration_field-48",
        "Grant_unicast_transmissionType": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.type-49",
        "Grant_unicast_transmissionLength": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.length-50",
        "Grant_unicast_transmissionMessage_type": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.message_type-51",
        "Grant_unicast_transmissionReserved": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.reserved-52",
        "Grant_unicast_transmissionLogInterMessagePeriod": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.logInterMessagePeriod-53",
        "Grant_unicast_transmissionDuration_field": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.duration_field-54",
        "Grant_unicast_transmissionReserved_8": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.reserved_8-55",
        "Grant_unicast_transmissionZero": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.zero-56",
        "Grant_unicast_transmissionR": "PTPv2_udp.header.tlvs.tlv.grant_unicast_transmission.r-57",
        "Cancel_unicast_transmissionType": "PTPv2_udp.header.tlvs.tlv.cancel_unicast_transmission.type-58",
        "Cancel_unicast_transmissionLength": "PTPv2_udp.header.tlvs.tlv.cancel_unicast_transmission.length-59",
        "Cancel_unicast_transmissionMessage_type": "PTPv2_udp.header.tlvs.tlv.cancel_unicast_transmission.message_type-60",
        "Cancel_unicast_transmissionReserved": "PTPv2_udp.header.tlvs.tlv.cancel_unicast_transmission.reserved-61",
    }

    def __init__(self, parent, list_op=False):
        super(PTPv2udp, self).__init__(parent, list_op)

    @property
    def HeaderTransportSpecific(self):
        """
        Display Name: Transport Specific
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTransportSpecific"])
        )

    @property
    def HeaderMessageType(self):
        """
        Display Name: Message Type
        Default Value: 0
        Value Format: decimal
        Available enum values: Sync, 0, Delay Request, 1, PDelay Request, 2, PDelay Response, 3, Follow Up, 8, Delay Response, 9, PDelay Response Follow Up, 10, Announce, 11, Signalling, 12, Management, 13
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageType"])
        )

    @property
    def HeaderReserved_4(self):
        """
        Display Name: Reserved_4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved_4"])
        )

    @property
    def HeaderVersionPTP(self):
        """
        Display Name: Version PTP
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersionPTP"])
        )

    @property
    def HeaderMessageLength(self):
        """
        Display Name: Message Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageLength"])
        )

    @property
    def HeaderDomainNumber(self):
        """
        Display Name: Domain Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDomainNumber"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderFlagField(self):
        """
        Display Name: Flag Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlagField"])
        )

    @property
    def HeaderCorrectionField(self):
        """
        Display Name: Correction Field
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCorrectionField"])
        )

    @property
    def HeaderReserved_4bytes(self):
        """
        Display Name: Reserved_4bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved_4bytes"])
        )

    @property
    def HeaderSourcePortIdentity(self):
        """
        Display Name: Source Port Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSourcePortIdentity"])
        )

    @property
    def HeaderSequenceId(self):
        """
        Display Name: Sequence Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSequenceId"])
        )

    @property
    def HeaderControlField(self):
        """
        Display Name: Control Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderControlField"])
        )

    @property
    def HeaderLogMessageInterval(self):
        """
        Display Name: Log Message Interval
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLogMessageInterval"])
        )

    @property
    def AnnounceOriginTimestamp(self):
        """
        Display Name: Origin Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceOriginTimestamp"])
        )

    @property
    def AnnounceCurrentUTCOffset(self):
        """
        Display Name: Current UTC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceCurrentUTCOffset"])
        )

    @property
    def AnnounceReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceReserved"])
        )

    @property
    def AnnounceGrandMasterPriority1(self):
        """
        Display Name: Grand Master Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceGrandMasterPriority1"])
        )

    @property
    def AnnounceGrandMasterClockQuality(self):
        """
        Display Name: Grand Master Clock Quality
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AnnounceGrandMasterClockQuality"]),
        )

    @property
    def AnnounceGrandMasterPriority2(self):
        """
        Display Name: Grand Master Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceGrandMasterPriority2"])
        )

    @property
    def AnnounceGrandMasterIdentity(self):
        """
        Display Name: Grand Master Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceGrandMasterIdentity"])
        )

    @property
    def AnnounceStepsRemoved(self):
        """
        Display Name: Steps Removed
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceStepsRemoved"])
        )

    @property
    def AnnounceTimeSource(self):
        """
        Display Name: Time Source
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AnnounceTimeSource"])
        )

    @property
    def SyncOriginTimestamp(self):
        """
        Display Name: Origin Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SyncOriginTimestamp"])
        )

    @property
    def FollowUpPreciseOriginTimestamp(self):
        """
        Display Name: Precise Origin Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FollowUpPreciseOriginTimestamp"]),
        )

    @property
    def DelayRequestOriginTimestamp(self):
        """
        Display Name: Origin Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DelayRequestOriginTimestamp"])
        )

    @property
    def DelayResponseReceiveTimestamp(self):
        """
        Display Name: Receive Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DelayResponseReceiveTimestamp"]),
        )

    @property
    def DelayResponseRequestingPortIdentity(self):
        """
        Display Name: Requesting Port Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DelayResponseRequestingPortIdentity"]
            ),
        )

    @property
    def PDelayReqOriginTimestamp(self):
        """
        Display Name: Origin Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PDelayReqOriginTimestamp"])
        )

    @property
    def PDelayReqReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PDelayReqReserved"])
        )

    @property
    def PDelayResponseRequestReceiptTimestamp(self):
        """
        Display Name: Request Receipt Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PDelayResponseRequestReceiptTimestamp"]
            ),
        )

    @property
    def PDelayResponseRequestPortIdentity(self):
        """
        Display Name: Request Port Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PDelayResponseRequestPortIdentity"]),
        )

    @property
    def PDelayResponseFollowUpResponseOriginTimestamp(self):
        """
        Display Name: responseOriginTimestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PDelayResponseFollowUpResponseOriginTimestamp"]
            ),
        )

    @property
    def PDelayResponseFollowUpRequestingPortIdentity(self):
        """
        Display Name: Requesting Port Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PDelayResponseFollowUpRequestingPortIdentity"]
            ),
        )

    @property
    def SignallingTargetPortIdentity(self):
        """
        Display Name: Target Port Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SignallingTargetPortIdentity"])
        )

    @property
    def ManagementTargetPortIdentity(self):
        """
        Display Name: Target Port Identity
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTargetPortIdentity"])
        )

    @property
    def ManagementStartingBoundaryHops(self):
        """
        Display Name: Starting Boundary Hops
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ManagementStartingBoundaryHops"]),
        )

    @property
    def ManagementBoundaryHops(self):
        """
        Display Name: Boundary Hops
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementBoundaryHops"])
        )

    @property
    def ManagementReserved_1(self):
        """
        Display Name: Reserved_1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementReserved_1"])
        )

    @property
    def ManagementActionField(self):
        """
        Display Name: Action Field
        Default Value: 0
        Value Format: decimal
        Available enum values: GET, 0, SET, 1, RESPONSE, 2, COMMAND, 3, ACKNOWLEDGE, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementActionField"])
        )

    @property
    def ManagementReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementReserved"])
        )

    @property
    def TlvNone(self):
        """
        Display Name: None
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TlvNone"]))

    @property
    def Request_unicast_transmissionType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Request_unicast_transmissionType"]),
        )

    @property
    def Request_unicast_transmissionLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Request_unicast_transmissionLength"]
            ),
        )

    @property
    def Request_unicast_transmissionMessage_type(self):
        """
        Display Name: Message Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Request_unicast_transmissionMessage_type"]
            ),
        )

    @property
    def Request_unicast_transmissionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Request_unicast_transmissionReserved"]
            ),
        )

    @property
    def Request_unicast_transmissionLogInterMessagePeriod(self):
        """
        Display Name: Log Inter Message Period
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Request_unicast_transmissionLogInterMessagePeriod"]
            ),
        )

    @property
    def Request_unicast_transmissionDuration_field(self):
        """
        Display Name: Duration Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Request_unicast_transmissionDuration_field"]
            ),
        )

    @property
    def Grant_unicast_transmissionType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Grant_unicast_transmissionType"]),
        )

    @property
    def Grant_unicast_transmissionLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Grant_unicast_transmissionLength"]),
        )

    @property
    def Grant_unicast_transmissionMessage_type(self):
        """
        Display Name: Message Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Grant_unicast_transmissionMessage_type"]
            ),
        )

    @property
    def Grant_unicast_transmissionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Grant_unicast_transmissionReserved"]
            ),
        )

    @property
    def Grant_unicast_transmissionLogInterMessagePeriod(self):
        """
        Display Name: Log Inter Message Period
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Grant_unicast_transmissionLogInterMessagePeriod"]
            ),
        )

    @property
    def Grant_unicast_transmissionDuration_field(self):
        """
        Display Name: Duration Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Grant_unicast_transmissionDuration_field"]
            ),
        )

    @property
    def Grant_unicast_transmissionReserved_8(self):
        """
        Display Name: Reserved_8
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Grant_unicast_transmissionReserved_8"]
            ),
        )

    @property
    def Grant_unicast_transmissionZero(self):
        """
        Display Name: Zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Grant_unicast_transmissionZero"]),
        )

    @property
    def Grant_unicast_transmissionR(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Grant_unicast_transmissionR"])
        )

    @property
    def Cancel_unicast_transmissionType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Cancel_unicast_transmissionType"]),
        )

    @property
    def Cancel_unicast_transmissionLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Cancel_unicast_transmissionLength"]),
        )

    @property
    def Cancel_unicast_transmissionMessage_type(self):
        """
        Display Name: Message Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Cancel_unicast_transmissionMessage_type"]
            ),
        )

    @property
    def Cancel_unicast_transmissionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Cancel_unicast_transmissionReserved"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

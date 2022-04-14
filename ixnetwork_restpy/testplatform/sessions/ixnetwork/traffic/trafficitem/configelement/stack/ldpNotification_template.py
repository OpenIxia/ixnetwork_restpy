from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpNotification(Base):
    __slots__ = ()
    _SDM_NAME = "ldpNotification"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpNotification.header.version-1",
        "HeaderPduLengthinOctets": "ldpNotification.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpNotification.header.lsrID-3",
        "HeaderLabelSpace": "ldpNotification.header.labelSpace-4",
        "HeaderUBit": "ldpNotification.header.uBit-5",
        "HeaderType": "ldpNotification.header.type-6",
        "HeaderLength": "ldpNotification.header.length-7",
        "HeaderMessageID": "ldpNotification.header.messageID-8",
        "StatusTLVUBit": "ldpNotification.header.statusTLV.uBit-9",
        "StatusTLVFBit": "ldpNotification.header.statusTLV.fBit-10",
        "StatusTLVType": "ldpNotification.header.statusTLV.type-11",
        "StatusTLVLength": "ldpNotification.header.statusTLV.length-12",
        "SuccessEBit": "ldpNotification.header.statusTLV.statusCode.success.eBit-13",
        "SuccessFBit": "ldpNotification.header.statusTLV.statusCode.success.fBit-14",
        "SuccessStatusData": "ldpNotification.header.statusTLV.statusCode.success.statusData-15",
        "BadLDPIdentifierEBit": "ldpNotification.header.statusTLV.statusCode.badLDPIdentifier.eBit-16",
        "BadLDPIdentifierFBit": "ldpNotification.header.statusTLV.statusCode.badLDPIdentifier.fBit-17",
        "BadLDPIdentifierStatusData": "ldpNotification.header.statusTLV.statusCode.badLDPIdentifier.statusData-18",
        "BadProtocolVersionEBit": "ldpNotification.header.statusTLV.statusCode.badProtocolVersion.eBit-19",
        "BadProtocolVersionFBit": "ldpNotification.header.statusTLV.statusCode.badProtocolVersion.fBit-20",
        "BadProtocolVersionStatusData": "ldpNotification.header.statusTLV.statusCode.badProtocolVersion.statusData-21",
        "BadPDULengthEBit": "ldpNotification.header.statusTLV.statusCode.badPDULength.eBit-22",
        "BadPDULengthFBit": "ldpNotification.header.statusTLV.statusCode.badPDULength.fBit-23",
        "BadPDULengthStatusData": "ldpNotification.header.statusTLV.statusCode.badPDULength.statusData-24",
        "UnknownMessageTypeEBit": "ldpNotification.header.statusTLV.statusCode.unknownMessageType.eBit-25",
        "UnknownMessageTypeFBit": "ldpNotification.header.statusTLV.statusCode.unknownMessageType.fBit-26",
        "UnknownMessageTypeStatusData": "ldpNotification.header.statusTLV.statusCode.unknownMessageType.statusData-27",
        "BadMessageLengthEBit": "ldpNotification.header.statusTLV.statusCode.badMessageLength.eBit-28",
        "BadMessageLengthFBit": "ldpNotification.header.statusTLV.statusCode.badMessageLength.fBit-29",
        "BadMessageLengthStatusData": "ldpNotification.header.statusTLV.statusCode.badMessageLength.statusData-30",
        "UnknownTLVEBit": "ldpNotification.header.statusTLV.statusCode.unknownTLV.eBit-31",
        "UnknownTLVFBit": "ldpNotification.header.statusTLV.statusCode.unknownTLV.fBit-32",
        "UnknownTLVStatusData": "ldpNotification.header.statusTLV.statusCode.unknownTLV.statusData-33",
        "BadTLVLengthEBit": "ldpNotification.header.statusTLV.statusCode.badTLVLength.eBit-34",
        "BadTLVLengthFBit": "ldpNotification.header.statusTLV.statusCode.badTLVLength.fBit-35",
        "BadTLVLengthStatusData": "ldpNotification.header.statusTLV.statusCode.badTLVLength.statusData-36",
        "MalformedTLVValueEBit": "ldpNotification.header.statusTLV.statusCode.malformedTLVValue.eBit-37",
        "MalformedTLVValueFBit": "ldpNotification.header.statusTLV.statusCode.malformedTLVValue.fBit-38",
        "MalformedTLVValueStatusData": "ldpNotification.header.statusTLV.statusCode.malformedTLVValue.statusData-39",
        "HoldTimerExpiredEBit": "ldpNotification.header.statusTLV.statusCode.holdTimerExpired.eBit-40",
        "HoldTimerExpiredFBit": "ldpNotification.header.statusTLV.statusCode.holdTimerExpired.fBit-41",
        "HoldTimerExpiredStatusData": "ldpNotification.header.statusTLV.statusCode.holdTimerExpired.statusData-42",
        "ShutdownEBit": "ldpNotification.header.statusTLV.statusCode.shutdown.eBit-43",
        "ShutdownFBit": "ldpNotification.header.statusTLV.statusCode.shutdown.fBit-44",
        "ShutdownStatusData": "ldpNotification.header.statusTLV.statusCode.shutdown.statusData-45",
        "LoopDetectedEBit": "ldpNotification.header.statusTLV.statusCode.loopDetected.eBit-46",
        "LoopDetectedFBit": "ldpNotification.header.statusTLV.statusCode.loopDetected.fBit-47",
        "LoopDetectedStatusData": "ldpNotification.header.statusTLV.statusCode.loopDetected.statusData-48",
        "UnknownFECEBit": "ldpNotification.header.statusTLV.statusCode.unknownFEC.eBit-49",
        "UnknownFECFBit": "ldpNotification.header.statusTLV.statusCode.unknownFEC.fBit-50",
        "UnknownFECStatusData": "ldpNotification.header.statusTLV.statusCode.unknownFEC.statusData-51",
        "NoRouteEBit": "ldpNotification.header.statusTLV.statusCode.noRoute.eBit-52",
        "NoRouteFBit": "ldpNotification.header.statusTLV.statusCode.noRoute.fBit-53",
        "NoRouteStatusData": "ldpNotification.header.statusTLV.statusCode.noRoute.statusData-54",
        "NoLabelResourcesEBit": "ldpNotification.header.statusTLV.statusCode.noLabelResources.eBit-55",
        "NoLabelResourcesFBit": "ldpNotification.header.statusTLV.statusCode.noLabelResources.fBit-56",
        "NoLabelResourcesStatusData": "ldpNotification.header.statusTLV.statusCode.noLabelResources.statusData-57",
        "LabelResourcesAvailableEBit": "ldpNotification.header.statusTLV.statusCode.labelResourcesAvailable.eBit-58",
        "LabelResourcesAvailableFBit": "ldpNotification.header.statusTLV.statusCode.labelResourcesAvailable.fBit-59",
        "LabelResourcesAvailableStatusData": "ldpNotification.header.statusTLV.statusCode.labelResourcesAvailable.statusData-60",
        "SessionRejectedNoHelloEBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedNoHello.eBit-61",
        "SessionRejectedNoHelloFBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedNoHello.fBit-62",
        "SessionRejectedNoHelloStatusData": "ldpNotification.header.statusTLV.statusCode.sessionRejectedNoHello.statusData-63",
        "SessionRejectedAdvertisementModeEBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedAdvertisementMode.eBit-64",
        "SessionRejectedAdvertisementModeFBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedAdvertisementMode.fBit-65",
        "SessionRejectedAdvertisementModeStatusData": "ldpNotification.header.statusTLV.statusCode.sessionRejectedAdvertisementMode.statusData-66",
        "SessionRejectedMaxPDULengthEBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedMaxPDULength.eBit-67",
        "SessionRejectedMaxPDULengthFBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedMaxPDULength.fBit-68",
        "SessionRejectedMaxPDULengthStatusData": "ldpNotification.header.statusTLV.statusCode.sessionRejectedMaxPDULength.statusData-69",
        "SessionRejectedLabelRangeEBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedLabelRange.eBit-70",
        "SessionRejectedLabelRangeFBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedLabelRange.fBit-71",
        "SessionRejectedLabelRangeStatusData": "ldpNotification.header.statusTLV.statusCode.sessionRejectedLabelRange.statusData-72",
        "KeepaliveTimerExiredEBit": "ldpNotification.header.statusTLV.statusCode.keepaliveTimerExired.eBit-73",
        "KeepaliveTimerExiredFBit": "ldpNotification.header.statusTLV.statusCode.keepaliveTimerExired.fBit-74",
        "KeepaliveTimerExiredStatusData": "ldpNotification.header.statusTLV.statusCode.keepaliveTimerExired.statusData-75",
        "LabelRequestAbortedEBit": "ldpNotification.header.statusTLV.statusCode.labelRequestAborted.eBit-76",
        "LabelRequestAbortedFBit": "ldpNotification.header.statusTLV.statusCode.labelRequestAborted.fBit-77",
        "LabelRequestAbortedStatusData": "ldpNotification.header.statusTLV.statusCode.labelRequestAborted.statusData-78",
        "MissingMessageParametersEBit": "ldpNotification.header.statusTLV.statusCode.missingMessageParameters.eBit-79",
        "MissingMessageParametersFBit": "ldpNotification.header.statusTLV.statusCode.missingMessageParameters.fBit-80",
        "MissingMessageParametersStatusData": "ldpNotification.header.statusTLV.statusCode.missingMessageParameters.statusData-81",
        "UnsupportedAddressFamilyEBit": "ldpNotification.header.statusTLV.statusCode.unsupportedAddressFamily.eBit-82",
        "UnsupportedAddressFamilyFBit": "ldpNotification.header.statusTLV.statusCode.unsupportedAddressFamily.fBit-83",
        "UnsupportedAddressFamilyStatusData": "ldpNotification.header.statusTLV.statusCode.unsupportedAddressFamily.statusData-84",
        "SessionRejectedBadKeepaliveTimeEBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedBadKeepaliveTime.eBit-85",
        "SessionRejectedBadKeepaliveTimeFBit": "ldpNotification.header.statusTLV.statusCode.sessionRejectedBadKeepaliveTime.fBit-86",
        "SessionRejectedBadKeepaliveTimeStatusData": "ldpNotification.header.statusTLV.statusCode.sessionRejectedBadKeepaliveTime.statusData-87",
        "InternalErrorEBit": "ldpNotification.header.statusTLV.statusCode.internalError.eBit-88",
        "InternalErrorFBit": "ldpNotification.header.statusTLV.statusCode.internalError.fBit-89",
        "InternalErrorStatusData": "ldpNotification.header.statusTLV.statusCode.internalError.statusData-90",
        "StatusTLVMessageID": "ldpNotification.header.statusTLV.messageID-91",
        "StatusTLVMessageType": "ldpNotification.header.statusTLV.messageType-92",
        "TclLDPMpStatusTLVUBit": "ldpNotification.header.tclLDPMpStatusTLV.uBit-93",
        "TclLDPMpStatusTLVFBit": "ldpNotification.header.tclLDPMpStatusTLV.fBit-94",
        "TclLDPMpStatusTLVTclType": "ldpNotification.header.tclLDPMpStatusTLV.tclType-95",
        "TclLDPMpStatusTLVTclLength": "ldpNotification.header.tclLDPMpStatusTLV.tclLength-96",
        "TclCustomTypeTclType": "ldpNotification.header.tclLDPMpStatusTLV.tclLDPMPStatusValueElements.selectTLVType.tclCustomType.tclType-97",
        "TclCustomTypeTclLength": "ldpNotification.header.tclLDPMpStatusTLV.tclLDPMPStatusValueElements.selectTLVType.tclCustomType.tclLength-98",
        "TclCustomTypeTclValue": "ldpNotification.header.tclLDPMpStatusTLV.tclLDPMPStatusValueElements.selectTLVType.tclCustomType.tclValue-99",
        "FecTLVUBit": "ldpNotification.header.fecTLV.uBit-100",
        "FecTLVFBit": "ldpNotification.header.fecTLV.fBit-101",
        "FecTLVType": "ldpNotification.header.fecTLV.type-102",
        "FecTLVLength": "ldpNotification.header.fecTLV.length-103",
        "TclP2mpTclType": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclType-104",
        "TclIpv4P2mpAddressTclP2mpAddressFamily": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressFamily-105",
        "TclIpv4P2mpAddressTclP2mpAddressLength": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressLength-106",
        "TclIpv4P2mpAddressTclRootAddress": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclRootAddress-107",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressFamily": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressFamily-108",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressLength": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressLength-109",
        "TclIpv6P2mpAddressTclIpv6RootAddress": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclIpv6RootAddress-110",
        "TclP2mpTclOpaqueLength": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueLength-111",
        "TclGenericLSPIdentifierTLVTclType": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclType-112",
        "TclGenericLSPIdentifierTLVTclLength": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclLength-113",
        "TclGenericLSPIdentifierTLVTclValue": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclValue-114",
        "TclEditTLVTclType": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclType-115",
        "TclEditTLVTclLength": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclLength-116",
        "TclEditTLVTclValue": "ldpNotification.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclValue-117",
        "TclP2mpTypedWcardTclTypeTypedWcard": "ldpNotification.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeTypedWcard-118",
        "TclP2mpTypedWcardTclTypeWcard": "ldpNotification.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeWcard-119",
        "TclP2mpTypedWcardTclTypeLen": "ldpNotification.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeLen-120",
        "TclP2mpTypedWcardTclTypeAfi": "ldpNotification.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeAfi-121",
        "GenericLabelTLVUBit": "ldpNotification.header.labelTLV.genericLabelTLV.uBit-122",
        "GenericLabelTLVFBit": "ldpNotification.header.labelTLV.genericLabelTLV.fBit-123",
        "GenericLabelTLVType": "ldpNotification.header.labelTLV.genericLabelTLV.type-124",
        "GenericLabelTLVLength": "ldpNotification.header.labelTLV.genericLabelTLV.length-125",
        "GenericLabelTLVLabel": "ldpNotification.header.labelTLV.genericLabelTLV.label-126",
        "AtmLabelTLVUBit": "ldpNotification.header.labelTLV.atmLabelTLV.uBit-127",
        "AtmLabelTLVFBit": "ldpNotification.header.labelTLV.atmLabelTLV.fBit-128",
        "AtmLabelTLVType": "ldpNotification.header.labelTLV.atmLabelTLV.type-129",
        "AtmLabelTLVLength": "ldpNotification.header.labelTLV.atmLabelTLV.length-130",
        "AtmLabelTLVReserved": "ldpNotification.header.labelTLV.atmLabelTLV.reserved-131",
        "AtmLabelTLVVBits": "ldpNotification.header.labelTLV.atmLabelTLV.vBits-132",
        "AtmLabelTLVVpi": "ldpNotification.header.labelTLV.atmLabelTLV.vpi-133",
        "AtmLabelTLVVci": "ldpNotification.header.labelTLV.atmLabelTLV.vci-134",
        "FrameRelayLabelTLVUBit": "ldpNotification.header.labelTLV.frameRelayLabelTLV.uBit-135",
        "FrameRelayLabelTLVFBit": "ldpNotification.header.labelTLV.frameRelayLabelTLV.fBit-136",
        "FrameRelayLabelTLVType": "ldpNotification.header.labelTLV.frameRelayLabelTLV.type-137",
        "FrameRelayLabelTLVLength": "ldpNotification.header.labelTLV.frameRelayLabelTLV.length-138",
        "FrameRelayLabelTLVReserved": "ldpNotification.header.labelTLV.frameRelayLabelTLV.reserved-139",
        "FrameRelayLabelTLVDlciLength": "ldpNotification.header.labelTLV.frameRelayLabelTLV.dlciLength-140",
        "FrameRelayLabelTLVDlci": "ldpNotification.header.labelTLV.frameRelayLabelTLV.dlci-141",
        "ExtendedStatusTLVUBit": "ldpNotification.header.optionalParameter.extendedStatusTLV.uBit-142",
        "ExtendedStatusTLVFBit": "ldpNotification.header.optionalParameter.extendedStatusTLV.fBit-143",
        "ExtendedStatusTLVType": "ldpNotification.header.optionalParameter.extendedStatusTLV.type-144",
        "ExtendedStatusTLVLength": "ldpNotification.header.optionalParameter.extendedStatusTLV.length-145",
        "ExtendedStatusTLVCode": "ldpNotification.header.optionalParameter.extendedStatusTLV.code-146",
        "ReturnedPDUTLVUBit": "ldpNotification.header.optionalParameter.returnedPDUTLV.uBit-147",
        "ReturnedPDUTLVFBit": "ldpNotification.header.optionalParameter.returnedPDUTLV.fBit-148",
        "ReturnedPDUTLVType": "ldpNotification.header.optionalParameter.returnedPDUTLV.type-149",
        "ReturnedPDUTLVLength": "ldpNotification.header.optionalParameter.returnedPDUTLV.length-150",
        "ReturnedMessageTLVUBit": "ldpNotification.header.optionalParameter.returnedMessageTLV.uBit-151",
        "ReturnedMessageTLVFBit": "ldpNotification.header.optionalParameter.returnedMessageTLV.fBit-152",
        "ReturnedMessageTLVType": "ldpNotification.header.optionalParameter.returnedMessageTLV.type-153",
        "ReturnedMessageTLVLength": "ldpNotification.header.optionalParameter.returnedMessageTLV.length-154",
        "ExtendedStatusTLVUBit": "ldpNotification.header.optionalParameter.extendedStatusTLV.uBit-155",
        "ExtendedStatusTLVFBit": "ldpNotification.header.optionalParameter.extendedStatusTLV.fBit-156",
        "ExtendedStatusTLVType": "ldpNotification.header.optionalParameter.extendedStatusTLV.type-157",
        "ExtendedStatusTLVLength": "ldpNotification.header.optionalParameter.extendedStatusTLV.length-158",
        "ExtendedStatusTLVCode": "ldpNotification.header.optionalParameter.extendedStatusTLV.code-159",
    }

    def __init__(self, parent, list_op=False):
        super(LdpNotification, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderPduLengthinOctets(self):
        """
        Display Name: PDU length(in octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPduLengthinOctets"])
        )

    @property
    def HeaderLsrID(self):
        """
        Display Name: LSR ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLsrID"]))

    @property
    def HeaderLabelSpace(self):
        """
        Display Name: Label space
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLabelSpace"])
        )

    @property
    def HeaderUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderUBit"]))

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderMessageID(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageID"])
        )

    @property
    def StatusTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StatusTLVUBit"]))

    @property
    def StatusTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StatusTLVFBit"]))

    @property
    def StatusTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0300
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StatusTLVType"]))

    @property
    def StatusTLVLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusTLVLength"])
        )

    @property
    def SuccessEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SuccessEBit"]))

    @property
    def SuccessFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SuccessFBit"]))

    @property
    def SuccessStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SuccessStatusData"])
        )

    @property
    def BadLDPIdentifierEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadLDPIdentifierEBit"])
        )

    @property
    def BadLDPIdentifierFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadLDPIdentifierFBit"])
        )

    @property
    def BadLDPIdentifierStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadLDPIdentifierStatusData"])
        )

    @property
    def BadProtocolVersionEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadProtocolVersionEBit"])
        )

    @property
    def BadProtocolVersionFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadProtocolVersionFBit"])
        )

    @property
    def BadProtocolVersionStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadProtocolVersionStatusData"])
        )

    @property
    def BadPDULengthEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadPDULengthEBit"])
        )

    @property
    def BadPDULengthFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadPDULengthFBit"])
        )

    @property
    def BadPDULengthStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000003
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadPDULengthStatusData"])
        )

    @property
    def UnknownMessageTypeEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownMessageTypeEBit"])
        )

    @property
    def UnknownMessageTypeFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownMessageTypeFBit"])
        )

    @property
    def UnknownMessageTypeStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000004
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownMessageTypeStatusData"])
        )

    @property
    def BadMessageLengthEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadMessageLengthEBit"])
        )

    @property
    def BadMessageLengthFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadMessageLengthFBit"])
        )

    @property
    def BadMessageLengthStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000005
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadMessageLengthStatusData"])
        )

    @property
    def UnknownTLVEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownTLVEBit"])
        )

    @property
    def UnknownTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownTLVFBit"])
        )

    @property
    def UnknownTLVStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000006
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownTLVStatusData"])
        )

    @property
    def BadTLVLengthEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadTLVLengthEBit"])
        )

    @property
    def BadTLVLengthFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadTLVLengthFBit"])
        )

    @property
    def BadTLVLengthStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000007
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BadTLVLengthStatusData"])
        )

    @property
    def MalformedTLVValueEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MalformedTLVValueEBit"])
        )

    @property
    def MalformedTLVValueFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MalformedTLVValueFBit"])
        )

    @property
    def MalformedTLVValueStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000008
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MalformedTLVValueStatusData"])
        )

    @property
    def HoldTimerExpiredEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HoldTimerExpiredEBit"])
        )

    @property
    def HoldTimerExpiredFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HoldTimerExpiredFBit"])
        )

    @property
    def HoldTimerExpiredStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000009
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HoldTimerExpiredStatusData"])
        )

    @property
    def ShutdownEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ShutdownEBit"]))

    @property
    def ShutdownFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ShutdownFBit"]))

    @property
    def ShutdownStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x000000A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShutdownStatusData"])
        )

    @property
    def LoopDetectedEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LoopDetectedEBit"])
        )

    @property
    def LoopDetectedFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LoopDetectedFBit"])
        )

    @property
    def LoopDetectedStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x000000B
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LoopDetectedStatusData"])
        )

    @property
    def UnknownFECEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownFECEBit"])
        )

    @property
    def UnknownFECFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownFECFBit"])
        )

    @property
    def UnknownFECStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x000000C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnknownFECStatusData"])
        )

    @property
    def NoRouteEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NoRouteEBit"]))

    @property
    def NoRouteFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NoRouteFBit"]))

    @property
    def NoRouteStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x000000D
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoRouteStatusData"])
        )

    @property
    def NoLabelResourcesEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoLabelResourcesEBit"])
        )

    @property
    def NoLabelResourcesFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoLabelResourcesFBit"])
        )

    @property
    def NoLabelResourcesStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x000000E
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoLabelResourcesStatusData"])
        )

    @property
    def LabelResourcesAvailableEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelResourcesAvailableEBit"])
        )

    @property
    def LabelResourcesAvailableFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelResourcesAvailableFBit"])
        )

    @property
    def LabelResourcesAvailableStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x000000F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LabelResourcesAvailableStatusData"]),
        )

    @property
    def SessionRejectedNoHelloEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SessionRejectedNoHelloEBit"])
        )

    @property
    def SessionRejectedNoHelloFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SessionRejectedNoHelloFBit"])
        )

    @property
    def SessionRejectedNoHelloStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000010
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SessionRejectedNoHelloStatusData"]),
        )

    @property
    def SessionRejectedAdvertisementModeEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedAdvertisementModeEBit"]
            ),
        )

    @property
    def SessionRejectedAdvertisementModeFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedAdvertisementModeFBit"]
            ),
        )

    @property
    def SessionRejectedAdvertisementModeStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000011
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedAdvertisementModeStatusData"]
            ),
        )

    @property
    def SessionRejectedMaxPDULengthEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SessionRejectedMaxPDULengthEBit"]),
        )

    @property
    def SessionRejectedMaxPDULengthFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SessionRejectedMaxPDULengthFBit"]),
        )

    @property
    def SessionRejectedMaxPDULengthStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000012
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedMaxPDULengthStatusData"]
            ),
        )

    @property
    def SessionRejectedLabelRangeEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SessionRejectedLabelRangeEBit"]),
        )

    @property
    def SessionRejectedLabelRangeFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SessionRejectedLabelRangeFBit"]),
        )

    @property
    def SessionRejectedLabelRangeStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000013
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedLabelRangeStatusData"]
            ),
        )

    @property
    def KeepaliveTimerExiredEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeepaliveTimerExiredEBit"])
        )

    @property
    def KeepaliveTimerExiredFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeepaliveTimerExiredFBit"])
        )

    @property
    def KeepaliveTimerExiredStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000014
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["KeepaliveTimerExiredStatusData"]),
        )

    @property
    def LabelRequestAbortedEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelRequestAbortedEBit"])
        )

    @property
    def LabelRequestAbortedFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelRequestAbortedFBit"])
        )

    @property
    def LabelRequestAbortedStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000015
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LabelRequestAbortedStatusData"]),
        )

    @property
    def MissingMessageParametersEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MissingMessageParametersEBit"])
        )

    @property
    def MissingMessageParametersFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MissingMessageParametersFBit"])
        )

    @property
    def MissingMessageParametersStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000016
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MissingMessageParametersStatusData"]
            ),
        )

    @property
    def UnsupportedAddressFamilyEBit(self):
        """
        Display Name: E bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnsupportedAddressFamilyEBit"])
        )

    @property
    def UnsupportedAddressFamilyFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnsupportedAddressFamilyFBit"])
        )

    @property
    def UnsupportedAddressFamilyStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000017
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UnsupportedAddressFamilyStatusData"]
            ),
        )

    @property
    def SessionRejectedBadKeepaliveTimeEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedBadKeepaliveTimeEBit"]
            ),
        )

    @property
    def SessionRejectedBadKeepaliveTimeFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedBadKeepaliveTimeFBit"]
            ),
        )

    @property
    def SessionRejectedBadKeepaliveTimeStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000018
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SessionRejectedBadKeepaliveTimeStatusData"]
            ),
        )

    @property
    def InternalErrorEBit(self):
        """
        Display Name: E bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Advisory notification, 0, Fatal error, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InternalErrorEBit"])
        )

    @property
    def InternalErrorFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InternalErrorFBit"])
        )

    @property
    def InternalErrorStatusData(self):
        """
        Display Name: Status data
        Default Value: 0x0000019
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InternalErrorStatusData"])
        )

    @property
    def StatusTLVMessageID(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusTLVMessageID"])
        )

    @property
    def StatusTLVMessageType(self):
        """
        Display Name: Message type
        Default Value: 256
        Value Format: decimal
        Available enum values: Notification message, 1, Hello message, 256, Initialization message, 512, Keepalive message, 513, Address message, 768, Address withdraw message, 769, Label mapping message, 1024, Label request message, 1025, Label withdraw message, 1026, Label release message, 1027, Label abort request message, 1028
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusTLVMessageType"])
        )

    @property
    def TclLDPMpStatusTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclLDPMpStatusTLVUBit"])
        )

    @property
    def TclLDPMpStatusTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclLDPMpStatusTLVFBit"])
        )

    @property
    def TclLDPMpStatusTLVTclType(self):
        """
        Display Name: Type
        Default Value: 0x0040
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclLDPMpStatusTLVTclType"])
        )

    @property
    def TclLDPMpStatusTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclLDPMpStatusTLVTclLength"])
        )

    @property
    def TclCustomTypeTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclCustomTypeTclType"])
        )

    @property
    def TclCustomTypeTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclCustomTypeTclLength"])
        )

    @property
    def TclCustomTypeTclValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclCustomTypeTclValue"])
        )

    @property
    def FecTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVUBit"]))

    @property
    def FecTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVFBit"]))

    @property
    def FecTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVType"]))

    @property
    def FecTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVLength"]))

    @property
    def TclP2mpTclType(self):
        """
        Display Name: Type
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTclType"])
        )

    @property
    def TclIpv4P2mpAddressTclP2mpAddressFamily(self):
        """
        Display Name: Address Family
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv4P2mpAddressTclP2mpAddressFamily"]
            ),
        )

    @property
    def TclIpv4P2mpAddressTclP2mpAddressLength(self):
        """
        Display Name: Address length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv4P2mpAddressTclP2mpAddressLength"]
            ),
        )

    @property
    def TclIpv4P2mpAddressTclRootAddress(self):
        """
        Display Name: Root Node Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclIpv4P2mpAddressTclRootAddress"]),
        )

    @property
    def TclIpv6P2mpAddressTclP2mpIpv6AddressFamily(self):
        """
        Display Name: Address Family
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv6P2mpAddressTclP2mpIpv6AddressFamily"]
            ),
        )

    @property
    def TclIpv6P2mpAddressTclP2mpIpv6AddressLength(self):
        """
        Display Name: Address length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv6P2mpAddressTclP2mpIpv6AddressLength"]
            ),
        )

    @property
    def TclIpv6P2mpAddressTclIpv6RootAddress(self):
        """
        Display Name: Root Node Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv6P2mpAddressTclIpv6RootAddress"]
            ),
        )

    @property
    def TclP2mpTclOpaqueLength(self):
        """
        Display Name: Opaque Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTclOpaqueLength"])
        )

    @property
    def TclGenericLSPIdentifierTLVTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclGenericLSPIdentifierTLVTclType"]),
        )

    @property
    def TclGenericLSPIdentifierTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclGenericLSPIdentifierTLVTclLength"]
            ),
        )

    @property
    def TclGenericLSPIdentifierTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclGenericLSPIdentifierTLVTclValue"]
            ),
        )

    @property
    def TclEditTLVTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclEditTLVTclType"])
        )

    @property
    def TclEditTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclEditTLVTclLength"])
        )

    @property
    def TclEditTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclEditTLVTclValue"])
        )

    @property
    def TclP2mpTypedWcardTclTypeTypedWcard(self):
        """
        Display Name: Typed Wcard
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeTypedWcard"]
            ),
        )

    @property
    def TclP2mpTypedWcardTclTypeWcard(self):
        """
        Display Name: Type
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeWcard"]),
        )

    @property
    def TclP2mpTypedWcardTclTypeLen(self):
        """
        Display Name: Len
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeLen"])
        )

    @property
    def TclP2mpTypedWcardTclTypeAfi(self):
        """
        Display Name: AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeAfi"])
        )

    @property
    def GenericLabelTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVUBit"])
        )

    @property
    def GenericLabelTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVFBit"])
        )

    @property
    def GenericLabelTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0200
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVType"])
        )

    @property
    def GenericLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVLength"])
        )

    @property
    def GenericLabelTLVLabel(self):
        """
        Display Name: Label
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVLabel"])
        )

    @property
    def AtmLabelTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVUBit"])
        )

    @property
    def AtmLabelTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVFBit"])
        )

    @property
    def AtmLabelTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0201
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVType"])
        )

    @property
    def AtmLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVLength"])
        )

    @property
    def AtmLabelTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVReserved"])
        )

    @property
    def AtmLabelTLVVBits(self):
        """
        Display Name: V bits
        Default Value: 0
        Value Format: decimal
        Available enum values: VPI and VCI significant, 0, Only VPI significant, 1, Only VCI significant, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVVBits"])
        )

    @property
    def AtmLabelTLVVpi(self):
        """
        Display Name: VPI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVVpi"])
        )

    @property
    def AtmLabelTLVVci(self):
        """
        Display Name: VCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVVci"])
        )

    @property
    def FrameRelayLabelTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVUBit"])
        )

    @property
    def FrameRelayLabelTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVFBit"])
        )

    @property
    def FrameRelayLabelTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0202
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVType"])
        )

    @property
    def FrameRelayLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVLength"])
        )

    @property
    def FrameRelayLabelTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVReserved"])
        )

    @property
    def FrameRelayLabelTLVDlciLength(self):
        """
        Display Name: DLCI length
        Default Value: 0
        Value Format: decimal
        Available enum values: 10 bits, 0, 23 bits, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVDlciLength"])
        )

    @property
    def FrameRelayLabelTLVDlci(self):
        """
        Display Name: DLCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVDlci"])
        )

    @property
    def ExtendedStatusTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVUBit"])
        )

    @property
    def ExtendedStatusTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVFBit"])
        )

    @property
    def ExtendedStatusTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0301
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVType"])
        )

    @property
    def ExtendedStatusTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVLength"])
        )

    @property
    def ExtendedStatusTLVCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVCode"])
        )

    @property
    def ReturnedPDUTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedPDUTLVUBit"])
        )

    @property
    def ReturnedPDUTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedPDUTLVFBit"])
        )

    @property
    def ReturnedPDUTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0302
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedPDUTLVType"])
        )

    @property
    def ReturnedPDUTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedPDUTLVLength"])
        )

    @property
    def ReturnedMessageTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedMessageTLVUBit"])
        )

    @property
    def ReturnedMessageTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedMessageTLVFBit"])
        )

    @property
    def ReturnedMessageTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0303
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedMessageTLVType"])
        )

    @property
    def ReturnedMessageTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReturnedMessageTLVLength"])
        )

    @property
    def ExtendedStatusTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVUBit"])
        )

    @property
    def ExtendedStatusTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVFBit"])
        )

    @property
    def ExtendedStatusTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0301
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVType"])
        )

    @property
    def ExtendedStatusTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVLength"])
        )

    @property
    def ExtendedStatusTLVCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedStatusTLVCode"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

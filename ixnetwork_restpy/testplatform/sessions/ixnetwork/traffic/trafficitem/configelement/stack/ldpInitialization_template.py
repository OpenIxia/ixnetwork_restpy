from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpInitialization(Base):
    __slots__ = ()
    _SDM_NAME = "ldpInitialization"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpInitialization.header.version-1",
        "HeaderPduLengthinOctets": "ldpInitialization.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpInitialization.header.lsrID-3",
        "HeaderLabelSpace": "ldpInitialization.header.labelSpace-4",
        "HeaderUBit": "ldpInitialization.header.uBit-5",
        "HeaderType": "ldpInitialization.header.type-6",
        "HeaderLength": "ldpInitialization.header.length-7",
        "HeaderMessageID": "ldpInitialization.header.messageID-8",
        "CommonSessionParametersTLVUBit": "ldpInitialization.header.commonSessionParametersTLV.uBit-9",
        "CommonSessionParametersTLVFBit": "ldpInitialization.header.commonSessionParametersTLV.fBit-10",
        "CommonSessionParametersTLVType": "ldpInitialization.header.commonSessionParametersTLV.type-11",
        "CommonSessionParametersTLVLength": "ldpInitialization.header.commonSessionParametersTLV.length-12",
        "CommonSessionParametersTLVVersion": "ldpInitialization.header.commonSessionParametersTLV.version-13",
        "CommonSessionParametersTLVKeepaliveTime": "ldpInitialization.header.commonSessionParametersTLV.keepaliveTime-14",
        "CommonSessionParametersTLVABit": "ldpInitialization.header.commonSessionParametersTLV.aBit-15",
        "CommonSessionParametersTLVDBit": "ldpInitialization.header.commonSessionParametersTLV.dBit-16",
        "CommonSessionParametersTLVReserved": "ldpInitialization.header.commonSessionParametersTLV.reserved-17",
        "CommonSessionParametersTLVPathVectorLimit": "ldpInitialization.header.commonSessionParametersTLV.pathVectorLimit-18",
        "CommonSessionParametersTLVMaxPDULength": "ldpInitialization.header.commonSessionParametersTLV.maxPDULength-19",
        "CommonSessionParametersTLVLsrID": "ldpInitialization.header.commonSessionParametersTLV.lsrID-20",
        "CommonSessionParametersTLVLabelSpace": "ldpInitialization.header.commonSessionParametersTLV.labelSpace-21",
        "AtmSessionParametersTLVUBit": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.uBit-22",
        "AtmSessionParametersTLVFBit": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.fBit-23",
        "AtmSessionParametersTLVType": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.type-24",
        "AtmSessionParametersTLVLength": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.length-25",
        "AtmSessionParametersTLVAtmMergeCapabilities": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmMergeCapabilities-26",
        "AtmSessionParametersTLVNumberOfLabelRangeComponents": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.numberOfLabelRangeComponents-27",
        "AtmSessionParametersTLVDBit": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.dBit-28",
        "AtmSessionParametersTLVReserved": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.reserved-29",
        "AtmLabelRangeComponentReserved": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmLabelRangeComponent.reserved-30",
        "AtmLabelRangeComponentMinimumVPI": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmLabelRangeComponent.minimumVPI-31",
        "AtmLabelRangeComponentMinimumVCI": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmLabelRangeComponent.minimumVCI-32",
        "AtmsessionparameterstlvAtmLabelRangeComponentReserved": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmLabelRangeComponent.reserved-33",
        "AtmLabelRangeComponentMaximumVPI": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmLabelRangeComponent.maximumVPI-34",
        "AtmLabelRangeComponentMaximumVCI": "ldpInitialization.header.optionalParameter.atmSessionParametersTLV.atmLabelRangeComponent.maximumVCI-35",
        "FrameRelaySessionParametersTLVUBit": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.uBit-36",
        "FrameRelaySessionParametersTLVFBit": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.fBit-37",
        "FrameRelaySessionParametersTLVType": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.type-38",
        "FrameRelaySessionParametersTLVLength": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.length-39",
        "FrameRelaySessionParametersTLVFrameRelayMergeCapabilities": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.frameRelayMergeCapabilities-40",
        "FrameRelaySessionParametersTLVNumberOfLabelRangeComponents": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.numberOfLabelRangeComponents-41",
        "FrameRelaySessionParametersTLVDBit": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.dBit-42",
        "FrameRelaySessionParametersTLVReserved": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.reserved-43",
        "FrameRelayLabelRangeComponentReserved": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.frameRelayLabelRangeComponent.reserved-44",
        "FrameRelayLabelRangeComponentDlciLength": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.frameRelayLabelRangeComponent.dlciLength-45",
        "FrameRelayLabelRangeComponentMinimumDLCI": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.frameRelayLabelRangeComponent.minimumDLCI-46",
        "FramerelaysessionparameterstlvFrameRelayLabelRangeComponentReserved": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.frameRelayLabelRangeComponent.reserved-47",
        "FrameRelayLabelRangeComponentMaximumDLCI": "ldpInitialization.header.optionalParameter.frameRelaySessionParametersTLV.frameRelayLabelRangeComponent.maximumDLCI-48",
        "P2mpCapabilityParametersTLVUBit": "ldpInitialization.header.optionalParameter.p2mpCapabilityParametersTLV.uBit-49",
        "P2mpCapabilityParametersTLVFBit": "ldpInitialization.header.optionalParameter.p2mpCapabilityParametersTLV.fBit-50",
        "P2mpCapabilityParametersTLVTclP2mpCapabilityParameter": "ldpInitialization.header.optionalParameter.p2mpCapabilityParametersTLV.tclP2mpCapabilityParameter-51",
        "P2mpCapabilityParametersTLVTclP2mpCapabilityParameterLength": "ldpInitialization.header.optionalParameter.p2mpCapabilityParametersTLV.tclP2mpCapabilityParameterLength-52",
        "P2mpCapabilityParametersTLVSBit": "ldpInitialization.header.optionalParameter.p2mpCapabilityParametersTLV.sBit-53",
        "P2mpCapabilityParametersTLVTclP2mpCapabilityParameterReserved": "ldpInitialization.header.optionalParameter.p2mpCapabilityParametersTLV.tclP2mpCapabilityParameterReserved-54",
    }

    def __init__(self, parent, list_op=False):
        super(LdpInitialization, self).__init__(parent, list_op)

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
        Default Value: 0x0200
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
    def CommonSessionParametersTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVUBit"]),
        )

    @property
    def CommonSessionParametersTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVFBit"]),
        )

    @property
    def CommonSessionParametersTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0500
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVType"]),
        )

    @property
    def CommonSessionParametersTLVLength(self):
        """
        Display Name: Length
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVLength"]),
        )

    @property
    def CommonSessionParametersTLVVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVVersion"]),
        )

    @property
    def CommonSessionParametersTLVKeepaliveTime(self):
        """
        Display Name: Keepalive time
        Default Value: 30
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonSessionParametersTLVKeepaliveTime"]
            ),
        )

    @property
    def CommonSessionParametersTLVABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Downstream unsolicited, 0, Downstream on demand, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVABit"]),
        )

    @property
    def CommonSessionParametersTLVDBit(self):
        """
        Display Name: D bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Loop detection disabled, 0, Loop detection enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVDBit"]),
        )

    @property
    def CommonSessionParametersTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonSessionParametersTLVReserved"]
            ),
        )

    @property
    def CommonSessionParametersTLVPathVectorLimit(self):
        """
        Display Name: Path vector limit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonSessionParametersTLVPathVectorLimit"]
            ),
        )

    @property
    def CommonSessionParametersTLVMaxPDULength(self):
        """
        Display Name: Max PDU length
        Default Value: 4096
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonSessionParametersTLVMaxPDULength"]
            ),
        )

    @property
    def CommonSessionParametersTLVLsrID(self):
        """
        Display Name: LSR ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonSessionParametersTLVLsrID"]),
        )

    @property
    def CommonSessionParametersTLVLabelSpace(self):
        """
        Display Name: Label space
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonSessionParametersTLVLabelSpace"]
            ),
        )

    @property
    def AtmSessionParametersTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmSessionParametersTLVUBit"])
        )

    @property
    def AtmSessionParametersTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmSessionParametersTLVFBit"])
        )

    @property
    def AtmSessionParametersTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0501
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmSessionParametersTLVType"])
        )

    @property
    def AtmSessionParametersTLVLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmSessionParametersTLVLength"]),
        )

    @property
    def AtmSessionParametersTLVAtmMergeCapabilities(self):
        """
        Display Name: ATM merge capabilities
        Default Value: 0
        Value Format: decimal
        Available enum values: Merge not supported, 0, VP merge supported, 1, VC merge supported, 2, VP and VC merge supported, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AtmSessionParametersTLVAtmMergeCapabilities"]
            ),
        )

    @property
    def AtmSessionParametersTLVNumberOfLabelRangeComponents(self):
        """
        Display Name: Number of label range components
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AtmSessionParametersTLVNumberOfLabelRangeComponents"]
            ),
        )

    @property
    def AtmSessionParametersTLVDBit(self):
        """
        Display Name: D bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bidirectional VC capability, 0, Unidirectional VC capability, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmSessionParametersTLVDBit"])
        )

    @property
    def AtmSessionParametersTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmSessionParametersTLVReserved"]),
        )

    @property
    def AtmLabelRangeComponentReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmLabelRangeComponentReserved"]),
        )

    @property
    def AtmLabelRangeComponentMinimumVPI(self):
        """
        Display Name: Minimum VPI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmLabelRangeComponentMinimumVPI"]),
        )

    @property
    def AtmLabelRangeComponentMinimumVCI(self):
        """
        Display Name: Minimum VCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmLabelRangeComponentMinimumVCI"]),
        )

    @property
    def AtmsessionparameterstlvAtmLabelRangeComponentReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "AtmsessionparameterstlvAtmLabelRangeComponentReserved"
                ]
            ),
        )

    @property
    def AtmLabelRangeComponentMaximumVPI(self):
        """
        Display Name: Maximum VPI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmLabelRangeComponentMaximumVPI"]),
        )

    @property
    def AtmLabelRangeComponentMaximumVCI(self):
        """
        Display Name: Maximum VCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AtmLabelRangeComponentMaximumVCI"]),
        )

    @property
    def FrameRelaySessionParametersTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelaySessionParametersTLVUBit"]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVFBit(self):
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
                self._SDM_ATT_MAP["FrameRelaySessionParametersTLVFBit"]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0502
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelaySessionParametersTLVType"]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelaySessionParametersTLVLength"]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVFrameRelayMergeCapabilities(self):
        """
        Display Name: Frame Relay merge capabilities
        Default Value: 0
        Value Format: decimal
        Available enum values: Merge not supported, 0, Merge supported, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FrameRelaySessionParametersTLVFrameRelayMergeCapabilities"
                ]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVNumberOfLabelRangeComponents(self):
        """
        Display Name: Number of label range components
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FrameRelaySessionParametersTLVNumberOfLabelRangeComponents"
                ]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVDBit(self):
        """
        Display Name: D bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bidirectional VC capability, 0, Unidirectional VC capability, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelaySessionParametersTLVDBit"]
            ),
        )

    @property
    def FrameRelaySessionParametersTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelaySessionParametersTLVReserved"]
            ),
        )

    @property
    def FrameRelayLabelRangeComponentReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelayLabelRangeComponentReserved"]
            ),
        )

    @property
    def FrameRelayLabelRangeComponentDlciLength(self):
        """
        Display Name: DLCI length
        Default Value: 0
        Value Format: decimal
        Available enum values: 10 bits, 0, 23 bits, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelayLabelRangeComponentDlciLength"]
            ),
        )

    @property
    def FrameRelayLabelRangeComponentMinimumDLCI(self):
        """
        Display Name: Minimum DLCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelayLabelRangeComponentMinimumDLCI"]
            ),
        )

    @property
    def FramerelaysessionparameterstlvFrameRelayLabelRangeComponentReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FramerelaysessionparameterstlvFrameRelayLabelRangeComponentReserved"
                ]
            ),
        )

    @property
    def FrameRelayLabelRangeComponentMaximumDLCI(self):
        """
        Display Name: Maximum DLCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FrameRelayLabelRangeComponentMaximumDLCI"]
            ),
        )

    @property
    def P2mpCapabilityParametersTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["P2mpCapabilityParametersTLVUBit"]),
        )

    @property
    def P2mpCapabilityParametersTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["P2mpCapabilityParametersTLVFBit"]),
        )

    @property
    def P2mpCapabilityParametersTLVTclP2mpCapabilityParameter(self):
        """
        Display Name: P2MP Capability Parameter
        Default Value: 0x0508
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpCapabilityParametersTLVTclP2mpCapabilityParameter"
                ]
            ),
        )

    @property
    def P2mpCapabilityParametersTLVTclP2mpCapabilityParameterLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpCapabilityParametersTLVTclP2mpCapabilityParameterLength"
                ]
            ),
        )

    @property
    def P2mpCapabilityParametersTLVSBit(self):
        """
        Display Name: S bit
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["P2mpCapabilityParametersTLVSBit"]),
        )

    @property
    def P2mpCapabilityParametersTLVTclP2mpCapabilityParameterReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpCapabilityParametersTLVTclP2mpCapabilityParameterReserved"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

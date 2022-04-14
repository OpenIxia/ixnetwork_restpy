from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MstpBPDU(Base):
    __slots__ = ()
    _SDM_NAME = "mstpBPDU"
    _SDM_ATT_MAP = {
        "HeaderProtocolIdentifier": "mstpBPDU.header.protocolIdentifier-1",
        "HeaderProtocolVersionIdentifier": "mstpBPDU.header.protocolVersionIdentifier-2",
        "HeaderBpduType": "mstpBPDU.header.bpduType-3",
        "CistFlagsTopologyChangeAcknowledgement": "mstpBPDU.header.cistFlags.topologyChangeAcknowledgement-4",
        "CistFlagsAgreement": "mstpBPDU.header.cistFlags.agreement-5",
        "CistFlagsForwarding": "mstpBPDU.header.cistFlags.forwarding-6",
        "CistFlagsLearning": "mstpBPDU.header.cistFlags.learning-7",
        "CistFlagsPortRole": "mstpBPDU.header.cistFlags.portRole-8",
        "CistFlagsProposal": "mstpBPDU.header.cistFlags.proposal-9",
        "CistFlagsTopologyChange": "mstpBPDU.header.cistFlags.topologyChange-10",
        "HeaderCistRootIdentifier": "mstpBPDU.header.cistRootIdentifier-11",
        "HeaderCistExternalPathCost": "mstpBPDU.header.cistExternalPathCost-12",
        "HeaderCistRegionalRootIdentifier": "mstpBPDU.header.cistRegionalRootIdentifier-13",
        "HeaderCistPortIdentifier": "mstpBPDU.header.cistPortIdentifier-14",
        "HeaderMessageAge": "mstpBPDU.header.messageAge-15",
        "HeaderMaxAgeinMsecs": "mstpBPDU.header.maxAgeinMsecs-16",
        "HeaderHelloTimeinMsecs": "mstpBPDU.header.helloTimeinMsecs-17",
        "HeaderForwardDelayinMsecs": "mstpBPDU.header.forwardDelayinMsecs-18",
        "HeaderVersion1Length": "mstpBPDU.header.version1Length-19",
        "HeaderVersion3LengthinOctets": "mstpBPDU.header.version3LengthinOctets-20",
        "MstiConfigurationIdentifierConfigurationIDFormat": "mstpBPDU.header.mstiConfigurationIdentifier.configurationIDFormat-21",
        "MstiConfigurationIdentifierConfigurationName": "mstpBPDU.header.mstiConfigurationIdentifier.configurationName-22",
        "MstiConfigurationIdentifierRevisionLevel": "mstpBPDU.header.mstiConfigurationIdentifier.revisionLevel-23",
        "MstiConfigurationIdentifierConfigurationDigest": "mstpBPDU.header.mstiConfigurationIdentifier.configurationDigest-24",
        "HeaderCistInternalRootPathCost": "mstpBPDU.header.cistInternalRootPathCost-25",
        "HeaderCistBridgeIdentifier": "mstpBPDU.header.cistBridgeIdentifier-26",
        "HeaderCistRemainingHops": "mstpBPDU.header.cistRemainingHops-27",
        "FlagsMaster": "mstpBPDU.header.mstiConfigurationMessage.flags.master-28",
        "FlagsAgreement": "mstpBPDU.header.mstiConfigurationMessage.flags.agreement-29",
        "FlagsForwarding": "mstpBPDU.header.mstiConfigurationMessage.flags.forwarding-30",
        "FlagsLearning": "mstpBPDU.header.mstiConfigurationMessage.flags.learning-31",
        "FlagsPortRole": "mstpBPDU.header.mstiConfigurationMessage.flags.portRole-32",
        "FlagsProposal": "mstpBPDU.header.mstiConfigurationMessage.flags.proposal-33",
        "FlagsTopologyChange": "mstpBPDU.header.mstiConfigurationMessage.flags.topologyChange-34",
        "MstiConfigurationMessageRegionalRootIdentifier": "mstpBPDU.header.mstiConfigurationMessage.regionalRootIdentifier-35",
        "MstiConfigurationMessageInternalRootPathCost": "mstpBPDU.header.mstiConfigurationMessage.internalRootPathCost-36",
        "MstiConfigurationMessageBridgePriority": "mstpBPDU.header.mstiConfigurationMessage.bridgePriority-37",
        "MstiConfigurationMessagePortPriority": "mstpBPDU.header.mstiConfigurationMessage.portPriority-38",
        "MstiConfigurationMessageRemainingHops": "mstpBPDU.header.mstiConfigurationMessage.remainingHops-39",
    }

    def __init__(self, parent, list_op=False):
        super(MstpBPDU, self).__init__(parent, list_op)

    @property
    def HeaderProtocolIdentifier(self):
        """
        Display Name: Protocol identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolIdentifier"])
        )

    @property
    def HeaderProtocolVersionIdentifier(self):
        """
        Display Name: Protocol version identifier
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolVersionIdentifier"]),
        )

    @property
    def HeaderBpduType(self):
        """
        Display Name: BPDU type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBpduType"])
        )

    @property
    def CistFlagsTopologyChangeAcknowledgement(self):
        """
        Display Name: Topology change acknowledgement
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CistFlagsTopologyChangeAcknowledgement"]
            ),
        )

    @property
    def CistFlagsAgreement(self):
        """
        Display Name: Agreement
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CistFlagsAgreement"])
        )

    @property
    def CistFlagsForwarding(self):
        """
        Display Name: Forwarding
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CistFlagsForwarding"])
        )

    @property
    def CistFlagsLearning(self):
        """
        Display Name: Learning
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CistFlagsLearning"])
        )

    @property
    def CistFlagsPortRole(self):
        """
        Display Name: Port role
        Default Value: 3
        Value Format: decimal
        Available enum values: Master port, 0, Alternate/Backup, 1, Root, 2, Designated, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CistFlagsPortRole"])
        )

    @property
    def CistFlagsProposal(self):
        """
        Display Name: Proposal
        Default Value: 1
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CistFlagsProposal"])
        )

    @property
    def CistFlagsTopologyChange(self):
        """
        Display Name: Topology change
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CistFlagsTopologyChange"])
        )

    @property
    def HeaderCistRootIdentifier(self):
        """
        Display Name: CIST root identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCistRootIdentifier"])
        )

    @property
    def HeaderCistExternalPathCost(self):
        """
        Display Name: CIST external path cost
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCistExternalPathCost"])
        )

    @property
    def HeaderCistRegionalRootIdentifier(self):
        """
        Display Name: CIST regional root identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderCistRegionalRootIdentifier"]),
        )

    @property
    def HeaderCistPortIdentifier(self):
        """
        Display Name: CIST port identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCistPortIdentifier"])
        )

    @property
    def HeaderMessageAge(self):
        """
        Display Name: Message age
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageAge"])
        )

    @property
    def HeaderMaxAgeinMsecs(self):
        """
        Display Name: Max age(in msecs)
        Default Value: 5120
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMaxAgeinMsecs"])
        )

    @property
    def HeaderHelloTimeinMsecs(self):
        """
        Display Name: Hello time(in msecs)
        Default Value: 512
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHelloTimeinMsecs"])
        )

    @property
    def HeaderForwardDelayinMsecs(self):
        """
        Display Name: Forward delay(in msecs)
        Default Value: 3840
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderForwardDelayinMsecs"])
        )

    @property
    def HeaderVersion1Length(self):
        """
        Display Name: Version 1 Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion1Length"])
        )

    @property
    def HeaderVersion3LengthinOctets(self):
        """
        Display Name: Version 3 length(in octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion3LengthinOctets"])
        )

    @property
    def MstiConfigurationIdentifierConfigurationIDFormat(self):
        """
        Display Name: Configuration ID format
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationIdentifierConfigurationIDFormat"]
            ),
        )

    @property
    def MstiConfigurationIdentifierConfigurationName(self):
        """
        Display Name: Configuration name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationIdentifierConfigurationName"]
            ),
        )

    @property
    def MstiConfigurationIdentifierRevisionLevel(self):
        """
        Display Name: Revision level
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationIdentifierRevisionLevel"]
            ),
        )

    @property
    def MstiConfigurationIdentifierConfigurationDigest(self):
        """
        Display Name: Configuration digest
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationIdentifierConfigurationDigest"]
            ),
        )

    @property
    def HeaderCistInternalRootPathCost(self):
        """
        Display Name: CIST internal root path cost
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderCistInternalRootPathCost"]),
        )

    @property
    def HeaderCistBridgeIdentifier(self):
        """
        Display Name: CIST bridge identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCistBridgeIdentifier"])
        )

    @property
    def HeaderCistRemainingHops(self):
        """
        Display Name: CIST remaining hops
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCistRemainingHops"])
        )

    @property
    def FlagsMaster(self):
        """
        Display Name: Master
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsMaster"]))

    @property
    def FlagsAgreement(self):
        """
        Display Name: Agreement
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsAgreement"])
        )

    @property
    def FlagsForwarding(self):
        """
        Display Name: Forwarding
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsForwarding"])
        )

    @property
    def FlagsLearning(self):
        """
        Display Name: Learning
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsLearning"]))

    @property
    def FlagsPortRole(self):
        """
        Display Name: Port role
        Default Value: 3
        Value Format: decimal
        Available enum values: Master port, 0, Alternate/Backup, 1, Root, 2, Designated, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsPortRole"]))

    @property
    def FlagsProposal(self):
        """
        Display Name: Proposal
        Default Value: 1
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsProposal"]))

    @property
    def FlagsTopologyChange(self):
        """
        Display Name: Topology change
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsTopologyChange"])
        )

    @property
    def MstiConfigurationMessageRegionalRootIdentifier(self):
        """
        Display Name: Regional root identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationMessageRegionalRootIdentifier"]
            ),
        )

    @property
    def MstiConfigurationMessageInternalRootPathCost(self):
        """
        Display Name: Internal root path cost
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationMessageInternalRootPathCost"]
            ),
        )

    @property
    def MstiConfigurationMessageBridgePriority(self):
        """
        Display Name: Bridge priority
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationMessageBridgePriority"]
            ),
        )

    @property
    def MstiConfigurationMessagePortPriority(self):
        """
        Display Name: Port priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationMessagePortPriority"]
            ),
        )

    @property
    def MstiConfigurationMessageRemainingHops(self):
        """
        Display Name: Remaining hops
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MstiConfigurationMessageRemainingHops"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

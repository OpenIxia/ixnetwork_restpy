from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RstpBPDU(Base):
    __slots__ = ()
    _SDM_NAME = "rstpBPDU"
    _SDM_ATT_MAP = {
        "HeaderProtocolIdentifier": "rstpBPDU.header.protocolIdentifier-1",
        "HeaderProtocolVersionIdentifier": "rstpBPDU.header.protocolVersionIdentifier-2",
        "HeaderBpduType": "rstpBPDU.header.bpduType-3",
        "FlagsTopologyChangeAcknowledgement": "rstpBPDU.header.flags.topologyChangeAcknowledgement-4",
        "FlagsAgreement": "rstpBPDU.header.flags.agreement-5",
        "FlagsForwarding": "rstpBPDU.header.flags.forwarding-6",
        "FlagsLearning": "rstpBPDU.header.flags.learning-7",
        "FlagsPortRole": "rstpBPDU.header.flags.portRole-8",
        "FlagsProposal": "rstpBPDU.header.flags.proposal-9",
        "FlagsTopologyChange": "rstpBPDU.header.flags.topologyChange-10",
        "HeaderRootIdentifier": "rstpBPDU.header.rootIdentifier-11",
        "HeaderExternalRootPathCost": "rstpBPDU.header.externalRootPathCost-12",
        "HeaderRegionalRootIdentifier": "rstpBPDU.header.regionalRootIdentifier-13",
        "HeaderPortIdentifier": "rstpBPDU.header.portIdentifier-14",
        "HeaderMessageAge": "rstpBPDU.header.messageAge-15",
        "HeaderMaxAge": "rstpBPDU.header.maxAge-16",
        "HeaderHelloTime": "rstpBPDU.header.helloTime-17",
        "HeaderForwardDelay": "rstpBPDU.header.forwardDelay-18",
        "HeaderVersion1Length": "rstpBPDU.header.version1Length-19",
    }

    def __init__(self, parent, list_op=False):
        super(RstpBPDU, self).__init__(parent, list_op)

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
        Default Value: 2
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
    def FlagsTopologyChangeAcknowledgement(self):
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
                self._SDM_ATT_MAP["FlagsTopologyChangeAcknowledgement"]
            ),
        )

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
    def HeaderRootIdentifier(self):
        """
        Display Name: Root identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRootIdentifier"])
        )

    @property
    def HeaderExternalRootPathCost(self):
        """
        Display Name: External root path cost
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderExternalRootPathCost"])
        )

    @property
    def HeaderRegionalRootIdentifier(self):
        """
        Display Name: Regional root identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRegionalRootIdentifier"])
        )

    @property
    def HeaderPortIdentifier(self):
        """
        Display Name: Port identifier
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPortIdentifier"])
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
    def HeaderMaxAge(self):
        """
        Display Name: Max age
        Default Value: 5120
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderMaxAge"]))

    @property
    def HeaderHelloTime(self):
        """
        Display Name: Hello time
        Default Value: 512
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHelloTime"])
        )

    @property
    def HeaderForwardDelay(self):
        """
        Display Name: Forward delay
        Default Value: 3840
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderForwardDelay"])
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

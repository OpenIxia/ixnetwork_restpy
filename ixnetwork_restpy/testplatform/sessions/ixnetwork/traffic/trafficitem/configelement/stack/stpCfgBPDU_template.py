from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class StpCfgBPDU(Base):
    __slots__ = ()
    _SDM_NAME = "stpCfgBPDU"
    _SDM_ATT_MAP = {
        "HeaderProtocolIdentifier": "stpCfgBPDU.header.protocolIdentifier-1",
        "HeaderProtocolVersionIdentifier": "stpCfgBPDU.header.protocolVersionIdentifier-2",
        "HeaderBpduType": "stpCfgBPDU.header.bpduType-3",
        "FlagsTopologyChangeAcknowledgement": "stpCfgBPDU.header.flags.topologyChangeAcknowledgement-4",
        "FlagsThBitnotUsed": "stpCfgBPDU.header.flags.thBitnotUsed-5",
        "FlagsThBitnotUsed": "stpCfgBPDU.header.flags.thBitnotUsed-6",
        "FlagsThBitnotUsed": "stpCfgBPDU.header.flags.thBitnotUsed-7",
        "FlagsThBitnotUsed": "stpCfgBPDU.header.flags.thBitnotUsed-8",
        "FlagsRdBitnotUsed": "stpCfgBPDU.header.flags.rdBitnotUsed-9",
        "FlagsNdBitnotUsed": "stpCfgBPDU.header.flags.ndBitnotUsed-10",
        "FlagsTopologyChange": "stpCfgBPDU.header.flags.topologyChange-11",
        "HeaderRootIdentifier": "stpCfgBPDU.header.rootIdentifier-12",
        "HeaderRootPathCost": "stpCfgBPDU.header.rootPathCost-13",
        "HeaderBridgeIdentifier": "stpCfgBPDU.header.bridgeIdentifier-14",
        "HeaderPortIdentifier": "stpCfgBPDU.header.portIdentifier-15",
        "HeaderMessageAge": "stpCfgBPDU.header.messageAge-16",
        "HeaderMaxAge": "stpCfgBPDU.header.maxAge-17",
        "HeaderHelloTime": "stpCfgBPDU.header.helloTime-18",
        "HeaderForwardDelay": "stpCfgBPDU.header.forwardDelay-19",
    }

    def __init__(self, parent, list_op=False):
        super(StpCfgBPDU, self).__init__(parent, list_op)

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
        Default Value: 0
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
        Default Value: 0x00
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
    def FlagsThBitnotUsed(self):
        """
        Display Name: 7th bit(not used)
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsThBitnotUsed"])
        )

    @property
    def FlagsThBitnotUsed(self):
        """
        Display Name: 6th bit(not used)
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsThBitnotUsed"])
        )

    @property
    def FlagsThBitnotUsed(self):
        """
        Display Name: 5th bit(not used)
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsThBitnotUsed"])
        )

    @property
    def FlagsThBitnotUsed(self):
        """
        Display Name: 4th bit(not used)
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsThBitnotUsed"])
        )

    @property
    def FlagsRdBitnotUsed(self):
        """
        Display Name: 3rd bit(not used)
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsRdBitnotUsed"])
        )

    @property
    def FlagsNdBitnotUsed(self):
        """
        Display Name: 2nd bit(not used)
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsNdBitnotUsed"])
        )

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
    def HeaderRootPathCost(self):
        """
        Display Name: Root path cost
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRootPathCost"])
        )

    @property
    def HeaderBridgeIdentifier(self):
        """
        Display Name: Bridge identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBridgeIdentifier"])
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Csig(Base):
    __slots__ = ()
    _SDM_NAME = "csig"
    _SDM_ATT_MAP = {
        "TypeAbwType": "csig.header.tag.compactCsigTag.signalType.typeAbw.type-1",
        "TypeAbwCType": "csig.header.tag.compactCsigTag.signalType.typeAbwC.type-2",
        "TypeDelayType": "csig.header.tag.compactCsigTag.signalType.typeDelay.type-3",
        "TypeNormalizedQDType": "csig.header.tag.compactCsigTag.signalType.typeNormalizedQD.type-4",
        "ExperimentalType": "csig.header.tag.compactCsigTag.signalType.experimental.type-5",
        "TypeCustomType": "csig.header.tag.compactCsigTag.signalType.typeCustom.type-6",
        "CompactCsigTagSignalType": "csig.header.tag.compactCsigTag.signalType-7",
        "CompactCsigTagSignalValue": "csig.header.tag.compactCsigTag.signalValue-8",
        "CompactCsigTagLocatorMetadata": "csig.header.tag.compactCsigTag.locatorMetadata-9",
        "CompactCsigTagDoNotModify": "csig.header.tag.compactCsigTag.doNotModify-10",
        "ExpandedCsigTagLocatorMetadata": "csig.header.tag.expandedCsigTag.locatorMetadata-11",
        "ExpandedCsigTagDoNotModify": "csig.header.tag.expandedCsigTag.doNotModify-12",
        "SignaltypeTypeAbwType": "csig.header.tag.expandedCsigTag.signalType.typeAbw.type-13",
        "SignaltypeTypeAbwCType": "csig.header.tag.expandedCsigTag.signalType.typeAbwC.type-14",
        "SignaltypeTypeDelayType": "csig.header.tag.expandedCsigTag.signalType.typeDelay.type-15",
        "SignaltypeTypeNormalizedQDType": "csig.header.tag.expandedCsigTag.signalType.typeNormalizedQD.type-16",
        "SignaltypeExperimentalType": "csig.header.tag.expandedCsigTag.signalType.experimental.type-17",
        "SignaltypeTypeCustomType": "csig.header.tag.expandedCsigTag.signalType.typeCustom.type-18",
        "ExpandedCsigTagSignalValue": "csig.header.tag.expandedCsigTag.signalValue-19",
        "ExpandedCsigTagSignalType": "csig.header.tag.expandedCsigTag.signalType-20",
        "ProtocolID": "csig.header.protocolID-21",
    }

    def __init__(self, parent, list_op=False):
        super(Csig, self).__init__(parent, list_op)

    @property
    def TypeAbwType(self):
        """
        Display Name: T (Type)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeAbwType"]))

    @property
    def TypeAbwCType(self):
        """
        Display Name: T (Type)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeAbwCType"]))

    @property
    def TypeDelayType(self):
        """
        Display Name: T (Type)
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeDelayType"]))

    @property
    def TypeNormalizedQDType(self):
        """
        Display Name: T (Type)
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeNormalizedQDType"])
        )

    @property
    def ExperimentalType(self):
        """
        Display Name: T (Type)
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExperimentalType"])
        )

    @property
    def TypeCustomType(self):
        """
        Display Name: T (Type)
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeCustomType"])
        )

    @property
    def CompactCsigTagSignalType(self):
        """
        Display Name: R (Reserved)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompactCsigTagSignalType"])
        )

    @property
    def CompactCsigTagSignalValue(self):
        """
        Display Name: S (Signal Value)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompactCsigTagSignalValue"])
        )

    @property
    def CompactCsigTagLocatorMetadata(self):
        """
        Display Name: LM (Locator Metadata)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CompactCsigTagLocatorMetadata"]),
        )

    @property
    def CompactCsigTagDoNotModify(self):
        """
        Display Name: D (Do not modify)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompactCsigTagDoNotModify"])
        )

    @property
    def ExpandedCsigTagLocatorMetadata(self):
        """
        Display Name: LM (Locator Metadata)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ExpandedCsigTagLocatorMetadata"]),
        )

    @property
    def ExpandedCsigTagDoNotModify(self):
        """
        Display Name: D (Do not modify)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExpandedCsigTagDoNotModify"])
        )

    @property
    def SignaltypeTypeAbwType(self):
        """
        Display Name: T (Type)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SignaltypeTypeAbwType"])
        )

    @property
    def SignaltypeTypeAbwCType(self):
        """
        Display Name: T (Type)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SignaltypeTypeAbwCType"])
        )

    @property
    def SignaltypeTypeDelayType(self):
        """
        Display Name: T (Type)
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SignaltypeTypeDelayType"])
        )

    @property
    def SignaltypeTypeNormalizedQDType(self):
        """
        Display Name: T (Type)
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SignaltypeTypeNormalizedQDType"]),
        )

    @property
    def SignaltypeExperimentalType(self):
        """
        Display Name: T (Type)
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SignaltypeExperimentalType"])
        )

    @property
    def SignaltypeTypeCustomType(self):
        """
        Display Name: T (Type)
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SignaltypeTypeCustomType"])
        )

    @property
    def ExpandedCsigTagSignalValue(self):
        """
        Display Name: S (Signal Value)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExpandedCsigTagSignalValue"])
        )

    @property
    def ExpandedCsigTagSignalType(self):
        """
        Display Name: R (Reserved)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExpandedCsigTagSignalType"])
        )

    @property
    def ProtocolID(self):
        """
        Display Name: Protocol-ID
        Default Value: 0xffff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProtocolID"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

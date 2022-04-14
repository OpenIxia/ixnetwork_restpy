from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimHelloMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimHelloMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimHelloMessage.header.version-1",
        "HeaderType": "pimHelloMessage.header.type-2",
        "HeaderReserved": "pimHelloMessage.header.reserved-3",
        "HeaderHeaderChecksum": "pimHelloMessage.header.headerChecksum-4",
        "HoldtimeType": "pimHelloMessage.header.helloOptionsFields.options.holdtime.type-5",
        "HoldtimeLength": "pimHelloMessage.header.helloOptionsFields.options.holdtime.length-6",
        "HoldtimeHoldtimesec": "pimHelloMessage.header.helloOptionsFields.options.holdtime.holdtimesec-7",
        "LanPruneDelayType": "pimHelloMessage.header.helloOptionsFields.options.lanPruneDelay.type-8",
        "LanPruneDelayLength": "pimHelloMessage.header.helloOptionsFields.options.lanPruneDelay.length-9",
        "LanPruneDelayTBit": "pimHelloMessage.header.helloOptionsFields.options.lanPruneDelay.tBit-10",
        "LanPruneDelayLanDelay": "pimHelloMessage.header.helloOptionsFields.options.lanPruneDelay.lanDelay-11",
        "LanPruneDelayOverrideInterval": "pimHelloMessage.header.helloOptionsFields.options.lanPruneDelay.overrideInterval-12",
        "DrPriorityType": "pimHelloMessage.header.helloOptionsFields.options.drPriority.type-13",
        "DrPriorityLength": "pimHelloMessage.header.helloOptionsFields.options.drPriority.length-14",
        "DrPriorityDrPriority": "pimHelloMessage.header.helloOptionsFields.options.drPriority.drPriority-15",
        "GenerationIDType": "pimHelloMessage.header.helloOptionsFields.options.generationID.type-16",
        "GenerationIDLength": "pimHelloMessage.header.helloOptionsFields.options.generationID.length-17",
        "GenerationIDGenerationID": "pimHelloMessage.header.helloOptionsFields.options.generationID.generationID-18",
        "BidirCapableType": "pimHelloMessage.header.helloOptionsFields.options.bidirCapable.type-19",
        "BidirCapableLength": "pimHelloMessage.header.helloOptionsFields.options.bidirCapable.length-20",
        "PrivateUsageFieldType": "pimHelloMessage.header.helloOptionsFields.options.privateUsageField.type-21",
        "PrivateUsageFieldLength": "pimHelloMessage.header.helloOptionsFields.options.privateUsageField.length-22",
        "PrivateUsageFieldValue": "pimHelloMessage.header.helloOptionsFields.options.privateUsageField.value-23",
        "UserDefinedFieldType": "pimHelloMessage.header.helloOptionsFields.options.userDefinedField.type-24",
        "UserDefinedFieldLength": "pimHelloMessage.header.helloOptionsFields.options.userDefinedField.length-25",
        "UserDefinedFieldValue": "pimHelloMessage.header.helloOptionsFields.options.userDefinedField.value-26",
    }

    def __init__(self, parent, list_op=False):
        super(PimHelloMessage, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

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
    def HeaderHeaderChecksum(self):
        """
        Display Name: Header checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHeaderChecksum"])
        )

    @property
    def HoldtimeType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HoldtimeType"]))

    @property
    def HoldtimeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HoldtimeLength"])
        )

    @property
    def HoldtimeHoldtimesec(self):
        """
        Display Name: Holdtime (sec)
        Default Value: 0x69
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HoldtimeHoldtimesec"])
        )

    @property
    def LanPruneDelayType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LanPruneDelayType"])
        )

    @property
    def LanPruneDelayLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LanPruneDelayLength"])
        )

    @property
    def LanPruneDelayTBit(self):
        """
        Display Name: T bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LanPruneDelayTBit"])
        )

    @property
    def LanPruneDelayLanDelay(self):
        """
        Display Name: LAN delay
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LanPruneDelayLanDelay"])
        )

    @property
    def LanPruneDelayOverrideInterval(self):
        """
        Display Name: Override interval
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LanPruneDelayOverrideInterval"]),
        )

    @property
    def DrPriorityType(self):
        """
        Display Name: Type
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DrPriorityType"])
        )

    @property
    def DrPriorityLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DrPriorityLength"])
        )

    @property
    def DrPriorityDrPriority(self):
        """
        Display Name: DR priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DrPriorityDrPriority"])
        )

    @property
    def GenerationIDType(self):
        """
        Display Name: Type
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenerationIDType"])
        )

    @property
    def GenerationIDLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenerationIDLength"])
        )

    @property
    def GenerationIDGenerationID(self):
        """
        Display Name: Generation ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenerationIDGenerationID"])
        )

    @property
    def BidirCapableType(self):
        """
        Display Name: Type
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BidirCapableType"])
        )

    @property
    def BidirCapableLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BidirCapableLength"])
        )

    @property
    def PrivateUsageFieldType(self):
        """
        Display Name: Type
        Default Value: 65001
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrivateUsageFieldType"])
        )

    @property
    def PrivateUsageFieldLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrivateUsageFieldLength"])
        )

    @property
    def PrivateUsageFieldValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrivateUsageFieldValue"])
        )

    @property
    def UserDefinedFieldType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedFieldType"])
        )

    @property
    def UserDefinedFieldLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedFieldLength"])
        )

    @property
    def UserDefinedFieldValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedFieldValue"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

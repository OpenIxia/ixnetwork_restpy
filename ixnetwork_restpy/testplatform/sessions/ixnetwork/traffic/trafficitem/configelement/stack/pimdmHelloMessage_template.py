from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimdmHelloMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimdmHelloMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimdmHelloMessage.header.version-1",
        "HeaderType": "pimdmHelloMessage.header.type-2",
        "HeaderReserved": "pimdmHelloMessage.header.reserved-3",
        "HeaderHeaderChecksum": "pimdmHelloMessage.header.headerChecksum-4",
        "HoldtimeType": "pimdmHelloMessage.header.helloOptionsFields.options.holdtime.type-5",
        "HoldtimeLength": "pimdmHelloMessage.header.helloOptionsFields.options.holdtime.length-6",
        "HoldtimeHoldtimesec": "pimdmHelloMessage.header.helloOptionsFields.options.holdtime.holdtimesec-7",
        "LanPruneDelayType": "pimdmHelloMessage.header.helloOptionsFields.options.lanPruneDelay.type-8",
        "LanPruneDelayLength": "pimdmHelloMessage.header.helloOptionsFields.options.lanPruneDelay.length-9",
        "LanPruneDelayTBit": "pimdmHelloMessage.header.helloOptionsFields.options.lanPruneDelay.tBit-10",
        "LanPruneDelayLanDelay": "pimdmHelloMessage.header.helloOptionsFields.options.lanPruneDelay.lanDelay-11",
        "LanPruneDelayOverrideInterval": "pimdmHelloMessage.header.helloOptionsFields.options.lanPruneDelay.overrideInterval-12",
        "GenerationIDType": "pimdmHelloMessage.header.helloOptionsFields.options.generationID.type-13",
        "GenerationIDLength": "pimdmHelloMessage.header.helloOptionsFields.options.generationID.length-14",
        "GenerationIDGenerationID": "pimdmHelloMessage.header.helloOptionsFields.options.generationID.generationID-15",
        "StateRefreshCapableType": "pimdmHelloMessage.header.helloOptionsFields.options.stateRefreshCapable.type-16",
        "StateRefreshCapableLength": "pimdmHelloMessage.header.helloOptionsFields.options.stateRefreshCapable.length-17",
        "StateRefreshCapableVersion": "pimdmHelloMessage.header.helloOptionsFields.options.stateRefreshCapable.version-18",
        "StateRefreshCapableInterval": "pimdmHelloMessage.header.helloOptionsFields.options.stateRefreshCapable.interval-19",
        "StateRefreshCapableReserved": "pimdmHelloMessage.header.helloOptionsFields.options.stateRefreshCapable.reserved-20",
        "UserDefinedFieldType": "pimdmHelloMessage.header.helloOptionsFields.options.userDefinedField.type-21",
        "UserDefinedFieldLength": "pimdmHelloMessage.header.helloOptionsFields.options.userDefinedField.length-22",
        "UserDefinedFieldValue": "pimdmHelloMessage.header.helloOptionsFields.options.userDefinedField.value-23",
    }

    def __init__(self, parent, list_op=False):
        super(PimdmHelloMessage, self).__init__(parent, list_op)

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
        Available enum values: Hello, 0
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
    def StateRefreshCapableType(self):
        """
        Display Name: Type
        Default Value: 21
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StateRefreshCapableType"])
        )

    @property
    def StateRefreshCapableLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StateRefreshCapableLength"])
        )

    @property
    def StateRefreshCapableVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StateRefreshCapableVersion"])
        )

    @property
    def StateRefreshCapableInterval(self):
        """
        Display Name: Interval
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StateRefreshCapableInterval"])
        )

    @property
    def StateRefreshCapableReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StateRefreshCapableReserved"])
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

from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP(Base):
    __slots__ = ()
    _SDM_NAME = "lISP"
    _SDM_ATT_MAP = {
        "Nonce-present-bit": "lISP.header.nonce-present-bit-1",
        "Locator-status-bit": "lISP.header.locator-status-bit-2",
        "Echo-nonce-request-bit": "lISP.header.echo-nonce-request-bit-3",
        "Map-version-present-bit": "lISP.header.map-version-present-bit-4",
        "Instance-id-bit": "lISP.header.instance-id-bit-5",
        "FlagsReserved1": "lISP.header.flags.reserved1-6",
        "FlagsReserved2": "lISP.header.flags.reserved2-7",
        "FlagsReserved3": "lISP.header.flags.reserved3-8",
        "Nonce-map-versionNonce": "lISP.header.nonce-map-version.nonce-9",
        "Map-versionSource-map-version": "lISP.header.nonce-map-version.map-version.source-map-version-10",
        "Map-versionDest-map-version": "lISP.header.nonce-map-version.map-version.dest-map-version-11",
        "Instance-id-locator-sstatus-bitsLocator-status-bits": "lISP.header.instance-id-locator-sstatus-bits.locator-status-bits-12",
        "Instance-id-lsbsInstance-id": "lISP.header.instance-id-locator-sstatus-bits.instance-id-lsbs.instance-id-13",
        "Instance-id-lsbsLsbs": "lISP.header.instance-id-locator-sstatus-bits.instance-id-lsbs.lsbs-14",
    }

    def __init__(self, parent, list_op=False):
        super(LISP, self).__init__(parent, list_op)

    @property
    def Noncepresentbit(self):
        """
        Display Name: nonce-present-bit
        Default Value: 0
        Value Format: decimal
        Available enum values: N-bit-disabled, 0, N-bit-enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Nonce-present-bit"])
        )

    @property
    def Locatorstatusbit(self):
        """
        Display Name: locator-status-bit
        Default Value: 0
        Value Format: decimal
        Available enum values: L-bit-disabled, 0, L-bit-enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Locator-status-bit"])
        )

    @property
    def Echononcerequestbit(self):
        """
        Display Name: echo-nonce-request-bit
        Default Value: 0
        Value Format: decimal
        Available enum values: E-bit-disabled, 0, E-bit-enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Echo-nonce-request-bit"])
        )

    @property
    def Mapversionpresentbit(self):
        """
        Display Name: map-version-present-bit
        Default Value: 0
        Value Format: decimal
        Available enum values: V-bit-disabled, 0, V-bit-enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Map-version-present-bit"])
        )

    @property
    def Instanceidbit(self):
        """
        Display Name: instance-id-bit
        Default Value: 0
        Value Format: decimal
        Available enum values: I-bit-disabled, 0, I-bit-enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Instance-id-bit"])
        )

    @property
    def FlagsReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: decimal
        Available enum values: 0, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved1"])
        )

    @property
    def FlagsReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: decimal
        Available enum values: 0, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved2"])
        )

    @property
    def FlagsReserved3(self):
        """
        Display Name: Reserved3
        Default Value: 0
        Value Format: decimal
        Available enum values: 0, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved3"])
        )

    @property
    def NoncemapversionNonce(self):
        """
        Display Name: Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Nonce-map-versionNonce"])
        )

    @property
    def MapversionSourcemapversion(self):
        """
        Display Name: Source Map-Version
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Map-versionSource-map-version"]),
        )

    @property
    def MapversionDestmapversion(self):
        """
        Display Name: Dest Map-Version
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Map-versionDest-map-version"])
        )

    @property
    def InstanceidlocatorsstatusbitsLocatorstatusbits(self):
        """
        Display Name: Locator Status Bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Instance-id-locator-sstatus-bitsLocator-status-bits"]
            ),
        )

    @property
    def InstanceidlsbsInstanceid(self):
        """
        Display Name: Instance ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Instance-id-lsbsInstance-id"])
        )

    @property
    def InstanceidlsbsLsbs(self):
        """
        Display Name: LSBs
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Instance-id-lsbsLsbs"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

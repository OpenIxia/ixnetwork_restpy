from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipDiscoverySolicitationEnode(Base):
    __slots__ = ()
    _SDM_NAME = "fipDiscoverySolicitationEnode"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipDiscoverySolicitationEnode.header.fipVersion-1",
        "HeaderFipReserved": "fipDiscoverySolicitationEnode.header.fipReserved-2",
        "FipOperationCodeFipDiscovery": "fipDiscoverySolicitationEnode.header.fipOperation.fipOperationCode.fipDiscovery-3",
        "FipOperationFipOperationReserved1": "fipDiscoverySolicitationEnode.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode01h": "fipDiscoverySolicitationEnode.header.fipOperation.fipSubcode.fipSubcode01h-5",
        "FipOperationFipDescriptorListLength": "fipDiscoverySolicitationEnode.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipDiscoverySolicitationEnode.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipDiscoverySolicitationEnode.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipDiscoverySolicitationEnode.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipDiscoverySolicitationEnode.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipDiscoverySolicitationEnode.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipDiscoverySolicitationEnode.header.fipOperation.fipFBit-12",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-13",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-14",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-15",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorType": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorType-16",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorLength": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorLength-17",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorReserved": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorReserved-18",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorValue": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorValue-19",
        "FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorType": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipDescriptorMaxFcoeSize.fipMaxFcoeSizeDescriptorType-20",
        "FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorLength": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipDescriptorMaxFcoeSize.fipMaxFcoeSizeDescriptorLength-21",
        "FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorValue": "fipDiscoverySolicitationEnode.header.fipDescriptors.fipSelectFipDescriptor.fipDescriptorMaxFcoeSize.fipMaxFcoeSizeDescriptorValue-22",
    }

    def __init__(self, parent, list_op=False):
        super(FipDiscoverySolicitationEnode, self).__init__(parent, list_op)

    @property
    def HeaderFipVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipVersion"])
        )

    @property
    def HeaderFipReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipReserved"])
        )

    @property
    def FipOperationCodeFipDiscovery(self):
        """
        Display Name: Discovery
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationCodeFipDiscovery"])
        )

    @property
    def FipOperationFipOperationReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FipOperationFipOperationReserved1"]),
        )

    @property
    def FipSubcodeFipSubcode01h(self):
        """
        Display Name: Subcode 01h
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipSubcodeFipSubcode01h"])
        )

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationFipDescriptorListLength"]
            ),
        )

    @property
    def FipOperationFipFp(self):
        """
        Display Name: FP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFp"])
        )

    @property
    def FipOperationFipSp(self):
        """
        Display Name: SP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSp"])
        )

    @property
    def FipOperationFipReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipReserved2"])
        )

    @property
    def FipOperationFipABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipABit"])
        )

    @property
    def FipOperationFipSBit(self):
        """
        Display Name: S bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSBit"])
        )

    @property
    def FipOperationFipFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFBit"])
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorType(self):
        """
        Display Name: MAC Address Descriptor Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipMacAddressDescriptorFipMacAddressDescriptorType"]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorLength(self):
        """
        Display Name: MAC Address Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipMacAddressDescriptorFipMacAddressDescriptorLength"
                ]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorValue(self):
        """
        Display Name: MAC Address Descriptor Value
        Default Value: 00:EE:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipMacAddressDescriptorFipMacAddressDescriptorValue"]
            ),
        )

    @property
    def FipNameIdentifierDescriptorFipNameIdentifierDescriptorType(self):
        """
        Display Name: Name_Identifier Descriptor Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNameIdentifierDescriptorFipNameIdentifierDescriptorType"
                ]
            ),
        )

    @property
    def FipNameIdentifierDescriptorFipNameIdentifierDescriptorLength(self):
        """
        Display Name: Name_Identifier Descriptor Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNameIdentifierDescriptorFipNameIdentifierDescriptorLength"
                ]
            ),
        )

    @property
    def FipNameIdentifierDescriptorFipNameIdentifierDescriptorReserved(self):
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
                    "FipNameIdentifierDescriptorFipNameIdentifierDescriptorReserved"
                ]
            ),
        )

    @property
    def FipNameIdentifierDescriptorFipNameIdentifierDescriptorValue(self):
        """
        Display Name: Name_Identifier Descriptor Value
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNameIdentifierDescriptorFipNameIdentifierDescriptorValue"
                ]
            ),
        )

    @property
    def FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorType(self):
        """
        Display Name: Max FCoE Size Descriptor Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorType"
                ]
            ),
        )

    @property
    def FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorLength(self):
        """
        Display Name: Max FCoE Size Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorLength"
                ]
            ),
        )

    @property
    def FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorValue(self):
        """
        Display Name: Max FCoE Size Descriptor Value
        Default Value: 2158
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipDescriptorMaxFcoeSizeFipMaxFcoeSizeDescriptorValue"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

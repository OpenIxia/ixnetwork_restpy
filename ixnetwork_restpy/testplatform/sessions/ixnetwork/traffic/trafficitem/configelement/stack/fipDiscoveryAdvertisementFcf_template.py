from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipDiscoveryAdvertisementFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipDiscoveryAdvertisementFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipDiscoveryAdvertisementFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipDiscoveryAdvertisementFcf.header.fipReserved-2",
        "FipOperationCodeFipDiscovery": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipOperationCode.fipDiscovery-3",
        "FipOperationFipOperationReserved1": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipDiscoveryAdvertisementFcf.header.fipOperation.fipFBit-12",
        "FipPriorityDescriptorFipPriorityDescriptorType": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipPriorityDescriptor.fipPriorityDescriptorType-13",
        "FipPriorityDescriptorFipPriorityDescriptorLength": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipPriorityDescriptor.fipPriorityDescriptorLength-14",
        "FipPriorityDescriptorFipPriorityDescriptorReserved": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipPriorityDescriptor.fipPriorityDescriptorReserved-15",
        "FipPriorityDescriptorFipPriorityDescriptorValue": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipPriorityDescriptor.fipPriorityDescriptorValue-16",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-17",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-18",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-19",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorType": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorType-20",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorLength": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorLength-21",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorReserved": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorReserved-22",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorValue": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorValue-23",
        "FipFabricDescriptorFipFabricDescriptorType": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFabricDescriptor.fipFabricDescriptorType-24",
        "FipFabricDescriptorFipFabricDescriptorLength": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFabricDescriptor.fipFabricDescriptorLength-25",
        "FipFabricDescriptorFipFabricDescriptorVfId": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFabricDescriptor.fipFabricDescriptorVfId-26",
        "FipFabricDescriptorFipFabricDescriptorReserved": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFabricDescriptor.fipFabricDescriptorReserved-27",
        "FipFabricDescriptorFipFabricDescriptorFc-map": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFabricDescriptor.fipFabricDescriptorFc-map-28",
        "FipFabricDescriptorFipFabricDescriptorValue": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFabricDescriptor.fipFabricDescriptorValue-29",
        "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorType": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFkaAdvPeriodDescriptor.fipFkaAdvPeriodDescriptorType-30",
        "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorLength": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFkaAdvPeriodDescriptor.fipFkaAdvPeriodDescriptorLength-31",
        "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorReserved": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFkaAdvPeriodDescriptor.fipFkaAdvPeriodDescriptorReserved-32",
        "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorDBit": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFkaAdvPeriodDescriptor.fipFkaAdvPeriodDescriptorDBit-33",
        "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorValue": "fipDiscoveryAdvertisementFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFkaAdvPeriodDescriptor.fipFkaAdvPeriodDescriptorValue-34",
    }

    def __init__(self, parent, list_op=False):
        super(FipDiscoveryAdvertisementFcf, self).__init__(parent, list_op)

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
    def FipSubcodeFipSubcode02h(self):
        """
        Display Name: Subcode 02h
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipSubcodeFipSubcode02h"])
        )

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 12
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
        Default Value: 1
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
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFBit"])
        )

    @property
    def FipPriorityDescriptorFipPriorityDescriptorType(self):
        """
        Display Name: Priority Descriptor Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipPriorityDescriptorFipPriorityDescriptorType"]
            ),
        )

    @property
    def FipPriorityDescriptorFipPriorityDescriptorLength(self):
        """
        Display Name: Priority Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipPriorityDescriptorFipPriorityDescriptorLength"]
            ),
        )

    @property
    def FipPriorityDescriptorFipPriorityDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipPriorityDescriptorFipPriorityDescriptorReserved"]
            ),
        )

    @property
    def FipPriorityDescriptorFipPriorityDescriptorValue(self):
        """
        Display Name: Priority Descriptor Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipPriorityDescriptorFipPriorityDescriptorValue"]
            ),
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
    def FipFabricDescriptorFipFabricDescriptorType(self):
        """
        Display Name: Fabric Descriptor Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFabricDescriptorFipFabricDescriptorType"]
            ),
        )

    @property
    def FipFabricDescriptorFipFabricDescriptorLength(self):
        """
        Display Name: Fabric Descriptor Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFabricDescriptorFipFabricDescriptorLength"]
            ),
        )

    @property
    def FipFabricDescriptorFipFabricDescriptorVfId(self):
        """
        Display Name: Fabric Descriptor VF_ID
        Default Value: 256
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFabricDescriptorFipFabricDescriptorVfId"]
            ),
        )

    @property
    def FipFabricDescriptorFipFabricDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFabricDescriptorFipFabricDescriptorReserved"]
            ),
        )

    @property
    def FipFabricDescriptorFipFabricDescriptorFcmap(self):
        """
        Display Name: Fabric Descriptor FC-MAP
        Default Value: 0x000EFC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFabricDescriptorFipFabricDescriptorFc-map"]
            ),
        )

    @property
    def FipFabricDescriptorFipFabricDescriptorValue(self):
        """
        Display Name: Fabric Descriptor Value
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFabricDescriptorFipFabricDescriptorValue"]
            ),
        )

    @property
    def FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorType(self):
        """
        Display Name: FKA_ADV_Period Descriptor Type
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorType"
                ]
            ),
        )

    @property
    def FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorLength(self):
        """
        Display Name: FKA_ADV_Period Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorLength"
                ]
            ),
        )

    @property
    def FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorReserved(self):
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
                    "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorReserved"
                ]
            ),
        )

    @property
    def FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorDBit(self):
        """
        Display Name: D bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorDBit"
                ]
            ),
        )

    @property
    def FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorValue(self):
        """
        Display Name: FKA_ADV_Period Descriptor Value
        Default Value: 8000
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipFkaAdvPeriodDescriptorFipFkaAdvPeriodDescriptorValue"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipVlanNotificationFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipVlanNotificationFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipVlanNotificationFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipVlanNotificationFcf.header.fipReserved-2",
        "FipOperationCodeFipVlanDiscovery": "fipVlanNotificationFcf.header.fipOperation.fipOperationCode.fipVlanDiscovery-3",
        "FipOperationFipOperationReserved1": "fipVlanNotificationFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipVlanNotificationFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipVlanNotificationFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipVlanNotificationFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipVlanNotificationFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipVlanNotificationFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipVlanNotificationFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipVlanNotificationFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipVlanNotificationFcf.header.fipOperation.fipFBit-12",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-13",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-14",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-15",
        "FipVlanDescriptorFipVlanDescriptorType": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVlanDescriptor.fipVlanDescriptorType-16",
        "FipVlanDescriptorFipVlanDescriptorLength": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVlanDescriptor.fipVlanDescriptorLength-17",
        "FipVlanDescriptorFipVlanDescriptorReserved": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVlanDescriptor.fipVlanDescriptorReserved-18",
        "FipVlanDescriptorFipVlanDescriptorValue": "fipVlanNotificationFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVlanDescriptor.fipVlanDescriptorValue-19",
    }

    def __init__(self, parent, list_op=False):
        super(FipVlanNotificationFcf, self).__init__(parent, list_op)

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
    def FipOperationCodeFipVlanDiscovery(self):
        """
        Display Name: FIP VLAN Discovery
        Default Value: 0x0004
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FipOperationCodeFipVlanDiscovery"]),
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
        Default Value: 3
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
    def FipVlanDescriptorFipVlanDescriptorType(self):
        """
        Display Name: VLAN Descriptor Type
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipVlanDescriptorFipVlanDescriptorType"]
            ),
        )

    @property
    def FipVlanDescriptorFipVlanDescriptorLength(self):
        """
        Display Name: VLAN Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipVlanDescriptorFipVlanDescriptorLength"]
            ),
        )

    @property
    def FipVlanDescriptorFipVlanDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipVlanDescriptorFipVlanDescriptorReserved"]
            ),
        )

    @property
    def FipVlanDescriptorFipVlanDescriptorValue(self):
        """
        Display Name: VLAN Descriptor Value
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipVlanDescriptorFipVlanDescriptorValue"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

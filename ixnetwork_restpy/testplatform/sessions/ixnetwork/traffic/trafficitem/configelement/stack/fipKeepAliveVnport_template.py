from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipKeepAliveVnport(Base):
    __slots__ = ()
    _SDM_NAME = "fipKeepAliveVnport"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipKeepAliveVnport.header.fipVersion-1",
        "HeaderFipReserved": "fipKeepAliveVnport.header.fipReserved-2",
        "FipOperationCodeFipKeepaliveVirtualLink": "fipKeepAliveVnport.header.fipOperation.fipOperationCode.fipKeepaliveVirtualLink-3",
        "FipOperationFipOperationReserved1": "fipKeepAliveVnport.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode01h": "fipKeepAliveVnport.header.fipOperation.fipSubcode.fipSubcode01h-5",
        "FipOperationFipDescriptorListLength": "fipKeepAliveVnport.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipKeepAliveVnport.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipKeepAliveVnport.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipKeepAliveVnport.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipKeepAliveVnport.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipKeepAliveVnport.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipKeepAliveVnport.header.fipOperation.fipFBit-12",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-13",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-14",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-15",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorType": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorType-16",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorLength": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorLength-17",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationMacDescriptorAddress": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationMacDescriptorAddress-18",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorReserved": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorReserved-19",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorAddressIdentifier": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorAddressIdentifier-20",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorValue": "fipKeepAliveVnport.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorValue-21",
    }

    def __init__(self, parent, list_op=False):
        super(FipKeepAliveVnport, self).__init__(parent, list_op)

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
    def FipOperationCodeFipKeepaliveVirtualLink(self):
        """
        Display Name: Keep Alive/Clear Virtual Links
        Default Value: 0x0003
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationCodeFipKeepaliveVirtualLink"]
            ),
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
        Default Value: 7
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
    def FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorType(self):
        """
        Display Name: Vx_Port Identification Descriptor Type
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorType"
                ]
            ),
        )

    @property
    def FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorLength(self):
        """
        Display Name: Vx_Port Identification Descriptor Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorLength"
                ]
            ),
        )

    @property
    def FipVxPortIdentificationDescriptorFipVxPortIdentificationMacDescriptorAddress(
        self,
    ):
        """
        Display Name: Vx_Port Identification Descriptor MAC Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVxPortIdentificationDescriptorFipVxPortIdentificationMacDescriptorAddress"
                ]
            ),
        )

    @property
    def FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorReserved(
        self,
    ):
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
                    "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorReserved"
                ]
            ),
        )

    @property
    def FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorAddressIdentifier(
        self,
    ):
        """
        Display Name: Vx_Port Identification Descriptor Address Identifier
        Default Value: 0x000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorAddressIdentifier"
                ]
            ),
        )

    @property
    def FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorValue(self):
        """
        Display Name: Vx_Port Identification Descriptor Value
        Default Value: 0x0000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorValue"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

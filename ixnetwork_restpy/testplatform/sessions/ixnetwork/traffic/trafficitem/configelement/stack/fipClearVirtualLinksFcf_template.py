from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipClearVirtualLinksFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipClearVirtualLinksFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipClearVirtualLinksFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipClearVirtualLinksFcf.header.fipReserved-2",
        "FipProtocolCodeFipKeepaliveVirtualLink": "fipClearVirtualLinksFcf.header.fipOperation.fipProtocolCode.fipKeepaliveVirtualLink-3",
        "FipOperationFipOperationReserved1": "fipClearVirtualLinksFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipClearVirtualLinksFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipClearVirtualLinksFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipClearVirtualLinksFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipClearVirtualLinksFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipClearVirtualLinksFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipClearVirtualLinksFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipClearVirtualLinksFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipClearVirtualLinksFcf.header.fipOperation.fipFBit-12",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-13",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-14",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-15",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorType": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorType-16",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorLength": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorLength-17",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorReserved": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorReserved-18",
        "FipNameIdentifierDescriptorFipNameIdentifierDescriptorValue": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNameIdentifierDescriptor.fipNameIdentifierDescriptorValue-19",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorType": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorType-20",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorLength": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorLength-21",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationMacDescriptorAddress": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationMacDescriptorAddress-22",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorReserved": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorReserved-23",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorAddressIdentifier": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorAddressIdentifier-24",
        "FipVxPortIdentificationDescriptorFipVxPortIdentificationDescriptorValue": "fipClearVirtualLinksFcf.header.fipDescriptors.fipSelectFipDescriptor.fipVxPortIdentificationDescriptor.fipVxPortIdentificationDescriptorValue-25",
    }

    def __init__(self, parent, list_op=False):
        super(FipClearVirtualLinksFcf, self).__init__(parent, list_op)

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
    def FipProtocolCodeFipKeepaliveVirtualLink(self):
        """
        Display Name: Keep Alive/Clear Virtual Links
        Default Value: 0x0003
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipProtocolCodeFipKeepaliveVirtualLink"]
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
        Default Value: 10
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

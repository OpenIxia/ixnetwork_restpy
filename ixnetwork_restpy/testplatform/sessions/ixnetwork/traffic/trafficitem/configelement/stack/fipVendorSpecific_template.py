from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipVendorSpecific(Base):
    __slots__ = ()
    _SDM_NAME = "fipVendorSpecific"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipVendorSpecific.header.fipVersion-1",
        "HeaderFipReserved": "fipVendorSpecific.header.fipReserved-2",
        "FipOperationCodeFipVendorSpecific": "fipVendorSpecific.header.fipOperation.fipOperationCode.fipVendorSpecific-3",
        "FipOperationFipOperationReserved1": "fipVendorSpecific.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipVendorSpecificSubcode": "fipVendorSpecific.header.fipOperation.fipSubcode.fipVendorSpecificSubcode-5",
        "FipOperationFipDescriptorListLength": "fipVendorSpecific.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipVendorSpecific.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipVendorSpecific.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipVendorSpecific.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipVendorSpecific.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipVendorSpecific.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipVendorSpecific.header.fipOperation.fipFBit-12",
        "FipVendorSpecificDescriptorFipVendorSpecificDescriptorType": "fipVendorSpecific.header.fipDescriptors.fipSelectFipDescriptor.fipVendorSpecificDescriptor.fipVendorSpecificDescriptorType-13",
        "FipVendorSpecificDescriptorFipVendorSpecificDescriptorLength": "fipVendorSpecific.header.fipDescriptors.fipSelectFipDescriptor.fipVendorSpecificDescriptor.fipVendorSpecificDescriptorLength-14",
        "FipVendorSpecificDescriptorFipVendorSpecificDescriptorReserved": "fipVendorSpecific.header.fipDescriptors.fipSelectFipDescriptor.fipVendorSpecificDescriptor.fipVendorSpecificDescriptorReserved-15",
        "FipVendorSpecificDescriptorFipVendorSpecificDescriptorVendorId": "fipVendorSpecific.header.fipDescriptors.fipSelectFipDescriptor.fipVendorSpecificDescriptor.fipVendorSpecificDescriptorVendorId-16",
        "FipVendorSpecificDescriptorFipVendorSpecificDescriptorValue": "fipVendorSpecific.header.fipDescriptors.fipSelectFipDescriptor.fipVendorSpecificDescriptor.fipVendorSpecificDescriptorValue-17",
    }

    def __init__(self, parent, list_op=False):
        super(FipVendorSpecific, self).__init__(parent, list_op)

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
    def FipOperationCodeFipVendorSpecific(self):
        """
        Display Name: Vendor Specific
        Default Value: 0xFFF8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FipOperationCodeFipVendorSpecific"]),
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
    def FipSubcodeFipVendorSpecificSubcode(self):
        """
        Display Name: Vendor Specific
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipSubcodeFipVendorSpecificSubcode"]
            ),
        )

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 5
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
    def FipVendorSpecificDescriptorFipVendorSpecificDescriptorType(self):
        """
        Display Name: Vendor Specific Descriptor Type
        Default Value: 241
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVendorSpecificDescriptorFipVendorSpecificDescriptorType"
                ]
            ),
        )

    @property
    def FipVendorSpecificDescriptorFipVendorSpecificDescriptorLength(self):
        """
        Display Name: Vendor Specific Descriptor Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVendorSpecificDescriptorFipVendorSpecificDescriptorLength"
                ]
            ),
        )

    @property
    def FipVendorSpecificDescriptorFipVendorSpecificDescriptorReserved(self):
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
                    "FipVendorSpecificDescriptorFipVendorSpecificDescriptorReserved"
                ]
            ),
        )

    @property
    def FipVendorSpecificDescriptorFipVendorSpecificDescriptorVendorId(self):
        """
        Display Name: Vendor Specific Descriptor Vendor_ID
        Default Value: 0x000000FFFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVendorSpecificDescriptorFipVendorSpecificDescriptorVendorId"
                ]
            ),
        )

    @property
    def FipVendorSpecificDescriptorFipVendorSpecificDescriptorValue(self):
        """
        Display Name: Vendor Specific Descriptor Value
        Default Value: 123456789
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipVendorSpecificDescriptorFipVendorSpecificDescriptorValue"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

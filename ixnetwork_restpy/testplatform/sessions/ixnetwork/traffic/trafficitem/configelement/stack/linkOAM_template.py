from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LinkOAM(Base):
    __slots__ = ()
    _SDM_NAME = "linkOAM"
    _SDM_ATT_MAP = {
        "PacketSubtype": "linkOAM.header.packet.subtype-1",
        "PacketFlags": "linkOAM.header.packet.flags-2",
        "InformationOAMPDUCode": "linkOAM.header.packet.pduType.informationOAMPDU.code-3",
        "LocalInfoTLVType": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.type-4",
        "LocalInfoTLVLength": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.length-5",
        "LocalInfoTLVVersion": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.version-6",
        "LocalInfoTLVRevision": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.revision-7",
        "LocalInfoTLVState": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.state-8",
        "LocalInfoTLVOamConfig": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.oamConfig-9",
        "LocalInfoTLVOamPDUConfig": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.oamPDUConfig-10",
        "LocalInfoTLVOui": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.oui-11",
        "LocalInfoTLVVendorInfo": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.localInfoTLV.vendorInfo-12",
        "RemoteInfoTLVType": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.type-13",
        "RemoteInfoTLVLength": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.length-14",
        "RemoteInfoTLVVersion": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.version-15",
        "RemoteInfoTLVRevision": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.revision-16",
        "RemoteInfoTLVState": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.state-17",
        "RemoteInfoTLVOamConfig": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.oamConfig-18",
        "RemoteInfoTLVOamPDUConfig": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.oamPDUConfig-19",
        "RemoteInfoTLVOui": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.oui-20",
        "RemoteInfoTLVVendorInfo": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.remoteInfoTLV.vendorInfo-21",
        "OrganizationSpecificInfoTLVType": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.organizationSpecificInfoTLV.type-22",
        "OrganizationSpecificInfoTLVLength": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.organizationSpecificInfoTLV.length-23",
        "OrganizationSpecificInfoTLVOui": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.organizationSpecificInfoTLV.oui-24",
        "OrganizationSpecificInfoTLVValueLength": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.organizationSpecificInfoTLV.valueLength-25",
        "OrganizationSpecificInfoTLVValue": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.organizationSpecificInfoTLV.value-26",
        "ReservedTLVType": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.reservedTLV.type-27",
        "ReservedTLVLength": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.reservedTLV.length-28",
        "ReservedTLVValueLength": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.reservedTLV.valueLength-29",
        "ReservedTLVValue": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.reservedTLV.value-30",
        "EndTLVType": "linkOAM.header.packet.pduType.informationOAMPDU.informationTLV.tlvType.endTLV.type-31",
        "LoopbackControlOAMPDUCode": "linkOAM.header.packet.pduType.loopbackControlOAMPDU.code-32",
        "LoopbackControlOAMPDULoopbackCommand": "linkOAM.header.packet.pduType.loopbackControlOAMPDU.loopbackCommand-33",
        "OrganizationSpecificOAMPDUCode": "linkOAM.header.packet.pduType.organizationSpecificOAMPDU.code-34",
        "OrganizationSpecificOAMPDUOui": "linkOAM.header.packet.pduType.organizationSpecificOAMPDU.oui-35",
        "OrganizationSpecificOAMPDUValueLength": "linkOAM.header.packet.pduType.organizationSpecificOAMPDU.valueLength-36",
        "OrganizationSpecificOAMPDUValue": "linkOAM.header.packet.pduType.organizationSpecificOAMPDU.value-37",
        "EventNotificationOAMPDUCode": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.code-38",
        "EventNotificationOAMPDUSequenceNumber": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.sequenceNumber-39",
        "TlvtypeEndTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.endTLV.type-40",
        "ErroredSymbolPeriodEventTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.type-41",
        "ErroredSymbolPeriodEventTLVLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.length-42",
        "ErroredSymbolPeriodEventTLVTimestamp": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.timestamp-43",
        "ErroredSymbolPeriodEventTLVSymbolWindow": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.symbolWindow-44",
        "ErroredSymbolPeriodEventTLVSymbolThreshold": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.symbolThreshold-45",
        "ErroredSymbolPeriodEventTLVSymbols": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.symbols-46",
        "ErroredSymbolPeriodEventTLVErrorRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.errorRunningTotal-47",
        "ErroredSymbolPeriodEventTLVEventRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredSymbolPeriodEventTLV.eventRunningTotal-48",
        "ErroredFrameEventTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.type-49",
        "ErroredFrameEventTLVLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.length-50",
        "ErroredFrameEventTLVTimestamp": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.timestamp-51",
        "ErroredFrameEventTLVFrameWindow": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.frameWindow-52",
        "ErroredFrameEventTLVFrameThreshold": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.frameThreshold-53",
        "ErroredFrameEventTLVFrames": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.frames-54",
        "ErroredFrameEventTLVErrorRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.errorRunningTotal-55",
        "ErroredFrameEventTLVEventRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFrameEventTLV.eventRunningTotal-56",
        "ErroredFramesPeriodEventTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.type-57",
        "ErroredFramesPeriodEventTLVLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.length-58",
        "ErroredFramesPeriodEventTLVTimestamp": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.timestamp-59",
        "ErroredFramesPeriodEventTLVFrameWindow": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.frameWindow-60",
        "ErroredFramesPeriodEventTLVFrameThreshold": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.frameThreshold-61",
        "ErroredFramesPeriodEventTLVFrames": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.frames-62",
        "ErroredFramesPeriodEventTLVErrorRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.errorRunningTotal-63",
        "ErroredFramesPeriodEventTLVEventRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesPeriodEventTLV.eventRunningTotal-64",
        "ErroredFramesSecondsSummaryEventTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.type-65",
        "ErroredFramesSecondsSummaryEventTLVLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.length-66",
        "ErroredFramesSecondsSummaryEventTLVTimestamp": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.timestamp-67",
        "ErroredFramesSecondsSummaryEventTLVFrameSecondsWindow": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.frameSecondsWindow-68",
        "ErroredFramesSecondsSummaryEventTLVFrameSecondsThreshold": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.frameSecondsThreshold-69",
        "ErroredFramesSecondsSummaryEventTLVFrameSeconds": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.frameSeconds-70",
        "ErroredFramesSecondsSummaryEventTLVErrorRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.errorRunningTotal-71",
        "ErroredFramesSecondsSummaryEventTLVEventRunningTotal": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.erroredFramesSecondsSummaryEventTLV.eventRunningTotal-72",
        "OrganizationSpecificEventTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.organizationSpecificEventTLV.type-73",
        "OrganizationSpecificEventTLVLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.organizationSpecificEventTLV.length-74",
        "OrganizationSpecificEventTLVOui": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.organizationSpecificEventTLV.oui-75",
        "OrganizationSpecificEventTLVValueLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.organizationSpecificEventTLV.valueLength-76",
        "OrganizationSpecificEventTLVValue": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.organizationSpecificEventTLV.value-77",
        "TlvtypeReservedTLVType": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.reservedTLV.type-78",
        "TlvtypeReservedTLVLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.reservedTLV.length-79",
        "TlvtypeReservedTLVValueLength": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.reservedTLV.valueLength-80",
        "TlvtypeReservedTLVValue": "linkOAM.header.packet.pduType.eventNotificationOAMPDU.eventTVL.tlvType.reservedTLV.value-81",
        "VariableRequestOAMPDUCode": "linkOAM.header.packet.pduType.variableRequestOAMPDU.code-82",
        "VariableDescriptorBranch": "linkOAM.header.packet.pduType.variableRequestOAMPDU.descriptors.tlvType.variableDescriptor.branch-83",
        "VariableDescriptorLeaf": "linkOAM.header.packet.pduType.variableRequestOAMPDU.descriptors.tlvType.variableDescriptor.leaf-84",
        "EndDescriptorEndOfDescriptor": "linkOAM.header.packet.pduType.variableRequestOAMPDU.descriptors.tlvType.endDescriptor.endOfDescriptor-85",
        "VariableResponseOAMPDUCode": "linkOAM.header.packet.pduType.variableResponseOAMPDU.code-86",
        "VariableContainerBranch": "linkOAM.header.packet.pduType.variableResponseOAMPDU.containers.tlvType.variableContainer.branch-87",
        "VariableContainerLeaf": "linkOAM.header.packet.pduType.variableResponseOAMPDU.containers.tlvType.variableContainer.leaf-88",
        "VariableContainerWidth": "linkOAM.header.packet.pduType.variableResponseOAMPDU.containers.tlvType.variableContainer.width-89",
        "VariableContainerValueLength": "linkOAM.header.packet.pduType.variableResponseOAMPDU.containers.tlvType.variableContainer.valueLength-90",
        "VariableContainerValue": "linkOAM.header.packet.pduType.variableResponseOAMPDU.containers.tlvType.variableContainer.value-91",
        "EndContainerEndOfContainer": "linkOAM.header.packet.pduType.variableResponseOAMPDU.containers.tlvType.endContainer.endOfContainer-92",
        "HeaderFcs": "linkOAM.header.fcs-93",
    }

    def __init__(self, parent, list_op=False):
        super(LinkOAM, self).__init__(parent, list_op)

    @property
    def PacketSubtype(self):
        """
        Display Name: Sub Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PacketSubtype"]))

    @property
    def PacketFlags(self):
        """
        Display Name: Flags
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PacketFlags"]))

    @property
    def InformationOAMPDUCode(self):
        """
        Display Name: Code
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InformationOAMPDUCode"])
        )

    @property
    def LocalInfoTLVType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVType"])
        )

    @property
    def LocalInfoTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x10
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVLength"])
        )

    @property
    def LocalInfoTLVVersion(self):
        """
        Display Name: OAM Version
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVVersion"])
        )

    @property
    def LocalInfoTLVRevision(self):
        """
        Display Name: Revision
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVRevision"])
        )

    @property
    def LocalInfoTLVState(self):
        """
        Display Name: State
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVState"])
        )

    @property
    def LocalInfoTLVOamConfig(self):
        """
        Display Name: OAM Configuration
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVOamConfig"])
        )

    @property
    def LocalInfoTLVOamPDUConfig(self):
        """
        Display Name: OAMPDU Configuration
        Default Value: 0x5DC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVOamPDUConfig"])
        )

    @property
    def LocalInfoTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0x000100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVOui"])
        )

    @property
    def LocalInfoTLVVendorInfo(self):
        """
        Display Name: Vendor Specific Information
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalInfoTLVVendorInfo"])
        )

    @property
    def RemoteInfoTLVType(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVType"])
        )

    @property
    def RemoteInfoTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x10
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVLength"])
        )

    @property
    def RemoteInfoTLVVersion(self):
        """
        Display Name: OAM Version
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVVersion"])
        )

    @property
    def RemoteInfoTLVRevision(self):
        """
        Display Name: Revision
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVRevision"])
        )

    @property
    def RemoteInfoTLVState(self):
        """
        Display Name: State
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVState"])
        )

    @property
    def RemoteInfoTLVOamConfig(self):
        """
        Display Name: OAM Configuration
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVOamConfig"])
        )

    @property
    def RemoteInfoTLVOamPDUConfig(self):
        """
        Display Name: OAMPDU Configuration
        Default Value: 0x5DC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVOamPDUConfig"])
        )

    @property
    def RemoteInfoTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0x000100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVOui"])
        )

    @property
    def RemoteInfoTLVVendorInfo(self):
        """
        Display Name: Vendor Specific Information
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInfoTLVVendorInfo"])
        )

    @property
    def OrganizationSpecificInfoTLVType(self):
        """
        Display Name: Type
        Default Value: 0xFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificInfoTLVType"]),
        )

    @property
    def OrganizationSpecificInfoTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificInfoTLVLength"]),
        )

    @property
    def OrganizationSpecificInfoTLVOui(self):
        """
        Display Name: Organizationally Unique Identifier
        Default Value: 0x000100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificInfoTLVOui"]),
        )

    @property
    def OrganizationSpecificInfoTLVValueLength(self):
        """
        Display Name: Organization Specific Value Len
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OrganizationSpecificInfoTLVValueLength"]
            ),
        )

    @property
    def OrganizationSpecificInfoTLVValue(self):
        """
        Display Name: Organization Specific Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificInfoTLVValue"]),
        )

    @property
    def ReservedTLVType(self):
        """
        Display Name: Type
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedTLVType"])
        )

    @property
    def ReservedTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedTLVLength"])
        )

    @property
    def ReservedTLVValueLength(self):
        """
        Display Name: Value Len
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedTLVValueLength"])
        )

    @property
    def ReservedTLVValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedTLVValue"])
        )

    @property
    def EndTLVType(self):
        """
        Display Name: end_of_tlv
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndTLVType"]))

    @property
    def LoopbackControlOAMPDUCode(self):
        """
        Display Name: Code
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LoopbackControlOAMPDUCode"])
        )

    @property
    def LoopbackControlOAMPDULoopbackCommand(self):
        """
        Display Name: Loopback Command
        Default Value: 1
        Value Format: decimal
        Available enum values: Enable OAM Remote Loopback, 1, Disable OAM Remote Loopback, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LoopbackControlOAMPDULoopbackCommand"]
            ),
        )

    @property
    def OrganizationSpecificOAMPDUCode(self):
        """
        Display Name: Code
        Default Value: 0xFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificOAMPDUCode"]),
        )

    @property
    def OrganizationSpecificOAMPDUOui(self):
        """
        Display Name: OUI
        Default Value: 0x000100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificOAMPDUOui"]),
        )

    @property
    def OrganizationSpecificOAMPDUValueLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OrganizationSpecificOAMPDUValueLength"]
            ),
        )

    @property
    def OrganizationSpecificOAMPDUValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificOAMPDUValue"]),
        )

    @property
    def EventNotificationOAMPDUCode(self):
        """
        Display Name: Code
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EventNotificationOAMPDUCode"])
        )

    @property
    def EventNotificationOAMPDUSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EventNotificationOAMPDUSequenceNumber"]
            ),
        )

    @property
    def TlvtypeEndTLVType(self):
        """
        Display Name: end_of_tlv
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvtypeEndTLVType"])
        )

    @property
    def ErroredSymbolPeriodEventTLVType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVType"]),
        )

    @property
    def ErroredSymbolPeriodEventTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x28
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVLength"]),
        )

    @property
    def ErroredSymbolPeriodEventTLVTimestamp(self):
        """
        Display Name: Time Stamp
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVTimestamp"]
            ),
        )

    @property
    def ErroredSymbolPeriodEventTLVSymbolWindow(self):
        """
        Display Name: Symbol Window
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVSymbolWindow"]
            ),
        )

    @property
    def ErroredSymbolPeriodEventTLVSymbolThreshold(self):
        """
        Display Name: Symbol Threshold
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVSymbolThreshold"]
            ),
        )

    @property
    def ErroredSymbolPeriodEventTLVSymbols(self):
        """
        Display Name: Symbols
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVSymbols"]
            ),
        )

    @property
    def ErroredSymbolPeriodEventTLVErrorRunningTotal(self):
        """
        Display Name: Error Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVErrorRunningTotal"]
            ),
        )

    @property
    def ErroredSymbolPeriodEventTLVEventRunningTotal(self):
        """
        Display Name: Event Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredSymbolPeriodEventTLVEventRunningTotal"]
            ),
        )

    @property
    def ErroredFrameEventTLVType(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventTLVType"])
        )

    @property
    def ErroredFrameEventTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x1A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventTLVLength"])
        )

    @property
    def ErroredFrameEventTLVTimestamp(self):
        """
        Display Name: Time Stamp
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventTLVTimestamp"]),
        )

    @property
    def ErroredFrameEventTLVFrameWindow(self):
        """
        Display Name: Frame Window
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventTLVFrameWindow"]),
        )

    @property
    def ErroredFrameEventTLVFrameThreshold(self):
        """
        Display Name: Frame Threshold
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFrameEventTLVFrameThreshold"]
            ),
        )

    @property
    def ErroredFrameEventTLVFrames(self):
        """
        Display Name: Frames
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ErroredFrameEventTLVFrames"])
        )

    @property
    def ErroredFrameEventTLVErrorRunningTotal(self):
        """
        Display Name: Error Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFrameEventTLVErrorRunningTotal"]
            ),
        )

    @property
    def ErroredFrameEventTLVEventRunningTotal(self):
        """
        Display Name: Event Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFrameEventTLVEventRunningTotal"]
            ),
        )

    @property
    def ErroredFramesPeriodEventTLVType(self):
        """
        Display Name: Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVType"]),
        )

    @property
    def ErroredFramesPeriodEventTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x1C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVLength"]),
        )

    @property
    def ErroredFramesPeriodEventTLVTimestamp(self):
        """
        Display Name: Time Stamp
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVTimestamp"]
            ),
        )

    @property
    def ErroredFramesPeriodEventTLVFrameWindow(self):
        """
        Display Name: Frame Window
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVFrameWindow"]
            ),
        )

    @property
    def ErroredFramesPeriodEventTLVFrameThreshold(self):
        """
        Display Name: Frame Threshold
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVFrameThreshold"]
            ),
        )

    @property
    def ErroredFramesPeriodEventTLVFrames(self):
        """
        Display Name: Frames
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVFrames"]),
        )

    @property
    def ErroredFramesPeriodEventTLVErrorRunningTotal(self):
        """
        Display Name: Error Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVErrorRunningTotal"]
            ),
        )

    @property
    def ErroredFramesPeriodEventTLVEventRunningTotal(self):
        """
        Display Name: Event Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesPeriodEventTLVEventRunningTotal"]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVType(self):
        """
        Display Name: Type
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesSecondsSummaryEventTLVType"]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x12
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesSecondsSummaryEventTLVLength"]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVTimestamp(self):
        """
        Display Name: Time Stamp
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesSecondsSummaryEventTLVTimestamp"]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVFrameSecondsWindow(self):
        """
        Display Name: Frame Seconds Summary Window
        Default Value: 60
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ErroredFramesSecondsSummaryEventTLVFrameSecondsWindow"
                ]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVFrameSecondsThreshold(self):
        """
        Display Name: Frame Seconds Summary Threshold
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ErroredFramesSecondsSummaryEventTLVFrameSecondsThreshold"
                ]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVFrameSeconds(self):
        """
        Display Name: Frame Seconds Summary
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ErroredFramesSecondsSummaryEventTLVFrameSeconds"]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVErrorRunningTotal(self):
        """
        Display Name: Error Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ErroredFramesSecondsSummaryEventTLVErrorRunningTotal"
                ]
            ),
        )

    @property
    def ErroredFramesSecondsSummaryEventTLVEventRunningTotal(self):
        """
        Display Name: Event Running Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ErroredFramesSecondsSummaryEventTLVEventRunningTotal"
                ]
            ),
        )

    @property
    def OrganizationSpecificEventTLVType(self):
        """
        Display Name: Type
        Default Value: 0xFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificEventTLVType"]),
        )

    @property
    def OrganizationSpecificEventTLVLength(self):
        """
        Display Name: Length
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OrganizationSpecificEventTLVLength"]
            ),
        )

    @property
    def OrganizationSpecificEventTLVOui(self):
        """
        Display Name: Organizationally Unique Identifier
        Default Value: 0x000100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificEventTLVOui"]),
        )

    @property
    def OrganizationSpecificEventTLVValueLength(self):
        """
        Display Name: Organization Specific Value Len
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OrganizationSpecificEventTLVValueLength"]
            ),
        )

    @property
    def OrganizationSpecificEventTLVValue(self):
        """
        Display Name: Organization Specific Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificEventTLVValue"]),
        )

    @property
    def TlvtypeReservedTLVType(self):
        """
        Display Name: Type
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvtypeReservedTLVType"])
        )

    @property
    def TlvtypeReservedTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvtypeReservedTLVLength"])
        )

    @property
    def TlvtypeReservedTLVValueLength(self):
        """
        Display Name: Value Len
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvtypeReservedTLVValueLength"]),
        )

    @property
    def TlvtypeReservedTLVValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvtypeReservedTLVValue"])
        )

    @property
    def VariableRequestOAMPDUCode(self):
        """
        Display Name: Code
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableRequestOAMPDUCode"])
        )

    @property
    def VariableDescriptorBranch(self):
        """
        Display Name: Variable Branch
        Default Value: 0x07
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableDescriptorBranch"])
        )

    @property
    def VariableDescriptorLeaf(self):
        """
        Display Name: Variable Leaf
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableDescriptorLeaf"])
        )

    @property
    def EndDescriptorEndOfDescriptor(self):
        """
        Display Name: end_of_descriptor
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndDescriptorEndOfDescriptor"])
        )

    @property
    def VariableResponseOAMPDUCode(self):
        """
        Display Name: Code
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableResponseOAMPDUCode"])
        )

    @property
    def VariableContainerBranch(self):
        """
        Display Name: Variable Branch
        Default Value: 0x07
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableContainerBranch"])
        )

    @property
    def VariableContainerLeaf(self):
        """
        Display Name: Variable Leaf
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableContainerLeaf"])
        )

    @property
    def VariableContainerWidth(self):
        """
        Display Name: Variable Width
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableContainerWidth"])
        )

    @property
    def VariableContainerValueLength(self):
        """
        Display Name: Variable Value Len
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableContainerValueLength"])
        )

    @property
    def VariableContainerValue(self):
        """
        Display Name: Variable Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableContainerValue"])
        )

    @property
    def EndContainerEndOfContainer(self):
        """
        Display Name: end_of_container
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndContainerEndOfContainer"])
        )

    @property
    def HeaderFcs(self):
        """
        Display Name: Frame Check Sequence CRC-32
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFcs"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

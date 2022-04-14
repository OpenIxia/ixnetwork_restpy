from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Cfm(Base):
    __slots__ = ()
    _SDM_NAME = "cfm"
    _SDM_ATT_MAP = {
        "CommonHeaderMdLevel": "cfm.cfmHeader.commonHeader.mdLevel-1",
        "CommonHeaderVersion": "cfm.cfmHeader.commonHeader.version-2",
        "CommonHeaderOpCode": "cfm.cfmHeader.commonHeader.opCode-3",
        "CommonHeaderFlags": "cfm.cfmHeader.commonHeader.flags-4",
        "CommonHeaderFirstTLVOffset": "cfm.cfmHeader.commonHeader.firstTLVOffset-5",
        "CcmSequenceNumber": "cfm.cfmHeader.selectPacketHeader.ccm.sequenceNumber-6",
        "CcmMaintenanceAssociationEndPointIdentifier": "cfm.cfmHeader.selectPacketHeader.ccm.maintenanceAssociationEndPointIdentifier-7",
        "MaintenanceDomainPresentMaintenanceDomainNameFormat": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.maintenanceDomainNameFormat-8",
        "MaintenanceDomainPresentMaintenanceDomainNameLength": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.maintenanceDomainNameLength-9",
        "MaintenanceDomainPresentMaintenanceDomainName": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.maintenanceDomainName-10",
        "MaintenanceDomainPresentShortMANameFormat": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.shortMANameFormat-11",
        "MaintenanceDomainPresentShortMANameLength": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.shortMANameLength-12",
        "MaintenanceDomainPresentShortMAName": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.shortMAName-13",
        "ZeroPaddingLength": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.zeroPadding.length-14",
        "ZeroPaddingValue": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainPresent.zeroPadding.value-15",
        "MaintenanceDomainNotPresentMaintenanceDomainNameFormat": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainNotPresent.maintenanceDomainNameFormat-16",
        "MaintenanceDomainNotPresentShortMANameFormat": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainNotPresent.shortMANameFormat-17",
        "MaintenanceDomainNotPresentShortMANameLength": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainNotPresent.shortMANameLength-18",
        "MaintenanceDomainNotPresentShortMAName": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainNotPresent.shortMAName-19",
        "MaintenancedomainnotpresentZeroPaddingLength": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainNotPresent.zeroPadding.length-20",
        "MaintenancedomainnotpresentZeroPaddingValue": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.maid.maintenanceDomainNotPresent.zeroPadding.value-21",
        "ItutY1731": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.cfm.itutY1731-22",
        "MegIDReserved": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.megID.reserved-23",
        "MegIDMegIDFormat": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.megID.megIDFormat-24",
        "MegIDMegIDLength": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.megID.megIDLength-25",
        "MegIDMegIDValue": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.megID.megIDValue-26",
        "Y1731TxFCf": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.txFCf-27",
        "Y1731RxFCb": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.rxFCb-28",
        "Y1731TxFCb": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.txFCb-29",
        "Y1731Resvd0": "cfm.cfmHeader.selectPacketHeader.ccm.cfmY1731Specific.y1731.resvd0-30",
        "DmmTxTimeStampf": "cfm.cfmHeader.selectPacketHeader.dmm.txTimeStampf-31",
        "DmmReservedForDMMReceivingEquipment": "cfm.cfmHeader.selectPacketHeader.dmm.reservedForDMMReceivingEquipment-32",
        "DmmReservedForDMR": "cfm.cfmHeader.selectPacketHeader.dmm.reservedForDMR-33",
        "DmmReservedForDMRReceivingEquipment": "cfm.cfmHeader.selectPacketHeader.dmm.reservedForDMRReceivingEquipment-34",
        "DmrTxTimeStampf": "cfm.cfmHeader.selectPacketHeader.dmr.txTimeStampf-35",
        "DmrRxTimeStampf": "cfm.cfmHeader.selectPacketHeader.dmr.rxTimeStampf-36",
        "DmrTxTimeStampb": "cfm.cfmHeader.selectPacketHeader.dmr.txTimeStampb-37",
        "DmrReservedForDMRReceivingEquipment": "cfm.cfmHeader.selectPacketHeader.dmr.reservedForDMRReceivingEquipment-38",
        "LtmTransactionId": "cfm.cfmHeader.selectPacketHeader.ltm.transactionId-39",
        "LtmTtl": "cfm.cfmHeader.selectPacketHeader.ltm.ttl-40",
        "LtmOriginalMACAddress": "cfm.cfmHeader.selectPacketHeader.ltm.originalMACAddress-41",
        "LtmTargetMACAddress": "cfm.cfmHeader.selectPacketHeader.ltm.targetMACAddress-42",
        "LtrTransactionID": "cfm.cfmHeader.selectPacketHeader.ltr.transactionID-43",
        "LtrReplyTTL": "cfm.cfmHeader.selectPacketHeader.ltr.replyTTL-44",
        "LtrRelayAction": "cfm.cfmHeader.selectPacketHeader.ltr.relayAction-45",
        "LbmTransactionIDSeqNumber": "cfm.cfmHeader.selectPacketHeader.lbm.transactionIDSeqNumber-46",
        "LbrTransactionIDSeqNumber": "cfm.cfmHeader.selectPacketHeader.lbr.transactionIDSeqNumber-47",
        "LmrTxFCf": "cfm.cfmHeader.selectPacketHeader.lmr.txFCf-48",
        "LmrRxFCf": "cfm.cfmHeader.selectPacketHeader.lmr.rxFCf-49",
        "LmrTxFCb": "cfm.cfmHeader.selectPacketHeader.lmr.txFCb-50",
        "LmmTxFCf": "cfm.cfmHeader.selectPacketHeader.lmm.txFCf-51",
        "LmmRes_rxFCf_lmr": "cfm.cfmHeader.selectPacketHeader.lmm.res_rxFCf_lmr-52",
        "LmmRes_txFCb_lmr": "cfm.cfmHeader.selectPacketHeader.lmm.res_txFCb_lmr-53",
        "TstSequenceNumber": "cfm.cfmHeader.selectPacketHeader.tst.SequenceNumber-54",
        "ApsRequest_state": "cfm.cfmHeader.selectPacketHeader.aps.request_state-55",
        "Prot_typeA_prot_type": "cfm.cfmHeader.selectPacketHeader.aps.prot_type.a_prot_type-56",
        "Prot_typeB_prot_type": "cfm.cfmHeader.selectPacketHeader.aps.prot_type.b_prot_type-57",
        "Prot_typeD_prot_type": "cfm.cfmHeader.selectPacketHeader.aps.prot_type.d_prot_type-58",
        "Prot_typeR_prot_type": "cfm.cfmHeader.selectPacketHeader.aps.prot_type.r_prot_type-59",
        "ApsReq_sign": "cfm.cfmHeader.selectPacketHeader.aps.req_sign-60",
        "ApsBri_sign": "cfm.cfmHeader.selectPacketHeader.aps.bri_sign-61",
        "ApsReserved": "cfm.cfmHeader.selectPacketHeader.aps.reserved-62",
        "GnmGnmSubOpCode": "cfm.cfmHeader.selectPacketHeader.gnm.gnmSubOpCode-63",
        "BnmNominalBandwidth": "cfm.cfmHeader.selectPacketHeader.gnm.selectGnmSubHeader.bnm.nominalBandwidth-64",
        "BnmCurrentBandwidth": "cfm.cfmHeader.selectPacketHeader.gnm.selectGnmSubHeader.bnm.currentBandwidth-65",
        "BnmPortId": "cfm.cfmHeader.selectPacketHeader.gnm.selectGnmSubHeader.bnm.portId-66",
        "EndTLVEndOfTlv": "cfm.cfmHeader.tlvs.selectTLVType.endTLV.endOfTlv-67",
        "SenderIDTLVType": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.type-68",
        "SenderIDTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.length-69",
        "ChassisIDLengthnonzeroChassisIDLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.chassisIDLength-70",
        "ChassisIDLengthnonzeroChassisIDSubtype": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.chassisIDSubtype-71",
        "ChassisIDLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.chassisID.length-72",
        "ChassisIDValue": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.chassisID.value-73",
        "ManagementAddressDomainLengthnonzeroManagementAddressDomainLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.managementAddressDomainLength.managementAddressDomainLengthnonzero.managementAddressDomainLength-74",
        "ManagementAddressDomainLengthnonzeroManagementAddressDomain": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.managementAddressDomainLength.managementAddressDomainLengthnonzero.managementAddressDomain-75",
        "ManagementAddressLengthnonzeroManagementAddressLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.managementAddressDomainLength.managementAddressDomainLengthnonzero.managementAddressLength.managementAddressLengthnonzero.managementAddressLength-76",
        "ManagementAddressLengthnonzeroManagementAddress": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.managementAddressDomainLength.managementAddressDomainLengthnonzero.managementAddressLength.managementAddressLengthnonzero.managementAddress-77",
        "ManagementAddressLengthzeroManagementAddressLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.managementAddressDomainLength.managementAddressDomainLengthnonzero.managementAddressLength.managementAddressLengthzero.managementAddressLength-78",
        "ManagementAddressDomainLengthzeroManagementAddressDomainLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthnonzero.managementAddressDomainLength.managementAddressDomainLengthzero.managementAddressDomainLength-79",
        "ChassisIDLengthzeroChassisIDLength": "cfm.cfmHeader.tlvs.selectTLVType.senderIDTLV.chassisIDLength.chassisIDLengthzero.chassisIDLength-80",
        "PortStatusTLVType": "cfm.cfmHeader.tlvs.selectTLVType.portStatusTLV.type-81",
        "PortStatusTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.portStatusTLV.length-82",
        "PortStatusTLVStatus": "cfm.cfmHeader.tlvs.selectTLVType.portStatusTLV.status-83",
        "DataTLVType": "cfm.cfmHeader.tlvs.selectTLVType.dataTLV.type-84",
        "DataTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.dataTLV.length-85",
        "DataTLVData": "cfm.cfmHeader.tlvs.selectTLVType.dataTLV.data-86",
        "TesttlvType": "cfm.cfmHeader.tlvs.selectTLVType.testtlv.type-87",
        "TesttlvLength": "cfm.cfmHeader.tlvs.selectTLVType.testtlv.length-88",
        "TesttlvPatternType": "cfm.cfmHeader.tlvs.selectTLVType.testtlv.patternType-89",
        "TstPatternLength1": "cfm.cfmHeader.tlvs.selectTLVType.testtlv.tstPattern.length1-90",
        "TstPatternData": "cfm.cfmHeader.tlvs.selectTLVType.testtlv.tstPattern.data-91",
        "CrcCrc": "cfm.cfmHeader.tlvs.selectTLVType.testtlv.crc.crc-92",
        "InterfaceStatusTLVType": "cfm.cfmHeader.tlvs.selectTLVType.interfaceStatusTLV.type-93",
        "InterfaceStatusTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.interfaceStatusTLV.length-94",
        "InterfaceStatusTLVStatus": "cfm.cfmHeader.tlvs.selectTLVType.interfaceStatusTLV.status-95",
        "ReplyIngressTLVwithPortIdType": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.type-96",
        "ReplyIngressTLVwithPortIdLength": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.length-97",
        "ReplyIngressTLVwithPortIdIngressAction": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.ingressAction-98",
        "ReplyIngressTLVwithPortIdIngressMACAddress": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.ingressMACAddress-99",
        "ReplyIngressTLVwithPortIdIngressPortIDLength": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.ingressPortIDLength-100",
        "ReplyIngressTLVwithPortIdIngressPortIDSubtype": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.ingressPortIDSubtype-101",
        "IngressPortIDLength": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.ingressPortID.length-102",
        "IngressPortIDIngressPortID": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithPortId.ingressPortID.ingressPortID-103",
        "ReplyIngressTLVwithoutPortIdType": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithoutPortId.type-104",
        "ReplyIngressTLVwithoutPortIdLength": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithoutPortId.length-105",
        "ReplyIngressTLVwithoutPortIdIngressAction": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithoutPortId.ingressAction-106",
        "ReplyIngressTLVwithoutPortIdIngressMACAddress": "cfm.cfmHeader.tlvs.selectTLVType.replyIngressTLV.replyIngressTLVwithoutPortId.ingressMACAddress-107",
        "ReplyEgressTLVwithPortType": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.type-108",
        "ReplyEgressTLVwithPortLength": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.length-109",
        "ReplyEgressTLVwithPortEgressAction": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.egressAction-110",
        "ReplyEgressTLVwithPortEgressMACAddress": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.egressMACAddress-111",
        "ReplyEgressTLVwithPortEgressPortLength": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.egressPortLength-112",
        "ReplyEgressTLVwithPortEgressPortIdSubType": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.egressPortIdSubType-113",
        "EgressPortIDLength": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.egressPortID.length-114",
        "EgressPortIDEgressPortID": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithPort.egressPortID.egressPortID-115",
        "ReplyEgressTLVwithoutPortType": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithoutPort.type-116",
        "ReplyEgressTLVwithoutPortLength": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithoutPort.length-117",
        "ReplyEgressTLVwithoutPortEgressAction": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithoutPort.egressAction-118",
        "ReplyEgressTLVwithoutPortEgressMACAddress": "cfm.cfmHeader.tlvs.selectTLVType.replyEgressTLV.replyEgressTLVwithoutPort.egressMACAddress-119",
        "LtmEgressIdentifierTLVType": "cfm.cfmHeader.tlvs.selectTLVType.ltmEgressIdentifierTLV.type-120",
        "LtmEgressIdentifierTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.ltmEgressIdentifierTLV.length-121",
        "LtmEgressIdentifierTLVEgressIdentifier": "cfm.cfmHeader.tlvs.selectTLVType.ltmEgressIdentifierTLV.egressIdentifier-122",
        "LtrEgressIdentifierTLVType": "cfm.cfmHeader.tlvs.selectTLVType.ltrEgressIdentifierTLV.type-123",
        "LtrEgressIdentifierTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.ltrEgressIdentifierTLV.length-124",
        "LtrEgressIdentifierTLVLastEgressIdentifier": "cfm.cfmHeader.tlvs.selectTLVType.ltrEgressIdentifierTLV.lastEgressIdentifier-125",
        "LtrEgressIdentifierTLVNextEgressIdentifier": "cfm.cfmHeader.tlvs.selectTLVType.ltrEgressIdentifierTLV.nextEgressIdentifier-126",
        "ReservedForIEEE8021930Type": "cfm.cfmHeader.tlvs.selectTLVType.reservedForIEEE8021930.type-127",
        "ReservedForIEEE8021930Length": "cfm.cfmHeader.tlvs.selectTLVType.reservedForIEEE8021930.length-128",
        "ReservedForIEEE8021930Value": "cfm.cfmHeader.tlvs.selectTLVType.reservedForIEEE8021930.value-129",
        "OrganizationSpecificTLVType": "cfm.cfmHeader.tlvs.selectTLVType.organizationSpecificTLV.type-130",
        "OrganizationSpecificTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.organizationSpecificTLV.length-131",
        "OrganizationSpecificTLVOui": "cfm.cfmHeader.tlvs.selectTLVType.organizationSpecificTLV.oui-132",
        "OrganizationSpecificTLVSubtype": "cfm.cfmHeader.tlvs.selectTLVType.organizationSpecificTLV.subtype-133",
        "ValueOptionalLength": "cfm.cfmHeader.tlvs.selectTLVType.organizationSpecificTLV.valueOptional.length-134",
        "ValueOptionalValue": "cfm.cfmHeader.tlvs.selectTLVType.organizationSpecificTLV.valueOptional.value-135",
        "DefinedByITUTY1731Type": "cfm.cfmHeader.tlvs.selectTLVType.definedByITUTY1731.type-136",
        "DefinedByITUTY1731Length": "cfm.cfmHeader.tlvs.selectTLVType.definedByITUTY1731.length-137",
        "DefinedByITUTY1731Value": "cfm.cfmHeader.tlvs.selectTLVType.definedByITUTY1731.value-138",
        "ReservedForIEEE802164255Type": "cfm.cfmHeader.tlvs.selectTLVType.reservedForIEEE802164255.type-139",
        "ReservedForIEEE802164255Length": "cfm.cfmHeader.tlvs.selectTLVType.reservedForIEEE802164255.length-140",
        "ReservedForIEEE802164255Value": "cfm.cfmHeader.tlvs.selectTLVType.reservedForIEEE802164255.value-141",
        "UserDefinedTLVLength": "cfm.cfmHeader.tlvs.selectTLVType.userDefinedTLV.length-142",
        "UserDefinedTLVValue": "cfm.cfmHeader.tlvs.selectTLVType.userDefinedTLV.value-143",
    }

    def __init__(self, parent, list_op=False):
        super(Cfm, self).__init__(parent, list_op)

    @property
    def CommonHeaderMdLevel(self):
        """
        Display Name: MD Level
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderMdLevel"])
        )

    @property
    def CommonHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderVersion"])
        )

    @property
    def CommonHeaderOpCode(self):
        """
        Display Name: Op. Code
        Default Value: 1
        Value Format: decimal
        Available enum values: Continuity Check Message (CCM), 1, Loopback Reply (LBR), 2, Loopback Message (LBM), 3, Linktrace Reply (LTR), 4, Linktrace Message (LTM), 5, Generic Notification Message (GNM), 32, Alarm Indication Signal (AIS), 33, Locked Signal (LCK), 35, Test Signal (TST), 37, Automatic Protection Switching_Linear (APS), 39, Automatic Protection Switching_Ring (APS), 40, Loss Measurement Reply (LMR), 42, Loss Measurement Message (LMM), 43, Delay Measurement Reply (DMR), 46, Delay Measurement Message (DMM), 47
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderOpCode"])
        )

    @property
    def CommonHeaderFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderFlags"])
        )

    @property
    def CommonHeaderFirstTLVOffset(self):
        """
        Display Name: First TLV offset
        Default Value: 70
        Value Format: decimal
        Available enum values: CCM - 70, 70, LBM / LBR / APS / TST- 4, 4, LTR - 6, 6, LTM - 17, 17, AIS / LCK - 0, 0, LMM / LMR - 12, 12, DMM / DMR - 32, 32, GNM - 13, 13
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderFirstTLVOffset"])
        )

    @property
    def CcmSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CcmSequenceNumber"])
        )

    @property
    def CcmMaintenanceAssociationEndPointIdentifier(self):
        """
        Display Name: Maintenance Association EndPoint Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CcmMaintenanceAssociationEndPointIdentifier"]
            ),
        )

    @property
    def MaintenanceDomainPresentMaintenanceDomainNameFormat(self):
        """
        Display Name: Maintenance Domain Name Format
        Default Value: 4
        Value Format: decimal
        Available enum values: domain_name_based_str, 2, mac_addr_2_oct_int, 3, char_str, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainPresentMaintenanceDomainNameFormat"]
            ),
        )

    @property
    def MaintenanceDomainPresentMaintenanceDomainNameLength(self):
        """
        Display Name: Maintenance Domain Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainPresentMaintenanceDomainNameLength"]
            ),
        )

    @property
    def MaintenanceDomainPresentMaintenanceDomainName(self):
        """
        Display Name: Maintenance Domain Name
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainPresentMaintenanceDomainName"]
            ),
        )

    @property
    def MaintenanceDomainPresentShortMANameFormat(self):
        """
        Display Name: Short MA Name Format
        Default Value: 2
        Value Format: decimal
        Available enum values: primary_vid, 1, char_str, 2, 2-oct_int, 3, rfc_2685_vpn_id, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainPresentShortMANameFormat"]
            ),
        )

    @property
    def MaintenanceDomainPresentShortMANameLength(self):
        """
        Display Name: Short MA Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainPresentShortMANameLength"]
            ),
        )

    @property
    def MaintenanceDomainPresentShortMAName(self):
        """
        Display Name: Short MA Name
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainPresentShortMAName"]
            ),
        )

    @property
    def ZeroPaddingLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ZeroPaddingLength"])
        )

    @property
    def ZeroPaddingValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ZeroPaddingValue"])
        )

    @property
    def MaintenanceDomainNotPresentMaintenanceDomainNameFormat(self):
        """
        Display Name: Maintenance Domain Name Format
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MaintenanceDomainNotPresentMaintenanceDomainNameFormat"
                ]
            ),
        )

    @property
    def MaintenanceDomainNotPresentShortMANameFormat(self):
        """
        Display Name: Short MA Name Format
        Default Value: 2
        Value Format: decimal
        Available enum values: primary_vid, 1, char_str, 2, 2-oct_int, 3, rfc_2685_vpn_id, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainNotPresentShortMANameFormat"]
            ),
        )

    @property
    def MaintenanceDomainNotPresentShortMANameLength(self):
        """
        Display Name: Short MA Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainNotPresentShortMANameLength"]
            ),
        )

    @property
    def MaintenanceDomainNotPresentShortMAName(self):
        """
        Display Name: Short MA Name
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenanceDomainNotPresentShortMAName"]
            ),
        )

    @property
    def MaintenancedomainnotpresentZeroPaddingLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenancedomainnotpresentZeroPaddingLength"]
            ),
        )

    @property
    def MaintenancedomainnotpresentZeroPaddingValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaintenancedomainnotpresentZeroPaddingValue"]
            ),
        )

    @property
    def ItutY1731(self):
        """
        Display Name: ITU-T Y.1731
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ItutY1731"]))

    @property
    def MegIDReserved(self):
        """
        Display Name: Reserved
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MegIDReserved"]))

    @property
    def MegIDMegIDFormat(self):
        """
        Display Name: MEG ID Format
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MegIDMegIDFormat"])
        )

    @property
    def MegIDMegIDLength(self):
        """
        Display Name: MEG ID Length
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MegIDMegIDLength"])
        )

    @property
    def MegIDMegIDValue(self):
        """
        Display Name: MEG ID Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MegIDMegIDValue"])
        )

    @property
    def Y1731TxFCf(self):
        """
        Display Name: TxFCf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Y1731TxFCf"]))

    @property
    def Y1731RxFCb(self):
        """
        Display Name: RxFCb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Y1731RxFCb"]))

    @property
    def Y1731TxFCb(self):
        """
        Display Name: TxFCb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Y1731TxFCb"]))

    @property
    def Y1731Resvd0(self):
        """
        Display Name: Reserved_0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Y1731Resvd0"]))

    @property
    def DmmTxTimeStampf(self):
        """
        Display Name: TxTimeStampf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DmmTxTimeStampf"])
        )

    @property
    def DmmReservedForDMMReceivingEquipment(self):
        """
        Display Name: Reserved for DMM receiving equipment
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DmmReservedForDMMReceivingEquipment"]
            ),
        )

    @property
    def DmmReservedForDMR(self):
        """
        Display Name: Reserved for DMR
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DmmReservedForDMR"])
        )

    @property
    def DmmReservedForDMRReceivingEquipment(self):
        """
        Display Name: Reserved for DMR receiving equipment
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DmmReservedForDMRReceivingEquipment"]
            ),
        )

    @property
    def DmrTxTimeStampf(self):
        """
        Display Name: TxTimeStampf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DmrTxTimeStampf"])
        )

    @property
    def DmrRxTimeStampf(self):
        """
        Display Name: RxTimeStampf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DmrRxTimeStampf"])
        )

    @property
    def DmrTxTimeStampb(self):
        """
        Display Name: TxTimeStampb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DmrTxTimeStampb"])
        )

    @property
    def DmrReservedForDMRReceivingEquipment(self):
        """
        Display Name: Reserved for DMR receiving equipment
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DmrReservedForDMRReceivingEquipment"]
            ),
        )

    @property
    def LtmTransactionId(self):
        """
        Display Name: Transaction Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtmTransactionId"])
        )

    @property
    def LtmTtl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LtmTtl"]))

    @property
    def LtmOriginalMACAddress(self):
        """
        Display Name: Original MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtmOriginalMACAddress"])
        )

    @property
    def LtmTargetMACAddress(self):
        """
        Display Name: TargetMAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtmTargetMACAddress"])
        )

    @property
    def LtrTransactionID(self):
        """
        Display Name: Transaction ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtrTransactionID"])
        )

    @property
    def LtrReplyTTL(self):
        """
        Display Name: Reply TTL
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LtrReplyTTL"]))

    @property
    def LtrRelayAction(self):
        """
        Display Name: Relay Action
        Default Value: 2
        Value Format: decimal
        Available enum values: RlyHit, 1, RlyFDB, 2, RlyMPDB, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtrRelayAction"])
        )

    @property
    def LbmTransactionIDSeqNumber(self):
        """
        Display Name: Transaction ID/Seq. Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LbmTransactionIDSeqNumber"])
        )

    @property
    def LbrTransactionIDSeqNumber(self):
        """
        Display Name: Transaction ID/Seq. Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LbrTransactionIDSeqNumber"])
        )

    @property
    def LmrTxFCf(self):
        """
        Display Name: TxFCf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LmrTxFCf"]))

    @property
    def LmrRxFCf(self):
        """
        Display Name: RxFCf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LmrRxFCf"]))

    @property
    def LmrTxFCb(self):
        """
        Display Name: TxFCb
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LmrTxFCb"]))

    @property
    def LmmTxFCf(self):
        """
        Display Name: TxFCf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LmmTxFCf"]))

    @property
    def LmmRes_rxFCf_lmr(self):
        """
        Display Name: Reserved for RxFCf in LMR
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LmmRes_rxFCf_lmr"])
        )

    @property
    def LmmRes_txFCb_lmr(self):
        """
        Display Name: Reserved for TxFCb in LMR
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LmmRes_txFCb_lmr"])
        )

    @property
    def TstSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TstSequenceNumber"])
        )

    @property
    def ApsRequest_state(self):
        """
        Display Name: Request/State
        Default Value: 0000
        Value Format: decimal
        Available enum values: Lockout Protection(LO), 1111, Signal Fail Protection(SF-P), 1110, Forced Switch(FS), 1101, Signal Fail Working(SF), 1011, Signal Degrade(SD), 1001, Manual Switch(MS), 111, Wait To Restore(WTR), 101, Exercise(EXER), 100, Reverse Request(RR), 10, Do Not Revert(DNR), 1, No Request, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApsRequest_state"])
        )

    @property
    def Prot_typeA_prot_type(self):
        """
        Display Name: A
        Default Value: 0
        Value Format: decimal
        Available enum values: No APS Channel, 0, APS Channel, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Prot_typeA_prot_type"])
        )

    @property
    def Prot_typeB_prot_type(self):
        """
        Display Name: B
        Default Value: 0
        Value Format: decimal
        Available enum values: 1+1(Permanent Bridge), 0, 1:1 (No Permanent Bridge), 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Prot_typeB_prot_type"])
        )

    @property
    def Prot_typeD_prot_type(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: decimal
        Available enum values: Unidirectional Switch, 0, Bidirectional Switch, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Prot_typeD_prot_type"])
        )

    @property
    def Prot_typeR_prot_type(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        Available enum values: Non-revertive Operation, 0, Revertive operation, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Prot_typeR_prot_type"])
        )

    @property
    def ApsReq_sign(self):
        """
        Display Name: Requested Signal
        Default Value: 0
        Value Format: decimal
        Available enum values: Null Signal, 0, Normal Traffic Signal, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ApsReq_sign"]))

    @property
    def ApsBri_sign(self):
        """
        Display Name: Bridged Signal
        Default Value: 0
        Value Format: decimal
        Available enum values: Null Signal, 0, Normal Traffic Signal, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ApsBri_sign"]))

    @property
    def ApsReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ApsReserved"]))

    @property
    def GnmGnmSubOpCode(self):
        """
        Display Name: Sub-OpCode
        Default Value: 1
        Value Format: decimal
        Available enum values: Bandwidth Notification Message (BNM), 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GnmGnmSubOpCode"])
        )

    @property
    def BnmNominalBandwidth(self):
        """
        Display Name: Nominal Bandwidth
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BnmNominalBandwidth"])
        )

    @property
    def BnmCurrentBandwidth(self):
        """
        Display Name: Current Bandwidth
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BnmCurrentBandwidth"])
        )

    @property
    def BnmPortId(self):
        """
        Display Name: Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BnmPortId"]))

    @property
    def EndTLVEndOfTlv(self):
        """
        Display Name: end_of_tlv
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndTLVEndOfTlv"])
        )

    @property
    def SenderIDTLVType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SenderIDTLVType"])
        )

    @property
    def SenderIDTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SenderIDTLVLength"])
        )

    @property
    def ChassisIDLengthnonzeroChassisIDLength(self):
        """
        Display Name: Chassis ID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChassisIDLengthnonzeroChassisIDLength"]
            ),
        )

    @property
    def ChassisIDLengthnonzeroChassisIDSubtype(self):
        """
        Display Name: Chassis ID Subtype
        Default Value: 4
        Value Format: decimal
        Available enum values: Chassis component, 1, Interface alias, 2, Port component, 3, MAC address, 4, Network address, 5, Interface name, 6, Locally assigned, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChassisIDLengthnonzeroChassisIDSubtype"]
            ),
        )

    @property
    def ChassisIDLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisIDLength"])
        )

    @property
    def ChassisIDValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisIDValue"])
        )

    @property
    def ManagementAddressDomainLengthnonzeroManagementAddressDomainLength(self):
        """
        Display Name: Management Address Domain Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ManagementAddressDomainLengthnonzeroManagementAddressDomainLength"
                ]
            ),
        )

    @property
    def ManagementAddressDomainLengthnonzeroManagementAddressDomain(self):
        """
        Display Name: Management Address Domain
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ManagementAddressDomainLengthnonzeroManagementAddressDomain"
                ]
            ),
        )

    @property
    def ManagementAddressLengthnonzeroManagementAddressLength(self):
        """
        Display Name: Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ManagementAddressLengthnonzeroManagementAddressLength"
                ]
            ),
        )

    @property
    def ManagementAddressLengthnonzeroManagementAddress(self):
        """
        Display Name: Management Address
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ManagementAddressLengthnonzeroManagementAddress"]
            ),
        )

    @property
    def ManagementAddressLengthzeroManagementAddressLength(self):
        """
        Display Name: Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ManagementAddressLengthzeroManagementAddressLength"]
            ),
        )

    @property
    def ManagementAddressDomainLengthzeroManagementAddressDomainLength(self):
        """
        Display Name: Management Address Domain Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ManagementAddressDomainLengthzeroManagementAddressDomainLength"
                ]
            ),
        )

    @property
    def ChassisIDLengthzeroChassisIDLength(self):
        """
        Display Name: Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChassisIDLengthzeroChassisIDLength"]
            ),
        )

    @property
    def PortStatusTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortStatusTLVType"])
        )

    @property
    def PortStatusTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortStatusTLVLength"])
        )

    @property
    def PortStatusTLVStatus(self):
        """
        Display Name: Status
        Default Value: 2
        Value Format: decimal
        Available enum values: Port blocked (psBlocked), 1, Port up (psUp), 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortStatusTLVStatus"])
        )

    @property
    def DataTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataTLVType"]))

    @property
    def DataTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataTLVLength"]))

    @property
    def DataTLVData(self):
        """
        Display Name: Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataTLVData"]))

    @property
    def TesttlvType(self):
        """
        Display Name: Type
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TesttlvType"]))

    @property
    def TesttlvLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TesttlvLength"]))

    @property
    def TesttlvPatternType(self):
        """
        Display Name: Pattern type
        Default Value: 0
        Value Format: decimal
        Available enum values: Null Signal without CRC-32, 0, Null Signal with CRC-32, 1, PRBS without CRC-32, 2, PRBS with CRC-32, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TesttlvPatternType"])
        )

    @property
    def TstPatternLength1(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TstPatternLength1"])
        )

    @property
    def TstPatternData(self):
        """
        Display Name: Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TstPatternData"])
        )

    @property
    def CrcCrc(self):
        """
        Display Name: CRC-32
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CrcCrc"]))

    @property
    def InterfaceStatusTLVType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceStatusTLVType"])
        )

    @property
    def InterfaceStatusTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceStatusTLVLength"])
        )

    @property
    def InterfaceStatusTLVStatus(self):
        """
        Display Name: Status
        Default Value: 1
        Value Format: decimal
        Available enum values: isUp, 1, isDown, 2, isTesting, 3, isUnknown, 4, isDormant, 5, isNotPresent, 6, isLowerlayerdown, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceStatusTLVStatus"])
        )

    @property
    def ReplyIngressTLVwithPortIdType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVwithPortIdType"]),
        )

    @property
    def ReplyIngressTLVwithPortIdLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVwithPortIdLength"]),
        )

    @property
    def ReplyIngressTLVwithPortIdIngressAction(self):
        """
        Display Name: Ingress Action
        Default Value: 1
        Value Format: decimal
        Available enum values: IngOK, 1, IngDown, 2, IngBlocked, 3, IngVID, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithPortIdIngressAction"]
            ),
        )

    @property
    def ReplyIngressTLVwithPortIdIngressMACAddress(self):
        """
        Display Name: Ingress MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithPortIdIngressMACAddress"]
            ),
        )

    @property
    def ReplyIngressTLVwithPortIdIngressPortIDLength(self):
        """
        Display Name: Ingress Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithPortIdIngressPortIDLength"]
            ),
        )

    @property
    def ReplyIngressTLVwithPortIdIngressPortIDSubtype(self):
        """
        Display Name: Ingress Port ID Subtype
        Default Value: 3
        Value Format: decimal
        Available enum values: Interface alias, 1, Port component, 2, MAC address, 3, Network address, 4, Interface name, 5, Agent circuit ID, 6, Locally assigned, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithPortIdIngressPortIDSubtype"]
            ),
        )

    @property
    def IngressPortIDLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressPortIDLength"])
        )

    @property
    def IngressPortIDIngressPortID(self):
        """
        Display Name: Ingress Port ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressPortIDIngressPortID"])
        )

    @property
    def ReplyIngressTLVwithoutPortIdType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVwithoutPortIdType"]),
        )

    @property
    def ReplyIngressTLVwithoutPortIdLength(self):
        """
        Display Name: Length
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithoutPortIdLength"]
            ),
        )

    @property
    def ReplyIngressTLVwithoutPortIdIngressAction(self):
        """
        Display Name: Ingress Action
        Default Value: 1
        Value Format: decimal
        Available enum values: OK, 1, Down, 2, Blocked, 3, VID, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithoutPortIdIngressAction"]
            ),
        )

    @property
    def ReplyIngressTLVwithoutPortIdIngressMACAddress(self):
        """
        Display Name: Ingress MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyIngressTLVwithoutPortIdIngressMACAddress"]
            ),
        )

    @property
    def ReplyEgressTLVwithPortType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVwithPortType"])
        )

    @property
    def ReplyEgressTLVwithPortLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVwithPortLength"])
        )

    @property
    def ReplyEgressTLVwithPortEgressAction(self):
        """
        Display Name: Egress Action
        Default Value: 1
        Value Format: decimal
        Available enum values: EgrOK, 1, EgrDown, 2, EgrBlocked, 3, EgrVID, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyEgressTLVwithPortEgressAction"]
            ),
        )

    @property
    def ReplyEgressTLVwithPortEgressMACAddress(self):
        """
        Display Name: Egress MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyEgressTLVwithPortEgressMACAddress"]
            ),
        )

    @property
    def ReplyEgressTLVwithPortEgressPortLength(self):
        """
        Display Name: Egress Port Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyEgressTLVwithPortEgressPortLength"]
            ),
        )

    @property
    def ReplyEgressTLVwithPortEgressPortIdSubType(self):
        """
        Display Name: Egress Port Id SubType
        Default Value: 3
        Value Format: decimal
        Available enum values: Interface alias, 1, Port component, 2, MAC address, 3, Network address, 4, Interface name, 5, Agent circuit ID, 6, Locally assigned, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyEgressTLVwithPortEgressPortIdSubType"]
            ),
        )

    @property
    def EgressPortIDLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressPortIDLength"])
        )

    @property
    def EgressPortIDEgressPortID(self):
        """
        Display Name: Egress Port ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressPortIDEgressPortID"])
        )

    @property
    def ReplyEgressTLVwithoutPortType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVwithoutPortType"]),
        )

    @property
    def ReplyEgressTLVwithoutPortLength(self):
        """
        Display Name: Length
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVwithoutPortLength"]),
        )

    @property
    def ReplyEgressTLVwithoutPortEgressAction(self):
        """
        Display Name: Egress Action
        Default Value: 1
        Value Format: decimal
        Available enum values: OK, 1, Down, 2, Blocked, 3, VID, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyEgressTLVwithoutPortEgressAction"]
            ),
        )

    @property
    def ReplyEgressTLVwithoutPortEgressMACAddress(self):
        """
        Display Name: Egress MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyEgressTLVwithoutPortEgressMACAddress"]
            ),
        )

    @property
    def LtmEgressIdentifierTLVType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtmEgressIdentifierTLVType"])
        )

    @property
    def LtmEgressIdentifierTLVLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtmEgressIdentifierTLVLength"])
        )

    @property
    def LtmEgressIdentifierTLVEgressIdentifier(self):
        """
        Display Name: Egress Identifier
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LtmEgressIdentifierTLVEgressIdentifier"]
            ),
        )

    @property
    def LtrEgressIdentifierTLVType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtrEgressIdentifierTLVType"])
        )

    @property
    def LtrEgressIdentifierTLVLength(self):
        """
        Display Name: Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LtrEgressIdentifierTLVLength"])
        )

    @property
    def LtrEgressIdentifierTLVLastEgressIdentifier(self):
        """
        Display Name: Last Egress Identifier
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LtrEgressIdentifierTLVLastEgressIdentifier"]
            ),
        )

    @property
    def LtrEgressIdentifierTLVNextEgressIdentifier(self):
        """
        Display Name: Next Egress Identifier
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LtrEgressIdentifierTLVNextEgressIdentifier"]
            ),
        )

    @property
    def ReservedForIEEE8021930Type(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedForIEEE8021930Type"])
        )

    @property
    def ReservedForIEEE8021930Length(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedForIEEE8021930Length"])
        )

    @property
    def ReservedForIEEE8021930Value(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedForIEEE8021930Value"])
        )

    @property
    def OrganizationSpecificTLVType(self):
        """
        Display Name: Type
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificTLVType"])
        )

    @property
    def OrganizationSpecificTLVLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificTLVLength"]),
        )

    @property
    def OrganizationSpecificTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificTLVOui"])
        )

    @property
    def OrganizationSpecificTLVSubtype(self):
        """
        Display Name: Sub-type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganizationSpecificTLVSubtype"]),
        )

    @property
    def ValueOptionalLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueOptionalLength"])
        )

    @property
    def ValueOptionalValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueOptionalValue"])
        )

    @property
    def DefinedByITUTY1731Type(self):
        """
        Display Name: Type
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefinedByITUTY1731Type"])
        )

    @property
    def DefinedByITUTY1731Length(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefinedByITUTY1731Length"])
        )

    @property
    def DefinedByITUTY1731Value(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefinedByITUTY1731Value"])
        )

    @property
    def ReservedForIEEE802164255Type(self):
        """
        Display Name: Type
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedForIEEE802164255Type"])
        )

    @property
    def ReservedForIEEE802164255Length(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReservedForIEEE802164255Length"]),
        )

    @property
    def ReservedForIEEE802164255Value(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReservedForIEEE802164255Value"]),
        )

    @property
    def UserDefinedTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedTLVLength"])
        )

    @property
    def UserDefinedTLVValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedTLVValue"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

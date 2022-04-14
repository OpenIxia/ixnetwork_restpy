from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ecp(Base):
    __slots__ = ()
    _SDM_NAME = "ecp"
    _SDM_ATT_MAP = {
        "Ecp_packetEcpVersion": "ecp.ecp_packet.ecpVersion-1",
        "EcpReqEcpReqField": "ecp.ecp_packet.evbOperation.ecpReq.ecpReqField-2",
        "EcpAckEcpAckField": "ecp.ecp_packet.evbOperation.ecpAck.ecpAckField-3",
        "EcpVdpSubtypeEcpVdpSubtypeField": "ecp.ecp_packet.evbSubtype.ecpVdpSubtype.ecpVdpSubtypeField-4",
        "EcpCSPSubtypeEcpCSPSubtypeField": "ecp.ecp_packet.evbSubtype.ecpCSPSubtype.ecpCSPSubtypeField-5",
        "Ecp_packetEcpSequenceNo": "ecp.ecp_packet.ecpSequenceNo-6",
        "VsiMgrIDVsi_mgr_id_tlv_type": "ecp.ecp_packet.vdpEntries.vsiMgrID.vsi_mgr_id_tlv_type-7",
        "VsiMgrIDLength": "ecp.ecp_packet.vdpEntries.vsiMgrID.length-8",
        "VsiMgrIDVsi_mgr_id": "ecp.ecp_packet.vdpEntries.vsiMgrID.vsi_mgr_id-9",
        "VsiPreassocVsiPreassocField": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiAssocType.vsiPreassoc.vsiPreassocField-10",
        "VsiPreassocRRVsiPreassocRRField": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiAssocType.vsiPreassocRR.vsiPreassocRRField-11",
        "VsiAssocVsiAssocField": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiAssocType.vsiAssoc.vsiAssocField-12",
        "VsiDeassocVsiDeassocField": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiAssocType.vsiDeassoc.vsiDeassocField-13",
        "VdpEntryLength": "ecp.ecp_packet.vdpEntries.vdpEntry.length-14",
        "VsiErrorTypeVsiSuccess": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiErrorType.vsiSuccess-15",
        "VsiErrorTypeVsiInvalidFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiErrorType.vsiInvalidFormat-16",
        "VsiErrorTypeVsiInsuffRes": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiErrorType.vsiInsuffRes-17",
        "VsiErrorTypeVsiNoMgr": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiErrorType.vsiNoMgr-18",
        "VsiErrorTypeVsiFailure": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiErrorType.vsiFailure-19",
        "VsiErrorTypeVsiInvalid": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiErrorType.vsiInvalid-20",
        "VsiStatusFlagsVsiMBit": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiStatusFlags.vsiMBit-21",
        "VsiStatusFlagsVsiSBit": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiStatusFlags.vsiSBit-22",
        "VsiStatusFlagsVsiReqAck": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiStatusFlags.vsiReqAck-23",
        "VsiStatusFlagsVsiReservedBit": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiStatusField.vsiStatusFlags.vsiReservedBit-24",
        "VdpEntryVsiTypeID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiTypeID-25",
        "VdpEntryVsiTypeVersion": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiTypeVersion-26",
        "VsiIDFormatIPv4VsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv4.vsiIDFormat-27",
        "VsiIDFormatIPv4VsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv4.vsiID-28",
        "VsiidVsiIDFormatIPv4VsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv4.vsiIDFormat-29",
        "VsiidVsiIDFormatIPv4VsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv4.vsiID-30",
        "VsiIDFormatIPv6VsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv6.vsiIDFormat-31",
        "VsiIDFormatIPv6VsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv6.vsiID-32",
        "VsiidVsiIDFormatIPv6VsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv6.vsiIDFormat-33",
        "VsiidVsiIDFormatIPv6VsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatIPv6.vsiID-34",
        "VsiIDFormatMACVsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatMAC.vsiIDFormat-35",
        "VsiIDFormatMACVsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatMAC.vsiID-36",
        "VsiidVsiIDFormatMACVsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatMAC.vsiIDFormat-37",
        "VsiidVsiIDFormatMACVsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatMAC.vsiID-38",
        "VsiIDFormatLocalVsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatLocal.vsiIDFormat-39",
        "VsiIDFormatLocalVsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatLocal.vsiID-40",
        "VsiidVsiIDFormatLocalVsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatLocal.vsiIDFormat-41",
        "VsiidVsiIDFormatLocalVsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatLocal.vsiID-42",
        "VsiIDFormatUUIDVsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatUUID.vsiIDFormat-43",
        "VsiIDFormatUUIDVsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatUUID.vsiID-44",
        "VsiidVsiIDFormatUUIDVsiIDFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatUUID.vsiIDFormat-45",
        "VsiidVsiIDFormatUUIDVsiID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiID.vsiIDFormatUUID.vsiID-46",
        "VidFiltersVsiFilterFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.vidFilters.vsiFilterFormat-47",
        "VidFiltersFiltersNo": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.vidFilters.filtersNo-48",
        "EntriesPs": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.vidFilters.entries.ps-49",
        "EntriesPcp": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.vidFilters.entries.pcp-50",
        "EntriesVid": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.vidFilters.entries.vid-51",
        "MacvidFiltersVsiFilterFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.macvidFilters.vsiFilterFormat-52",
        "MacvidFiltersFiltersNo": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.macvidFilters.filtersNo-53",
        "EntriesMac": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.macvidFilters.entries.mac-54",
        "MacvidfiltersEntriesPs": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.macvidFilters.entries.ps-55",
        "MacvidfiltersEntriesPcp": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.macvidFilters.entries.pcp-56",
        "MacvidfiltersEntriesVid": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.macvidFilters.entries.vid-57",
        "GroupvidFiltersVsiFilterFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupvidFilters.vsiFilterFormat-58",
        "GroupvidFiltersFiltersNo": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupvidFilters.filtersNo-59",
        "EntriesGroupID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupvidFilters.entries.groupID-60",
        "GroupvidfiltersEntriesPs": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupvidFilters.entries.ps-61",
        "GroupvidfiltersEntriesPcp": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupvidFilters.entries.pcp-62",
        "GroupvidfiltersEntriesVid": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupvidFilters.entries.vid-63",
        "GroupmacvidFiltersVsiFilterFormat": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.vsiFilterFormat-64",
        "GroupmacvidFiltersFiltersNo": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.filtersNo-65",
        "GroupmacvidfiltersEntriesGroupID": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.entries.groupID-66",
        "GroupmacvidfiltersEntriesMac": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.entries.mac-67",
        "GroupmacvidfiltersEntriesPs": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.entries.ps-68",
        "GroupmacvidfiltersEntriesPcp": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.entries.pcp-69",
        "GroupmacvidfiltersEntriesVid": "ecp.ecp_packet.vdpEntries.vdpEntry.vsiFilters.groupmacvidFilters.entries.vid-70",
    }

    def __init__(self, parent, list_op=False):
        super(Ecp, self).__init__(parent, list_op)

    @property
    def Ecp_packetEcpVersion(self):
        """
        Display Name: Version
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ecp_packetEcpVersion"])
        )

    @property
    def EcpReqEcpReqField(self):
        """
        Display Name: Request Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EcpReqEcpReqField"])
        )

    @property
    def EcpAckEcpAckField(self):
        """
        Display Name: Acknowledgement Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EcpAckEcpAckField"])
        )

    @property
    def EcpVdpSubtypeEcpVdpSubtypeField(self):
        """
        Display Name: VDP Field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EcpVdpSubtypeEcpVdpSubtypeField"]),
        )

    @property
    def EcpCSPSubtypeEcpCSPSubtypeField(self):
        """
        Display Name: PE CSP Field
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EcpCSPSubtypeEcpCSPSubtypeField"]),
        )

    @property
    def Ecp_packetEcpSequenceNo(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ecp_packetEcpSequenceNo"])
        )

    @property
    def VsiMgrIDVsi_mgr_id_tlv_type(self):
        """
        Display Name: Type
        Default Value: 0x05
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiMgrIDVsi_mgr_id_tlv_type"])
        )

    @property
    def VsiMgrIDLength(self):
        """
        Display Name: Length
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiMgrIDLength"])
        )

    @property
    def VsiMgrIDVsi_mgr_id(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiMgrIDVsi_mgr_id"])
        )

    @property
    def VsiPreassocVsiPreassocField(self):
        """
        Display Name: Pre-associate Field
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiPreassocVsiPreassocField"])
        )

    @property
    def VsiPreassocRRVsiPreassocRRField(self):
        """
        Display Name: Pre-associate with Resource Reservation Field
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VsiPreassocRRVsiPreassocRRField"]),
        )

    @property
    def VsiAssocVsiAssocField(self):
        """
        Display Name: Associate Field
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiAssocVsiAssocField"])
        )

    @property
    def VsiDeassocVsiDeassocField(self):
        """
        Display Name: De-associate Field
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiDeassocVsiDeassocField"])
        )

    @property
    def VdpEntryLength(self):
        """
        Display Name: Length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VdpEntryLength"])
        )

    @property
    def VsiErrorTypeVsiSuccess(self):
        """
        Display Name: Success
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiErrorTypeVsiSuccess"])
        )

    @property
    def VsiErrorTypeVsiInvalidFormat(self):
        """
        Display Name: Invalid Format
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiErrorTypeVsiInvalidFormat"])
        )

    @property
    def VsiErrorTypeVsiInsuffRes(self):
        """
        Display Name: Insufficient Resources
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiErrorTypeVsiInsuffRes"])
        )

    @property
    def VsiErrorTypeVsiNoMgr(self):
        """
        Display Name: Unable to contact VSI manager
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiErrorTypeVsiNoMgr"])
        )

    @property
    def VsiErrorTypeVsiFailure(self):
        """
        Display Name: Other Failure
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiErrorTypeVsiFailure"])
        )

    @property
    def VsiErrorTypeVsiInvalid(self):
        """
        Display Name: Invalid VID, GroupID, or MAC address
        Default Value: 0x05
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiErrorTypeVsiInvalid"])
        )

    @property
    def VsiStatusFlagsVsiMBit(self):
        """
        Display Name: M-bit/Hard Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiStatusFlagsVsiMBit"])
        )

    @property
    def VsiStatusFlagsVsiSBit(self):
        """
        Display Name: S-bit/Keep
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiStatusFlagsVsiSBit"])
        )

    @property
    def VsiStatusFlagsVsiReqAck(self):
        """
        Display Name: Request/Ack
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiStatusFlagsVsiReqAck"])
        )

    @property
    def VsiStatusFlagsVsiReservedBit(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiStatusFlagsVsiReservedBit"])
        )

    @property
    def VdpEntryVsiTypeID(self):
        """
        Display Name: VSI Type ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VdpEntryVsiTypeID"])
        )

    @property
    def VdpEntryVsiTypeVersion(self):
        """
        Display Name: VSI Type Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VdpEntryVsiTypeVersion"])
        )

    @property
    def VsiIDFormatIPv4VsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatIPv4VsiIDFormat"])
        )

    @property
    def VsiIDFormatIPv4VsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatIPv4VsiID"])
        )

    @property
    def VsiidVsiIDFormatIPv4VsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatIPv4VsiIDFormat"]),
        )

    @property
    def VsiidVsiIDFormatIPv4VsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatIPv4VsiID"])
        )

    @property
    def VsiIDFormatIPv6VsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatIPv6VsiIDFormat"])
        )

    @property
    def VsiIDFormatIPv6VsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatIPv6VsiID"])
        )

    @property
    def VsiidVsiIDFormatIPv6VsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatIPv6VsiIDFormat"]),
        )

    @property
    def VsiidVsiIDFormatIPv6VsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatIPv6VsiID"])
        )

    @property
    def VsiIDFormatMACVsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatMACVsiIDFormat"])
        )

    @property
    def VsiIDFormatMACVsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatMACVsiID"])
        )

    @property
    def VsiidVsiIDFormatMACVsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatMACVsiIDFormat"]),
        )

    @property
    def VsiidVsiIDFormatMACVsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatMACVsiID"])
        )

    @property
    def VsiIDFormatLocalVsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatLocalVsiIDFormat"])
        )

    @property
    def VsiIDFormatLocalVsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatLocalVsiID"])
        )

    @property
    def VsiidVsiIDFormatLocalVsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatLocalVsiIDFormat"]),
        )

    @property
    def VsiidVsiIDFormatLocalVsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatLocalVsiID"])
        )

    @property
    def VsiIDFormatUUIDVsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x05
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatUUIDVsiIDFormat"])
        )

    @property
    def VsiIDFormatUUIDVsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiIDFormatUUIDVsiID"])
        )

    @property
    def VsiidVsiIDFormatUUIDVsiIDFormat(self):
        """
        Display Name: Format
        Default Value: 0x05
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatUUIDVsiIDFormat"]),
        )

    @property
    def VsiidVsiIDFormatUUIDVsiID(self):
        """
        Display Name: VSI ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VsiidVsiIDFormatUUIDVsiID"])
        )

    @property
    def VidFiltersVsiFilterFormat(self):
        """
        Display Name: Format
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VidFiltersVsiFilterFormat"])
        )

    @property
    def VidFiltersFiltersNo(self):
        """
        Display Name: Number of entries
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VidFiltersFiltersNo"])
        )

    @property
    def EntriesPs(self):
        """
        Display Name: PCP Significant
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EntriesPs"]))

    @property
    def EntriesPcp(self):
        """
        Display Name: Priority Code Point
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EntriesPcp"]))

    @property
    def EntriesVid(self):
        """
        Display Name: VID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EntriesVid"]))

    @property
    def MacvidFiltersVsiFilterFormat(self):
        """
        Display Name: Format
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacvidFiltersVsiFilterFormat"])
        )

    @property
    def MacvidFiltersFiltersNo(self):
        """
        Display Name: Number of entries
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacvidFiltersFiltersNo"])
        )

    @property
    def EntriesMac(self):
        """
        Display Name: MAC
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EntriesMac"]))

    @property
    def MacvidfiltersEntriesPs(self):
        """
        Display Name: PCP Significant
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacvidfiltersEntriesPs"])
        )

    @property
    def MacvidfiltersEntriesPcp(self):
        """
        Display Name: Priority Code Point
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacvidfiltersEntriesPcp"])
        )

    @property
    def MacvidfiltersEntriesVid(self):
        """
        Display Name: VID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacvidfiltersEntriesVid"])
        )

    @property
    def GroupvidFiltersVsiFilterFormat(self):
        """
        Display Name: Format
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupvidFiltersVsiFilterFormat"]),
        )

    @property
    def GroupvidFiltersFiltersNo(self):
        """
        Display Name: Number of entries
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupvidFiltersFiltersNo"])
        )

    @property
    def EntriesGroupID(self):
        """
        Display Name: Group ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EntriesGroupID"])
        )

    @property
    def GroupvidfiltersEntriesPs(self):
        """
        Display Name: PCP Significant
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupvidfiltersEntriesPs"])
        )

    @property
    def GroupvidfiltersEntriesPcp(self):
        """
        Display Name: Priority Code Point
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupvidfiltersEntriesPcp"])
        )

    @property
    def GroupvidfiltersEntriesVid(self):
        """
        Display Name: VID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupvidfiltersEntriesVid"])
        )

    @property
    def GroupmacvidFiltersVsiFilterFormat(self):
        """
        Display Name: Format
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupmacvidFiltersVsiFilterFormat"]),
        )

    @property
    def GroupmacvidFiltersFiltersNo(self):
        """
        Display Name: Number of entries
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupmacvidFiltersFiltersNo"])
        )

    @property
    def GroupmacvidfiltersEntriesGroupID(self):
        """
        Display Name: Group ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupmacvidfiltersEntriesGroupID"]),
        )

    @property
    def GroupmacvidfiltersEntriesMac(self):
        """
        Display Name: MAC
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupmacvidfiltersEntriesMac"])
        )

    @property
    def GroupmacvidfiltersEntriesPs(self):
        """
        Display Name: PCP Significant
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupmacvidfiltersEntriesPs"])
        )

    @property
    def GroupmacvidfiltersEntriesPcp(self):
        """
        Display Name: Priority Code Point
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupmacvidfiltersEntriesPcp"])
        )

    @property
    def GroupmacvidfiltersEntriesVid(self):
        """
        Display Name: VID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupmacvidfiltersEntriesVid"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

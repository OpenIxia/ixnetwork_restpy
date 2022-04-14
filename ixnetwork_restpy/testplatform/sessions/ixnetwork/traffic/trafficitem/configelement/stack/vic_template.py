from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Vic(Base):
    __slots__ = ()
    _SDM_NAME = "vic"
    _SDM_ATT_MAP = {
        "VicPduHeaderVicVersion": "vic.header.vicPduHeader.vicVersion-1",
        "VicPduHeaderVicPDULength": "vic.header.vicPduHeader.vicPDULength-2",
        "VicPduHeaderVicPeerMacAddress": "vic.header.vicPduHeader.vicPeerMacAddress-3",
        "VicPduHeaderVicReserved": "vic.header.vicPduHeader.vicReserved-4",
        "VicOpenRequestVicMessageType": "vic.header.messageTypes.vicOpenRequest.vicMessageType-5",
        "VicOpenRequestVicMessageVersion": "vic.header.messageTypes.vicOpenRequest.vicMessageVersion-6",
        "VicMessageFlagsVicZFlag": "vic.header.messageTypes.vicOpenRequest.vicMessageFlags.vicZFlag-7",
        "VicMessageFlagsVicPFlag": "vic.header.messageTypes.vicOpenRequest.vicMessageFlags.vicPFlag-8",
        "VicMessageFlagsVicMFlag": "vic.header.messageTypes.vicOpenRequest.vicMessageFlags.vicMFlag-9",
        "VicMessageFlagsVicRFlag": "vic.header.messageTypes.vicOpenRequest.vicMessageFlags.vicRFlag-10",
        "VicOpenRequestVicMessageLen": "vic.header.messageTypes.vicOpenRequest.vicMessageLen-11",
        "VicOpenRequestVicMessageId": "vic.header.messageTypes.vicOpenRequest.vicMessageId-12",
        "VicOpenRequestVicFragmentId": "vic.header.messageTypes.vicOpenRequest.vicFragmentId-13",
        "VicOpenRequestVicCompletionCode": "vic.header.messageTypes.vicOpenRequest.vicCompletionCode-14",
        "VicOpenRequestVicVifIndex": "vic.header.messageTypes.vicOpenRequest.vicVifIndex-15",
        "VicControlChannelCapabilityVicTLVType": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicTLVType-16",
        "VicControlChannelCapabilityVicTLVLength": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicTLVLength-17",
        "VicControlChannelCapabilityVicCccRsvd": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccRsvd-18",
        "VicCccCapabilityFlagsVicCccOFlag": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccOFlag-19",
        "VicCccCapabilityFlagsVicCccRsvdFlags": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccRsvdFlags-20",
        "VicCccCapabilityFlagsVicCccSFlag": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccSFlag-21",
        "VicCccCapabilityFlagsVicCccDFlag": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccDFlag-22",
        "VicCccCapabilityFlagsVicCccVFlag": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccVFlag-23",
        "VicCccCapabilityFlagsVicCccFFlag": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccFFlag-24",
        "VicCccCapabilityFlagsVicCccRFlag": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccCapabilityFlags.vicCccRFlag-25",
        "VicControlChannelCapabilityVicCccMaxCredit": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccMaxCredit-26",
        "VicControlChannelCapabilityVicCccMaxMessageSize": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicControlChannelCapability.vicCccMaxMessageSize-27",
        "VicMsgTypeArrayVicTLVType": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicMsgTypeArray.vicTLVType-28",
        "VicMsgTypeArrayVicTLVLength": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicMsgTypeArray.vicTLVLength-29",
        "VicMsgTypeEntryVicMsgType": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicMsgTypeArray.vicMsgTypes.vicMsgTypeEntry.vicMsgType-30",
        "VicMsgTypeEntryVicMsgVersions": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicMsgTypeArray.vicMsgTypes.vicMsgTypeEntry.vicMsgVersions-31",
        "VicResourceLimitCapabilityVicTLVType": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicResourceLimitCapability.vicTLVType-32",
        "VicResourceLimitCapabilityVicTLVLength": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicResourceLimitCapability.vicTLVLength-33",
        "VicResourceLimitCapabilityVicRlcTotalVifs": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicResourceLimitCapability.vicRlcTotalVifs-34",
        "VicResourceLimitCapabilityVicRlcTotalVifLists": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicResourceLimitCapability.vicRlcTotalVifLists-35",
        "VicResourceLimitCapabilityVicRlcTotalUifs": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicResourceLimitCapability.vicRlcTotalUifs-36",
        "VicEthernetCapabilityVicTLVType": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicEthernetCapability.vicTLVType-37",
        "VicEthernetCapabilityVicTLVLength": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicEthernetCapability.vicTLVLength-38",
        "VicEthernetCapabilityVicEcTotalVifs": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicEthernetCapability.vicEcTotalVifs-39",
        "VicFcoeCapabilityVicTLVType": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicFcoeCapability.vicTLVType-40",
        "VicFcoeCapabilityVicTLVLength": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicFcoeCapability.vicTLVLength-41",
        "VicFcoeCapabilityVicFcTotalVifs": "vic.header.messageTypes.vicOpenRequest.vicMandatoryTLVs.vicFcoeCapability.vicFcTotalVifs-42",
        "VicOpenResponseVicMessageType": "vic.header.messageTypes.vicOpenResponse.vicMessageType-43",
        "VicOpenResponseVicMessageVersion": "vic.header.messageTypes.vicOpenResponse.vicMessageVersion-44",
        "VicopenresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicOpenResponse.vicMessageFlags.vicZFlag-45",
        "VicopenresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicOpenResponse.vicMessageFlags.vicPFlag-46",
        "VicopenresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicOpenResponse.vicMessageFlags.vicMFlag-47",
        "VicopenresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicOpenResponse.vicMessageFlags.vicRFlag-48",
        "VicOpenResponseVicMessageLen": "vic.header.messageTypes.vicOpenResponse.vicMessageLen-49",
        "VicOpenResponseVicMessageId": "vic.header.messageTypes.vicOpenResponse.vicMessageId-50",
        "VicOpenResponseVicFragmentId": "vic.header.messageTypes.vicOpenResponse.vicFragmentId-51",
        "VicOpenResponseVicCompletionCode": "vic.header.messageTypes.vicOpenResponse.vicCompletionCode-52",
        "VicOpenResponseVicVifIndex": "vic.header.messageTypes.vicOpenResponse.vicVifIndex-53",
        "VicVifCreateRequestVicMessageType": "vic.header.messageTypes.vicVifCreateRequest.vicMessageType-54",
        "VicVifCreateRequestVicMessageVersion": "vic.header.messageTypes.vicVifCreateRequest.vicMessageVersion-55",
        "VicvifcreaterequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifCreateRequest.vicMessageFlags.vicZFlag-56",
        "VicvifcreaterequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifCreateRequest.vicMessageFlags.vicPFlag-57",
        "VicvifcreaterequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifCreateRequest.vicMessageFlags.vicMFlag-58",
        "VicvifcreaterequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifCreateRequest.vicMessageFlags.vicRFlag-59",
        "VicVifCreateRequestVicMessageLen": "vic.header.messageTypes.vicVifCreateRequest.vicMessageLen-60",
        "VicVifCreateRequestVicMessageId": "vic.header.messageTypes.vicVifCreateRequest.vicMessageId-61",
        "VicVifCreateRequestVicFragmentId": "vic.header.messageTypes.vicVifCreateRequest.vicFragmentId-62",
        "VicVifCreateRequestVicCompletionCode": "vic.header.messageTypes.vicVifCreateRequest.vicCompletionCode-63",
        "VicVifCreateRequestVicVifIndex": "vic.header.messageTypes.vicVifCreateRequest.vicVifIndex-64",
        "VicProvisioningInfoVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicTLVType-65",
        "VicProvisioningInfoVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicTLVLength-66",
        "VicPiCiscoTypeSpaceVicPiTypeSpace": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiTypeSpace-67",
        "VicPiVmwareVicPiType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiType-68",
        "VicPiVmwareVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicTLVLength-69",
        "VicPiVmwareVicPiVmwareNumberOfTlvs": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareNumberOfTlvs-70",
        "VicPiVmwareProfileNameTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareProfileNameTlv.vicTLVType-71",
        "VicPiVmwareProfileNameTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareProfileNameTlv.vicTLVLength-72",
        "VicPiVmwareProfileNameTlvVicVariableProfileNameLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareProfileNameTlv.vicVariableProfileNameLength-73",
        "VicPiVmwareProfileNameTlvVicProfileName": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareProfileNameTlv.vicProfileName-74",
        "VicPiVmwareClientMacAddrTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientMacAddrTlv.vicTLVType-75",
        "VicPiVmwareClientMacAddrTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientMacAddrTlv.vicTLVLength-76",
        "VicPiVmwareClientMacAddrTlvVicPiVmwareClientMacAddr": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientMacAddrTlv.vicPiVmwareClientMacAddr-77",
        "VicPiVmwareClientNameTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientNameTlv.vicTLVType-78",
        "VicPiVmwareClientNameTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientNameTlv.vicTLVLength-79",
        "VicPiVmwareClientNameTlvVicVariableClientNameLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientNameTlv.vicVariableClientNameLength-80",
        "VicPiVmwareClientNameTlvVicClientName": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientNameTlv.vicClientName-81",
        "VicPiVmwarePortIdTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwarePortIdTlv.vicTLVType-82",
        "VicPiVmwarePortIdTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwarePortIdTlv.vicTLVLength-83",
        "VicPiVmwarePortIdTlvVicPiVmwarePortIndex": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwarePortIdTlv.vicPiVmwarePortIndex-84",
        "VicPiVmwareClusterPortUuidTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortUuidTlv.vicTLVType-85",
        "VicPiVmwareClusterPortUuidTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortUuidTlv.vicTLVLength-86",
        "VicPiVmwareClusterPortUuidTlvVicVariableClusterPortUuidLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortUuidTlv.vicVariableClusterPortUuidLength-87",
        "VicPiVmwareClusterPortUuidTlvVicClusterPortUuid": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortUuidTlv.vicClusterPortUuid-88",
        "VicPiVmwareClusterUuidTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterUuidTlv.vicTLVType-89",
        "VicPiVmwareClusterUuidTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterUuidTlv.vicTLVLength-90",
        "VicPiVmwareClusterUuidTlvVicVariableClusterUuidLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterUuidTlv.vicVariableClusterUuidLength-91",
        "VicPiVmwareClusterUuidTlvVicClusterUuid": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterUuidTlv.vicClusterUuid-92",
        "VicPiVmwareHostPortSetNameTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostPortSetNameTlv.vicTLVType-93",
        "VicPiVmwareHostPortSetNameTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostPortSetNameTlv.vicTLVLength-94",
        "VicPiVmwareHostPortSetNameTlvVicVariableHostPortSetNameLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostPortSetNameTlv.vicVariableHostPortSetNameLength-95",
        "VicPiVmwareHostPortSetNameTlvVicHostPortSetName": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostPortSetNameTlv.vicHostPortSetName-96",
        "VicPiVmwareClusterNameTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterNameTlv.vicTLVType-97",
        "VicPiVmwareClusterNameTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterNameTlv.vicTLVLength-98",
        "VicPiVmwareClusterNameTlvVicVariableClusterNameLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterNameTlv.vicVariableClusterNameLength-99",
        "VicPiVmwareClusterNameTlvVicClusterName": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterNameTlv.vicClusterName-100",
        "VicPiVmwareHostUuidTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostUuidTlv.vicTLVType-101",
        "VicPiVmwareHostUuidTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostUuidTlv.vicTLVLength-102",
        "VicPiVmwareHostUuidTlvVicVariableHostUuidLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostUuidTlv.vicVariableHostUuidLength-103",
        "VicPiVmwareHostUuidTlvVicHostUuid": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHostUuidTlv.vicHostUuid-104",
        "VicPiVmwareClientUuidTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientUuidTlv.vicTLVType-105",
        "VicPiVmwareClientUuidTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientUuidTlv.vicTLVLength-106",
        "VicPiVmwareClientUuidTlvVicVariableClientUuidLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientUuidTlv.vicVariableClientUuidLength-107",
        "VicPiVmwareClientUuidTlvVicClientUuid": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClientUuidTlv.vicClientUuid-108",
        "VicPiVmwareIncarnationNumberTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareIncarnationNumberTlv.vicTLVType-109",
        "VicPiVmwareIncarnationNumberTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareIncarnationNumberTlv.vicTLVLength-110",
        "VicPiVmwareIncarnationNumberTlvVicVariableIncarnationNumberLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareIncarnationNumberTlv.vicVariableIncarnationNumberLength-111",
        "VicPiVmwareIncarnationNumberTlvVicIncarnationNumber": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareIncarnationNumberTlv.vicIncarnationNumber-112",
        "VicPiVmwareOstypeTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareOstypeTlv.vicTLVType-113",
        "VicPiVmwareOstypeTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareOstypeTlv.vicTLVLength-114",
        "VicPiVmwareOstypeTlvVicPiVmwareOstype": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareOstypeTlv.vicPiVmwareOstype-115",
        "VicPiVmwareOsvendorTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareOsvendorTlv.vicTLVType-116",
        "VicPiVmwareOsvendorTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareOsvendorTlv.vicTLVLength-117",
        "VicPiVmwareOsvendorTlvVicPiVmwareOsvendor": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareOsvendorTlv.vicPiVmwareOsvendor-118",
        "VicPiVmwareHypervisortypeTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHypervisortypeTlv.vicTLVType-119",
        "VicPiVmwareHypervisortypeTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHypervisortypeTlv.vicTLVLength-120",
        "VicPiVmwareHypervisortypeTlvVicPiVmwareHypervisortype": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHypervisortypeTlv.vicPiVmwareHypervisortype-121",
        "VicPiVmwareHypervisorvendorTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHypervisorvendorTlv.vicTLVType-122",
        "VicPiVmwareHypervisorvendorTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHypervisorvendorTlv.vicTLVLength-123",
        "VicPiVmwareHypervisorvendorTlvVicPiVmwareHypervisortype": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareHypervisorvendorTlv.vicPiVmwareHypervisortype-124",
        "VicPiVmwareClienttypeTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClienttypeTlv.vicTLVType-125",
        "VicPiVmwareClienttypeTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClienttypeTlv.vicTLVLength-126",
        "VicPiVmwareClienttypeTlvVicPiVmwareClienttype": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClienttypeTlv.vicPiVmwareClienttype-127",
        "VicPiVmwareManagementPlaneTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareManagementPlaneTlv.vicTLVType-128",
        "VicPiVmwareManagementPlaneTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareManagementPlaneTlv.vicTLVLength-129",
        "VicPiVmwareManagementPlaneTlvVicPiVmwareManagementplane": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareManagementPlaneTlv.vicPiVmwareManagementplane-130",
        "VicPiVmwareClusterPortNameTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortNameTlv.vicTLVType-131",
        "VicPiVmwareClusterPortNameTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortNameTlv.vicTLVLength-132",
        "VicPiVmwareClusterPortNameTlvVicVariableClusterPortNameLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortNameTlv.vicVariableClusterPortNameLength-133",
        "VicPiVmwareClusterPortNameTlvVicClusterPortName": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiVmware.vicPiVmwareClusterPortNameTlv.vicClusterPortName-134",
        "VicPiFixedVicPiType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiType-135",
        "VicPiFixedVicPiFixedVifType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedVifType-136",
        "VicPiFixedVicPiFixedInstance": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedInstance-137",
        "VicPiFixedVicPiFixedNumberOfTlvs": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedNumberOfTlvs-138",
        "VicPiFixedProfileNameTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedProfileNameTlv.vicTLVType-139",
        "VicPiFixedProfileNameTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedProfileNameTlv.vicTLVLength-140",
        "VicPiFixedProfileNameTlvVicVariableProfileNameLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedProfileNameTlv.vicVariableProfileNameLength-141",
        "VicPiFixedProfileNameTlvVicProfileName": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedProfileNameTlv.vicProfileName-142",
        "VicPiFixedVnicUuidTlvVicTLVType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedVnicUuidTlv.vicTLVType-143",
        "VicPiFixedVnicUuidTlvVicTLVLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedVnicUuidTlv.vicTLVLength-144",
        "VicPiFixedVnicUuidTlvVicPiFixedVnicUuid": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiCiscoTypeSpace.vicPiCiscoTypes.vicPiFixed.vicPiFixedVnicUuidTlv.vicPiFixedVnicUuid-145",
        "VicPiOtherTypeSpaceVicPiTypeSpace": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiOtherTypeSpace.vicPiTypeSpace-146",
        "VicPiOtherTypeSpaceVicPiType": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiOtherTypeSpace.vicPiType-147",
        "VicPiOtherTypeSpaceVicVariablePiLength": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiOtherTypeSpace.vicVariablePiLength-148",
        "VicPiOtherTypeSpaceVicPi": "vic.header.messageTypes.vicVifCreateRequest.vicMandatoryTLVs.vicProvisioningInfo.vicPiTypeSpaces.vicPiOtherTypeSpace.vicPi-149",
        "VicVifCreateResponseVicMessageType": "vic.header.messageTypes.vicVifCreateResponse.vicMessageType-150",
        "VicVifCreateResponseVicMessageVersion": "vic.header.messageTypes.vicVifCreateResponse.vicMessageVersion-151",
        "VicvifcreateresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifCreateResponse.vicMessageFlags.vicZFlag-152",
        "VicvifcreateresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifCreateResponse.vicMessageFlags.vicPFlag-153",
        "VicvifcreateresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifCreateResponse.vicMessageFlags.vicMFlag-154",
        "VicvifcreateresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifCreateResponse.vicMessageFlags.vicRFlag-155",
        "VicVifCreateResponseVicMessageLen": "vic.header.messageTypes.vicVifCreateResponse.vicMessageLen-156",
        "VicVifCreateResponseVicMessageId": "vic.header.messageTypes.vicVifCreateResponse.vicMessageId-157",
        "VicVifCreateResponseVicFragmentId": "vic.header.messageTypes.vicVifCreateResponse.vicFragmentId-158",
        "VicVifCreateResponseVicCompletionCode": "vic.header.messageTypes.vicVifCreateResponse.vicCompletionCode-159",
        "VicVifCreateResponseVicVifIndex": "vic.header.messageTypes.vicVifCreateResponse.vicVifIndex-160",
        "VicPriorityVicTLVType": "vic.header.messageTypes.vicVifCreateResponse.vicMandatoryTLVs.vicPriority.vicTLVType-161",
        "VicPriorityVicTLVLength": "vic.header.messageTypes.vicVifCreateResponse.vicMandatoryTLVs.vicPriority.vicTLVLength-162",
        "VicPriorityVicPValue": "vic.header.messageTypes.vicVifCreateResponse.vicMandatoryTLVs.vicPriority.vicPValue-163",
        "VicVifDeleteRequestVicMessageType": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageType-164",
        "VicVifDeleteRequestVicMessageVersion": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageVersion-165",
        "VicvifdeleterequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageFlags.vicZFlag-166",
        "VicvifdeleterequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageFlags.vicPFlag-167",
        "VicvifdeleterequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageFlags.vicMFlag-168",
        "VicvifdeleterequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageFlags.vicRFlag-169",
        "VicVifDeleteRequestVicMessageLen": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageLen-170",
        "VicVifDeleteRequestVicMessageId": "vic.header.messageTypes.vicVifDeleteRequest.vicMessageId-171",
        "VicVifDeleteRequestVicFragmentId": "vic.header.messageTypes.vicVifDeleteRequest.vicFragmentId-172",
        "VicVifDeleteRequestVicCompletionCode": "vic.header.messageTypes.vicVifDeleteRequest.vicCompletionCode-173",
        "VicVifDeleteRequestVicVifIndex": "vic.header.messageTypes.vicVifDeleteRequest.vicVifIndex-174",
        "VicVifDeleteResponseVicMessageType": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageType-175",
        "VicVifDeleteResponseVicMessageVersion": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageVersion-176",
        "VicvifdeleteresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageFlags.vicZFlag-177",
        "VicvifdeleteresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageFlags.vicPFlag-178",
        "VicvifdeleteresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageFlags.vicMFlag-179",
        "VicvifdeleteresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageFlags.vicRFlag-180",
        "VicVifDeleteResponseVicMessageLen": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageLen-181",
        "VicVifDeleteResponseVicMessageId": "vic.header.messageTypes.vicVifDeleteResponse.vicMessageId-182",
        "VicVifDeleteResponseVicFragmentId": "vic.header.messageTypes.vicVifDeleteResponse.vicFragmentId-183",
        "VicVifDeleteResponseVicCompletionCode": "vic.header.messageTypes.vicVifDeleteResponse.vicCompletionCode-184",
        "VicVifDeleteResponseVicVifIndex": "vic.header.messageTypes.vicVifDeleteResponse.vicVifIndex-185",
        "VicVifEnableRequestVicMessageType": "vic.header.messageTypes.vicVifEnableRequest.vicMessageType-186",
        "VicVifEnableRequestVicMessageVersion": "vic.header.messageTypes.vicVifEnableRequest.vicMessageVersion-187",
        "VicvifenablerequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifEnableRequest.vicMessageFlags.vicZFlag-188",
        "VicvifenablerequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifEnableRequest.vicMessageFlags.vicPFlag-189",
        "VicvifenablerequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifEnableRequest.vicMessageFlags.vicMFlag-190",
        "VicvifenablerequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifEnableRequest.vicMessageFlags.vicRFlag-191",
        "VicVifEnableRequestVicMessageLen": "vic.header.messageTypes.vicVifEnableRequest.vicMessageLen-192",
        "VicVifEnableRequestVicMessageId": "vic.header.messageTypes.vicVifEnableRequest.vicMessageId-193",
        "VicVifEnableRequestVicFragmentId": "vic.header.messageTypes.vicVifEnableRequest.vicFragmentId-194",
        "VicVifEnableRequestVicCompletionCode": "vic.header.messageTypes.vicVifEnableRequest.vicCompletionCode-195",
        "VicVifEnableRequestVicVifIndex": "vic.header.messageTypes.vicVifEnableRequest.vicVifIndex-196",
        "VicVifStateVicTLVType": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicTLVType-197",
        "VicVifStateVicTLVLength": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicTLVLength-198",
        "VicVifStateVicVsRsvd": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicVsRsvd-199",
        "VicVifStateVicVsSFlag": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicVsSFlag-200",
        "VicVifStateVicVsPFlag": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicVsPFlag-201",
        "VicVifStateVicVsDFlag": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicVsDFlag-202",
        "VicVifStateVicVsEFlag": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifState.vicVsEFlag-203",
        "VicAddressArrayVicTLVType": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicAddressArray.vicTLVType-204",
        "VicAddressArrayVicTLVLength": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicAddressArray.vicTLVLength-205",
        "VicAddressEntryVicAddressType": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressType-206",
        "VicAddressEntryVicAddressLen": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressLen-207",
        "VicAddressValueVicAddressVlan": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressValue.vicAddressVlan-208",
        "VicAddressValueVicAddressMac": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressValue.vicAddressMac-209",
        "VicVifIdVicTLVType": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifId.vicTLVType-210",
        "VicVifIdVicTLVLength": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifId.vicTLVLength-211",
        "VicVifIdVicViRsvd": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifId.vicViRsvd-212",
        "VicVifIdVicViValueInVntag": "vic.header.messageTypes.vicVifEnableRequest.vicOptionalTLVs.vicVifId.vicViValueInVntag-213",
        "VicVifEnableResponseVicMessageType": "vic.header.messageTypes.vicVifEnableResponse.vicMessageType-214",
        "VicVifEnableResponseVicMessageVersion": "vic.header.messageTypes.vicVifEnableResponse.vicMessageVersion-215",
        "VicvifenableresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifEnableResponse.vicMessageFlags.vicZFlag-216",
        "VicvifenableresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifEnableResponse.vicMessageFlags.vicPFlag-217",
        "VicvifenableresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifEnableResponse.vicMessageFlags.vicMFlag-218",
        "VicvifenableresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifEnableResponse.vicMessageFlags.vicRFlag-219",
        "VicVifEnableResponseVicMessageLen": "vic.header.messageTypes.vicVifEnableResponse.vicMessageLen-220",
        "VicVifEnableResponseVicMessageId": "vic.header.messageTypes.vicVifEnableResponse.vicMessageId-221",
        "VicVifEnableResponseVicFragmentId": "vic.header.messageTypes.vicVifEnableResponse.vicFragmentId-222",
        "VicVifEnableResponseVicCompletionCode": "vic.header.messageTypes.vicVifEnableResponse.vicCompletionCode-223",
        "VicVifEnableResponseVicVifIndex": "vic.header.messageTypes.vicVifEnableResponse.vicVifIndex-224",
        "VicVifDisableRequestVicMessageType": "vic.header.messageTypes.vicVifDisableRequest.vicMessageType-225",
        "VicVifDisableRequestVicMessageVersion": "vic.header.messageTypes.vicVifDisableRequest.vicMessageVersion-226",
        "VicvifdisablerequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDisableRequest.vicMessageFlags.vicZFlag-227",
        "VicvifdisablerequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDisableRequest.vicMessageFlags.vicPFlag-228",
        "VicvifdisablerequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDisableRequest.vicMessageFlags.vicMFlag-229",
        "VicvifdisablerequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDisableRequest.vicMessageFlags.vicRFlag-230",
        "VicVifDisableRequestVicMessageLen": "vic.header.messageTypes.vicVifDisableRequest.vicMessageLen-231",
        "VicVifDisableRequestVicMessageId": "vic.header.messageTypes.vicVifDisableRequest.vicMessageId-232",
        "VicVifDisableRequestVicFragmentId": "vic.header.messageTypes.vicVifDisableRequest.vicFragmentId-233",
        "VicVifDisableRequestVicCompletionCode": "vic.header.messageTypes.vicVifDisableRequest.vicCompletionCode-234",
        "VicVifDisableRequestVicVifIndex": "vic.header.messageTypes.vicVifDisableRequest.vicVifIndex-235",
        "VicVifDisableResponseVicMessageType": "vic.header.messageTypes.vicVifDisableResponse.vicMessageType-236",
        "VicVifDisableResponseVicMessageVersion": "vic.header.messageTypes.vicVifDisableResponse.vicMessageVersion-237",
        "VicvifdisableresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDisableResponse.vicMessageFlags.vicZFlag-238",
        "VicvifdisableresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDisableResponse.vicMessageFlags.vicPFlag-239",
        "VicvifdisableresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDisableResponse.vicMessageFlags.vicMFlag-240",
        "VicvifdisableresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDisableResponse.vicMessageFlags.vicRFlag-241",
        "VicVifDisableResponseVicMessageLen": "vic.header.messageTypes.vicVifDisableResponse.vicMessageLen-242",
        "VicVifDisableResponseVicMessageId": "vic.header.messageTypes.vicVifDisableResponse.vicMessageId-243",
        "VicVifDisableResponseVicFragmentId": "vic.header.messageTypes.vicVifDisableResponse.vicFragmentId-244",
        "VicVifDisableResponseVicCompletionCode": "vic.header.messageTypes.vicVifDisableResponse.vicCompletionCode-245",
        "VicVifDisableResponseVicVifIndex": "vic.header.messageTypes.vicVifDisableResponse.vicVifIndex-246",
        "VicVifSetRequestVicMessageType": "vic.header.messageTypes.vicVifSetRequest.vicMessageType-247",
        "VicVifSetRequestVicMessageVersion": "vic.header.messageTypes.vicVifSetRequest.vicMessageVersion-248",
        "VicvifsetrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifSetRequest.vicMessageFlags.vicZFlag-249",
        "VicvifsetrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifSetRequest.vicMessageFlags.vicPFlag-250",
        "VicvifsetrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifSetRequest.vicMessageFlags.vicMFlag-251",
        "VicvifsetrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifSetRequest.vicMessageFlags.vicRFlag-252",
        "VicVifSetRequestVicMessageLen": "vic.header.messageTypes.vicVifSetRequest.vicMessageLen-253",
        "VicVifSetRequestVicMessageId": "vic.header.messageTypes.vicVifSetRequest.vicMessageId-254",
        "VicVifSetRequestVicFragmentId": "vic.header.messageTypes.vicVifSetRequest.vicFragmentId-255",
        "VicVifSetRequestVicCompletionCode": "vic.header.messageTypes.vicVifSetRequest.vicCompletionCode-256",
        "VicVifSetRequestVicVifIndex": "vic.header.messageTypes.vicVifSetRequest.vicVifIndex-257",
        "VicmandatorytlvsVicVifIdVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifId.vicTLVType-258",
        "VicmandatorytlvsVicVifIdVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifId.vicTLVLength-259",
        "VicmandatorytlvsVicVifIdVicViRsvd": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifId.vicViRsvd-260",
        "VicmandatorytlvsVicVifIdVicViValueInVntag": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifId.vicViValueInVntag-261",
        "VicVlanVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVlan.vicTLVType-262",
        "VicVlanVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVlan.vicTLVLength-263",
        "VicVlanVicVRsvd": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVlan.vicVRsvd-264",
        "VicVlanVicVMode": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVlan.vicVMode-265",
        "VicVlanVicVValue": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVlan.vicVValue-266",
        "VicmandatorytlvsVicVifStateVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicTLVType-267",
        "VicmandatorytlvsVicVifStateVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicTLVLength-268",
        "VicmandatorytlvsVicVifStateVicVsRsvd": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicVsRsvd-269",
        "VicmandatorytlvsVicVifStateVicVsSFlag": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicVsSFlag-270",
        "VicmandatorytlvsVicVifStateVicVsPFlag": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicVsPFlag-271",
        "VicmandatorytlvsVicVifStateVicVsDFlag": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicVsDFlag-272",
        "VicmandatorytlvsVicVifStateVicVsEFlag": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicVifState.vicVsEFlag-273",
        "VicmandatorytlvsVicPriorityVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicPriority.vicTLVType-274",
        "VicmandatorytlvsVicPriorityVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicPriority.vicTLVLength-275",
        "VicmandatorytlvsVicPriorityVicPValue": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicPriority.vicPValue-276",
        "VicDefaultCosVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicDefaultCos.vicTLVType-277",
        "VicDefaultCosVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicDefaultCos.vicTLVLength-278",
        "VicDefaultCosVicDcRsvd": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicDefaultCos.vicDcRsvd-279",
        "VicDefaultCosVicDc": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicDefaultCos.vicDc-280",
        "VicCosFilterVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicCosFilter.vicTLVType-281",
        "VicCosFilterVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicCosFilter.vicTLVLength-282",
        "VicCosFilterVicCfMap": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicCosFilter.vicCfMap-283",
        "VicRateLimitVicTLVType": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicRateLimit.vicTLVType-284",
        "VicRateLimitVicTLVLength": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicRateLimit.vicTLVLength-285",
        "VicRateLimitVicRlRate": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicRateLimit.vicRlRate-286",
        "VicRateLimitVicBurstSize": "vic.header.messageTypes.vicVifSetRequest.vicMandatoryTLVs.vicRateLimit.vicBurstSize-287",
        "VicVifSetResponseVicMessageType": "vic.header.messageTypes.vicVifSetResponse.vicMessageType-288",
        "VicVifSetResponseVicMessageVersion": "vic.header.messageTypes.vicVifSetResponse.vicMessageVersion-289",
        "VicvifsetresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifSetResponse.vicMessageFlags.vicZFlag-290",
        "VicvifsetresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifSetResponse.vicMessageFlags.vicPFlag-291",
        "VicvifsetresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifSetResponse.vicMessageFlags.vicMFlag-292",
        "VicvifsetresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifSetResponse.vicMessageFlags.vicRFlag-293",
        "VicVifSetResponseVicMessageLen": "vic.header.messageTypes.vicVifSetResponse.vicMessageLen-294",
        "VicVifSetResponseVicMessageId": "vic.header.messageTypes.vicVifSetResponse.vicMessageId-295",
        "VicVifSetResponseVicFragmentId": "vic.header.messageTypes.vicVifSetResponse.vicFragmentId-296",
        "VicVifSetResponseVicCompletionCode": "vic.header.messageTypes.vicVifSetResponse.vicCompletionCode-297",
        "VicVifSetResponseVicVifIndex": "vic.header.messageTypes.vicVifSetResponse.vicVifIndex-298",
        "VicvifsetresponseVicmandatorytlvsVicVifIdVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifId.vicTLVType-299",
        "VicvifsetresponseVicmandatorytlvsVicVifIdVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifId.vicTLVLength-300",
        "VicvifsetresponseVicmandatorytlvsVicVifIdVicViRsvd": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifId.vicViRsvd-301",
        "VicvifsetresponseVicmandatorytlvsVicVifIdVicViValueInVntag": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifId.vicViValueInVntag-302",
        "VicmandatorytlvsVicVlanVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVlan.vicTLVType-303",
        "VicmandatorytlvsVicVlanVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVlan.vicTLVLength-304",
        "VicmandatorytlvsVicVlanVicVRsvd": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVlan.vicVRsvd-305",
        "VicmandatorytlvsVicVlanVicVMode": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVlan.vicVMode-306",
        "VicmandatorytlvsVicVlanVicVValue": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVlan.vicVValue-307",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicTLVType-308",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicTLVLength-309",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsRsvd": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicVsRsvd-310",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsSFlag": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicVsSFlag-311",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsPFlag": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicVsPFlag-312",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsDFlag": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicVsDFlag-313",
        "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsEFlag": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicVifState.vicVsEFlag-314",
        "VicvifsetresponseVicmandatorytlvsVicPriorityVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicPriority.vicTLVType-315",
        "VicvifsetresponseVicmandatorytlvsVicPriorityVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicPriority.vicTLVLength-316",
        "VicvifsetresponseVicmandatorytlvsVicPriorityVicPValue": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicPriority.vicPValue-317",
        "VicmandatorytlvsVicDefaultCosVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicDefaultCos.vicTLVType-318",
        "VicmandatorytlvsVicDefaultCosVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicDefaultCos.vicTLVLength-319",
        "VicmandatorytlvsVicDefaultCosVicDcRsvd": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicDefaultCos.vicDcRsvd-320",
        "VicmandatorytlvsVicDefaultCosVicDc": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicDefaultCos.vicDc-321",
        "VicmandatorytlvsVicCosFilterVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicCosFilter.vicTLVType-322",
        "VicmandatorytlvsVicCosFilterVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicCosFilter.vicTLVLength-323",
        "VicmandatorytlvsVicCosFilterVicCfMap": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicCosFilter.vicCfMap-324",
        "VicmandatorytlvsVicRateLimitVicTLVType": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicRateLimit.vicTLVType-325",
        "VicmandatorytlvsVicRateLimitVicTLVLength": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicRateLimit.vicTLVLength-326",
        "VicmandatorytlvsVicRateLimitVicRlRate": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicRateLimit.vicRlRate-327",
        "VicmandatorytlvsVicRateLimitVicBurstSize": "vic.header.messageTypes.vicVifSetResponse.vicMandatoryTLVs.vicRateLimit.vicBurstSize-328",
        "VicVifGetRequestVicMessageType": "vic.header.messageTypes.vicVifGetRequest.vicMessageType-329",
        "VicVifGetRequestVicMessageVersion": "vic.header.messageTypes.vicVifGetRequest.vicMessageVersion-330",
        "VicvifgetrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifGetRequest.vicMessageFlags.vicZFlag-331",
        "VicvifgetrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifGetRequest.vicMessageFlags.vicPFlag-332",
        "VicvifgetrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifGetRequest.vicMessageFlags.vicMFlag-333",
        "VicvifgetrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifGetRequest.vicMessageFlags.vicRFlag-334",
        "VicVifGetRequestVicMessageLen": "vic.header.messageTypes.vicVifGetRequest.vicMessageLen-335",
        "VicVifGetRequestVicMessageId": "vic.header.messageTypes.vicVifGetRequest.vicMessageId-336",
        "VicVifGetRequestVicFragmentId": "vic.header.messageTypes.vicVifGetRequest.vicFragmentId-337",
        "VicVifGetRequestVicCompletionCode": "vic.header.messageTypes.vicVifGetRequest.vicCompletionCode-338",
        "VicVifGetRequestVicVifIndex": "vic.header.messageTypes.vicVifGetRequest.vicVifIndex-339",
        "VicVifGetResponseVicMessageType": "vic.header.messageTypes.vicVifGetResponse.vicMessageType-340",
        "VicVifGetResponseVicMessageVersion": "vic.header.messageTypes.vicVifGetResponse.vicMessageVersion-341",
        "VicvifgetresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifGetResponse.vicMessageFlags.vicZFlag-342",
        "VicvifgetresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifGetResponse.vicMessageFlags.vicPFlag-343",
        "VicvifgetresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifGetResponse.vicMessageFlags.vicMFlag-344",
        "VicvifgetresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifGetResponse.vicMessageFlags.vicRFlag-345",
        "VicVifGetResponseVicMessageLen": "vic.header.messageTypes.vicVifGetResponse.vicMessageLen-346",
        "VicVifGetResponseVicMessageId": "vic.header.messageTypes.vicVifGetResponse.vicMessageId-347",
        "VicVifGetResponseVicFragmentId": "vic.header.messageTypes.vicVifGetResponse.vicFragmentId-348",
        "VicVifGetResponseVicCompletionCode": "vic.header.messageTypes.vicVifGetResponse.vicCompletionCode-349",
        "VicVifGetResponseVicVifIndex": "vic.header.messageTypes.vicVifGetResponse.vicVifIndex-350",
        "VicvifgetresponseVicmandatorytlvsVicVifIdVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifId.vicTLVType-351",
        "VicvifgetresponseVicmandatorytlvsVicVifIdVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifId.vicTLVLength-352",
        "VicvifgetresponseVicmandatorytlvsVicVifIdVicViRsvd": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifId.vicViRsvd-353",
        "VicvifgetresponseVicmandatorytlvsVicVifIdVicViValueInVntag": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifId.vicViValueInVntag-354",
        "VicvifgetresponseVicmandatorytlvsVicVlanVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVlan.vicTLVType-355",
        "VicvifgetresponseVicmandatorytlvsVicVlanVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVlan.vicTLVLength-356",
        "VicvifgetresponseVicmandatorytlvsVicVlanVicVRsvd": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVlan.vicVRsvd-357",
        "VicvifgetresponseVicmandatorytlvsVicVlanVicVMode": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVlan.vicVMode-358",
        "VicvifgetresponseVicmandatorytlvsVicVlanVicVValue": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVlan.vicVValue-359",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicTLVType-360",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicTLVLength-361",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsRsvd": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicVsRsvd-362",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsSFlag": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicVsSFlag-363",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsPFlag": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicVsPFlag-364",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsDFlag": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicVsDFlag-365",
        "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsEFlag": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicVifState.vicVsEFlag-366",
        "VicvifgetresponseVicmandatorytlvsVicPriorityVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicPriority.vicTLVType-367",
        "VicvifgetresponseVicmandatorytlvsVicPriorityVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicPriority.vicTLVLength-368",
        "VicvifgetresponseVicmandatorytlvsVicPriorityVicPValue": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicPriority.vicPValue-369",
        "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicDefaultCos.vicTLVType-370",
        "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicDefaultCos.vicTLVLength-371",
        "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicDcRsvd": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicDefaultCos.vicDcRsvd-372",
        "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicDc": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicDefaultCos.vicDc-373",
        "VicvifgetresponseVicmandatorytlvsVicCosFilterVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicCosFilter.vicTLVType-374",
        "VicvifgetresponseVicmandatorytlvsVicCosFilterVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicCosFilter.vicTLVLength-375",
        "VicvifgetresponseVicmandatorytlvsVicCosFilterVicCfMap": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicCosFilter.vicCfMap-376",
        "VicvifgetresponseVicmandatorytlvsVicRateLimitVicTLVType": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicRateLimit.vicTLVType-377",
        "VicvifgetresponseVicmandatorytlvsVicRateLimitVicTLVLength": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicRateLimit.vicTLVLength-378",
        "VicvifgetresponseVicmandatorytlvsVicRateLimitVicRlRate": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicRateLimit.vicRlRate-379",
        "VicvifgetresponseVicmandatorytlvsVicRateLimitVicBurstSize": "vic.header.messageTypes.vicVifGetResponse.vicMandatoryTLVs.vicRateLimit.vicBurstSize-380",
        "VicVifListSetRequestVicMessageType": "vic.header.messageTypes.vicVifListSetRequest.vicMessageType-381",
        "VicVifListSetRequestVicMessageVersion": "vic.header.messageTypes.vicVifListSetRequest.vicMessageVersion-382",
        "VicviflistsetrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifListSetRequest.vicMessageFlags.vicZFlag-383",
        "VicviflistsetrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifListSetRequest.vicMessageFlags.vicPFlag-384",
        "VicviflistsetrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifListSetRequest.vicMessageFlags.vicMFlag-385",
        "VicviflistsetrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifListSetRequest.vicMessageFlags.vicRFlag-386",
        "VicVifListSetRequestVicMessageLen": "vic.header.messageTypes.vicVifListSetRequest.vicMessageLen-387",
        "VicVifListSetRequestVicMessageId": "vic.header.messageTypes.vicVifListSetRequest.vicMessageId-388",
        "VicVifListSetRequestVicFragmentId": "vic.header.messageTypes.vicVifListSetRequest.vicFragmentId-389",
        "VicVifListSetRequestVicCompletionCode": "vic.header.messageTypes.vicVifListSetRequest.vicCompletionCode-390",
        "VicVifListSetRequestVicVifIndex": "vic.header.messageTypes.vicVifListSetRequest.vicVifIndex-391",
        "VicviflistsetrequestVicmandatorytlvsVicVifIdVicTLVType": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicVifId.vicTLVType-392",
        "VicviflistsetrequestVicmandatorytlvsVicVifIdVicTLVLength": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicVifId.vicTLVLength-393",
        "VicviflistsetrequestVicmandatorytlvsVicVifIdVicViRsvd": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicVifId.vicViRsvd-394",
        "VicviflistsetrequestVicmandatorytlvsVicVifIdVicViValueInVntag": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicVifId.vicViValueInVntag-395",
        "VicIndexArrayVicTLVType": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicIndexArray.vicTLVType-396",
        "VicIndexArrayVicTLVLength": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicIndexArray.vicTLVLength-397",
        "VicIndexEntryVicVifIndex": "vic.header.messageTypes.vicVifListSetRequest.vicMandatoryTLVs.vicIndexArray.vicIndexes.vicIndexEntry.vicVifIndex-398",
        "VicVifListSetResponseVicMessageType": "vic.header.messageTypes.vicVifListSetResponse.vicMessageType-399",
        "VicVifListSetResponseVicMessageVersion": "vic.header.messageTypes.vicVifListSetResponse.vicMessageVersion-400",
        "VicviflistsetresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifListSetResponse.vicMessageFlags.vicZFlag-401",
        "VicviflistsetresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifListSetResponse.vicMessageFlags.vicPFlag-402",
        "VicviflistsetresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifListSetResponse.vicMessageFlags.vicMFlag-403",
        "VicviflistsetresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifListSetResponse.vicMessageFlags.vicRFlag-404",
        "VicVifListSetResponseVicMessageLen": "vic.header.messageTypes.vicVifListSetResponse.vicMessageLen-405",
        "VicVifListSetResponseVicMessageId": "vic.header.messageTypes.vicVifListSetResponse.vicMessageId-406",
        "VicVifListSetResponseVicFragmentId": "vic.header.messageTypes.vicVifListSetResponse.vicFragmentId-407",
        "VicVifListSetResponseVicCompletionCode": "vic.header.messageTypes.vicVifListSetResponse.vicCompletionCode-408",
        "VicVifListSetResponseVicVifIndex": "vic.header.messageTypes.vicVifListSetResponse.vicVifIndex-409",
        "VicVifListGetRequestVicMessageType": "vic.header.messageTypes.vicVifListGetRequest.vicMessageType-410",
        "VicVifListGetRequestVicMessageVersion": "vic.header.messageTypes.vicVifListGetRequest.vicMessageVersion-411",
        "VicviflistgetrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifListGetRequest.vicMessageFlags.vicZFlag-412",
        "VicviflistgetrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifListGetRequest.vicMessageFlags.vicPFlag-413",
        "VicviflistgetrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifListGetRequest.vicMessageFlags.vicMFlag-414",
        "VicviflistgetrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifListGetRequest.vicMessageFlags.vicRFlag-415",
        "VicVifListGetRequestVicMessageLen": "vic.header.messageTypes.vicVifListGetRequest.vicMessageLen-416",
        "VicVifListGetRequestVicMessageId": "vic.header.messageTypes.vicVifListGetRequest.vicMessageId-417",
        "VicVifListGetRequestVicFragmentId": "vic.header.messageTypes.vicVifListGetRequest.vicFragmentId-418",
        "VicVifListGetRequestVicCompletionCode": "vic.header.messageTypes.vicVifListGetRequest.vicCompletionCode-419",
        "VicVifListGetRequestVicVifIndex": "vic.header.messageTypes.vicVifListGetRequest.vicVifIndex-420",
        "VicVifListGetResponseVicMessageType": "vic.header.messageTypes.vicVifListGetResponse.vicMessageType-421",
        "VicVifListGetResponseVicMessageVersion": "vic.header.messageTypes.vicVifListGetResponse.vicMessageVersion-422",
        "VicviflistgetresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifListGetResponse.vicMessageFlags.vicZFlag-423",
        "VicviflistgetresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifListGetResponse.vicMessageFlags.vicPFlag-424",
        "VicviflistgetresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifListGetResponse.vicMessageFlags.vicMFlag-425",
        "VicviflistgetresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifListGetResponse.vicMessageFlags.vicRFlag-426",
        "VicVifListGetResponseVicMessageLen": "vic.header.messageTypes.vicVifListGetResponse.vicMessageLen-427",
        "VicVifListGetResponseVicMessageId": "vic.header.messageTypes.vicVifListGetResponse.vicMessageId-428",
        "VicVifListGetResponseVicFragmentId": "vic.header.messageTypes.vicVifListGetResponse.vicFragmentId-429",
        "VicVifListGetResponseVicCompletionCode": "vic.header.messageTypes.vicVifListGetResponse.vicCompletionCode-430",
        "VicVifListGetResponseVicVifIndex": "vic.header.messageTypes.vicVifListGetResponse.vicVifIndex-431",
        "VicviflistgetresponseVicmandatorytlvsVicVifIdVicTLVType": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicVifId.vicTLVType-432",
        "VicviflistgetresponseVicmandatorytlvsVicVifIdVicTLVLength": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicVifId.vicTLVLength-433",
        "VicviflistgetresponseVicmandatorytlvsVicVifIdVicViRsvd": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicVifId.vicViRsvd-434",
        "VicviflistgetresponseVicmandatorytlvsVicVifIdVicViValueInVntag": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicVifId.vicViValueInVntag-435",
        "VicmandatorytlvsVicIndexArrayVicTLVType": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicIndexArray.vicTLVType-436",
        "VicmandatorytlvsVicIndexArrayVicTLVLength": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicIndexArray.vicTLVLength-437",
        "VicindexesVicIndexEntryVicVifIndex": "vic.header.messageTypes.vicVifListGetResponse.vicMandatoryTLVs.vicIndexArray.vicIndexes.vicIndexEntry.vicVifIndex-438",
        "VicVifRegisterRequestVicMessageType": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageType-439",
        "VicVifRegisterRequestVicMessageVersion": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageVersion-440",
        "VicvifregisterrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageFlags.vicZFlag-441",
        "VicvifregisterrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageFlags.vicPFlag-442",
        "VicvifregisterrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageFlags.vicMFlag-443",
        "VicvifregisterrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageFlags.vicRFlag-444",
        "VicVifRegisterRequestVicMessageLen": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageLen-445",
        "VicVifRegisterRequestVicMessageId": "vic.header.messageTypes.vicVifRegisterRequest.vicMessageId-446",
        "VicVifRegisterRequestVicFragmentId": "vic.header.messageTypes.vicVifRegisterRequest.vicFragmentId-447",
        "VicVifRegisterRequestVicCompletionCode": "vic.header.messageTypes.vicVifRegisterRequest.vicCompletionCode-448",
        "VicVifRegisterRequestVicVifIndex": "vic.header.messageTypes.vicVifRegisterRequest.vicVifIndex-449",
        "VicoptionaltlvsVicAddressArrayVicTLVType": "vic.header.messageTypes.vicVifRegisterRequest.vicOptionalTLVs.vicAddressArray.vicTLVType-450",
        "VicoptionaltlvsVicAddressArrayVicTLVLength": "vic.header.messageTypes.vicVifRegisterRequest.vicOptionalTLVs.vicAddressArray.vicTLVLength-451",
        "VicaddressesVicAddressEntryVicAddressType": "vic.header.messageTypes.vicVifRegisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressType-452",
        "VicaddressesVicAddressEntryVicAddressLen": "vic.header.messageTypes.vicVifRegisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressLen-453",
        "VicaddressentryVicAddressValueVicAddressVlan": "vic.header.messageTypes.vicVifRegisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressValue.vicAddressVlan-454",
        "VicaddressentryVicAddressValueVicAddressMac": "vic.header.messageTypes.vicVifRegisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressValue.vicAddressMac-455",
        "VicVifRegisterResponseVicMessageType": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageType-456",
        "VicVifRegisterResponseVicMessageVersion": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageVersion-457",
        "VicvifregisterresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageFlags.vicZFlag-458",
        "VicvifregisterresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageFlags.vicPFlag-459",
        "VicvifregisterresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageFlags.vicMFlag-460",
        "VicvifregisterresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageFlags.vicRFlag-461",
        "VicVifRegisterResponseVicMessageLen": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageLen-462",
        "VicVifRegisterResponseVicMessageId": "vic.header.messageTypes.vicVifRegisterResponse.vicMessageId-463",
        "VicVifRegisterResponseVicFragmentId": "vic.header.messageTypes.vicVifRegisterResponse.vicFragmentId-464",
        "VicVifRegisterResponseVicCompletionCode": "vic.header.messageTypes.vicVifRegisterResponse.vicCompletionCode-465",
        "VicVifRegisterResponseVicVifIndex": "vic.header.messageTypes.vicVifRegisterResponse.vicVifIndex-466",
        "VicVifDeregisterRequestVicMessageType": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageType-467",
        "VicVifDeregisterRequestVicMessageVersion": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageVersion-468",
        "VicvifderegisterrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageFlags.vicZFlag-469",
        "VicvifderegisterrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageFlags.vicPFlag-470",
        "VicvifderegisterrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageFlags.vicMFlag-471",
        "VicvifderegisterrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageFlags.vicRFlag-472",
        "VicVifDeregisterRequestVicMessageLen": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageLen-473",
        "VicVifDeregisterRequestVicMessageId": "vic.header.messageTypes.vicVifDeregisterRequest.vicMessageId-474",
        "VicVifDeregisterRequestVicFragmentId": "vic.header.messageTypes.vicVifDeregisterRequest.vicFragmentId-475",
        "VicVifDeregisterRequestVicCompletionCode": "vic.header.messageTypes.vicVifDeregisterRequest.vicCompletionCode-476",
        "VicVifDeregisterRequestVicVifIndex": "vic.header.messageTypes.vicVifDeregisterRequest.vicVifIndex-477",
        "VicvifderegisterrequestVicoptionaltlvsVicAddressArrayVicTLVType": "vic.header.messageTypes.vicVifDeregisterRequest.vicOptionalTLVs.vicAddressArray.vicTLVType-478",
        "VicvifderegisterrequestVicoptionaltlvsVicAddressArrayVicTLVLength": "vic.header.messageTypes.vicVifDeregisterRequest.vicOptionalTLVs.vicAddressArray.vicTLVLength-479",
        "VicaddressarrayVicaddressesVicAddressEntryVicAddressType": "vic.header.messageTypes.vicVifDeregisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressType-480",
        "VicaddressarrayVicaddressesVicAddressEntryVicAddressLen": "vic.header.messageTypes.vicVifDeregisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressLen-481",
        "VicaddressesVicaddressentryVicAddressValueVicAddressVlan": "vic.header.messageTypes.vicVifDeregisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressValue.vicAddressVlan-482",
        "VicaddressesVicaddressentryVicAddressValueVicAddressMac": "vic.header.messageTypes.vicVifDeregisterRequest.vicOptionalTLVs.vicAddressArray.vicAddresses.vicAddressEntry.vicAddressValue.vicAddressMac-483",
        "VicVifDeregisterResponseVicMessageType": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageType-484",
        "VicVifDeregisterResponseVicMessageVersion": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageVersion-485",
        "VicvifderegisterresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageFlags.vicZFlag-486",
        "VicvifderegisterresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageFlags.vicPFlag-487",
        "VicvifderegisterresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageFlags.vicMFlag-488",
        "VicvifderegisterresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageFlags.vicRFlag-489",
        "VicVifDeregisterResponseVicMessageLen": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageLen-490",
        "VicVifDeregisterResponseVicMessageId": "vic.header.messageTypes.vicVifDeregisterResponse.vicMessageId-491",
        "VicVifDeregisterResponseVicFragmentId": "vic.header.messageTypes.vicVifDeregisterResponse.vicFragmentId-492",
        "VicVifDeregisterResponseVicCompletionCode": "vic.header.messageTypes.vicVifDeregisterResponse.vicCompletionCode-493",
        "VicVifDeregisterResponseVicVifIndex": "vic.header.messageTypes.vicVifDeregisterResponse.vicVifIndex-494",
        "VicVifActivateRequestVicMessageType": "vic.header.messageTypes.vicVifActivateRequest.vicMessageType-495",
        "VicVifActivateRequestVicMessageVersion": "vic.header.messageTypes.vicVifActivateRequest.vicMessageVersion-496",
        "VicvifactivaterequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifActivateRequest.vicMessageFlags.vicZFlag-497",
        "VicvifactivaterequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifActivateRequest.vicMessageFlags.vicPFlag-498",
        "VicvifactivaterequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifActivateRequest.vicMessageFlags.vicMFlag-499",
        "VicvifactivaterequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifActivateRequest.vicMessageFlags.vicRFlag-500",
        "VicVifActivateRequestVicMessageLen": "vic.header.messageTypes.vicVifActivateRequest.vicMessageLen-501",
        "VicVifActivateRequestVicMessageId": "vic.header.messageTypes.vicVifActivateRequest.vicMessageId-502",
        "VicVifActivateRequestVicFragmentId": "vic.header.messageTypes.vicVifActivateRequest.vicFragmentId-503",
        "VicVifActivateRequestVicCompletionCode": "vic.header.messageTypes.vicVifActivateRequest.vicCompletionCode-504",
        "VicVifActivateRequestVicVifIndex": "vic.header.messageTypes.vicVifActivateRequest.vicVifIndex-505",
        "VicoptionaltlvsVicIndexArrayVicTLVType": "vic.header.messageTypes.vicVifActivateRequest.vicOptionalTLVs.vicIndexArray.vicTLVType-506",
        "VicoptionaltlvsVicIndexArrayVicTLVLength": "vic.header.messageTypes.vicVifActivateRequest.vicOptionalTLVs.vicIndexArray.vicTLVLength-507",
        "VicindexarrayVicindexesVicIndexEntryVicVifIndex": "vic.header.messageTypes.vicVifActivateRequest.vicOptionalTLVs.vicIndexArray.vicIndexes.vicIndexEntry.vicVifIndex-508",
        "VicVifActivateResponseVicMessageType": "vic.header.messageTypes.vicVifActivateResponse.vicMessageType-509",
        "VicVifActivateResponseVicMessageVersion": "vic.header.messageTypes.vicVifActivateResponse.vicMessageVersion-510",
        "VicvifactivateresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifActivateResponse.vicMessageFlags.vicZFlag-511",
        "VicvifactivateresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifActivateResponse.vicMessageFlags.vicPFlag-512",
        "VicvifactivateresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifActivateResponse.vicMessageFlags.vicMFlag-513",
        "VicvifactivateresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifActivateResponse.vicMessageFlags.vicRFlag-514",
        "VicVifActivateResponseVicMessageLen": "vic.header.messageTypes.vicVifActivateResponse.vicMessageLen-515",
        "VicVifActivateResponseVicMessageId": "vic.header.messageTypes.vicVifActivateResponse.vicMessageId-516",
        "VicVifActivateResponseVicFragmentId": "vic.header.messageTypes.vicVifActivateResponse.vicFragmentId-517",
        "VicVifActivateResponseVicCompletionCode": "vic.header.messageTypes.vicVifActivateResponse.vicCompletionCode-518",
        "VicVifActivateResponseVicVifIndex": "vic.header.messageTypes.vicVifActivateResponse.vicVifIndex-519",
        "VicVifDeactivateRequestVicMessageType": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageType-520",
        "VicVifDeactivateRequestVicMessageVersion": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageVersion-521",
        "VicvifdeactivaterequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageFlags.vicZFlag-522",
        "VicvifdeactivaterequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageFlags.vicPFlag-523",
        "VicvifdeactivaterequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageFlags.vicMFlag-524",
        "VicvifdeactivaterequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageFlags.vicRFlag-525",
        "VicVifDeactivateRequestVicMessageLen": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageLen-526",
        "VicVifDeactivateRequestVicMessageId": "vic.header.messageTypes.vicVifDeactivateRequest.vicMessageId-527",
        "VicVifDeactivateRequestVicFragmentId": "vic.header.messageTypes.vicVifDeactivateRequest.vicFragmentId-528",
        "VicVifDeactivateRequestVicCompletionCode": "vic.header.messageTypes.vicVifDeactivateRequest.vicCompletionCode-529",
        "VicVifDeactivateRequestVicVifIndex": "vic.header.messageTypes.vicVifDeactivateRequest.vicVifIndex-530",
        "VicvifdeactivaterequestVicoptionaltlvsVicIndexArrayVicTLVType": "vic.header.messageTypes.vicVifDeactivateRequest.vicOptionalTLVs.vicIndexArray.vicTLVType-531",
        "VicvifdeactivaterequestVicoptionaltlvsVicIndexArrayVicTLVLength": "vic.header.messageTypes.vicVifDeactivateRequest.vicOptionalTLVs.vicIndexArray.vicTLVLength-532",
        "VicoptionaltlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex": "vic.header.messageTypes.vicVifDeactivateRequest.vicOptionalTLVs.vicIndexArray.vicIndexes.vicIndexEntry.vicVifIndex-533",
        "VicVifDeactivateResponseVicMessageType": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageType-534",
        "VicVifDeactivateResponseVicMessageVersion": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageVersion-535",
        "VicvifdeactivateresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageFlags.vicZFlag-536",
        "VicvifdeactivateresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageFlags.vicPFlag-537",
        "VicvifdeactivateresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageFlags.vicMFlag-538",
        "VicvifdeactivateresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageFlags.vicRFlag-539",
        "VicVifDeactivateResponseVicMessageLen": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageLen-540",
        "VicVifDeactivateResponseVicMessageId": "vic.header.messageTypes.vicVifDeactivateResponse.vicMessageId-541",
        "VicVifDeactivateResponseVicFragmentId": "vic.header.messageTypes.vicVifDeactivateResponse.vicFragmentId-542",
        "VicVifDeactivateResponseVicCompletionCode": "vic.header.messageTypes.vicVifDeactivateResponse.vicCompletionCode-543",
        "VicVifDeactivateResponseVicVifIndex": "vic.header.messageTypes.vicVifDeactivateResponse.vicVifIndex-544",
        "VicStatsGetRequestVicMessageType": "vic.header.messageTypes.vicStatsGetRequest.vicMessageType-545",
        "VicStatsGetRequestVicMessageVersion": "vic.header.messageTypes.vicStatsGetRequest.vicMessageVersion-546",
        "VicstatsgetrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicStatsGetRequest.vicMessageFlags.vicZFlag-547",
        "VicstatsgetrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicStatsGetRequest.vicMessageFlags.vicPFlag-548",
        "VicstatsgetrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicStatsGetRequest.vicMessageFlags.vicMFlag-549",
        "VicstatsgetrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicStatsGetRequest.vicMessageFlags.vicRFlag-550",
        "VicStatsGetRequestVicMessageLen": "vic.header.messageTypes.vicStatsGetRequest.vicMessageLen-551",
        "VicStatsGetRequestVicMessageId": "vic.header.messageTypes.vicStatsGetRequest.vicMessageId-552",
        "VicStatsGetRequestVicFragmentId": "vic.header.messageTypes.vicStatsGetRequest.vicFragmentId-553",
        "VicStatsGetRequestVicCompletionCode": "vic.header.messageTypes.vicStatsGetRequest.vicCompletionCode-554",
        "VicStatsGetRequestVicVifIndex": "vic.header.messageTypes.vicStatsGetRequest.vicVifIndex-555",
        "VicStatsTypeVicTLVType": "vic.header.messageTypes.vicStatsGetRequest.vicMandatoryTLVs.vicStatsType.vicTLVType-556",
        "VicStatsTypeVicTLVLength": "vic.header.messageTypes.vicStatsGetRequest.vicMandatoryTLVs.vicStatsType.vicTLVLength-557",
        "VicStatsTypeVicStType": "vic.header.messageTypes.vicStatsGetRequest.vicMandatoryTLVs.vicStatsType.vicStType-558",
        "VicStatsGetResponseVicMessageType": "vic.header.messageTypes.vicStatsGetResponse.vicMessageType-559",
        "VicStatsGetResponseVicMessageVersion": "vic.header.messageTypes.vicStatsGetResponse.vicMessageVersion-560",
        "VicstatsgetresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicStatsGetResponse.vicMessageFlags.vicZFlag-561",
        "VicstatsgetresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicStatsGetResponse.vicMessageFlags.vicPFlag-562",
        "VicstatsgetresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicStatsGetResponse.vicMessageFlags.vicMFlag-563",
        "VicstatsgetresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicStatsGetResponse.vicMessageFlags.vicRFlag-564",
        "VicStatsGetResponseVicMessageLen": "vic.header.messageTypes.vicStatsGetResponse.vicMessageLen-565",
        "VicStatsGetResponseVicMessageId": "vic.header.messageTypes.vicStatsGetResponse.vicMessageId-566",
        "VicStatsGetResponseVicFragmentId": "vic.header.messageTypes.vicStatsGetResponse.vicFragmentId-567",
        "VicStatsGetResponseVicCompletionCode": "vic.header.messageTypes.vicStatsGetResponse.vicCompletionCode-568",
        "VicStatsGetResponseVicVifIndex": "vic.header.messageTypes.vicStatsGetResponse.vicVifIndex-569",
        "VicStatsVicTLVType": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicTLVType-570",
        "VicStatsVicTLVLength": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicTLVLength-571",
        "VicStatsVicSAdapterToSwFramesTot": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSAdapterToSwFramesTot-572",
        "VicStatsVicSAdapterToSwFramesDiscarded": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSAdapterToSwFramesDiscarded-573",
        "VicStatsVicSAdapterToSwFramesDropped": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSAdapterToSwFramesDropped-574",
        "VicStatsVicSAdapterToSwGoodBytesTot": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSAdapterToSwGoodBytesTot-575",
        "VicStatsVicSSwToAdapterFramesTot": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSSwToAdapterFramesTot-576",
        "VicStatsVicSSwToAdapterFramesDiscarded": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSSwToAdapterFramesDiscarded-577",
        "VicStatsVicSSwToAdapterFramesDropped": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSSwToAdapterFramesDropped-578",
        "VicStatsVicSSwToAdapterGoodBytesTot": "vic.header.messageTypes.vicStatsGetResponse.vicMandatoryTLVs.vicStats.vicSSwToAdapterGoodBytesTot-579",
        "VicStatsArrayGetRequestVicMessageType": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageType-580",
        "VicStatsArrayGetRequestVicMessageVersion": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageVersion-581",
        "VicstatsarraygetrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageFlags.vicZFlag-582",
        "VicstatsarraygetrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageFlags.vicPFlag-583",
        "VicstatsarraygetrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageFlags.vicMFlag-584",
        "VicstatsarraygetrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageFlags.vicRFlag-585",
        "VicStatsArrayGetRequestVicMessageLen": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageLen-586",
        "VicStatsArrayGetRequestVicMessageId": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMessageId-587",
        "VicStatsArrayGetRequestVicFragmentId": "vic.header.messageTypes.vicStatsArrayGetRequest.vicFragmentId-588",
        "VicStatsArrayGetRequestVicCompletionCode": "vic.header.messageTypes.vicStatsArrayGetRequest.vicCompletionCode-589",
        "VicStatsArrayGetRequestVicVifIndex": "vic.header.messageTypes.vicStatsArrayGetRequest.vicVifIndex-590",
        "VicmandatorytlvsVicStatsTypeVicTLVType": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMandatoryTLVs.vicStatsType.vicTLVType-591",
        "VicmandatorytlvsVicStatsTypeVicTLVLength": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMandatoryTLVs.vicStatsType.vicTLVLength-592",
        "VicmandatorytlvsVicStatsTypeVicStType": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMandatoryTLVs.vicStatsType.vicStType-593",
        "VicstatsarraygetrequestVicmandatorytlvsVicIndexArrayVicTLVType": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMandatoryTLVs.vicIndexArray.vicTLVType-594",
        "VicstatsarraygetrequestVicmandatorytlvsVicIndexArrayVicTLVLength": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMandatoryTLVs.vicIndexArray.vicTLVLength-595",
        "VicmandatorytlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex": "vic.header.messageTypes.vicStatsArrayGetRequest.vicMandatoryTLVs.vicIndexArray.vicIndexes.vicIndexEntry.vicVifIndex-596",
        "VicStatsArrayGetResponseVicMessageType": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageType-597",
        "VicStatsArrayGetResponseVicMessageVersion": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageVersion-598",
        "VicstatsarraygetresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageFlags.vicZFlag-599",
        "VicstatsarraygetresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageFlags.vicPFlag-600",
        "VicstatsarraygetresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageFlags.vicMFlag-601",
        "VicstatsarraygetresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageFlags.vicRFlag-602",
        "VicStatsArrayGetResponseVicMessageLen": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageLen-603",
        "VicStatsArrayGetResponseVicMessageId": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMessageId-604",
        "VicStatsArrayGetResponseVicFragmentId": "vic.header.messageTypes.vicStatsArrayGetResponse.vicFragmentId-605",
        "VicStatsArrayGetResponseVicCompletionCode": "vic.header.messageTypes.vicStatsArrayGetResponse.vicCompletionCode-606",
        "VicStatsArrayGetResponseVicVifIndex": "vic.header.messageTypes.vicStatsArrayGetResponse.vicVifIndex-607",
        "VicExtendedStatsArrayVicTLVType": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicTLVType-608",
        "VicExtendedStatsArrayVicTLVLength": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicTLVLength-609",
        "VicStatsDataEntryVicVifIndex": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicVifIndex-610",
        "VicStatsDataEntryVicEsaAdapterToSwUnicastFrames": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwUnicastFrames-611",
        "VicStatsDataEntryVicEsaAdapterToSwUnicastBytes": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwUnicastBytes-612",
        "VicStatsDataEntryVicEsaAdapterToSwMulticastFrames": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwMulticastFrames-613",
        "VicStatsDataEntryVicEsaAdapterToSwMulticastBytes": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwMulticastBytes-614",
        "VicStatsDataEntryVicEsaAdapterToSwBroadcastFrames": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwBroadcastFrames-615",
        "VicStatsDataEntryVicEsaAdapterToSwBroadcastBytes": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwBroadcastBytes-616",
        "VicStatsDataEntryVicEsaAdapterToSwFramesDiscarded": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwFramesDiscarded-617",
        "VicStatsDataEntryVicEsaAdapterToSwFramesDropped": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaAdapterToSwFramesDropped-618",
        "VicStatsDataEntryVicEsaSwToAdapterUnicastFrames": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterUnicastFrames-619",
        "VicStatsDataEntryVicEsaSwToAdapterUnicastBytes": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterUnicastBytes-620",
        "VicStatsDataEntryVicEsaSwToAdapterMulticastFrames": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterMulticastFrames-621",
        "VicStatsDataEntryVicEsaSwToAdapterMulticastBytes": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterMulticastBytes-622",
        "VicStatsDataEntryVicEsaSwToAdapterBroadcastFrames": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterBroadcastFrames-623",
        "VicStatsDataEntryVicEsaSwToAdapterBroadcastBytes": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterBroadcastBytes-624",
        "VicStatsDataEntryVicEsaSwToAdapterFramesDiscarded": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterFramesDiscarded-625",
        "VicStatsDataEntryVicEsaSwToAdapterFramesDropped": "vic.header.messageTypes.vicStatsArrayGetResponse.vicMandatoryTLVs.vicExtendedStatsArray.vicStatsData.vicStatsDataEntry.vicEsaSwToAdapterFramesDropped-626",
        "VicProfileAddRequestVicMessageType": "vic.header.messageTypes.vicProfileAddRequest.vicMessageType-627",
        "VicProfileAddRequestVicMessageVersion": "vic.header.messageTypes.vicProfileAddRequest.vicMessageVersion-628",
        "VicprofileaddrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicProfileAddRequest.vicMessageFlags.vicZFlag-629",
        "VicprofileaddrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicProfileAddRequest.vicMessageFlags.vicPFlag-630",
        "VicprofileaddrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicProfileAddRequest.vicMessageFlags.vicMFlag-631",
        "VicprofileaddrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicProfileAddRequest.vicMessageFlags.vicRFlag-632",
        "VicProfileAddRequestVicMessageLen": "vic.header.messageTypes.vicProfileAddRequest.vicMessageLen-633",
        "VicProfileAddRequestVicMessageId": "vic.header.messageTypes.vicProfileAddRequest.vicMessageId-634",
        "VicProfileAddRequestVicFragmentId": "vic.header.messageTypes.vicProfileAddRequest.vicFragmentId-635",
        "VicProfileAddRequestVicCompletionCode": "vic.header.messageTypes.vicProfileAddRequest.vicCompletionCode-636",
        "VicProfileAddRequestVicVifIndex": "vic.header.messageTypes.vicProfileAddRequest.vicVifIndex-637",
        "VicPortProfileNameListVicTLVType": "vic.header.messageTypes.vicProfileAddRequest.vicMandatoryTLVs.vicPortProfileNameList.vicTLVType-638",
        "VicPortProfileNameListVicTLVLength": "vic.header.messageTypes.vicProfileAddRequest.vicMandatoryTLVs.vicPortProfileNameList.vicTLVLength-639",
        "VicPpnlPortProfileNameVicPpnlVariableNameLength": "vic.header.messageTypes.vicProfileAddRequest.vicMandatoryTLVs.vicPortProfileNameList.vicPpnlPortProfileNames.vicPpnlPortProfileName.vicPpnlVariableNameLength-640",
        "VicPpnlPortProfileNameVicPpnlName": "vic.header.messageTypes.vicProfileAddRequest.vicMandatoryTLVs.vicPortProfileNameList.vicPpnlPortProfileNames.vicPpnlPortProfileName.vicPpnlName-641",
        "VicProfileAddResponseVicMessageType": "vic.header.messageTypes.vicProfileAddResponse.vicMessageType-642",
        "VicProfileAddResponseVicMessageVersion": "vic.header.messageTypes.vicProfileAddResponse.vicMessageVersion-643",
        "VicprofileaddresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicProfileAddResponse.vicMessageFlags.vicZFlag-644",
        "VicprofileaddresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicProfileAddResponse.vicMessageFlags.vicPFlag-645",
        "VicprofileaddresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicProfileAddResponse.vicMessageFlags.vicMFlag-646",
        "VicprofileaddresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicProfileAddResponse.vicMessageFlags.vicRFlag-647",
        "VicProfileAddResponseVicMessageLen": "vic.header.messageTypes.vicProfileAddResponse.vicMessageLen-648",
        "VicProfileAddResponseVicMessageId": "vic.header.messageTypes.vicProfileAddResponse.vicMessageId-649",
        "VicProfileAddResponseVicFragmentId": "vic.header.messageTypes.vicProfileAddResponse.vicFragmentId-650",
        "VicProfileAddResponseVicCompletionCode": "vic.header.messageTypes.vicProfileAddResponse.vicCompletionCode-651",
        "VicProfileAddResponseVicVifIndex": "vic.header.messageTypes.vicProfileAddResponse.vicVifIndex-652",
        "VicProfileDeleteRequestVicMessageType": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageType-653",
        "VicProfileDeleteRequestVicMessageVersion": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageVersion-654",
        "VicprofiledeleterequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageFlags.vicZFlag-655",
        "VicprofiledeleterequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageFlags.vicPFlag-656",
        "VicprofiledeleterequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageFlags.vicMFlag-657",
        "VicprofiledeleterequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageFlags.vicRFlag-658",
        "VicProfileDeleteRequestVicMessageLen": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageLen-659",
        "VicProfileDeleteRequestVicMessageId": "vic.header.messageTypes.vicProfileDeleteRequest.vicMessageId-660",
        "VicProfileDeleteRequestVicFragmentId": "vic.header.messageTypes.vicProfileDeleteRequest.vicFragmentId-661",
        "VicProfileDeleteRequestVicCompletionCode": "vic.header.messageTypes.vicProfileDeleteRequest.vicCompletionCode-662",
        "VicProfileDeleteRequestVicVifIndex": "vic.header.messageTypes.vicProfileDeleteRequest.vicVifIndex-663",
        "VicmandatorytlvsVicPortProfileNameListVicTLVType": "vic.header.messageTypes.vicProfileDeleteRequest.vicMandatoryTLVs.vicPortProfileNameList.vicTLVType-664",
        "VicmandatorytlvsVicPortProfileNameListVicTLVLength": "vic.header.messageTypes.vicProfileDeleteRequest.vicMandatoryTLVs.vicPortProfileNameList.vicTLVLength-665",
        "VicppnlportprofilenamesVicPpnlPortProfileNameVicPpnlVariableNameLength": "vic.header.messageTypes.vicProfileDeleteRequest.vicMandatoryTLVs.vicPortProfileNameList.vicPpnlPortProfileNames.vicPpnlPortProfileName.vicPpnlVariableNameLength-666",
        "VicppnlportprofilenamesVicPpnlPortProfileNameVicPpnlName": "vic.header.messageTypes.vicProfileDeleteRequest.vicMandatoryTLVs.vicPortProfileNameList.vicPpnlPortProfileNames.vicPpnlPortProfileName.vicPpnlName-667",
        "VicProfileDeleteResponseVicMessageType": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageType-668",
        "VicProfileDeleteResponseVicMessageVersion": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageVersion-669",
        "VicprofiledeleteresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageFlags.vicZFlag-670",
        "VicprofiledeleteresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageFlags.vicPFlag-671",
        "VicprofiledeleteresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageFlags.vicMFlag-672",
        "VicprofiledeleteresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageFlags.vicRFlag-673",
        "VicProfileDeleteResponseVicMessageLen": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageLen-674",
        "VicProfileDeleteResponseVicMessageId": "vic.header.messageTypes.vicProfileDeleteResponse.vicMessageId-675",
        "VicProfileDeleteResponseVicFragmentId": "vic.header.messageTypes.vicProfileDeleteResponse.vicFragmentId-676",
        "VicProfileDeleteResponseVicCompletionCode": "vic.header.messageTypes.vicProfileDeleteResponse.vicCompletionCode-677",
        "VicProfileDeleteResponseVicVifIndex": "vic.header.messageTypes.vicProfileDeleteResponse.vicVifIndex-678",
        "VicEnumRequestVicMessageType": "vic.header.messageTypes.vicEnumRequest.vicMessageType-679",
        "VicEnumRequestVicMessageVersion": "vic.header.messageTypes.vicEnumRequest.vicMessageVersion-680",
        "VicenumrequestVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicEnumRequest.vicMessageFlags.vicZFlag-681",
        "VicenumrequestVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicEnumRequest.vicMessageFlags.vicPFlag-682",
        "VicenumrequestVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicEnumRequest.vicMessageFlags.vicMFlag-683",
        "VicenumrequestVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicEnumRequest.vicMessageFlags.vicRFlag-684",
        "VicEnumRequestVicMessageLen": "vic.header.messageTypes.vicEnumRequest.vicMessageLen-685",
        "VicEnumRequestVicMessageId": "vic.header.messageTypes.vicEnumRequest.vicMessageId-686",
        "VicEnumRequestVicFragmentId": "vic.header.messageTypes.vicEnumRequest.vicFragmentId-687",
        "VicEnumRequestVicCompletionCode": "vic.header.messageTypes.vicEnumRequest.vicCompletionCode-688",
        "VicEnumRequestVicVifIndex": "vic.header.messageTypes.vicEnumRequest.vicVifIndex-689",
        "VicEnumTypeVicTLVType": "vic.header.messageTypes.vicEnumRequest.vicMandatoryTLVs.vicEnumType.vicTLVType-690",
        "VicEnumTypeVicTLVLength": "vic.header.messageTypes.vicEnumRequest.vicMandatoryTLVs.vicEnumType.vicTLVLength-691",
        "VicEnumTypeVicEtType": "vic.header.messageTypes.vicEnumRequest.vicMandatoryTLVs.vicEnumType.vicEtType-692",
        "VicEnumResponseVicMessageType": "vic.header.messageTypes.vicEnumResponse.vicMessageType-693",
        "VicEnumResponseVicMessageVersion": "vic.header.messageTypes.vicEnumResponse.vicMessageVersion-694",
        "VicenumresponseVicMessageFlagsVicZFlag": "vic.header.messageTypes.vicEnumResponse.vicMessageFlags.vicZFlag-695",
        "VicenumresponseVicMessageFlagsVicPFlag": "vic.header.messageTypes.vicEnumResponse.vicMessageFlags.vicPFlag-696",
        "VicenumresponseVicMessageFlagsVicMFlag": "vic.header.messageTypes.vicEnumResponse.vicMessageFlags.vicMFlag-697",
        "VicenumresponseVicMessageFlagsVicRFlag": "vic.header.messageTypes.vicEnumResponse.vicMessageFlags.vicRFlag-698",
        "VicEnumResponseVicMessageLen": "vic.header.messageTypes.vicEnumResponse.vicMessageLen-699",
        "VicEnumResponseVicMessageId": "vic.header.messageTypes.vicEnumResponse.vicMessageId-700",
        "VicEnumResponseVicFragmentId": "vic.header.messageTypes.vicEnumResponse.vicFragmentId-701",
        "VicEnumResponseVicCompletionCode": "vic.header.messageTypes.vicEnumResponse.vicCompletionCode-702",
        "VicEnumResponseVicVifIndex": "vic.header.messageTypes.vicEnumResponse.vicVifIndex-703",
        "VicenumresponseVicmandatorytlvsVicIndexArrayVicTLVType": "vic.header.messageTypes.vicEnumResponse.vicMandatoryTLVs.vicIndexArray.vicTLVType-704",
        "VicenumresponseVicmandatorytlvsVicIndexArrayVicTLVLength": "vic.header.messageTypes.vicEnumResponse.vicMandatoryTLVs.vicIndexArray.vicTLVLength-705",
        "VicenumresponseVicmandatorytlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex": "vic.header.messageTypes.vicEnumResponse.vicMandatoryTLVs.vicIndexArray.vicIndexes.vicIndexEntry.vicVifIndex-706",
    }

    def __init__(self, parent, list_op=False):
        super(Vic, self).__init__(parent, list_op)

    @property
    def VicPduHeaderVicVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPduHeaderVicVersion"])
        )

    @property
    def VicPduHeaderVicPDULength(self):
        """
        Display Name: PDU Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPduHeaderVicPDULength"])
        )

    @property
    def VicPduHeaderVicPeerMacAddress(self):
        """
        Display Name: VIC Peer MAC Address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPduHeaderVicPeerMacAddress"]),
        )

    @property
    def VicPduHeaderVicReserved(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPduHeaderVicReserved"])
        )

    @property
    def VicOpenRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicMessageType"])
        )

    @property
    def VicOpenRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicMessageVersion"]),
        )

    @property
    def VicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMessageFlagsVicZFlag"])
        )

    @property
    def VicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMessageFlagsVicPFlag"])
        )

    @property
    def VicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMessageFlagsVicMFlag"])
        )

    @property
    def VicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMessageFlagsVicRFlag"])
        )

    @property
    def VicOpenRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicMessageLen"])
        )

    @property
    def VicOpenRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicMessageId"])
        )

    @property
    def VicOpenRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicFragmentId"])
        )

    @property
    def VicOpenRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicCompletionCode"]),
        )

    @property
    def VicOpenRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenRequestVicVifIndex"])
        )

    @property
    def VicControlChannelCapabilityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicControlChannelCapabilityVicTLVType"]
            ),
        )

    @property
    def VicControlChannelCapabilityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicControlChannelCapabilityVicTLVLength"]
            ),
        )

    @property
    def VicControlChannelCapabilityVicCccRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicControlChannelCapabilityVicCccRsvd"]
            ),
        )

    @property
    def VicCccCapabilityFlagsVicCccOFlag(self):
        """
        Display Name: O
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccOFlag"]),
        )

    @property
    def VicCccCapabilityFlagsVicCccRsvdFlags(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccRsvdFlags"]
            ),
        )

    @property
    def VicCccCapabilityFlagsVicCccSFlag(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccSFlag"]),
        )

    @property
    def VicCccCapabilityFlagsVicCccDFlag(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccDFlag"]),
        )

    @property
    def VicCccCapabilityFlagsVicCccVFlag(self):
        """
        Display Name: V
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccVFlag"]),
        )

    @property
    def VicCccCapabilityFlagsVicCccFFlag(self):
        """
        Display Name: F
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccFFlag"]),
        )

    @property
    def VicCccCapabilityFlagsVicCccRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        Available enum values: switch, 1, adapter, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicCccCapabilityFlagsVicCccRFlag"]),
        )

    @property
    def VicControlChannelCapabilityVicCccMaxCredit(self):
        """
        Display Name: Maximum Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicControlChannelCapabilityVicCccMaxCredit"]
            ),
        )

    @property
    def VicControlChannelCapabilityVicCccMaxMessageSize(self):
        """
        Display Name: Maximum Message Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicControlChannelCapabilityVicCccMaxMessageSize"]
            ),
        )

    @property
    def VicMsgTypeArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMsgTypeArrayVicTLVType"])
        )

    @property
    def VicMsgTypeArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMsgTypeArrayVicTLVLength"])
        )

    @property
    def VicMsgTypeEntryVicMsgType(self):
        """
        Display Name: MSG Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicMsgTypeEntryVicMsgType"])
        )

    @property
    def VicMsgTypeEntryVicMsgVersions(self):
        """
        Display Name: MSG Versions
        Default Value: 0
        Value Format: decimal
        Available enum values: 0, 1, 1, 2, 2, 4, 3, 8, 4, 16, 5, 32, 6, 64, 7, 128
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicMsgTypeEntryVicMsgVersions"]),
        )

    @property
    def VicResourceLimitCapabilityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicResourceLimitCapabilityVicTLVType"]
            ),
        )

    @property
    def VicResourceLimitCapabilityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicResourceLimitCapabilityVicTLVLength"]
            ),
        )

    @property
    def VicResourceLimitCapabilityVicRlcTotalVifs(self):
        """
        Display Name: Total Number of VIFs Supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicResourceLimitCapabilityVicRlcTotalVifs"]
            ),
        )

    @property
    def VicResourceLimitCapabilityVicRlcTotalVifLists(self):
        """
        Display Name: Total Number of VIF-Lists Supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicResourceLimitCapabilityVicRlcTotalVifLists"]
            ),
        )

    @property
    def VicResourceLimitCapabilityVicRlcTotalUifs(self):
        """
        Display Name: Total Number of UIFs Supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicResourceLimitCapabilityVicRlcTotalUifs"]
            ),
        )

    @property
    def VicEthernetCapabilityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEthernetCapabilityVicTLVType"]),
        )

    @property
    def VicEthernetCapabilityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEthernetCapabilityVicTLVLength"]),
        )

    @property
    def VicEthernetCapabilityVicEcTotalVifs(self):
        """
        Display Name: Number of Ethernet VIFs Supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicEthernetCapabilityVicEcTotalVifs"]
            ),
        )

    @property
    def VicFcoeCapabilityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicFcoeCapabilityVicTLVType"])
        )

    @property
    def VicFcoeCapabilityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicFcoeCapabilityVicTLVLength"]),
        )

    @property
    def VicFcoeCapabilityVicFcTotalVifs(self):
        """
        Display Name: Number of FCoE VIFs Supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicFcoeCapabilityVicFcTotalVifs"]),
        )

    @property
    def VicOpenResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicMessageType"]),
        )

    @property
    def VicOpenResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicMessageVersion"]),
        )

    @property
    def VicopenresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicopenresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicopenresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicopenresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicopenresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicopenresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicopenresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicopenresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicOpenResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicMessageLen"])
        )

    @property
    def VicOpenResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicMessageId"])
        )

    @property
    def VicOpenResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicFragmentId"])
        )

    @property
    def VicOpenResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicCompletionCode"]),
        )

    @property
    def VicOpenResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicOpenResponseVicVifIndex"])
        )

    @property
    def VicVifCreateRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateRequestVicMessageType"]),
        )

    @property
    def VicVifCreateRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifCreateRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifcreaterequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreaterequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifcreaterequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreaterequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifcreaterequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreaterequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifcreaterequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreaterequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifCreateRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateRequestVicMessageLen"]),
        )

    @property
    def VicVifCreateRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateRequestVicMessageId"]),
        )

    @property
    def VicVifCreateRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateRequestVicFragmentId"]),
        )

    @property
    def VicVifCreateRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifCreateRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifCreateRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateRequestVicVifIndex"]),
        )

    @property
    def VicProvisioningInfoVicTLVType(self):
        """
        Display Name: Type
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProvisioningInfoVicTLVType"]),
        )

    @property
    def VicProvisioningInfoVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProvisioningInfoVicTLVLength"]),
        )

    @property
    def VicPiCiscoTypeSpaceVicPiTypeSpace(self):
        """
        Display Name: Provisioning Information Type Space
        Default Value: 0x00000C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiCiscoTypeSpaceVicPiTypeSpace"]),
        )

    @property
    def VicPiVmwareVicPiType(self):
        """
        Display Name: Provisioning Information Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareVicPiType"])
        )

    @property
    def VicPiVmwareVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareVicTLVLength"])
        )

    @property
    def VicPiVmwareVicPiVmwareNumberOfTlvs(self):
        """
        Display Name: Number of TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareVicPiVmwareNumberOfTlvs"]
            ),
        )

    @property
    def VicPiVmwareProfileNameTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareProfileNameTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareProfileNameTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareProfileNameTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareProfileNameTlvVicVariableProfileNameLength(self):
        """
        Display Name: Variable Profile Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareProfileNameTlvVicVariableProfileNameLength"
                ]
            ),
        )

    @property
    def VicPiVmwareProfileNameTlvVicProfileName(self):
        """
        Display Name: Profile Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareProfileNameTlvVicProfileName"]
            ),
        )

    @property
    def VicPiVmwareClientMacAddrTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientMacAddrTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClientMacAddrTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientMacAddrTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClientMacAddrTlvVicPiVmwareClientMacAddr(self):
        """
        Display Name: Client Mac address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientMacAddrTlvVicPiVmwareClientMacAddr"]
            ),
        )

    @property
    def VicPiVmwareClientNameTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientNameTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClientNameTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientNameTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClientNameTlvVicVariableClientNameLength(self):
        """
        Display Name: Variable Client Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientNameTlvVicVariableClientNameLength"]
            ),
        )

    @property
    def VicPiVmwareClientNameTlvVicClientName(self):
        """
        Display Name: Client Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientNameTlvVicClientName"]
            ),
        )

    @property
    def VicPiVmwarePortIdTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwarePortIdTlvVicTLVType"]),
        )

    @property
    def VicPiVmwarePortIdTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwarePortIdTlvVicTLVLength"]),
        )

    @property
    def VicPiVmwarePortIdTlvVicPiVmwarePortIndex(self):
        """
        Display Name: Port Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwarePortIdTlvVicPiVmwarePortIndex"]
            ),
        )

    @property
    def VicPiVmwareClusterPortUuidTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterPortUuidTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClusterPortUuidTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterPortUuidTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClusterPortUuidTlvVicVariableClusterPortUuidLength(self):
        """
        Display Name: Variable Cluster Port UUID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareClusterPortUuidTlvVicVariableClusterPortUuidLength"
                ]
            ),
        )

    @property
    def VicPiVmwareClusterPortUuidTlvVicClusterPortUuid(self):
        """
        Display Name: Cluster Port UUID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterPortUuidTlvVicClusterPortUuid"]
            ),
        )

    @property
    def VicPiVmwareClusterUuidTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterUuidTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClusterUuidTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterUuidTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClusterUuidTlvVicVariableClusterUuidLength(self):
        """
        Display Name: Variable Cluster UUID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareClusterUuidTlvVicVariableClusterUuidLength"
                ]
            ),
        )

    @property
    def VicPiVmwareClusterUuidTlvVicClusterUuid(self):
        """
        Display Name: Cluster UUID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterUuidTlvVicClusterUuid"]
            ),
        )

    @property
    def VicPiVmwareHostPortSetNameTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHostPortSetNameTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareHostPortSetNameTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHostPortSetNameTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareHostPortSetNameTlvVicVariableHostPortSetNameLength(self):
        """
        Display Name: Variable Host Port-set name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareHostPortSetNameTlvVicVariableHostPortSetNameLength"
                ]
            ),
        )

    @property
    def VicPiVmwareHostPortSetNameTlvVicHostPortSetName(self):
        """
        Display Name: Host Port-set name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHostPortSetNameTlvVicHostPortSetName"]
            ),
        )

    @property
    def VicPiVmwareClusterNameTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterNameTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClusterNameTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterNameTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClusterNameTlvVicVariableClusterNameLength(self):
        """
        Display Name: Variable Cluster name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareClusterNameTlvVicVariableClusterNameLength"
                ]
            ),
        )

    @property
    def VicPiVmwareClusterNameTlvVicClusterName(self):
        """
        Display Name: Cluster name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterNameTlvVicClusterName"]
            ),
        )

    @property
    def VicPiVmwareHostUuidTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareHostUuidTlvVicTLVType"]),
        )

    @property
    def VicPiVmwareHostUuidTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHostUuidTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareHostUuidTlvVicVariableHostUuidLength(self):
        """
        Display Name: Variable Host UUID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHostUuidTlvVicVariableHostUuidLength"]
            ),
        )

    @property
    def VicPiVmwareHostUuidTlvVicHostUuid(self):
        """
        Display Name: Host UUID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareHostUuidTlvVicHostUuid"]),
        )

    @property
    def VicPiVmwareClientUuidTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientUuidTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClientUuidTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientUuidTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClientUuidTlvVicVariableClientUuidLength(self):
        """
        Display Name: Variable Client UUID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientUuidTlvVicVariableClientUuidLength"]
            ),
        )

    @property
    def VicPiVmwareClientUuidTlvVicClientUuid(self):
        """
        Display Name: Client UUID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClientUuidTlvVicClientUuid"]
            ),
        )

    @property
    def VicPiVmwareIncarnationNumberTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareIncarnationNumberTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareIncarnationNumberTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareIncarnationNumberTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareIncarnationNumberTlvVicVariableIncarnationNumberLength(self):
        """
        Display Name: Variable Incarnation Number Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareIncarnationNumberTlvVicVariableIncarnationNumberLength"
                ]
            ),
        )

    @property
    def VicPiVmwareIncarnationNumberTlvVicIncarnationNumber(self):
        """
        Display Name: Incarnation Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareIncarnationNumberTlvVicIncarnationNumber"]
            ),
        )

    @property
    def VicPiVmwareOstypeTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareOstypeTlvVicTLVType"]),
        )

    @property
    def VicPiVmwareOstypeTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareOstypeTlvVicTLVLength"]),
        )

    @property
    def VicPiVmwareOstypeTlvVicPiVmwareOstype(self):
        """
        Display Name: OSType
        Default Value: 1
        Value Format: decimal
        Available enum values: ESX, 1, Linux, 2, Windows, 3, Solaris, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareOstypeTlvVicPiVmwareOstype"]
            ),
        )

    @property
    def VicPiVmwareOsvendorTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiVmwareOsvendorTlvVicTLVType"]),
        )

    @property
    def VicPiVmwareOsvendorTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareOsvendorTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareOsvendorTlvVicPiVmwareOsvendor(self):
        """
        Display Name: OSVendor
        Default Value: 1
        Value Format: decimal
        Available enum values: VMware, 1, RedHat, 2, Microsoft, 3, Oracle, 4, Citrix, 5, Novell, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareOsvendorTlvVicPiVmwareOsvendor"]
            ),
        )

    @property
    def VicPiVmwareHypervisortypeTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHypervisortypeTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareHypervisortypeTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHypervisortypeTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareHypervisortypeTlvVicPiVmwareHypervisortype(self):
        """
        Display Name: HypervisorType
        Default Value: 1
        Value Format: decimal
        Available enum values: ESX, 1, KVM, 2, Hyper-V, 3, Oracle VM, 4, Xen, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareHypervisortypeTlvVicPiVmwareHypervisortype"
                ]
            ),
        )

    @property
    def VicPiVmwareHypervisorvendorTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHypervisorvendorTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareHypervisorvendorTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareHypervisorvendorTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareHypervisorvendorTlvVicPiVmwareHypervisortype(self):
        """
        Display Name: HypervisorVendor
        Default Value: 1
        Value Format: decimal
        Available enum values: VMware, 1, RedHat, 2, Microsoft, 3, Oracle, 4, Citrix, 5, Novell, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareHypervisorvendorTlvVicPiVmwareHypervisortype"
                ]
            ),
        )

    @property
    def VicPiVmwareClienttypeTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClienttypeTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClienttypeTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClienttypeTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClienttypeTlvVicPiVmwareClienttype(self):
        """
        Display Name: ClientType
        Default Value: 1
        Value Format: decimal
        Available enum values: Virtual Machine, 1, Application/Process, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClienttypeTlvVicPiVmwareClienttype"]
            ),
        )

    @property
    def VicPiVmwareManagementPlaneTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareManagementPlaneTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareManagementPlaneTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareManagementPlaneTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareManagementPlaneTlvVicPiVmwareManagementplane(self):
        """
        Display Name: ManagementPlane
        Default Value: 1
        Value Format: decimal
        Available enum values: VMware Virtual Center, 1, RHEV-M, 2, Microsoft SCVMM, 3, Oracle VM, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareManagementPlaneTlvVicPiVmwareManagementplane"
                ]
            ),
        )

    @property
    def VicPiVmwareClusterPortNameTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterPortNameTlvVicTLVType"]
            ),
        )

    @property
    def VicPiVmwareClusterPortNameTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterPortNameTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiVmwareClusterPortNameTlvVicVariableClusterPortNameLength(self):
        """
        Display Name: Variable Cluster Port Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiVmwareClusterPortNameTlvVicVariableClusterPortNameLength"
                ]
            ),
        )

    @property
    def VicPiVmwareClusterPortNameTlvVicClusterPortName(self):
        """
        Display Name: Cluster Port Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiVmwareClusterPortNameTlvVicClusterPortName"]
            ),
        )

    @property
    def VicPiFixedVicPiType(self):
        """
        Display Name: Provisioning Information Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiFixedVicPiType"])
        )

    @property
    def VicPiFixedVicPiFixedVifType(self):
        """
        Display Name: Vif Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Ethernet, 1, FC, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiFixedVicPiFixedVifType"])
        )

    @property
    def VicPiFixedVicPiFixedInstance(self):
        """
        Display Name: Instance
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiFixedVicPiFixedInstance"])
        )

    @property
    def VicPiFixedVicPiFixedNumberOfTlvs(self):
        """
        Display Name: Number of TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiFixedVicPiFixedNumberOfTlvs"]),
        )

    @property
    def VicPiFixedProfileNameTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiFixedProfileNameTlvVicTLVType"]
            ),
        )

    @property
    def VicPiFixedProfileNameTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiFixedProfileNameTlvVicTLVLength"]
            ),
        )

    @property
    def VicPiFixedProfileNameTlvVicVariableProfileNameLength(self):
        """
        Display Name: Variable Profile Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicPiFixedProfileNameTlvVicVariableProfileNameLength"
                ]
            ),
        )

    @property
    def VicPiFixedProfileNameTlvVicProfileName(self):
        """
        Display Name: Profile Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiFixedProfileNameTlvVicProfileName"]
            ),
        )

    @property
    def VicPiFixedVnicUuidTlvVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiFixedVnicUuidTlvVicTLVType"]),
        )

    @property
    def VicPiFixedVnicUuidTlvVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiFixedVnicUuidTlvVicTLVLength"]),
        )

    @property
    def VicPiFixedVnicUuidTlvVicPiFixedVnicUuid(self):
        """
        Display Name: vNic-UUID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiFixedVnicUuidTlvVicPiFixedVnicUuid"]
            ),
        )

    @property
    def VicPiOtherTypeSpaceVicPiTypeSpace(self):
        """
        Display Name: Provisioning Information Type Space
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPiOtherTypeSpaceVicPiTypeSpace"]),
        )

    @property
    def VicPiOtherTypeSpaceVicPiType(self):
        """
        Display Name: Provisioning Information Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiOtherTypeSpaceVicPiType"])
        )

    @property
    def VicPiOtherTypeSpaceVicVariablePiLength(self):
        """
        Display Name: Variable Provisioning Information Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPiOtherTypeSpaceVicVariablePiLength"]
            ),
        )

    @property
    def VicPiOtherTypeSpaceVicPi(self):
        """
        Display Name: Provisioning Information
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPiOtherTypeSpaceVicPi"])
        )

    @property
    def VicVifCreateResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifCreateResponseVicMessageType"]
            ),
        )

    @property
    def VicVifCreateResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifCreateResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifcreateresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreateresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifcreateresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreateresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifcreateresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreateresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifcreateresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifcreateresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifCreateResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateResponseVicMessageLen"]),
        )

    @property
    def VicVifCreateResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateResponseVicMessageId"]),
        )

    @property
    def VicVifCreateResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateResponseVicFragmentId"]),
        )

    @property
    def VicVifCreateResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifCreateResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifCreateResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifCreateResponseVicVifIndex"]),
        )

    @property
    def VicPriorityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPriorityVicTLVType"])
        )

    @property
    def VicPriorityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPriorityVicTLVLength"])
        )

    @property
    def VicPriorityVicPValue(self):
        """
        Display Name: Priority Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicPriorityVicPValue"])
        )

    @property
    def VicVifDeleteRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteRequestVicMessageType"]),
        )

    @property
    def VicVifDeleteRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeleteRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifdeleterequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleterequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifdeleterequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleterequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifdeleterequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleterequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifdeleterequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleterequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDeleteRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteRequestVicMessageLen"]),
        )

    @property
    def VicVifDeleteRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteRequestVicMessageId"]),
        )

    @property
    def VicVifDeleteRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteRequestVicFragmentId"]),
        )

    @property
    def VicVifDeleteRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeleteRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifDeleteRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteRequestVicVifIndex"]),
        )

    @property
    def VicVifDeleteResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeleteResponseVicMessageType"]
            ),
        )

    @property
    def VicVifDeleteResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeleteResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifdeleteresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleteresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifdeleteresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleteresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifdeleteresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleteresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifdeleteresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeleteresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDeleteResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteResponseVicMessageLen"]),
        )

    @property
    def VicVifDeleteResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteResponseVicMessageId"]),
        )

    @property
    def VicVifDeleteResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteResponseVicFragmentId"]),
        )

    @property
    def VicVifDeleteResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeleteResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifDeleteResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDeleteResponseVicVifIndex"]),
        )

    @property
    def VicVifEnableRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableRequestVicMessageType"]),
        )

    @property
    def VicVifEnableRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifEnableRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifenablerequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenablerequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifenablerequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenablerequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifenablerequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenablerequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifenablerequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenablerequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifEnableRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableRequestVicMessageLen"]),
        )

    @property
    def VicVifEnableRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableRequestVicMessageId"]),
        )

    @property
    def VicVifEnableRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableRequestVicFragmentId"]),
        )

    @property
    def VicVifEnableRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifEnableRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifEnableRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableRequestVicVifIndex"]),
        )

    @property
    def VicVifStateVicTLVType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicTLVType"])
        )

    @property
    def VicVifStateVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicTLVLength"])
        )

    @property
    def VicVifStateVicVsRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicVsRsvd"])
        )

    @property
    def VicVifStateVicVsSFlag(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        Available enum values: STANDBY, 1, no STANDBY, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicVsSFlag"])
        )

    @property
    def VicVifStateVicVsPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        Available enum values: PAUSE, 1, UN-PAUSE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicVsPFlag"])
        )

    @property
    def VicVifStateVicVsDFlag(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: decimal
        Available enum values: DOWN, 0, going DOWN, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicVsDFlag"])
        )

    @property
    def VicVifStateVicVsEFlag(self):
        """
        Display Name: E
        Default Value: 1
        Value Format: decimal
        Available enum values: ENABLED, 1, not ENABLED, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifStateVicVsEFlag"])
        )

    @property
    def VicAddressArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicAddressArrayVicTLVType"])
        )

    @property
    def VicAddressArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicAddressArrayVicTLVLength"])
        )

    @property
    def VicAddressEntryVicAddressType(self):
        """
        Display Name: Address-Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Ethernet MAC address, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicAddressEntryVicAddressType"]),
        )

    @property
    def VicAddressEntryVicAddressLen(self):
        """
        Display Name: Address-Len
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicAddressEntryVicAddressLen"])
        )

    @property
    def VicAddressValueVicAddressVlan(self):
        """
        Display Name: VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicAddressValueVicAddressVlan"]),
        )

    @property
    def VicAddressValueVicAddressMac(self):
        """
        Display Name: MAC address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicAddressValueVicAddressMac"])
        )

    @property
    def VicVifIdVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifIdVicTLVType"])
        )

    @property
    def VicVifIdVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifIdVicTLVLength"])
        )

    @property
    def VicVifIdVicViRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifIdVicViRsvd"])
        )

    @property
    def VicVifIdVicViValueInVntag(self):
        """
        Display Name: VIF-ID Value in the VN-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifIdVicViValueInVntag"])
        )

    @property
    def VicVifEnableResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifEnableResponseVicMessageType"]
            ),
        )

    @property
    def VicVifEnableResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifEnableResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifenableresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenableresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifenableresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenableresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifenableresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenableresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifenableresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifenableresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifEnableResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableResponseVicMessageLen"]),
        )

    @property
    def VicVifEnableResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableResponseVicMessageId"]),
        )

    @property
    def VicVifEnableResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableResponseVicFragmentId"]),
        )

    @property
    def VicVifEnableResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifEnableResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifEnableResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifEnableResponseVicVifIndex"]),
        )

    @property
    def VicVifDisableRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableRequestVicMessageType"]
            ),
        )

    @property
    def VicVifDisableRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifdisablerequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisablerequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifdisablerequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisablerequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifdisablerequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisablerequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifdisablerequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisablerequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDisableRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDisableRequestVicMessageLen"]),
        )

    @property
    def VicVifDisableRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDisableRequestVicMessageId"]),
        )

    @property
    def VicVifDisableRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDisableRequestVicFragmentId"]),
        )

    @property
    def VicVifDisableRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifDisableRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDisableRequestVicVifIndex"]),
        )

    @property
    def VicVifDisableResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableResponseVicMessageType"]
            ),
        )

    @property
    def VicVifDisableResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifdisableresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisableresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifdisableresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisableresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifdisableresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisableresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifdisableresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdisableresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDisableResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifDisableResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDisableResponseVicMessageId"]),
        )

    @property
    def VicVifDisableResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifDisableResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDisableResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifDisableResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifDisableResponseVicVifIndex"]),
        )

    @property
    def VicVifSetRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicMessageType"]),
        )

    @property
    def VicVifSetRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicMessageVersion"]),
        )

    @property
    def VicvifsetrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifsetrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifsetrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifsetrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifSetRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicMessageLen"]),
        )

    @property
    def VicVifSetRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicMessageId"])
        )

    @property
    def VicVifSetRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicFragmentId"]),
        )

    @property
    def VicVifSetRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicCompletionCode"]),
        )

    @property
    def VicVifSetRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifSetRequestVicVifIndex"])
        )

    @property
    def VicmandatorytlvsVicVifIdVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifIdVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifIdVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifIdVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifIdVicViRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicmandatorytlvsVicVifIdVicViRsvd"]),
        )

    @property
    def VicmandatorytlvsVicVifIdVicViValueInVntag(self):
        """
        Display Name: VIF-ID Value in the VN-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifIdVicViValueInVntag"]
            ),
        )

    @property
    def VicVlanVicTLVType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVlanVicTLVType"])
        )

    @property
    def VicVlanVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVlanVicTLVLength"])
        )

    @property
    def VicVlanVicVRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVlanVicVRsvd"])
        )

    @property
    def VicVlanVicVMode(self):
        """
        Display Name: Mode
        Default Value: 0
        Value Format: decimal
        Available enum values: Trunk, 0, Access, 1, Trunk tag-native VLAN, 2, Reserved for later use, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVlanVicVMode"])
        )

    @property
    def VicVlanVicVValue(self):
        """
        Display Name: VLAN Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVlanVicVValue"])
        )

    @property
    def VicmandatorytlvsVicVifStateVicTLVType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifStateVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifStateVicVsRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicVsRsvd"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifStateVicVsSFlag(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        Available enum values: STANDBY, 1, no STANDBY, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicVsSFlag"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifStateVicVsPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        Available enum values: PAUSE, 1, UN-PAUSE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicVsPFlag"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifStateVicVsDFlag(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: decimal
        Available enum values: DOWN, 0, going DOWN, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicVsDFlag"]
            ),
        )

    @property
    def VicmandatorytlvsVicVifStateVicVsEFlag(self):
        """
        Display Name: E
        Default Value: 0
        Value Format: decimal
        Available enum values: ENABLED, 1, not ENABLED, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVifStateVicVsEFlag"]
            ),
        )

    @property
    def VicmandatorytlvsVicPriorityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicPriorityVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicPriorityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicPriorityVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicPriorityVicPValue(self):
        """
        Display Name: Priority Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicPriorityVicPValue"]
            ),
        )

    @property
    def VicDefaultCosVicTLVType(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicDefaultCosVicTLVType"])
        )

    @property
    def VicDefaultCosVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicDefaultCosVicTLVLength"])
        )

    @property
    def VicDefaultCosVicDcRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicDefaultCosVicDcRsvd"])
        )

    @property
    def VicDefaultCosVicDc(self):
        """
        Display Name: Default COS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicDefaultCosVicDc"])
        )

    @property
    def VicCosFilterVicTLVType(self):
        """
        Display Name: Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicCosFilterVicTLVType"])
        )

    @property
    def VicCosFilterVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicCosFilterVicTLVLength"])
        )

    @property
    def VicCosFilterVicCfMap(self):
        """
        Display Name: Filter-CoS-Map
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicCosFilterVicCfMap"])
        )

    @property
    def VicRateLimitVicTLVType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicRateLimitVicTLVType"])
        )

    @property
    def VicRateLimitVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicRateLimitVicTLVLength"])
        )

    @property
    def VicRateLimitVicRlRate(self):
        """
        Display Name: Rate
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicRateLimitVicRlRate"])
        )

    @property
    def VicRateLimitVicBurstSize(self):
        """
        Display Name: Burst Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicRateLimitVicBurstSize"])
        )

    @property
    def VicVifSetResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetResponseVicMessageType"]),
        )

    @property
    def VicVifSetResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifSetResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifsetresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifsetresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifsetresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifsetresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifSetResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetResponseVicMessageLen"]),
        )

    @property
    def VicVifSetResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetResponseVicMessageId"]),
        )

    @property
    def VicVifSetResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifSetResponseVicFragmentId"]),
        )

    @property
    def VicVifSetResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifSetResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifSetResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifSetResponseVicVifIndex"])
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifIdVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetresponseVicmandatorytlvsVicVifIdVicTLVType"]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifIdVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifIdVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifIdVicViRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifsetresponseVicmandatorytlvsVicVifIdVicViRsvd"]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifIdVicViValueInVntag(self):
        """
        Display Name: VIF-ID Value in the VN-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifIdVicViValueInVntag"
                ]
            ),
        )

    @property
    def VicmandatorytlvsVicVlanVicTLVType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicmandatorytlvsVicVlanVicTLVType"]),
        )

    @property
    def VicmandatorytlvsVicVlanVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicVlanVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicVlanVicVRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicmandatorytlvsVicVlanVicVRsvd"]),
        )

    @property
    def VicmandatorytlvsVicVlanVicVMode(self):
        """
        Display Name: Mode
        Default Value: 0
        Value Format: decimal
        Available enum values: Trunk, 0, Access, 1, Trunk tag-native VLAN, 2, Reserved for later use, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicmandatorytlvsVicVlanVicVMode"]),
        )

    @property
    def VicmandatorytlvsVicVlanVicVValue(self):
        """
        Display Name: VLAN Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicmandatorytlvsVicVlanVicVValue"]),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicTLVType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicTLVType"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicVsRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsRsvd"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicVsSFlag(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        Available enum values: STANDBY, 1, no STANDBY, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsSFlag"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicVsPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        Available enum values: PAUSE, 1, UN-PAUSE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsPFlag"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicVsDFlag(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: decimal
        Available enum values: DOWN, 0, going DOWN, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsDFlag"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicVifStateVicVsEFlag(self):
        """
        Display Name: E
        Default Value: 0
        Value Format: decimal
        Available enum values: ENABLED, 1, not ENABLED, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicVifStateVicVsEFlag"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicPriorityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicPriorityVicTLVType"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicPriorityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicPriorityVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifsetresponseVicmandatorytlvsVicPriorityVicPValue(self):
        """
        Display Name: Priority Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifsetresponseVicmandatorytlvsVicPriorityVicPValue"
                ]
            ),
        )

    @property
    def VicmandatorytlvsVicDefaultCosVicTLVType(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicDefaultCosVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicDefaultCosVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicDefaultCosVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicDefaultCosVicDcRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicDefaultCosVicDcRsvd"]
            ),
        )

    @property
    def VicmandatorytlvsVicDefaultCosVicDc(self):
        """
        Display Name: Default COS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicDefaultCosVicDc"]
            ),
        )

    @property
    def VicmandatorytlvsVicCosFilterVicTLVType(self):
        """
        Display Name: Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicCosFilterVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicCosFilterVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicCosFilterVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicCosFilterVicCfMap(self):
        """
        Display Name: Filter-CoS-Map
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicCosFilterVicCfMap"]
            ),
        )

    @property
    def VicmandatorytlvsVicRateLimitVicTLVType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicRateLimitVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicRateLimitVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicRateLimitVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicRateLimitVicRlRate(self):
        """
        Display Name: Rate
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicRateLimitVicRlRate"]
            ),
        )

    @property
    def VicmandatorytlvsVicRateLimitVicBurstSize(self):
        """
        Display Name: Burst Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicRateLimitVicBurstSize"]
            ),
        )

    @property
    def VicVifGetRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicMessageType"]),
        )

    @property
    def VicVifGetRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicMessageVersion"]),
        )

    @property
    def VicvifgetrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifgetrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifgetrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifgetrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifGetRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicMessageLen"]),
        )

    @property
    def VicVifGetRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicMessageId"])
        )

    @property
    def VicVifGetRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicFragmentId"]),
        )

    @property
    def VicVifGetRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicCompletionCode"]),
        )

    @property
    def VicVifGetRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifGetRequestVicVifIndex"])
        )

    @property
    def VicVifGetResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetResponseVicMessageType"]),
        )

    @property
    def VicVifGetResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifGetResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifgetresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifgetresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifgetresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifgetresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifGetResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetResponseVicMessageLen"]),
        )

    @property
    def VicVifGetResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetResponseVicMessageId"]),
        )

    @property
    def VicVifGetResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifGetResponseVicFragmentId"]),
        )

    @property
    def VicVifGetResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifGetResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifGetResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicVifGetResponseVicVifIndex"])
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifIdVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicVifIdVicTLVType"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifIdVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifIdVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifIdVicViRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicVifIdVicViRsvd"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifIdVicViValueInVntag(self):
        """
        Display Name: VIF-ID Value in the VN-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifIdVicViValueInVntag"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVlanVicTLVType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicVlanVicTLVType"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVlanVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVlanVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVlanVicVRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicVlanVicVRsvd"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVlanVicVMode(self):
        """
        Display Name: Mode
        Default Value: 0
        Value Format: decimal
        Available enum values: Trunk, 0, Access, 1, Trunk tag-native VLAN, 2, Reserved for later use, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicVlanVicVMode"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVlanVicVValue(self):
        """
        Display Name: VLAN Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicVlanVicVValue"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicTLVType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicTLVType"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicVsRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsRsvd"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicVsSFlag(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        Available enum values: STANDBY, 1, no STANDBY, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsSFlag"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicVsPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        Available enum values: PAUSE, 1, UN-PAUSE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsPFlag"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicVsDFlag(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: decimal
        Available enum values: DOWN, 0, going DOWN, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsDFlag"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicVifStateVicVsEFlag(self):
        """
        Display Name: E
        Default Value: 0
        Value Format: decimal
        Available enum values: ENABLED, 1, not ENABLED, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicVifStateVicVsEFlag"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicPriorityVicTLVType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicPriorityVicTLVType"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicPriorityVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicPriorityVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicPriorityVicPValue(self):
        """
        Display Name: Priority Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicPriorityVicPValue"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicDefaultCosVicTLVType(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicTLVType"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicDefaultCosVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicDefaultCosVicDcRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicDefaultCosVicDcRsvd"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicDefaultCosVicDc(self):
        """
        Display Name: Default COS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifgetresponseVicmandatorytlvsVicDefaultCosVicDc"]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicCosFilterVicTLVType(self):
        """
        Display Name: Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicCosFilterVicTLVType"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicCosFilterVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicCosFilterVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicCosFilterVicCfMap(self):
        """
        Display Name: Filter-CoS-Map
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicCosFilterVicCfMap"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicRateLimitVicTLVType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicRateLimitVicTLVType"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicRateLimitVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicRateLimitVicTLVLength"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicRateLimitVicRlRate(self):
        """
        Display Name: Rate
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicRateLimitVicRlRate"
                ]
            ),
        )

    @property
    def VicvifgetresponseVicmandatorytlvsVicRateLimitVicBurstSize(self):
        """
        Display Name: Burst Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifgetresponseVicmandatorytlvsVicRateLimitVicBurstSize"
                ]
            ),
        )

    @property
    def VicVifListSetRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetRequestVicMessageType"]
            ),
        )

    @property
    def VicVifListSetRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetRequestVicMessageVersion"]
            ),
        )

    @property
    def VicviflistsetrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicviflistsetrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicviflistsetrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicviflistsetrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifListSetRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListSetRequestVicMessageLen"]),
        )

    @property
    def VicVifListSetRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListSetRequestVicMessageId"]),
        )

    @property
    def VicVifListSetRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListSetRequestVicFragmentId"]),
        )

    @property
    def VicVifListSetRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifListSetRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListSetRequestVicVifIndex"]),
        )

    @property
    def VicviflistsetrequestVicmandatorytlvsVicVifIdVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistsetrequestVicmandatorytlvsVicVifIdVicTLVType"
                ]
            ),
        )

    @property
    def VicviflistsetrequestVicmandatorytlvsVicVifIdVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistsetrequestVicmandatorytlvsVicVifIdVicTLVLength"
                ]
            ),
        )

    @property
    def VicviflistsetrequestVicmandatorytlvsVicVifIdVicViRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistsetrequestVicmandatorytlvsVicVifIdVicViRsvd"
                ]
            ),
        )

    @property
    def VicviflistsetrequestVicmandatorytlvsVicVifIdVicViValueInVntag(self):
        """
        Display Name: VIF-ID Value in the VN-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistsetrequestVicmandatorytlvsVicVifIdVicViValueInVntag"
                ]
            ),
        )

    @property
    def VicIndexArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicIndexArrayVicTLVType"])
        )

    @property
    def VicIndexArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicIndexArrayVicTLVLength"])
        )

    @property
    def VicIndexEntryVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicIndexEntryVicVifIndex"])
        )

    @property
    def VicVifListSetResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetResponseVicMessageType"]
            ),
        )

    @property
    def VicVifListSetResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetResponseVicMessageVersion"]
            ),
        )

    @property
    def VicviflistsetresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicviflistsetresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicviflistsetresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicviflistsetresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistsetresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifListSetResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifListSetResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListSetResponseVicMessageId"]),
        )

    @property
    def VicVifListSetResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifListSetResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListSetResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifListSetResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListSetResponseVicVifIndex"]),
        )

    @property
    def VicVifListGetRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetRequestVicMessageType"]
            ),
        )

    @property
    def VicVifListGetRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetRequestVicMessageVersion"]
            ),
        )

    @property
    def VicviflistgetrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicviflistgetrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicviflistgetrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicviflistgetrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifListGetRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListGetRequestVicMessageLen"]),
        )

    @property
    def VicVifListGetRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListGetRequestVicMessageId"]),
        )

    @property
    def VicVifListGetRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListGetRequestVicFragmentId"]),
        )

    @property
    def VicVifListGetRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifListGetRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListGetRequestVicVifIndex"]),
        )

    @property
    def VicVifListGetResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetResponseVicMessageType"]
            ),
        )

    @property
    def VicVifListGetResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetResponseVicMessageVersion"]
            ),
        )

    @property
    def VicviflistgetresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicviflistgetresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicviflistgetresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicviflistgetresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicviflistgetresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifListGetResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifListGetResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListGetResponseVicMessageId"]),
        )

    @property
    def VicVifListGetResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifListGetResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifListGetResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifListGetResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifListGetResponseVicVifIndex"]),
        )

    @property
    def VicviflistgetresponseVicmandatorytlvsVicVifIdVicTLVType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistgetresponseVicmandatorytlvsVicVifIdVicTLVType"
                ]
            ),
        )

    @property
    def VicviflistgetresponseVicmandatorytlvsVicVifIdVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistgetresponseVicmandatorytlvsVicVifIdVicTLVLength"
                ]
            ),
        )

    @property
    def VicviflistgetresponseVicmandatorytlvsVicVifIdVicViRsvd(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistgetresponseVicmandatorytlvsVicVifIdVicViRsvd"
                ]
            ),
        )

    @property
    def VicviflistgetresponseVicmandatorytlvsVicVifIdVicViValueInVntag(self):
        """
        Display Name: VIF-ID Value in the VN-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicviflistgetresponseVicmandatorytlvsVicVifIdVicViValueInVntag"
                ]
            ),
        )

    @property
    def VicmandatorytlvsVicIndexArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicIndexArrayVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicIndexArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicIndexArrayVicTLVLength"]
            ),
        )

    @property
    def VicindexesVicIndexEntryVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicindexesVicIndexEntryVicVifIndex"]
            ),
        )

    @property
    def VicVifRegisterRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterRequestVicMessageType"]
            ),
        )

    @property
    def VicVifRegisterRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifregisterrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifregisterrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifregisterrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifregisterrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifRegisterRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterRequestVicMessageLen"]
            ),
        )

    @property
    def VicVifRegisterRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifRegisterRequestVicMessageId"]),
        )

    @property
    def VicVifRegisterRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterRequestVicFragmentId"]
            ),
        )

    @property
    def VicVifRegisterRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifRegisterRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifRegisterRequestVicVifIndex"]),
        )

    @property
    def VicoptionaltlvsVicAddressArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicoptionaltlvsVicAddressArrayVicTLVType"]
            ),
        )

    @property
    def VicoptionaltlvsVicAddressArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicoptionaltlvsVicAddressArrayVicTLVLength"]
            ),
        )

    @property
    def VicaddressesVicAddressEntryVicAddressType(self):
        """
        Display Name: Address-Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Ethernet MAC address, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicaddressesVicAddressEntryVicAddressType"]
            ),
        )

    @property
    def VicaddressesVicAddressEntryVicAddressLen(self):
        """
        Display Name: Address-Len
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicaddressesVicAddressEntryVicAddressLen"]
            ),
        )

    @property
    def VicaddressentryVicAddressValueVicAddressVlan(self):
        """
        Display Name: VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicaddressentryVicAddressValueVicAddressVlan"]
            ),
        )

    @property
    def VicaddressentryVicAddressValueVicAddressMac(self):
        """
        Display Name: MAC address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicaddressentryVicAddressValueVicAddressMac"]
            ),
        )

    @property
    def VicVifRegisterResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterResponseVicMessageType"]
            ),
        )

    @property
    def VicVifRegisterResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifregisterresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifregisterresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifregisterresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifregisterresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifregisterresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifRegisterResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifRegisterResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterResponseVicMessageId"]
            ),
        )

    @property
    def VicVifRegisterResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifRegisterResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifRegisterResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifRegisterResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifRegisterResponseVicVifIndex"]),
        )

    @property
    def VicVifDeregisterRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicMessageType"]
            ),
        )

    @property
    def VicVifDeregisterRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifderegisterrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifderegisterrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifderegisterrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifderegisterrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDeregisterRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicMessageLen"]
            ),
        )

    @property
    def VicVifDeregisterRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicMessageId"]
            ),
        )

    @property
    def VicVifDeregisterRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicFragmentId"]
            ),
        )

    @property
    def VicVifDeregisterRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifDeregisterRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterRequestVicVifIndex"]
            ),
        )

    @property
    def VicvifderegisterrequestVicoptionaltlvsVicAddressArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifderegisterrequestVicoptionaltlvsVicAddressArrayVicTLVType"
                ]
            ),
        )

    @property
    def VicvifderegisterrequestVicoptionaltlvsVicAddressArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifderegisterrequestVicoptionaltlvsVicAddressArrayVicTLVLength"
                ]
            ),
        )

    @property
    def VicaddressarrayVicaddressesVicAddressEntryVicAddressType(self):
        """
        Display Name: Address-Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Ethernet MAC address, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicaddressarrayVicaddressesVicAddressEntryVicAddressType"
                ]
            ),
        )

    @property
    def VicaddressarrayVicaddressesVicAddressEntryVicAddressLen(self):
        """
        Display Name: Address-Len
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicaddressarrayVicaddressesVicAddressEntryVicAddressLen"
                ]
            ),
        )

    @property
    def VicaddressesVicaddressentryVicAddressValueVicAddressVlan(self):
        """
        Display Name: VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicaddressesVicaddressentryVicAddressValueVicAddressVlan"
                ]
            ),
        )

    @property
    def VicaddressesVicaddressentryVicAddressValueVicAddressMac(self):
        """
        Display Name: MAC address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicaddressesVicaddressentryVicAddressValueVicAddressMac"
                ]
            ),
        )

    @property
    def VicVifDeregisterResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicMessageType"]
            ),
        )

    @property
    def VicVifDeregisterResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifderegisterresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifderegisterresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifderegisterresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifderegisterresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifderegisterresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDeregisterResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifDeregisterResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicMessageId"]
            ),
        )

    @property
    def VicVifDeregisterResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifDeregisterResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifDeregisterResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeregisterResponseVicVifIndex"]
            ),
        )

    @property
    def VicVifActivateRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateRequestVicMessageType"]
            ),
        )

    @property
    def VicVifActivateRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifactivaterequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivaterequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifactivaterequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivaterequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifactivaterequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivaterequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifactivaterequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivaterequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifActivateRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateRequestVicMessageLen"]
            ),
        )

    @property
    def VicVifActivateRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifActivateRequestVicMessageId"]),
        )

    @property
    def VicVifActivateRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateRequestVicFragmentId"]
            ),
        )

    @property
    def VicVifActivateRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifActivateRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifActivateRequestVicVifIndex"]),
        )

    @property
    def VicoptionaltlvsVicIndexArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicoptionaltlvsVicIndexArrayVicTLVType"]
            ),
        )

    @property
    def VicoptionaltlvsVicIndexArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicoptionaltlvsVicIndexArrayVicTLVLength"]
            ),
        )

    @property
    def VicindexarrayVicindexesVicIndexEntryVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicindexarrayVicindexesVicIndexEntryVicVifIndex"]
            ),
        )

    @property
    def VicVifActivateResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateResponseVicMessageType"]
            ),
        )

    @property
    def VicVifActivateResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifactivateresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivateresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifactivateresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivateresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifactivateresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivateresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifactivateresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifactivateresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifActivateResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifActivateResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateResponseVicMessageId"]
            ),
        )

    @property
    def VicVifActivateResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifActivateResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifActivateResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifActivateResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicVifActivateResponseVicVifIndex"]),
        )

    @property
    def VicVifDeactivateRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicMessageType"]
            ),
        )

    @property
    def VicVifDeactivateRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicMessageVersion"]
            ),
        )

    @property
    def VicvifdeactivaterequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivaterequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifdeactivaterequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivaterequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifdeactivaterequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivaterequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifdeactivaterequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivaterequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDeactivateRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicMessageLen"]
            ),
        )

    @property
    def VicVifDeactivateRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicMessageId"]
            ),
        )

    @property
    def VicVifDeactivateRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicFragmentId"]
            ),
        )

    @property
    def VicVifDeactivateRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicCompletionCode"]
            ),
        )

    @property
    def VicVifDeactivateRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateRequestVicVifIndex"]
            ),
        )

    @property
    def VicvifdeactivaterequestVicoptionaltlvsVicIndexArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifdeactivaterequestVicoptionaltlvsVicIndexArrayVicTLVType"
                ]
            ),
        )

    @property
    def VicvifdeactivaterequestVicoptionaltlvsVicIndexArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicvifdeactivaterequestVicoptionaltlvsVicIndexArrayVicTLVLength"
                ]
            ),
        )

    @property
    def VicoptionaltlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicoptionaltlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex"
                ]
            ),
        )

    @property
    def VicVifDeactivateResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicMessageType"]
            ),
        )

    @property
    def VicVifDeactivateResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicMessageVersion"]
            ),
        )

    @property
    def VicvifdeactivateresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivateresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicvifdeactivateresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivateresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicvifdeactivateresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivateresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicvifdeactivateresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicvifdeactivateresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicVifDeactivateResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicMessageLen"]
            ),
        )

    @property
    def VicVifDeactivateResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicMessageId"]
            ),
        )

    @property
    def VicVifDeactivateResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicFragmentId"]
            ),
        )

    @property
    def VicVifDeactivateResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicCompletionCode"]
            ),
        )

    @property
    def VicVifDeactivateResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicVifDeactivateResponseVicVifIndex"]
            ),
        )

    @property
    def VicStatsGetRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetRequestVicMessageType"]),
        )

    @property
    def VicStatsGetRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsGetRequestVicMessageVersion"]
            ),
        )

    @property
    def VicstatsgetrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicstatsgetrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicstatsgetrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicstatsgetrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicStatsGetRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetRequestVicMessageLen"]),
        )

    @property
    def VicStatsGetRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetRequestVicMessageId"]),
        )

    @property
    def VicStatsGetRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetRequestVicFragmentId"]),
        )

    @property
    def VicStatsGetRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsGetRequestVicCompletionCode"]
            ),
        )

    @property
    def VicStatsGetRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetRequestVicVifIndex"]),
        )

    @property
    def VicStatsTypeVicTLVType(self):
        """
        Display Name: Type
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicStatsTypeVicTLVType"])
        )

    @property
    def VicStatsTypeVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicStatsTypeVicTLVLength"])
        )

    @property
    def VicStatsTypeVicStType(self):
        """
        Display Name: Type of the statistics request
        Default Value: 1
        Value Format: decimal
        Available enum values: Instantaneous Statistics of VIFs, 1, Instantaneous Statistics of UIFs, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicStatsTypeVicStType"])
        )

    @property
    def VicStatsGetResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetResponseVicMessageType"]),
        )

    @property
    def VicStatsGetResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsGetResponseVicMessageVersion"]
            ),
        )

    @property
    def VicstatsgetresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicstatsgetresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicstatsgetresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicstatsgetresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsgetresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicStatsGetResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetResponseVicMessageLen"]),
        )

    @property
    def VicStatsGetResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetResponseVicMessageId"]),
        )

    @property
    def VicStatsGetResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetResponseVicFragmentId"]),
        )

    @property
    def VicStatsGetResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsGetResponseVicCompletionCode"]
            ),
        )

    @property
    def VicStatsGetResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsGetResponseVicVifIndex"]),
        )

    @property
    def VicStatsVicTLVType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicStatsVicTLVType"])
        )

    @property
    def VicStatsVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicStatsVicTLVLength"])
        )

    @property
    def VicStatsVicSAdapterToSwFramesTot(self):
        """
        Display Name: Adapter-to-Switch Frames Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsVicSAdapterToSwFramesTot"]),
        )

    @property
    def VicStatsVicSAdapterToSwFramesDiscarded(self):
        """
        Display Name: Adapter-to-Switch Frames Discarded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsVicSAdapterToSwFramesDiscarded"]
            ),
        )

    @property
    def VicStatsVicSAdapterToSwFramesDropped(self):
        """
        Display Name: Adapter-to-Switch Frames Dropped
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsVicSAdapterToSwFramesDropped"]
            ),
        )

    @property
    def VicStatsVicSAdapterToSwGoodBytesTot(self):
        """
        Display Name: Adapter-to-Switch Good Bytes Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsVicSAdapterToSwGoodBytesTot"]
            ),
        )

    @property
    def VicStatsVicSSwToAdapterFramesTot(self):
        """
        Display Name: Switch-to-Adapter Frames Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicStatsVicSSwToAdapterFramesTot"]),
        )

    @property
    def VicStatsVicSSwToAdapterFramesDiscarded(self):
        """
        Display Name: Switch-to-Adapter Frames Discarded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsVicSSwToAdapterFramesDiscarded"]
            ),
        )

    @property
    def VicStatsVicSSwToAdapterFramesDropped(self):
        """
        Display Name: Switch-to-Adapter Frames Dropped
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsVicSSwToAdapterFramesDropped"]
            ),
        )

    @property
    def VicStatsVicSSwToAdapterGoodBytesTot(self):
        """
        Display Name: Switch-to-Adapter Good Bytes Total
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsVicSSwToAdapterGoodBytesTot"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 23
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicMessageType"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicMessageVersion"]
            ),
        )

    @property
    def VicstatsarraygetrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicstatsarraygetrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicstatsarraygetrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicstatsarraygetrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicMessageLen"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicMessageId"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicFragmentId"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicCompletionCode"]
            ),
        )

    @property
    def VicStatsArrayGetRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetRequestVicVifIndex"]
            ),
        )

    @property
    def VicmandatorytlvsVicStatsTypeVicTLVType(self):
        """
        Display Name: Type
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicStatsTypeVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicStatsTypeVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicStatsTypeVicTLVLength"]
            ),
        )

    @property
    def VicmandatorytlvsVicStatsTypeVicStType(self):
        """
        Display Name: Type of the statistics request
        Default Value: 1
        Value Format: decimal
        Available enum values: Instantaneous Statistics of VIFs, 1, Instantaneous Statistics of UIFs, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicStatsTypeVicStType"]
            ),
        )

    @property
    def VicstatsarraygetrequestVicmandatorytlvsVicIndexArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicstatsarraygetrequestVicmandatorytlvsVicIndexArrayVicTLVType"
                ]
            ),
        )

    @property
    def VicstatsarraygetrequestVicmandatorytlvsVicIndexArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicstatsarraygetrequestVicmandatorytlvsVicIndexArrayVicTLVLength"
                ]
            ),
        )

    @property
    def VicmandatorytlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicmandatorytlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex"
                ]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 23
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicMessageType"]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicMessageVersion"]
            ),
        )

    @property
    def VicstatsarraygetresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicstatsarraygetresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicstatsarraygetresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicstatsarraygetresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicstatsarraygetresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicMessageLen"]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicMessageId"]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicFragmentId"]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicCompletionCode"]
            ),
        )

    @property
    def VicStatsArrayGetResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsArrayGetResponseVicVifIndex"]
            ),
        )

    @property
    def VicExtendedStatsArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 23
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicExtendedStatsArrayVicTLVType"]),
        )

    @property
    def VicExtendedStatsArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicExtendedStatsArrayVicTLVLength"]),
        )

    @property
    def VicStatsDataEntryVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicStatsDataEntryVicVifIndex"])
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwUnicastFrames(self):
        """
        Display Name: Adapter-to-Switch Unicast Frames
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwUnicastFrames"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwUnicastBytes(self):
        """
        Display Name: Adapter-to-Switch Unicast Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwUnicastBytes"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwMulticastFrames(self):
        """
        Display Name: Adapter-to-Switch Multicast Frames
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwMulticastFrames"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwMulticastBytes(self):
        """
        Display Name: Adapter-to-Switch Multicast Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwMulticastBytes"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwBroadcastFrames(self):
        """
        Display Name: Adapter-to-Switch Broadcast Frames
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwBroadcastFrames"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwBroadcastBytes(self):
        """
        Display Name: Adapter-to-Switch Broadcast Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwBroadcastBytes"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwFramesDiscarded(self):
        """
        Display Name: Adapter-to-Switch Frames Discarded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwFramesDiscarded"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaAdapterToSwFramesDropped(self):
        """
        Display Name: Adapter-to-Switch Frames Dropped
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaAdapterToSwFramesDropped"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterUnicastFrames(self):
        """
        Display Name: Switch-to-Adapter Unicast Frames
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterUnicastFrames"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterUnicastBytes(self):
        """
        Display Name: Switch-to-Adapter Unicast Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterUnicastBytes"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterMulticastFrames(self):
        """
        Display Name: Switch-to-Adapter Multicast Frames
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterMulticastFrames"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterMulticastBytes(self):
        """
        Display Name: Switch-to-Adapter Multicast Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterMulticastBytes"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterBroadcastFrames(self):
        """
        Display Name: Switch-to-Adapter Broadcast Frames
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterBroadcastFrames"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterBroadcastBytes(self):
        """
        Display Name: Switch-to-Adapter Broadcast Bytes
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterBroadcastBytes"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterFramesDiscarded(self):
        """
        Display Name: Switch-to-Adapter Frames Discarded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterFramesDiscarded"]
            ),
        )

    @property
    def VicStatsDataEntryVicEsaSwToAdapterFramesDropped(self):
        """
        Display Name: Switch-to-Adapter Frames Dropped
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicStatsDataEntryVicEsaSwToAdapterFramesDropped"]
            ),
        )

    @property
    def VicProfileAddRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 21
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddRequestVicMessageType"]
            ),
        )

    @property
    def VicProfileAddRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddRequestVicMessageVersion"]
            ),
        )

    @property
    def VicprofileaddrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicprofileaddrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicprofileaddrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicprofileaddrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicProfileAddRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProfileAddRequestVicMessageLen"]),
        )

    @property
    def VicProfileAddRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProfileAddRequestVicMessageId"]),
        )

    @property
    def VicProfileAddRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProfileAddRequestVicFragmentId"]),
        )

    @property
    def VicProfileAddRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddRequestVicCompletionCode"]
            ),
        )

    @property
    def VicProfileAddRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProfileAddRequestVicVifIndex"]),
        )

    @property
    def VicPortProfileNameListVicTLVType(self):
        """
        Display Name: Type
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPortProfileNameListVicTLVType"]),
        )

    @property
    def VicPortProfileNameListVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPortProfileNameListVicTLVLength"]
            ),
        )

    @property
    def VicPpnlPortProfileNameVicPpnlVariableNameLength(self):
        """
        Display Name: Variable Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicPpnlPortProfileNameVicPpnlVariableNameLength"]
            ),
        )

    @property
    def VicPpnlPortProfileNameVicPpnlName(self):
        """
        Display Name: Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicPpnlPortProfileNameVicPpnlName"]),
        )

    @property
    def VicProfileAddResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 21
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddResponseVicMessageType"]
            ),
        )

    @property
    def VicProfileAddResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddResponseVicMessageVersion"]
            ),
        )

    @property
    def VicprofileaddresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicprofileaddresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicprofileaddresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicprofileaddresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofileaddresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicProfileAddResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddResponseVicMessageLen"]
            ),
        )

    @property
    def VicProfileAddResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProfileAddResponseVicMessageId"]),
        )

    @property
    def VicProfileAddResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddResponseVicFragmentId"]
            ),
        )

    @property
    def VicProfileAddResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileAddResponseVicCompletionCode"]
            ),
        )

    @property
    def VicProfileAddResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicProfileAddResponseVicVifIndex"]),
        )

    @property
    def VicProfileDeleteRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicMessageType"]
            ),
        )

    @property
    def VicProfileDeleteRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicMessageVersion"]
            ),
        )

    @property
    def VicprofiledeleterequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleterequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicprofiledeleterequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleterequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicprofiledeleterequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleterequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicprofiledeleterequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleterequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicProfileDeleteRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicMessageLen"]
            ),
        )

    @property
    def VicProfileDeleteRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicMessageId"]
            ),
        )

    @property
    def VicProfileDeleteRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicFragmentId"]
            ),
        )

    @property
    def VicProfileDeleteRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicCompletionCode"]
            ),
        )

    @property
    def VicProfileDeleteRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteRequestVicVifIndex"]
            ),
        )

    @property
    def VicmandatorytlvsVicPortProfileNameListVicTLVType(self):
        """
        Display Name: Type
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicPortProfileNameListVicTLVType"]
            ),
        )

    @property
    def VicmandatorytlvsVicPortProfileNameListVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicmandatorytlvsVicPortProfileNameListVicTLVLength"]
            ),
        )

    @property
    def VicppnlportprofilenamesVicPpnlPortProfileNameVicPpnlVariableNameLength(self):
        """
        Display Name: Variable Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicppnlportprofilenamesVicPpnlPortProfileNameVicPpnlVariableNameLength"
                ]
            ),
        )

    @property
    def VicppnlportprofilenamesVicPpnlPortProfileNameVicPpnlName(self):
        """
        Display Name: Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicppnlportprofilenamesVicPpnlPortProfileNameVicPpnlName"
                ]
            ),
        )

    @property
    def VicProfileDeleteResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicMessageType"]
            ),
        )

    @property
    def VicProfileDeleteResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicMessageVersion"]
            ),
        )

    @property
    def VicprofiledeleteresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleteresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicprofiledeleteresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleteresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicprofiledeleteresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleteresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicprofiledeleteresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicprofiledeleteresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicProfileDeleteResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicMessageLen"]
            ),
        )

    @property
    def VicProfileDeleteResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicMessageId"]
            ),
        )

    @property
    def VicProfileDeleteResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicFragmentId"]
            ),
        )

    @property
    def VicProfileDeleteResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicCompletionCode"]
            ),
        )

    @property
    def VicProfileDeleteResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicProfileDeleteResponseVicVifIndex"]
            ),
        )

    @property
    def VicEnumRequestVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicMessageType"])
        )

    @property
    def VicEnumRequestVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicMessageVersion"]),
        )

    @property
    def VicenumrequestVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumrequestVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicenumrequestVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumrequestVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicenumrequestVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumrequestVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicenumrequestVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumrequestVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicEnumRequestVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicMessageLen"])
        )

    @property
    def VicEnumRequestVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicMessageId"])
        )

    @property
    def VicEnumRequestVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicFragmentId"])
        )

    @property
    def VicEnumRequestVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicCompletionCode"]),
        )

    @property
    def VicEnumRequestVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumRequestVicVifIndex"])
        )

    @property
    def VicEnumTypeVicTLVType(self):
        """
        Display Name: Type
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumTypeVicTLVType"])
        )

    @property
    def VicEnumTypeVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumTypeVicTLVLength"])
        )

    @property
    def VicEnumTypeVicEtType(self):
        """
        Display Name: Type of the enumeration
        Default Value: 1
        Value Format: decimal
        Available enum values: enumeration of VIFs, 1, enumeration of VIF-LISTs, 2, enumeration of UIFs, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumTypeVicEtType"])
        )

    @property
    def VicEnumResponseVicMessageType(self):
        """
        Display Name: Message Type
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicMessageType"]),
        )

    @property
    def VicEnumResponseVicMessageVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicMessageVersion"]),
        )

    @property
    def VicenumresponseVicMessageFlagsVicZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumresponseVicMessageFlagsVicZFlag"]
            ),
        )

    @property
    def VicenumresponseVicMessageFlagsVicPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumresponseVicMessageFlagsVicPFlag"]
            ),
        )

    @property
    def VicenumresponseVicMessageFlagsVicMFlag(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumresponseVicMessageFlagsVicMFlag"]
            ),
        )

    @property
    def VicenumresponseVicMessageFlagsVicRFlag(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VicenumresponseVicMessageFlagsVicRFlag"]
            ),
        )

    @property
    def VicEnumResponseVicMessageLen(self):
        """
        Display Name: Message Len / Message Fragment Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicMessageLen"])
        )

    @property
    def VicEnumResponseVicMessageId(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicMessageId"])
        )

    @property
    def VicEnumResponseVicFragmentId(self):
        """
        Display Name: Fragment ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicFragmentId"])
        )

    @property
    def VicEnumResponseVicCompletionCode(self):
        """
        Display Name: Completion Code
        Default Value: 0
        Value Format: decimal
        Available enum values: SUCCESS, 0, ERR_IN_PROGRESS, 1, MORE_DATA, 2, CC_ERR_UNKNOWN_TLV, 255, CC_ERR_MALFORMED_TLV, 254, CC_ERR_MISSING_MANDATORY_TLV, 253, CC_ERR_CAPABILITIES_MISMATCH, 252, CC_ERR_INTERNAL, 251, CC_ERR_PARAMETERS_INVALID, 250, CC_ERR_UNKNOWN_MESSAGE, 249, CC_ERR_FRAGMENTS_NOT_SUPPORTED, 248, CC_ERR_VIF_ID_NOT_SUPPORTED, 247, CC_ERR_PORT_PROOFILE_NOT_FOUND, 246, CC_ERR_DUPLICATE_TLV, 245, CC_ERR_CHANNEL_NUMBER_NOT_FOUND, 244
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicCompletionCode"]),
        )

    @property
    def VicEnumResponseVicVifIndex(self):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VicEnumResponseVicVifIndex"])
        )

    @property
    def VicenumresponseVicmandatorytlvsVicIndexArrayVicTLVType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicenumresponseVicmandatorytlvsVicIndexArrayVicTLVType"
                ]
            ),
        )

    @property
    def VicenumresponseVicmandatorytlvsVicIndexArrayVicTLVLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicenumresponseVicmandatorytlvsVicIndexArrayVicTLVLength"
                ]
            ),
        )

    @property
    def VicenumresponseVicmandatorytlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex(
        self,
    ):
        """
        Display Name: VIF-INDEX / VIF-LIST-INDEX / UIF-INDEX
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "VicenumresponseVicmandatorytlvsVicindexarrayVicindexesVicIndexEntryVicVifIndex"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

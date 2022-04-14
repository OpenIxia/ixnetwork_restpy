# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class LearnedInformation(Base):
    """Indicates the port level aggregated view of Learned Information for per Interface.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnedInformation"
    _SDM_ATT_MAP = {
        "AsyncConfStatResponseTimeOut": "asyncConfStatResponseTimeOut",
        "DescriptionStatResponseTimeOut": "descriptionStatResponseTimeOut",
        "EnableAsyncConfMasterFlowRemovedFlowDelete": "enableAsyncConfMasterFlowRemovedFlowDelete",
        "EnableAsyncConfMasterFlowRemovedGroupDelete": "enableAsyncConfMasterFlowRemovedGroupDelete",
        "EnableAsyncConfMasterFlowRemovedHardTimeOut": "enableAsyncConfMasterFlowRemovedHardTimeOut",
        "EnableAsyncConfMasterFlowRemovedIdleTimeOut": "enableAsyncConfMasterFlowRemovedIdleTimeOut",
        "EnableAsyncConfMasterPacketInActionOutputToController": "enableAsyncConfMasterPacketInActionOutputToController",
        "EnableAsyncConfMasterPacketInInvalidTtl": "enableAsyncConfMasterPacketInInvalidTtl",
        "EnableAsyncConfMasterPacketInNoMatching": "enableAsyncConfMasterPacketInNoMatching",
        "EnableAsyncConfMasterPortStatusAdd": "enableAsyncConfMasterPortStatusAdd",
        "EnableAsyncConfMasterPortStatusDelete": "enableAsyncConfMasterPortStatusDelete",
        "EnableAsyncConfMasterPortStatusModify": "enableAsyncConfMasterPortStatusModify",
        "EnableAsyncConfSlaveFlowRemovedFlowDelete": "enableAsyncConfSlaveFlowRemovedFlowDelete",
        "EnableAsyncConfSlaveFlowRemovedGroupDelete": "enableAsyncConfSlaveFlowRemovedGroupDelete",
        "EnableAsyncConfSlaveFlowRemovedHardTimeOut": "enableAsyncConfSlaveFlowRemovedHardTimeOut",
        "EnableAsyncConfSlaveFlowRemovedIdleTimeOut": "enableAsyncConfSlaveFlowRemovedIdleTimeOut",
        "EnableAsyncConfSlavePacketInActionOutputToController": "enableAsyncConfSlavePacketInActionOutputToController",
        "EnableAsyncConfSlavePacketInInvalidTtl": "enableAsyncConfSlavePacketInInvalidTtl",
        "EnableAsyncConfSlavePacketInNoMatching": "enableAsyncConfSlavePacketInNoMatching",
        "EnableAsyncConfSlavePortStatusAdd": "enableAsyncConfSlavePortStatusAdd",
        "EnableAsyncConfSlavePortStatusDelete": "enableAsyncConfSlavePortStatusDelete",
        "EnableAsyncConfSlavePortStatusModify": "enableAsyncConfSlavePortStatusModify",
        "EnableFlowAggregatedStatMatchCapability": "enableFlowAggregatedStatMatchCapability",
        "EnableFlowStatMatchCapability": "enableFlowStatMatchCapability",
        "EnableGroupStatMatchCapability": "enableGroupStatMatchCapability",
        "EnablePortStatMatchCapability": "enablePortStatMatchCapability",
        "EnableQueueStatMatchCapability": "enableQueueStatMatchCapability",
        "EnableSendTableFeaturesTrigger": "enableSendTableFeaturesTrigger",
        "EnableSendTriggerPortFeaturesLearnedInformation": "enableSendTriggerPortFeaturesLearnedInformation",
        "EnableSendTriggeredAsyncConfStatLearnedInformation": "enableSendTriggeredAsyncConfStatLearnedInformation",
        "EnableSendTriggeredBarrierRequestMessage": "enableSendTriggeredBarrierRequestMessage",
        "EnableSendTriggeredDescriptionStatLearnedInformation": "enableSendTriggeredDescriptionStatLearnedInformation",
        "EnableSendTriggeredFlowAggregatedStatLearnedInformation": "enableSendTriggeredFlowAggregatedStatLearnedInformation",
        "EnableSendTriggeredFlowStatLearnedInformation": "enableSendTriggeredFlowStatLearnedInformation",
        "EnableSendTriggeredGroupDescriptionStatLearnedInformation": "enableSendTriggeredGroupDescriptionStatLearnedInformation",
        "EnableSendTriggeredGroupFeatureStatLearnedInformation": "enableSendTriggeredGroupFeatureStatLearnedInformation",
        "EnableSendTriggeredGroupStatLearnedInformation": "enableSendTriggeredGroupStatLearnedInformation",
        "EnableSendTriggeredPacketOutMessage": "enableSendTriggeredPacketOutMessage",
        "EnableSendTriggeredPortModificationMessage": "enableSendTriggeredPortModificationMessage",
        "EnableSendTriggeredPortStatLearnedInformation": "enableSendTriggeredPortStatLearnedInformation",
        "EnableSendTriggeredQueueConfigLearnedInformation": "enableSendTriggeredQueueConfigLearnedInformation",
        "EnableSendTriggeredQueueStatLearnedInformation": "enableSendTriggeredQueueStatLearnedInformation",
        "EnableSendTriggeredRoleRequestMessage": "enableSendTriggeredRoleRequestMessage",
        "EnableSendTriggeredSwitchConfigLearnedInformation": "enableSendTriggeredSwitchConfigLearnedInformation",
        "EnableSendTriggeredTableStatLearnedInformation": "enableSendTriggeredTableStatLearnedInformation",
        "EnableSendTriggeredVendorStatLearnedInformation": "enableSendTriggeredVendorStatLearnedInformation",
        "EnableSetAsyncConfig": "enableSetAsyncConfig",
        "EnableSetSwitchConfig": "enableSetSwitchConfig",
        "EnableSetTableFeatures": "enableSetTableFeatures",
        "EnableTableStatMatchCapability": "enableTableStatMatchCapability",
        "EnableTriggeredVendorMessage": "enableTriggeredVendorMessage",
        "FlowAggregatedStatEthernetDestination": "flowAggregatedStatEthernetDestination",
        "FlowAggregatedStatEthernetSource": "flowAggregatedStatEthernetSource",
        "FlowAggregatedStatEthernetType": "flowAggregatedStatEthernetType",
        "FlowAggregatedStatInPort": "flowAggregatedStatInPort",
        "FlowAggregatedStatIpDscp": "flowAggregatedStatIpDscp",
        "FlowAggregatedStatIpProtocol": "flowAggregatedStatIpProtocol",
        "FlowAggregatedStatIpv4Destination": "flowAggregatedStatIpv4Destination",
        "FlowAggregatedStatIpv4Source": "flowAggregatedStatIpv4Source",
        "FlowAggregatedStatOutPortInputMode": "flowAggregatedStatOutPortInputMode",
        "FlowAggregatedStatResponseTimeOut": "flowAggregatedStatResponseTimeOut",
        "FlowAggregatedStatTableIdInputMode": "flowAggregatedStatTableIdInputMode",
        "FlowAggregatedStatTableIdInputModeNumber": "flowAggregatedStatTableIdInputModeNumber",
        "FlowAggregatedStatTransportDestination": "flowAggregatedStatTransportDestination",
        "FlowAggregatedStatTransportSource": "flowAggregatedStatTransportSource",
        "FlowAggregatedStatVlanId": "flowAggregatedStatVlanId",
        "FlowAggregatedStatVlanPriority": "flowAggregatedStatVlanPriority",
        "FlowStatEthernetDestination": "flowStatEthernetDestination",
        "FlowStatEthernetSource": "flowStatEthernetSource",
        "FlowStatEthernetType": "flowStatEthernetType",
        "FlowStatInPort": "flowStatInPort",
        "FlowStatIpDscp": "flowStatIpDscp",
        "FlowStatIpProtocol": "flowStatIpProtocol",
        "FlowStatIpv4Destination": "flowStatIpv4Destination",
        "FlowStatIpv4Source": "flowStatIpv4Source",
        "FlowStatOutPortInputMode": "flowStatOutPortInputMode",
        "FlowStatResponseTimeOut": "flowStatResponseTimeOut",
        "FlowStatTableIdInputMode": "flowStatTableIdInputMode",
        "FlowStatTableIdInputModeNumber": "flowStatTableIdInputModeNumber",
        "FlowStatTransportDestination": "flowStatTransportDestination",
        "FlowStatTransportSource": "flowStatTransportSource",
        "FlowStatVlanId": "flowStatVlanId",
        "FlowStatVlanPriority": "flowStatVlanPriority",
        "GroupDescriptionStatResponseTimeOut": "groupDescriptionStatResponseTimeOut",
        "GroupFeatureStatResponseTimeOut": "groupFeatureStatResponseTimeOut",
        "GroupId": "groupId",
        "GroupIdType": "groupIdType",
        "GroupStatResponseTimeOut": "groupStatResponseTimeOut",
        "IsAsyncConfStatLearnedInformationRefreshed": "isAsyncConfStatLearnedInformationRefreshed",
        "IsDescriptionStatLearnedInformationRefreshed": "isDescriptionStatLearnedInformationRefreshed",
        "IsFlowAggregatedStatLearnedInformationRefreshed": "isFlowAggregatedStatLearnedInformationRefreshed",
        "IsFlowStatLearnedInformationRefreshed": "isFlowStatLearnedInformationRefreshed",
        "IsGroupDescriptionStatLearnedInformationRefreshed": "isGroupDescriptionStatLearnedInformationRefreshed",
        "IsGroupFeatureStatLearnedInformationRefreshed": "isGroupFeatureStatLearnedInformationRefreshed",
        "IsGroupStatLearnedInformationRefreshed": "isGroupStatLearnedInformationRefreshed",
        "IsOfChannelLearnedInformationRefreshed": "isOfChannelLearnedInformationRefreshed",
        "IsPortFeaturesLearnedInformationRefreshed": "isPortFeaturesLearnedInformationRefreshed",
        "IsPortStatLearnedInformationRefreshed": "isPortStatLearnedInformationRefreshed",
        "IsQueueConfigLearnedInformationRefreshed": "isQueueConfigLearnedInformationRefreshed",
        "IsQueueStatLearnedInformationRefreshed": "isQueueStatLearnedInformationRefreshed",
        "IsTableStatLearnedInformationRefreshed": "isTableStatLearnedInformationRefreshed",
        "IsVendorStatLearnedInformationRefreshed": "isVendorStatLearnedInformationRefreshed",
        "PacketOutAuxiliaryId": "packetOutAuxiliaryId",
        "PacketOutBufferId": "packetOutBufferId",
        "PacketOutBufferIdInputMode": "packetOutBufferIdInputMode",
        "PacketOutData": "packetOutData",
        "PacketOutDataLength": "packetOutDataLength",
        "PacketOutInPortInputMode": "packetOutInPortInputMode",
        "PacketOutInPortNumber": "packetOutInPortNumber",
        "PortFeaturesResponseTimeOut": "portFeaturesResponseTimeOut",
        "PortNumber": "portNumber",
        "PortNumberInputMode": "portNumberInputMode",
        "PortStatResponseTimeOut": "portStatResponseTimeOut",
        "QueueConfigPortNumber": "queueConfigPortNumber",
        "QueueConfigResponseTimeOut": "queueConfigResponseTimeOut",
        "QueueId": "queueId",
        "QueueIdInputMode": "queueIdInputMode",
        "QueueStatPortNumber": "queueStatPortNumber",
        "QueueStatPortNumberInputMode": "queueStatPortNumberInputMode",
        "QueueStatResponseTimeOut": "queueStatResponseTimeOut",
        "RoleRequestGenerationId": "roleRequestGenerationId",
        "RoleRequestType": "roleRequestType",
        "SwitchConfigDropFragments": "switchConfigDropFragments",
        "SwitchConfigMissSendLength": "switchConfigMissSendLength",
        "SwitchConfigReassembleFragments": "switchConfigReassembleFragments",
        "SwitchConfigResponseTimeOut": "switchConfigResponseTimeOut",
        "TableFeatureConfig": "tableFeatureConfig",
        "TableFeatureMaxEntries": "tableFeatureMaxEntries",
        "TableFeatureMetadataMatch": "tableFeatureMetadataMatch",
        "TableFeatureMetadataWrite": "tableFeatureMetadataWrite",
        "TableFeatureName": "tableFeatureName",
        "TableFeatureResponseTimeOut": "tableFeatureResponseTimeOut",
        "TableFeatureTableId": "tableFeatureTableId",
        "TableStatResponseTimeOut": "tableStatResponseTimeOut",
        "TriggeredVendorMessage": "triggeredVendorMessage",
        "TriggeredVendorMessageId": "triggeredVendorMessageId",
        "TriggeredVendorMessageLength": "triggeredVendorMessageLength",
        "VendorId": "vendorId",
        "VendorMessage": "vendorMessage",
        "VendorMessageLength": "vendorMessageLength",
        "VendorStateResponseTimeOut": "vendorStateResponseTimeOut",
    }
    _SDM_ENUM_MAP = {
        "flowAggregatedStatOutPortInputMode": [
            "ofppInPort",
            "ofppNormal",
            "ofppFlood",
            "ofppAll",
            "ofppController",
            "ofppLocal",
            "ofppNone",
            "custom",
        ],
        "flowAggregatedStatTableIdInputMode": ["allTables", "emergency", "custom"],
        "flowStatOutPortInputMode": [
            "ofppInPort",
            "ofppNormal",
            "ofppFlood",
            "ofppAll",
            "ofppController",
            "ofppLocal",
            "ofppNone",
            "custom",
        ],
        "flowStatTableIdInputMode": ["allTables", "emergency", "custom"],
        "groupIdType": ["ofpgAll", "ofpgAny", "manual"],
        "packetOutBufferIdInputMode": ["opfNoBuffer", "manual"],
        "packetOutInPortInputMode": ["ofppController", "ofppLocal", "manual"],
        "portNumberInputMode": ["ofppNone", "custom"],
        "queueIdInputMode": ["ofpqAll", "custom"],
        "queueStatPortNumberInputMode": ["ofppAll", "custom"],
        "roleRequestType": ["equal", "master", "slave", "noChange"],
    }

    def __init__(self, parent, list_op=False):
        super(LearnedInformation, self).__init__(parent, list_op)

    @property
    def AsyncConfStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_8263676c7436dc68c8c6376e412a59a0.AsyncConfStatLearnedInformation): An instance of the AsyncConfStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_8263676c7436dc68c8c6376e412a59a0 import (
            AsyncConfStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("AsyncConfStatLearnedInformation", None)
                is not None
            ):
                return self._properties.get("AsyncConfStatLearnedInformation")
        return AsyncConfStatLearnedInformation(self)

    @property
    def Controller131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_6cab58785fde2d113c2ae0cad7498273.Controller131TriggerAttributes): An instance of the Controller131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_6cab58785fde2d113c2ae0cad7498273 import (
            Controller131TriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Controller131TriggerAttributes", None) is not None:
                return self._properties.get("Controller131TriggerAttributes")
        return Controller131TriggerAttributes(self)._select()

    @property
    def DescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_a359e482aaae60d1717b225a494fa484.DescriptionStatLearnedInformation): An instance of the DescriptionStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_a359e482aaae60d1717b225a494fa484 import (
            DescriptionStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("DescriptionStatLearnedInformation", None)
                is not None
            ):
                return self._properties.get("DescriptionStatLearnedInformation")
        return DescriptionStatLearnedInformation(self)

    @property
    def FlowAggregatedStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_46c4230f1b3c053b903df6ed8cf276f3.FlowAggregatedStatLearnedInformation): An instance of the FlowAggregatedStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_46c4230f1b3c053b903df6ed8cf276f3 import (
            FlowAggregatedStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("FlowAggregatedStatLearnedInformation", None)
                is not None
            ):
                return self._properties.get("FlowAggregatedStatLearnedInformation")
        return FlowAggregatedStatLearnedInformation(self)

    @property
    def FlowAggregatedStatMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_315a5f3f92d4de91dc57b878df643d23.FlowAggregatedStatMatchCriteria131TriggerAttributes): An instance of the FlowAggregatedStatMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_315a5f3f92d4de91dc57b878df643d23 import (
            FlowAggregatedStatMatchCriteria131TriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get(
                    "FlowAggregatedStatMatchCriteria131TriggerAttributes", None
                )
                is not None
            ):
                return self._properties.get(
                    "FlowAggregatedStatMatchCriteria131TriggerAttributes"
                )
        return FlowAggregatedStatMatchCriteria131TriggerAttributes(self)._select()

    @property
    def FlowStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_30004ff541577c4d728de71d4d15d766.FlowStatLearnedInformation): An instance of the FlowStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_30004ff541577c4d728de71d4d15d766 import (
            FlowStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlowStatLearnedInformation", None) is not None:
                return self._properties.get("FlowStatLearnedInformation")
        return FlowStatLearnedInformation(self)

    @property
    def FlowStatMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_332604ca4d52c2eba1dfeb1164ec44dd.FlowStatMatchCriteria131TriggerAttributes): An instance of the FlowStatMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_332604ca4d52c2eba1dfeb1164ec44dd import (
            FlowStatMatchCriteria131TriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("FlowStatMatchCriteria131TriggerAttributes", None)
                is not None
            ):
                return self._properties.get("FlowStatMatchCriteria131TriggerAttributes")
        return FlowStatMatchCriteria131TriggerAttributes(self)._select()

    @property
    def GroupDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_8b9e5ac842eadde534391442ad6b9af1.GroupDescriptionStatLearnedInformation): An instance of the GroupDescriptionStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_8b9e5ac842eadde534391442ad6b9af1 import (
            GroupDescriptionStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("GroupDescriptionStatLearnedInformation", None)
                is not None
            ):
                return self._properties.get("GroupDescriptionStatLearnedInformation")
        return GroupDescriptionStatLearnedInformation(self)

    @property
    def GroupFeatureStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_a36a2e649d69b292cdb4a21ca980e647.GroupFeatureStatLearnedInformation): An instance of the GroupFeatureStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_a36a2e649d69b292cdb4a21ca980e647 import (
            GroupFeatureStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("GroupFeatureStatLearnedInformation", None)
                is not None
            ):
                return self._properties.get("GroupFeatureStatLearnedInformation")
        return GroupFeatureStatLearnedInformation(self)

    @property
    def GroupStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_100495e05f6e7b1b1650ad63b2ee4161.GroupStatLearnedInformation): An instance of the GroupStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_100495e05f6e7b1b1650ad63b2ee4161 import (
            GroupStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GroupStatLearnedInformation", None) is not None:
                return self._properties.get("GroupStatLearnedInformation")
        return GroupStatLearnedInformation(self)

    @property
    def MeterConfigStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_ee133b5ab250ce978ccd6e7000f18e28.MeterConfigStatsLearnedInformation): An instance of the MeterConfigStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_ee133b5ab250ce978ccd6e7000f18e28 import (
            MeterConfigStatsLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("MeterConfigStatsLearnedInformation", None)
                is not None
            ):
                return self._properties.get("MeterConfigStatsLearnedInformation")
        return MeterConfigStatsLearnedInformation(self)

    @property
    def MeterFeatureStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_ab32f8b3a8c2aa48d53fedc3e2df59dd.MeterFeatureStatsLearnedInformation): An instance of the MeterFeatureStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_ab32f8b3a8c2aa48d53fedc3e2df59dd import (
            MeterFeatureStatsLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("MeterFeatureStatsLearnedInformation", None)
                is not None
            ):
                return self._properties.get("MeterFeatureStatsLearnedInformation")
        return MeterFeatureStatsLearnedInformation(self)

    @property
    def MeterStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_bd5899f9e605047a4933dec0fdf73366.MeterStatsLearnedInformation): An instance of the MeterStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_bd5899f9e605047a4933dec0fdf73366 import (
            MeterStatsLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MeterStatsLearnedInformation", None) is not None:
                return self._properties.get("MeterStatsLearnedInformation")
        return MeterStatsLearnedInformation(self)

    @property
    def OfChannelLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_2c0d9c826a237f044b4b6368ca250839.OfChannelLearnedInformation): An instance of the OfChannelLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_2c0d9c826a237f044b4b6368ca250839 import (
            OfChannelLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OfChannelLearnedInformation", None) is not None:
                return self._properties.get("OfChannelLearnedInformation")
        return OfChannelLearnedInformation(self)

    @property
    def PacketOutTriggerActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_ec5821e9272e2ea2c05e3910edf98056.PacketOutTriggerActions): An instance of the PacketOutTriggerActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_ec5821e9272e2ea2c05e3910edf98056 import (
            PacketOutTriggerActions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PacketOutTriggerActions", None) is not None:
                return self._properties.get("PacketOutTriggerActions")
        return PacketOutTriggerActions(self)

    @property
    def PortFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_d0dbd87b574c9a18016cdef98678e453.PortFeaturesLearnedInformation): An instance of the PortFeaturesLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_d0dbd87b574c9a18016cdef98678e453 import (
            PortFeaturesLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PortFeaturesLearnedInformation", None) is not None:
                return self._properties.get("PortFeaturesLearnedInformation")
        return PortFeaturesLearnedInformation(self)

    @property
    def PortModificationTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_5bc5835d31569d2613fda0b3721ad681.PortModificationTriggerAttributes): An instance of the PortModificationTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_5bc5835d31569d2613fda0b3721ad681 import (
            PortModificationTriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PortModificationTriggerAttributes", None)
                is not None
            ):
                return self._properties.get("PortModificationTriggerAttributes")
        return PortModificationTriggerAttributes(self)._select()

    @property
    def PortStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_31c26a5bcbe87f62ff543b7a7ffb3432.PortStatLearnedInformation): An instance of the PortStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_31c26a5bcbe87f62ff543b7a7ffb3432 import (
            PortStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PortStatLearnedInformation", None) is not None:
                return self._properties.get("PortStatLearnedInformation")
        return PortStatLearnedInformation(self)

    @property
    def QueueConfigLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_10211d0e530099c486d9e89481f764c8.QueueConfigLearnedInformation): An instance of the QueueConfigLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_10211d0e530099c486d9e89481f764c8 import (
            QueueConfigLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("QueueConfigLearnedInformation", None) is not None:
                return self._properties.get("QueueConfigLearnedInformation")
        return QueueConfigLearnedInformation(self)

    @property
    def QueueStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_7fd65340d3c1f24a9ea2dfe8160d524a.QueueStatLearnedInformation): An instance of the QueueStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_7fd65340d3c1f24a9ea2dfe8160d524a import (
            QueueStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("QueueStatLearnedInformation", None) is not None:
                return self._properties.get("QueueStatLearnedInformation")
        return QueueStatLearnedInformation(self)

    @property
    def SwitchConfigLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_0ea07dc2417e7dcbb9cea0bd70f007ec.SwitchConfigLearnedInformation): An instance of the SwitchConfigLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_0ea07dc2417e7dcbb9cea0bd70f007ec import (
            SwitchConfigLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchConfigLearnedInformation", None) is not None:
                return self._properties.get("SwitchConfigLearnedInformation")
        return SwitchConfigLearnedInformation(self)

    @property
    def TableFeaturePropertiesTrigger(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_159cbb76bc90f1cb0a06dd89e98757fa.TableFeaturePropertiesTrigger): An instance of the TableFeaturePropertiesTrigger class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_159cbb76bc90f1cb0a06dd89e98757fa import (
            TableFeaturePropertiesTrigger,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TableFeaturePropertiesTrigger", None) is not None:
                return self._properties.get("TableFeaturePropertiesTrigger")
        return TableFeaturePropertiesTrigger(self)

    @property
    def TableFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_25618c8be71a4cf85be5f34e995db75e.TableFeaturesLearnedInformation): An instance of the TableFeaturesLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_25618c8be71a4cf85be5f34e995db75e import (
            TableFeaturesLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("TableFeaturesLearnedInformation", None)
                is not None
            ):
                return self._properties.get("TableFeaturesLearnedInformation")
        return TableFeaturesLearnedInformation(self)

    @property
    def TableStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_80bff3610dd3cd2ada6c7aca20b53b76.TableStatLearnedInformation): An instance of the TableStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_80bff3610dd3cd2ada6c7aca20b53b76 import (
            TableStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TableStatLearnedInformation", None) is not None:
                return self._properties.get("TableStatLearnedInformation")
        return TableStatLearnedInformation(self)

    @property
    def VendorStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_80b9796ada805b38f41bbaf9e9ecb473.VendorStatLearnedInformation): An instance of the VendorStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_80b9796ada805b38f41bbaf9e9ecb473 import (
            VendorStatLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VendorStatLearnedInformation", None) is not None:
                return self._properties.get("VendorStatLearnedInformation")
        return VendorStatLearnedInformation(self)

    @property
    def AsyncConfStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsyncConfStatResponseTimeOut"])

    @AsyncConfStatResponseTimeOut.setter
    def AsyncConfStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsyncConfStatResponseTimeOut"], value)

    @property
    def DescriptionStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptionStatResponseTimeOut"])

    @DescriptionStatResponseTimeOut.setter
    def DescriptionStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DescriptionStatResponseTimeOut"], value)

    @property
    def EnableAsyncConfMasterFlowRemovedFlowDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedFlowDelete"]
        )

    @EnableAsyncConfMasterFlowRemovedFlowDelete.setter
    def EnableAsyncConfMasterFlowRemovedFlowDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedFlowDelete"], value
        )

    @property
    def EnableAsyncConfMasterFlowRemovedGroupDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedGroupDelete"]
        )

    @EnableAsyncConfMasterFlowRemovedGroupDelete.setter
    def EnableAsyncConfMasterFlowRemovedGroupDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedGroupDelete"], value
        )

    @property
    def EnableAsyncConfMasterFlowRemovedHardTimeOut(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedHardTimeOut"]
        )

    @EnableAsyncConfMasterFlowRemovedHardTimeOut.setter
    def EnableAsyncConfMasterFlowRemovedHardTimeOut(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedHardTimeOut"], value
        )

    @property
    def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedIdleTimeOut"]
        )

    @EnableAsyncConfMasterFlowRemovedIdleTimeOut.setter
    def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterFlowRemovedIdleTimeOut"], value
        )

    @property
    def EnableAsyncConfMasterPacketInActionOutputToController(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPacketInActionOutputToController"]
        )

    @EnableAsyncConfMasterPacketInActionOutputToController.setter
    def EnableAsyncConfMasterPacketInActionOutputToController(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPacketInActionOutputToController"],
            value,
        )

    @property
    def EnableAsyncConfMasterPacketInInvalidTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPacketInInvalidTtl"]
        )

    @EnableAsyncConfMasterPacketInInvalidTtl.setter
    def EnableAsyncConfMasterPacketInInvalidTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPacketInInvalidTtl"], value
        )

    @property
    def EnableAsyncConfMasterPacketInNoMatching(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPacketInNoMatching"]
        )

    @EnableAsyncConfMasterPacketInNoMatching.setter
    def EnableAsyncConfMasterPacketInNoMatching(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPacketInNoMatching"], value
        )

    @property
    def EnableAsyncConfMasterPortStatusAdd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPortStatusAdd"]
        )

    @EnableAsyncConfMasterPortStatusAdd.setter
    def EnableAsyncConfMasterPortStatusAdd(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPortStatusAdd"], value
        )

    @property
    def EnableAsyncConfMasterPortStatusDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPortStatusDelete"]
        )

    @EnableAsyncConfMasterPortStatusDelete.setter
    def EnableAsyncConfMasterPortStatusDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPortStatusDelete"], value
        )

    @property
    def EnableAsyncConfMasterPortStatusModify(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPortStatusModify"]
        )

    @EnableAsyncConfMasterPortStatusModify.setter
    def EnableAsyncConfMasterPortStatusModify(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfMasterPortStatusModify"], value
        )

    @property
    def EnableAsyncConfSlaveFlowRemovedFlowDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedFlowDelete"]
        )

    @EnableAsyncConfSlaveFlowRemovedFlowDelete.setter
    def EnableAsyncConfSlaveFlowRemovedFlowDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedFlowDelete"], value
        )

    @property
    def EnableAsyncConfSlaveFlowRemovedGroupDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedGroupDelete"]
        )

    @EnableAsyncConfSlaveFlowRemovedGroupDelete.setter
    def EnableAsyncConfSlaveFlowRemovedGroupDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedGroupDelete"], value
        )

    @property
    def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedHardTimeOut"]
        )

    @EnableAsyncConfSlaveFlowRemovedHardTimeOut.setter
    def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedHardTimeOut"], value
        )

    @property
    def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedIdleTimeOut"]
        )

    @EnableAsyncConfSlaveFlowRemovedIdleTimeOut.setter
    def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlaveFlowRemovedIdleTimeOut"], value
        )

    @property
    def EnableAsyncConfSlavePacketInActionOutputToController(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePacketInActionOutputToController"]
        )

    @EnableAsyncConfSlavePacketInActionOutputToController.setter
    def EnableAsyncConfSlavePacketInActionOutputToController(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePacketInActionOutputToController"],
            value,
        )

    @property
    def EnableAsyncConfSlavePacketInInvalidTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePacketInInvalidTtl"]
        )

    @EnableAsyncConfSlavePacketInInvalidTtl.setter
    def EnableAsyncConfSlavePacketInInvalidTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePacketInInvalidTtl"], value
        )

    @property
    def EnableAsyncConfSlavePacketInNoMatching(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePacketInNoMatching"]
        )

    @EnableAsyncConfSlavePacketInNoMatching.setter
    def EnableAsyncConfSlavePacketInNoMatching(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePacketInNoMatching"], value
        )

    @property
    def EnableAsyncConfSlavePortStatusAdd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePortStatusAdd"]
        )

    @EnableAsyncConfSlavePortStatusAdd.setter
    def EnableAsyncConfSlavePortStatusAdd(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePortStatusAdd"], value
        )

    @property
    def EnableAsyncConfSlavePortStatusDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePortStatusDelete"]
        )

    @EnableAsyncConfSlavePortStatusDelete.setter
    def EnableAsyncConfSlavePortStatusDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePortStatusDelete"], value
        )

    @property
    def EnableAsyncConfSlavePortStatusModify(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePortStatusModify"]
        )

    @EnableAsyncConfSlavePortStatusModify.setter
    def EnableAsyncConfSlavePortStatusModify(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableAsyncConfSlavePortStatusModify"], value
        )

    @property
    def EnableFlowAggregatedStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Checks to see if the switch has the capability to publish Flow Aggregated Statistics
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableFlowAggregatedStatMatchCapability"]
        )

    @EnableFlowAggregatedStatMatchCapability.setter
    def EnableFlowAggregatedStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableFlowAggregatedStatMatchCapability"], value
        )

    @property
    def EnableFlowStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Checks to see if the switch has the capability to publish Flow Statistics
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFlowStatMatchCapability"])

    @EnableFlowStatMatchCapability.setter
    def EnableFlowStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFlowStatMatchCapability"], value)

    @property
    def EnableGroupStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Group Statistics Match Capability is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGroupStatMatchCapability"])

    @EnableGroupStatMatchCapability.setter
    def EnableGroupStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGroupStatMatchCapability"], value)

    @property
    def EnablePortStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Checks to see if the switch has the capability to publish Port Statistics
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePortStatMatchCapability"])

    @EnablePortStatMatchCapability.setter
    def EnablePortStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePortStatMatchCapability"], value)

    @property
    def EnableQueueStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the switch has the capability to publish Queue Statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableQueueStatMatchCapability"])

    @EnableQueueStatMatchCapability.setter
    def EnableQueueStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableQueueStatMatchCapability"], value)

    @property
    def EnableSendTableFeaturesTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Table Features Trigger is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSendTableFeaturesTrigger"])

    @EnableSendTableFeaturesTrigger.setter
    def EnableSendTableFeaturesTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSendTableFeaturesTrigger"], value)

    @property
    def EnableSendTriggerPortFeaturesLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Trigger for port features learned information.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerPortFeaturesLearnedInformation"]
        )

    @EnableSendTriggerPortFeaturesLearnedInformation.setter
    def EnableSendTriggerPortFeaturesLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggerPortFeaturesLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredAsyncConfStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredAsyncConfStatLearnedInformation"]
        )

    @EnableSendTriggeredAsyncConfStatLearnedInformation.setter
    def EnableSendTriggeredAsyncConfStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredAsyncConfStatLearnedInformation"],
            value,
        )

    @property
    def EnableSendTriggeredBarrierRequestMessage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables trigger for barrier request message
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredBarrierRequestMessage"]
        )

    @EnableSendTriggeredBarrierRequestMessage.setter
    def EnableSendTriggeredBarrierRequestMessage(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredBarrierRequestMessage"], value
        )

    @property
    def EnableSendTriggeredDescriptionStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the description statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredDescriptionStatLearnedInformation"]
        )

    @EnableSendTriggeredDescriptionStatLearnedInformation.setter
    def EnableSendTriggeredDescriptionStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredDescriptionStatLearnedInformation"],
            value,
        )

    @property
    def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the flow aggregated statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredFlowAggregatedStatLearnedInformation"]
        )

    @EnableSendTriggeredFlowAggregatedStatLearnedInformation.setter
    def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP[
                "EnableSendTriggeredFlowAggregatedStatLearnedInformation"
            ],
            value,
        )

    @property
    def EnableSendTriggeredFlowStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the flow statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredFlowStatLearnedInformation"]
        )

    @EnableSendTriggeredFlowStatLearnedInformation.setter
    def EnableSendTriggeredFlowStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredFlowStatLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP[
                "EnableSendTriggeredGroupDescriptionStatLearnedInformation"
            ]
        )

    @EnableSendTriggeredGroupDescriptionStatLearnedInformation.setter
    def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP[
                "EnableSendTriggeredGroupDescriptionStatLearnedInformation"
            ],
            value,
        )

    @property
    def EnableSendTriggeredGroupFeatureStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredGroupFeatureStatLearnedInformation"]
        )

    @EnableSendTriggeredGroupFeatureStatLearnedInformation.setter
    def EnableSendTriggeredGroupFeatureStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredGroupFeatureStatLearnedInformation"],
            value,
        )

    @property
    def EnableSendTriggeredGroupStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredGroupStatLearnedInformation"]
        )

    @EnableSendTriggeredGroupStatLearnedInformation.setter
    def EnableSendTriggeredGroupStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredGroupStatLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredPacketOutMessage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Packet Out Message is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredPacketOutMessage"]
        )

    @EnableSendTriggeredPacketOutMessage.setter
    def EnableSendTriggeredPacketOutMessage(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredPacketOutMessage"], value
        )

    @property
    def EnableSendTriggeredPortModificationMessage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Port Modification Message is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredPortModificationMessage"]
        )

    @EnableSendTriggeredPortModificationMessage.setter
    def EnableSendTriggeredPortModificationMessage(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredPortModificationMessage"], value
        )

    @property
    def EnableSendTriggeredPortStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the port statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredPortStatLearnedInformation"]
        )

    @EnableSendTriggeredPortStatLearnedInformation.setter
    def EnableSendTriggeredPortStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredPortStatLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredQueueConfigLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the queue config trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredQueueConfigLearnedInformation"]
        )

    @EnableSendTriggeredQueueConfigLearnedInformation.setter
    def EnableSendTriggeredQueueConfigLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredQueueConfigLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredQueueStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the queue statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredQueueStatLearnedInformation"]
        )

    @EnableSendTriggeredQueueStatLearnedInformation.setter
    def EnableSendTriggeredQueueStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredQueueStatLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredRoleRequestMessage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Triggered Role Request Message is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredRoleRequestMessage"]
        )

    @EnableSendTriggeredRoleRequestMessage.setter
    def EnableSendTriggeredRoleRequestMessage(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredRoleRequestMessage"], value
        )

    @property
    def EnableSendTriggeredSwitchConfigLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Switch Configuration Learned Information is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredSwitchConfigLearnedInformation"]
        )

    @EnableSendTriggeredSwitchConfigLearnedInformation.setter
    def EnableSendTriggeredSwitchConfigLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredSwitchConfigLearnedInformation"],
            value,
        )

    @property
    def EnableSendTriggeredTableStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the table statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredTableStatLearnedInformation"]
        )

    @EnableSendTriggeredTableStatLearnedInformation.setter
    def EnableSendTriggeredTableStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredTableStatLearnedInformation"], value
        )

    @property
    def EnableSendTriggeredVendorStatLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the vendor statistic trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredVendorStatLearnedInformation"]
        )

    @EnableSendTriggeredVendorStatLearnedInformation.setter
    def EnableSendTriggeredVendorStatLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSendTriggeredVendorStatLearnedInformation"], value
        )

    @property
    def EnableSetAsyncConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Set Asynchronous Configuration is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSetAsyncConfig"])

    @EnableSetAsyncConfig.setter
    def EnableSetAsyncConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSetAsyncConfig"], value)

    @property
    def EnableSetSwitchConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Set Switch Configuration is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSetSwitchConfig"])

    @EnableSetSwitchConfig.setter
    def EnableSetSwitchConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSetSwitchConfig"], value)

    @property
    def EnableSetTableFeatures(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSetTableFeatures"])

    @EnableSetTableFeatures.setter
    def EnableSetTableFeatures(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSetTableFeatures"], value)

    @property
    def EnableTableStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the switch has the capability to publish Table Statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTableStatMatchCapability"])

    @EnableTableStatMatchCapability.setter
    def EnableTableStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTableStatMatchCapability"], value)

    @property
    def EnableTriggeredVendorMessage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the vendor message trigger configuration parameters are available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTriggeredVendorMessage"])

    @EnableTriggeredVendorMessage.setter
    def EnableTriggeredVendorMessage(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTriggeredVendorMessage"], value)

    @property
    def FlowAggregatedStatEthernetDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the ethernet destination address.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatEthernetDestination"]
        )

    @FlowAggregatedStatEthernetDestination.setter
    def FlowAggregatedStatEthernetDestination(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatEthernetDestination"], value
        )

    @property
    def FlowAggregatedStatEthernetSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the ethernet source address.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatEthernetSource"]
        )

    @FlowAggregatedStatEthernetSource.setter
    def FlowAggregatedStatEthernetSource(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatEthernetSource"], value
        )

    @property
    def FlowAggregatedStatEthernetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the type of Ethernet used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatEthernetType"])

    @FlowAggregatedStatEthernetType.setter
    def FlowAggregatedStatEthernetType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatEthernetType"], value)

    @property
    def FlowAggregatedStatInPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the input port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatInPort"])

    @FlowAggregatedStatInPort.setter
    def FlowAggregatedStatInPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatInPort"], value)

    @property
    def FlowAggregatedStatIpDscp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IP DSCP value for advertising.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatIpDscp"])

    @FlowAggregatedStatIpDscp.setter
    def FlowAggregatedStatIpDscp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatIpDscp"], value)

    @property
    def FlowAggregatedStatIpProtocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IP protocol used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatIpProtocol"])

    @FlowAggregatedStatIpProtocol.setter
    def FlowAggregatedStatIpProtocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatIpProtocol"], value)

    @property
    def FlowAggregatedStatIpv4Destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IPv4 destination address.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatIpv4Destination"]
        )

    @FlowAggregatedStatIpv4Destination.setter
    def FlowAggregatedStatIpv4Destination(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatIpv4Destination"], value
        )

    @property
    def FlowAggregatedStatIpv4Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IPv4 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatIpv4Source"])

    @FlowAggregatedStatIpv4Source.setter
    def FlowAggregatedStatIpv4Source(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatIpv4Source"], value)

    @property
    def FlowAggregatedStatOutPortInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom): Signifies the identifier output mode of the aggregated flow statistics table.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatOutPortInputMode"]
        )

    @FlowAggregatedStatOutPortInputMode.setter
    def FlowAggregatedStatOutPortInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatOutPortInputMode"], value
        )

    @property
    def FlowAggregatedStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatResponseTimeOut"]
        )

    @FlowAggregatedStatResponseTimeOut.setter
    def FlowAggregatedStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatResponseTimeOut"], value
        )

    @property
    def FlowAggregatedStatTableIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allTables | emergency | custom): Signifies the identifier input mode of the flow aggregated statistics table.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTableIdInputMode"]
        )

    @FlowAggregatedStatTableIdInputMode.setter
    def FlowAggregatedStatTableIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTableIdInputMode"], value
        )

    @property
    def FlowAggregatedStatTableIdInputModeNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the identifier input mode of the flow aggregated statistics table.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTableIdInputModeNumber"]
        )

    @FlowAggregatedStatTableIdInputModeNumber.setter
    def FlowAggregatedStatTableIdInputModeNumber(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTableIdInputModeNumber"], value
        )

    @property
    def FlowAggregatedStatTransportDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Transport destination address.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTransportDestination"]
        )

    @FlowAggregatedStatTransportDestination.setter
    def FlowAggregatedStatTransportDestination(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTransportDestination"], value
        )

    @property
    def FlowAggregatedStatTransportSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Transport source address.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTransportSource"]
        )

    @FlowAggregatedStatTransportSource.setter
    def FlowAggregatedStatTransportSource(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FlowAggregatedStatTransportSource"], value
        )

    @property
    def FlowAggregatedStatVlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the unique VLAN Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatVlanId"])

    @FlowAggregatedStatVlanId.setter
    def FlowAggregatedStatVlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatVlanId"], value)

    @property
    def FlowAggregatedStatVlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the User Priority for this VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregatedStatVlanPriority"])

    @FlowAggregatedStatVlanPriority.setter
    def FlowAggregatedStatVlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregatedStatVlanPriority"], value)

    @property
    def FlowStatEthernetDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the Ethernet destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatEthernetDestination"])

    @FlowStatEthernetDestination.setter
    def FlowStatEthernetDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatEthernetDestination"], value)

    @property
    def FlowStatEthernetSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the Ethernet source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatEthernetSource"])

    @FlowStatEthernetSource.setter
    def FlowStatEthernetSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatEthernetSource"], value)

    @property
    def FlowStatEthernetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the type of Ethernet used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatEthernetType"])

    @FlowStatEthernetType.setter
    def FlowStatEthernetType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatEthernetType"], value)

    @property
    def FlowStatInPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the input port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatInPort"])

    @FlowStatInPort.setter
    def FlowStatInPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatInPort"], value)

    @property
    def FlowStatIpDscp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the IP DSCP value for advertising.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatIpDscp"])

    @FlowStatIpDscp.setter
    def FlowStatIpDscp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatIpDscp"], value)

    @property
    def FlowStatIpProtocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the IP protocol used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatIpProtocol"])

    @FlowStatIpProtocol.setter
    def FlowStatIpProtocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatIpProtocol"], value)

    @property
    def FlowStatIpv4Destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the The IPv4 destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatIpv4Destination"])

    @FlowStatIpv4Destination.setter
    def FlowStatIpv4Destination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatIpv4Destination"], value)

    @property
    def FlowStatIpv4Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the The IPv4 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatIpv4Source"])

    @FlowStatIpv4Source.setter
    def FlowStatIpv4Source(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatIpv4Source"], value)

    @property
    def FlowStatOutPortInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom): Specifies the output mode of the Table identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutPortInputMode"])

    @FlowStatOutPortInputMode.setter
    def FlowStatOutPortInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutPortInputMode"], value)

    @property
    def FlowStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatResponseTimeOut"])

    @FlowStatResponseTimeOut.setter
    def FlowStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatResponseTimeOut"], value)

    @property
    def FlowStatTableIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allTables | emergency | custom): Specifies the input mode of the Table identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTableIdInputMode"])

    @FlowStatTableIdInputMode.setter
    def FlowStatTableIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTableIdInputMode"], value)

    @property
    def FlowStatTableIdInputModeNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the identifier input mode of the flow statistics table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTableIdInputModeNumber"])

    @FlowStatTableIdInputModeNumber.setter
    def FlowStatTableIdInputModeNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTableIdInputModeNumber"], value)

    @property
    def FlowStatTransportDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the Transport destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTransportDestination"])

    @FlowStatTransportDestination.setter
    def FlowStatTransportDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTransportDestination"], value)

    @property
    def FlowStatTransportSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the Transport source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTransportSource"])

    @FlowStatTransportSource.setter
    def FlowStatTransportSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTransportSource"], value)

    @property
    def FlowStatVlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the unique VLAN Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatVlanId"])

    @FlowStatVlanId.setter
    def FlowStatVlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatVlanId"], value)

    @property
    def FlowStatVlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the User Priority for this VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatVlanPriority"])

    @FlowStatVlanPriority.setter
    def FlowStatVlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatVlanPriority"], value)

    @property
    def GroupDescriptionStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["GroupDescriptionStatResponseTimeOut"]
        )

    @GroupDescriptionStatResponseTimeOut.setter
    def GroupDescriptionStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["GroupDescriptionStatResponseTimeOut"], value
        )

    @property
    def GroupFeatureStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFeatureStatResponseTimeOut"])

    @GroupFeatureStatResponseTimeOut.setter
    def GroupFeatureStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFeatureStatResponseTimeOut"], value)

    @property
    def GroupId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The ID of the group used. .
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupId"])

    @GroupId.setter
    def GroupId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupId"], value)

    @property
    def GroupIdType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofpgAll | ofpgAny | manual): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupIdType"])

    @GroupIdType.setter
    def GroupIdType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupIdType"], value)

    @property
    def GroupStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatResponseTimeOut"])

    @GroupStatResponseTimeOut.setter
    def GroupStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatResponseTimeOut"], value)

    @property
    def IsAsyncConfStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Queue Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsAsyncConfStatLearnedInformationRefreshed"]
        )

    @property
    def IsDescriptionStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Description Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsDescriptionStatLearnedInformationRefreshed"]
        )

    @property
    def IsFlowAggregatedStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Flow Aggregated Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsFlowAggregatedStatLearnedInformationRefreshed"]
        )

    @property
    def IsFlowStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Flow Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsFlowStatLearnedInformationRefreshed"]
        )

    @property
    def IsGroupDescriptionStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsGroupDescriptionStatLearnedInformationRefreshed"]
        )

    @property
    def IsGroupFeatureStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsGroupFeatureStatLearnedInformationRefreshed"]
        )

    @property
    def IsGroupStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsGroupStatLearnedInformationRefreshed"]
        )

    @property
    def IsOfChannelLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the OF Channels is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsOfChannelLearnedInformationRefreshed"]
        )

    @property
    def IsPortFeaturesLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Checks if the learned information for the port feature Learned Information is refreshed.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsPortFeaturesLearnedInformationRefreshed"]
        )

    @property
    def IsPortStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Port Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsPortStatLearnedInformationRefreshed"]
        )

    @property
    def IsQueueConfigLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the reply for the queue config request is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsQueueConfigLearnedInformationRefreshed"]
        )

    @property
    def IsQueueStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Queue Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsQueueStatLearnedInformationRefreshed"]
        )

    @property
    def IsTableStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Table Statistics is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsTableStatLearnedInformationRefreshed"]
        )

    @property
    def IsVendorStatLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Vendor Statistics is received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsVendorStatLearnedInformationRefreshed"]
        )

    @property
    def PacketOutAuxiliaryId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutAuxiliaryId"])

    @PacketOutAuxiliaryId.setter
    def PacketOutAuxiliaryId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutAuxiliaryId"], value)

    @property
    def PacketOutBufferId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutBufferId"])

    @PacketOutBufferId.setter
    def PacketOutBufferId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutBufferId"], value)

    @property
    def PacketOutBufferIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(opfNoBuffer | manual): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutBufferIdInputMode"])

    @PacketOutBufferIdInputMode.setter
    def PacketOutBufferIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutBufferIdInputMode"], value)

    @property
    def PacketOutData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutData"])

    @PacketOutData.setter
    def PacketOutData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutData"], value)

    @property
    def PacketOutDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutDataLength"])

    @PacketOutDataLength.setter
    def PacketOutDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutDataLength"], value)

    @property
    def PacketOutInPortInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppController | ofppLocal | manual): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutInPortInputMode"])

    @PacketOutInPortInputMode.setter
    def PacketOutInPortInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutInPortInputMode"], value)

    @property
    def PacketOutInPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutInPortNumber"])

    @PacketOutInPortNumber.setter
    def PacketOutInPortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutInPortNumber"], value)

    @property
    def PortFeaturesResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortFeaturesResponseTimeOut"])

    @PortFeaturesResponseTimeOut.setter
    def PortFeaturesResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortFeaturesResponseTimeOut"], value)

    @property
    def PortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the port number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortNumber"])

    @PortNumber.setter
    def PortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortNumber"], value)

    @property
    def PortNumberInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppNone | custom): Specifies the input mode for the Port number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortNumberInputMode"])

    @PortNumberInputMode.setter
    def PortNumberInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortNumberInputMode"], value)

    @property
    def PortStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatResponseTimeOut"])

    @PortStatResponseTimeOut.setter
    def PortStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatResponseTimeOut"], value)

    @property
    def QueueConfigPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the Port for which the queue config request is sought.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigPortNumber"])

    @QueueConfigPortNumber.setter
    def QueueConfigPortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigPortNumber"], value)

    @property
    def QueueConfigResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigResponseTimeOut"])

    @QueueConfigResponseTimeOut.setter
    def QueueConfigResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigResponseTimeOut"], value)

    @property
    def QueueId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the queue ID for which queue statistics is being sought.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueId"])

    @QueueId.setter
    def QueueId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueId"], value)

    @property
    def QueueIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofpqAll | custom): Request queue statistics for the queues belonging to the specified ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueIdInputMode"])

    @QueueIdInputMode.setter
    def QueueIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueIdInputMode"], value)

    @property
    def QueueStatPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the port number for which queue statistics is sought.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatPortNumber"])

    @QueueStatPortNumber.setter
    def QueueStatPortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatPortNumber"], value)

    @property
    def QueueStatPortNumberInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppAll | custom): Indicates the ports for which queue statistics is sought.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatPortNumberInputMode"])

    @QueueStatPortNumberInputMode.setter
    def QueueStatPortNumberInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatPortNumberInputMode"], value)

    @property
    def QueueStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatResponseTimeOut"])

    @QueueStatResponseTimeOut.setter
    def QueueStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatResponseTimeOut"], value)

    @property
    def RoleRequestGenerationId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The generation ID number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRequestGenerationId"])

    @RoleRequestGenerationId.setter
    def RoleRequestGenerationId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRequestGenerationId"], value)

    @property
    def RoleRequestType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(equal | master | slave | noChange): Select the type of role for the controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRequestType"])

    @RoleRequestType.setter
    def RoleRequestType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRequestType"], value)

    @property
    def SwitchConfigDropFragments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigDropFragments"])

    @SwitchConfigDropFragments.setter
    def SwitchConfigDropFragments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigDropFragments"], value)

    @property
    def SwitchConfigMissSendLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigMissSendLength"])

    @SwitchConfigMissSendLength.setter
    def SwitchConfigMissSendLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigMissSendLength"], value)

    @property
    def SwitchConfigReassembleFragments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigReassembleFragments"])

    @SwitchConfigReassembleFragments.setter
    def SwitchConfigReassembleFragments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigReassembleFragments"], value)

    @property
    def SwitchConfigResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigResponseTimeOut"])

    @SwitchConfigResponseTimeOut.setter
    def SwitchConfigResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigResponseTimeOut"], value)

    @property
    def TableFeatureConfig(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The bitmap of OFPTC_* values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureConfig"])

    @TableFeatureConfig.setter
    def TableFeatureConfig(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureConfig"], value)

    @property
    def TableFeatureMaxEntries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of entries supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureMaxEntries"])

    @TableFeatureMaxEntries.setter
    def TableFeatureMaxEntries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureMaxEntries"], value)

    @property
    def TableFeatureMetadataMatch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The bits of metadata which the table can match.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureMetadataMatch"])

    @TableFeatureMetadataMatch.setter
    def TableFeatureMetadataMatch(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureMetadataMatch"], value)

    @property
    def TableFeatureMetadataWrite(self):
        # type: () -> str
        """
        Returns
        -------
        - str: MetaData Write The bits of metadata which the table can write.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureMetadataWrite"])

    @TableFeatureMetadataWrite.setter
    def TableFeatureMetadataWrite(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureMetadataWrite"], value)

    @property
    def TableFeatureName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The table name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureName"])

    @TableFeatureName.setter
    def TableFeatureName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureName"], value)

    @property
    def TableFeatureResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureResponseTimeOut"])

    @TableFeatureResponseTimeOut.setter
    def TableFeatureResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureResponseTimeOut"], value)

    @property
    def TableFeatureTableId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The table identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureTableId"])

    @TableFeatureTableId.setter
    def TableFeatureTableId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureTableId"], value)

    @property
    def TableStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatResponseTimeOut"])

    @TableStatResponseTimeOut.setter
    def TableStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatResponseTimeOut"], value)

    @property
    def TriggeredVendorMessage(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the vendor data of the vendor message trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggeredVendorMessage"])

    @TriggeredVendorMessage.setter
    def TriggeredVendorMessage(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggeredVendorMessage"], value)

    @property
    def TriggeredVendorMessageId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the ID of the vendor for which vendor message is triggered.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggeredVendorMessageId"])

    @TriggeredVendorMessageId.setter
    def TriggeredVendorMessageId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggeredVendorMessageId"], value)

    @property
    def TriggeredVendorMessageLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the length of vendor data of the vendor message trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggeredVendorMessageLength"])

    @TriggeredVendorMessageLength.setter
    def TriggeredVendorMessageLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggeredVendorMessageLength"], value)

    @property
    def VendorId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the unique Vendor identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorId"])

    @VendorId.setter
    def VendorId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorId"], value)

    @property
    def VendorMessage(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Speciifes the vendor message value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMessage"])

    @VendorMessage.setter
    def VendorMessage(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMessage"], value)

    @property
    def VendorMessageLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the length of the message being transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMessageLength"])

    @VendorMessageLength.setter
    def VendorMessageLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMessageLength"], value)

    @property
    def VendorStateResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStateResponseTimeOut"])

    @VendorStateResponseTimeOut.setter
    def VendorStateResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStateResponseTimeOut"], value)

    def update(
        self,
        AsyncConfStatResponseTimeOut=None,
        DescriptionStatResponseTimeOut=None,
        EnableAsyncConfMasterFlowRemovedFlowDelete=None,
        EnableAsyncConfMasterFlowRemovedGroupDelete=None,
        EnableAsyncConfMasterFlowRemovedHardTimeOut=None,
        EnableAsyncConfMasterFlowRemovedIdleTimeOut=None,
        EnableAsyncConfMasterPacketInActionOutputToController=None,
        EnableAsyncConfMasterPacketInInvalidTtl=None,
        EnableAsyncConfMasterPacketInNoMatching=None,
        EnableAsyncConfMasterPortStatusAdd=None,
        EnableAsyncConfMasterPortStatusDelete=None,
        EnableAsyncConfMasterPortStatusModify=None,
        EnableAsyncConfSlaveFlowRemovedFlowDelete=None,
        EnableAsyncConfSlaveFlowRemovedGroupDelete=None,
        EnableAsyncConfSlaveFlowRemovedHardTimeOut=None,
        EnableAsyncConfSlaveFlowRemovedIdleTimeOut=None,
        EnableAsyncConfSlavePacketInActionOutputToController=None,
        EnableAsyncConfSlavePacketInInvalidTtl=None,
        EnableAsyncConfSlavePacketInNoMatching=None,
        EnableAsyncConfSlavePortStatusAdd=None,
        EnableAsyncConfSlavePortStatusDelete=None,
        EnableAsyncConfSlavePortStatusModify=None,
        EnableFlowAggregatedStatMatchCapability=None,
        EnableFlowStatMatchCapability=None,
        EnableGroupStatMatchCapability=None,
        EnablePortStatMatchCapability=None,
        EnableQueueStatMatchCapability=None,
        EnableSendTableFeaturesTrigger=None,
        EnableSendTriggerPortFeaturesLearnedInformation=None,
        EnableSendTriggeredAsyncConfStatLearnedInformation=None,
        EnableSendTriggeredBarrierRequestMessage=None,
        EnableSendTriggeredDescriptionStatLearnedInformation=None,
        EnableSendTriggeredFlowAggregatedStatLearnedInformation=None,
        EnableSendTriggeredFlowStatLearnedInformation=None,
        EnableSendTriggeredGroupDescriptionStatLearnedInformation=None,
        EnableSendTriggeredGroupFeatureStatLearnedInformation=None,
        EnableSendTriggeredGroupStatLearnedInformation=None,
        EnableSendTriggeredPacketOutMessage=None,
        EnableSendTriggeredPortModificationMessage=None,
        EnableSendTriggeredPortStatLearnedInformation=None,
        EnableSendTriggeredQueueConfigLearnedInformation=None,
        EnableSendTriggeredQueueStatLearnedInformation=None,
        EnableSendTriggeredRoleRequestMessage=None,
        EnableSendTriggeredSwitchConfigLearnedInformation=None,
        EnableSendTriggeredTableStatLearnedInformation=None,
        EnableSendTriggeredVendorStatLearnedInformation=None,
        EnableSetAsyncConfig=None,
        EnableSetSwitchConfig=None,
        EnableSetTableFeatures=None,
        EnableTableStatMatchCapability=None,
        EnableTriggeredVendorMessage=None,
        FlowAggregatedStatEthernetDestination=None,
        FlowAggregatedStatEthernetSource=None,
        FlowAggregatedStatEthernetType=None,
        FlowAggregatedStatInPort=None,
        FlowAggregatedStatIpDscp=None,
        FlowAggregatedStatIpProtocol=None,
        FlowAggregatedStatIpv4Destination=None,
        FlowAggregatedStatIpv4Source=None,
        FlowAggregatedStatOutPortInputMode=None,
        FlowAggregatedStatResponseTimeOut=None,
        FlowAggregatedStatTableIdInputMode=None,
        FlowAggregatedStatTableIdInputModeNumber=None,
        FlowAggregatedStatTransportDestination=None,
        FlowAggregatedStatTransportSource=None,
        FlowAggregatedStatVlanId=None,
        FlowAggregatedStatVlanPriority=None,
        FlowStatEthernetDestination=None,
        FlowStatEthernetSource=None,
        FlowStatEthernetType=None,
        FlowStatInPort=None,
        FlowStatIpDscp=None,
        FlowStatIpProtocol=None,
        FlowStatIpv4Destination=None,
        FlowStatIpv4Source=None,
        FlowStatOutPortInputMode=None,
        FlowStatResponseTimeOut=None,
        FlowStatTableIdInputMode=None,
        FlowStatTableIdInputModeNumber=None,
        FlowStatTransportDestination=None,
        FlowStatTransportSource=None,
        FlowStatVlanId=None,
        FlowStatVlanPriority=None,
        GroupDescriptionStatResponseTimeOut=None,
        GroupFeatureStatResponseTimeOut=None,
        GroupId=None,
        GroupIdType=None,
        GroupStatResponseTimeOut=None,
        PacketOutAuxiliaryId=None,
        PacketOutBufferId=None,
        PacketOutBufferIdInputMode=None,
        PacketOutData=None,
        PacketOutDataLength=None,
        PacketOutInPortInputMode=None,
        PacketOutInPortNumber=None,
        PortFeaturesResponseTimeOut=None,
        PortNumber=None,
        PortNumberInputMode=None,
        PortStatResponseTimeOut=None,
        QueueConfigPortNumber=None,
        QueueConfigResponseTimeOut=None,
        QueueId=None,
        QueueIdInputMode=None,
        QueueStatPortNumber=None,
        QueueStatPortNumberInputMode=None,
        QueueStatResponseTimeOut=None,
        RoleRequestGenerationId=None,
        RoleRequestType=None,
        SwitchConfigDropFragments=None,
        SwitchConfigMissSendLength=None,
        SwitchConfigReassembleFragments=None,
        SwitchConfigResponseTimeOut=None,
        TableFeatureConfig=None,
        TableFeatureMaxEntries=None,
        TableFeatureMetadataMatch=None,
        TableFeatureMetadataWrite=None,
        TableFeatureName=None,
        TableFeatureResponseTimeOut=None,
        TableFeatureTableId=None,
        TableStatResponseTimeOut=None,
        TriggeredVendorMessage=None,
        TriggeredVendorMessageId=None,
        TriggeredVendorMessageLength=None,
        VendorId=None,
        VendorMessage=None,
        VendorMessageLength=None,
        VendorStateResponseTimeOut=None,
    ):
        # type: (int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, str, str, str, str, str, str, str, int, str, int, str, str, str, str, str, str, str, str, str, str, str, str, str, int, str, int, str, str, str, str, int, int, int, str, int, int, int, str, str, int, str, int, int, int, str, int, int, int, int, str, int, str, int, str, str, bool, int, bool, int, int, int, str, str, str, int, int, int, str, int, int, int, str, int, int) -> LearnedInformation
        """Updates learnedInformation resource on the server.

        Args
        ----
        - AsyncConfStatResponseTimeOut (number): NOT DEFINED
        - DescriptionStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.
        - EnableAsyncConfMasterFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.
        - EnableAsyncConfMasterFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.
        - EnableAsyncConfMasterFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.
        - EnableAsyncConfMasterFlowRemovedIdleTimeOut (bool): NOT DEFINED
        - EnableAsyncConfMasterPacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.
        - EnableAsyncConfMasterPacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.
        - EnableAsyncConfMasterPacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.
        - EnableAsyncConfMasterPortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.
        - EnableAsyncConfMasterPortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.
        - EnableAsyncConfMasterPortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        - EnableAsyncConfSlaveFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.
        - EnableAsyncConfSlaveFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.
        - EnableAsyncConfSlaveFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.
        - EnableAsyncConfSlaveFlowRemovedIdleTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.
        - EnableAsyncConfSlavePacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.
        - EnableAsyncConfSlavePacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.
        - EnableAsyncConfSlavePacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.
        - EnableAsyncConfSlavePortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.
        - EnableAsyncConfSlavePortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        - EnableAsyncConfSlavePortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.
        - EnableFlowAggregatedStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Aggregated Statistics
        - EnableFlowStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Statistics
        - EnableGroupStatMatchCapability (bool): If enabled,it denotes that the enable Group Statistics Match Capability is received.
        - EnablePortStatMatchCapability (bool): Checks to see if the switch has the capability to publish Port Statistics
        - EnableQueueStatMatchCapability (bool): If true, the switch has the capability to publish Queue Statistics.
        - EnableSendTableFeaturesTrigger (bool): If enabled,it denotes that the enable Send Table Features Trigger is received.
        - EnableSendTriggerPortFeaturesLearnedInformation (bool): Enables Trigger for port features learned information.
        - EnableSendTriggeredAsyncConfStatLearnedInformation (bool): If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.
        - EnableSendTriggeredBarrierRequestMessage (bool): If true, enables trigger for barrier request message
        - EnableSendTriggeredDescriptionStatLearnedInformation (bool): If true, the description statistic trigger configuration parameters are available.
        - EnableSendTriggeredFlowAggregatedStatLearnedInformation (bool): If true, the flow aggregated statistic trigger configuration parameters are available.
        - EnableSendTriggeredFlowStatLearnedInformation (bool): If true, the flow statistic trigger configuration parameters are available.
        - EnableSendTriggeredGroupDescriptionStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.
        - EnableSendTriggeredGroupFeatureStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.
        - EnableSendTriggeredGroupStatLearnedInformation (bool): If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.
        - EnableSendTriggeredPacketOutMessage (bool): If enabled,it denotes that the enable Send Triggered Packet Out Message is received.
        - EnableSendTriggeredPortModificationMessage (bool): If enabled,it denotes that the enable Send Triggered Port Modification Message is received.
        - EnableSendTriggeredPortStatLearnedInformation (bool): If true, the port statistic trigger configuration parameters are available.
        - EnableSendTriggeredQueueConfigLearnedInformation (bool): If true, the queue config trigger configuration parameters are available.
        - EnableSendTriggeredQueueStatLearnedInformation (bool): If true, the queue statistic trigger configuration parameters are available.
        - EnableSendTriggeredRoleRequestMessage (bool): If enabled,it denotes that the Triggered Role Request Message is received.
        - EnableSendTriggeredSwitchConfigLearnedInformation (bool): If enabled,it denotes that the enable Switch Configuration Learned Information is received.
        - EnableSendTriggeredTableStatLearnedInformation (bool): If true, the table statistic trigger configuration parameters are available.
        - EnableSendTriggeredVendorStatLearnedInformation (bool): If true, the vendor statistic trigger configuration parameters are available.
        - EnableSetAsyncConfig (bool): If enabled,it denotes that the Set Asynchronous Configuration is received.
        - EnableSetSwitchConfig (bool): If enabled,it denotes that the enable Set Switch Configuration is received.
        - EnableSetTableFeatures (bool): NOT DEFINED
        - EnableTableStatMatchCapability (bool): If true, the switch has the capability to publish Table Statistics.
        - EnableTriggeredVendorMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - FlowAggregatedStatEthernetDestination (str): Signifies the ethernet destination address.
        - FlowAggregatedStatEthernetSource (str): Signifies the ethernet source address.
        - FlowAggregatedStatEthernetType (str): Signifies the type of Ethernet used.
        - FlowAggregatedStatInPort (str): Signifies the input port used.
        - FlowAggregatedStatIpDscp (str): Signifies the IP DSCP value for advertising.
        - FlowAggregatedStatIpProtocol (str): Signifies the IP protocol used.
        - FlowAggregatedStatIpv4Destination (str): Signifies the IPv4 destination address.
        - FlowAggregatedStatIpv4Source (str): Signifies the IPv4 source address.
        - FlowAggregatedStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): Signifies the identifier output mode of the aggregated flow statistics table.
        - FlowAggregatedStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.
        - FlowAggregatedStatTableIdInputMode (str(allTables | emergency | custom)): Signifies the identifier input mode of the flow aggregated statistics table.
        - FlowAggregatedStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow aggregated statistics table.
        - FlowAggregatedStatTransportDestination (str): Signifies the Transport destination address.
        - FlowAggregatedStatTransportSource (str): Signifies the Transport source address.
        - FlowAggregatedStatVlanId (str): Signifies the unique VLAN Identifier.
        - FlowAggregatedStatVlanPriority (str): Signifies the User Priority for this VLAN.
        - FlowStatEthernetDestination (str): Specifies the Ethernet destination address.
        - FlowStatEthernetSource (str): Specifies the Ethernet source address.
        - FlowStatEthernetType (str): Specifies the type of Ethernet used.
        - FlowStatInPort (str): Specifies the input port used.
        - FlowStatIpDscp (str): Specifies the IP DSCP value for advertising.
        - FlowStatIpProtocol (str): Specifies the IP protocol used.
        - FlowStatIpv4Destination (str): Specifies the The IPv4 destination address.
        - FlowStatIpv4Source (str): Specifies the The IPv4 source address.
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): Specifies the output mode of the Table identifier.
        - FlowStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no response is received.
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): Specifies the input mode of the Table identifier.
        - FlowStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow statistics table.
        - FlowStatTransportDestination (str): Specifies the Transport destination address.
        - FlowStatTransportSource (str): Specifies the Transport source address.
        - FlowStatVlanId (str): Specifies the unique VLAN Identifier.
        - FlowStatVlanPriority (str): Specifies the User Priority for this VLAN.
        - GroupDescriptionStatResponseTimeOut (number): NOT DEFINED
        - GroupFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - GroupId (number): The ID of the group used. .
        - GroupIdType (str(ofpgAll | ofpgAny | manual)): NOT DEFINED
        - GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - PacketOutAuxiliaryId (number): NOT DEFINED
        - PacketOutBufferId (number): NOT DEFINED
        - PacketOutBufferIdInputMode (str(opfNoBuffer | manual)): NOT DEFINED
        - PacketOutData (str): NOT DEFINED
        - PacketOutDataLength (number): NOT DEFINED
        - PacketOutInPortInputMode (str(ofppController | ofppLocal | manual)): NOT DEFINED
        - PacketOutInPortNumber (number): NOT DEFINED
        - PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - PortNumber (number): Specifies the port number.
        - PortNumberInputMode (str(ofppNone | custom)): Specifies the input mode for the Port number.
        - PortStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.
        - QueueConfigPortNumber (number): Indicates the Port for which the queue config request is sought.
        - QueueConfigResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.
        - QueueId (number): Indicates the queue ID for which queue statistics is being sought.
        - QueueIdInputMode (str(ofpqAll | custom)): Request queue statistics for the queues belonging to the specified ports.
        - QueueStatPortNumber (number): Specifies the port number for which queue statistics is sought.
        - QueueStatPortNumberInputMode (str(ofppAll | custom)): Indicates the ports for which queue statistics is sought.
        - QueueStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.
        - RoleRequestGenerationId (str): The generation ID number.
        - RoleRequestType (str(equal | master | slave | noChange)): Select the type of role for the controller.
        - SwitchConfigDropFragments (bool): NOT DEFINED
        - SwitchConfigMissSendLength (number): NOT DEFINED
        - SwitchConfigReassembleFragments (bool): NOT DEFINED
        - SwitchConfigResponseTimeOut (number): NOT DEFINED
        - TableFeatureConfig (number): The bitmap of OFPTC_* values.
        - TableFeatureMaxEntries (number): The maximum number of entries supported.
        - TableFeatureMetadataMatch (str): The bits of metadata which the table can match.
        - TableFeatureMetadataWrite (str): MetaData Write The bits of metadata which the table can write.
        - TableFeatureName (str): The table name.
        - TableFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - TableFeatureTableId (number): The table identifier.
        - TableStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.
        - TriggeredVendorMessage (str): Indicates the vendor data of the vendor message trigger.
        - TriggeredVendorMessageId (number): Indicates the ID of the vendor for which vendor message is triggered.
        - TriggeredVendorMessageLength (number): Indicates the length of vendor data of the vendor message trigger.
        - VendorId (number): Specifies the unique Vendor identifier.
        - VendorMessage (str): Speciifes the vendor message value.
        - VendorMessageLength (number): Specifies the length of the message being transmitted.
        - VendorStateResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AsyncConfStatResponseTimeOut=None,
        DescriptionStatResponseTimeOut=None,
        EnableAsyncConfMasterFlowRemovedFlowDelete=None,
        EnableAsyncConfMasterFlowRemovedGroupDelete=None,
        EnableAsyncConfMasterFlowRemovedHardTimeOut=None,
        EnableAsyncConfMasterFlowRemovedIdleTimeOut=None,
        EnableAsyncConfMasterPacketInActionOutputToController=None,
        EnableAsyncConfMasterPacketInInvalidTtl=None,
        EnableAsyncConfMasterPacketInNoMatching=None,
        EnableAsyncConfMasterPortStatusAdd=None,
        EnableAsyncConfMasterPortStatusDelete=None,
        EnableAsyncConfMasterPortStatusModify=None,
        EnableAsyncConfSlaveFlowRemovedFlowDelete=None,
        EnableAsyncConfSlaveFlowRemovedGroupDelete=None,
        EnableAsyncConfSlaveFlowRemovedHardTimeOut=None,
        EnableAsyncConfSlaveFlowRemovedIdleTimeOut=None,
        EnableAsyncConfSlavePacketInActionOutputToController=None,
        EnableAsyncConfSlavePacketInInvalidTtl=None,
        EnableAsyncConfSlavePacketInNoMatching=None,
        EnableAsyncConfSlavePortStatusAdd=None,
        EnableAsyncConfSlavePortStatusDelete=None,
        EnableAsyncConfSlavePortStatusModify=None,
        EnableFlowAggregatedStatMatchCapability=None,
        EnableFlowStatMatchCapability=None,
        EnableGroupStatMatchCapability=None,
        EnablePortStatMatchCapability=None,
        EnableQueueStatMatchCapability=None,
        EnableSendTableFeaturesTrigger=None,
        EnableSendTriggerPortFeaturesLearnedInformation=None,
        EnableSendTriggeredAsyncConfStatLearnedInformation=None,
        EnableSendTriggeredBarrierRequestMessage=None,
        EnableSendTriggeredDescriptionStatLearnedInformation=None,
        EnableSendTriggeredFlowAggregatedStatLearnedInformation=None,
        EnableSendTriggeredFlowStatLearnedInformation=None,
        EnableSendTriggeredGroupDescriptionStatLearnedInformation=None,
        EnableSendTriggeredGroupFeatureStatLearnedInformation=None,
        EnableSendTriggeredGroupStatLearnedInformation=None,
        EnableSendTriggeredPacketOutMessage=None,
        EnableSendTriggeredPortModificationMessage=None,
        EnableSendTriggeredPortStatLearnedInformation=None,
        EnableSendTriggeredQueueConfigLearnedInformation=None,
        EnableSendTriggeredQueueStatLearnedInformation=None,
        EnableSendTriggeredRoleRequestMessage=None,
        EnableSendTriggeredSwitchConfigLearnedInformation=None,
        EnableSendTriggeredTableStatLearnedInformation=None,
        EnableSendTriggeredVendorStatLearnedInformation=None,
        EnableSetAsyncConfig=None,
        EnableSetSwitchConfig=None,
        EnableSetTableFeatures=None,
        EnableTableStatMatchCapability=None,
        EnableTriggeredVendorMessage=None,
        FlowAggregatedStatEthernetDestination=None,
        FlowAggregatedStatEthernetSource=None,
        FlowAggregatedStatEthernetType=None,
        FlowAggregatedStatInPort=None,
        FlowAggregatedStatIpDscp=None,
        FlowAggregatedStatIpProtocol=None,
        FlowAggregatedStatIpv4Destination=None,
        FlowAggregatedStatIpv4Source=None,
        FlowAggregatedStatOutPortInputMode=None,
        FlowAggregatedStatResponseTimeOut=None,
        FlowAggregatedStatTableIdInputMode=None,
        FlowAggregatedStatTableIdInputModeNumber=None,
        FlowAggregatedStatTransportDestination=None,
        FlowAggregatedStatTransportSource=None,
        FlowAggregatedStatVlanId=None,
        FlowAggregatedStatVlanPriority=None,
        FlowStatEthernetDestination=None,
        FlowStatEthernetSource=None,
        FlowStatEthernetType=None,
        FlowStatInPort=None,
        FlowStatIpDscp=None,
        FlowStatIpProtocol=None,
        FlowStatIpv4Destination=None,
        FlowStatIpv4Source=None,
        FlowStatOutPortInputMode=None,
        FlowStatResponseTimeOut=None,
        FlowStatTableIdInputMode=None,
        FlowStatTableIdInputModeNumber=None,
        FlowStatTransportDestination=None,
        FlowStatTransportSource=None,
        FlowStatVlanId=None,
        FlowStatVlanPriority=None,
        GroupDescriptionStatResponseTimeOut=None,
        GroupFeatureStatResponseTimeOut=None,
        GroupId=None,
        GroupIdType=None,
        GroupStatResponseTimeOut=None,
        IsAsyncConfStatLearnedInformationRefreshed=None,
        IsDescriptionStatLearnedInformationRefreshed=None,
        IsFlowAggregatedStatLearnedInformationRefreshed=None,
        IsFlowStatLearnedInformationRefreshed=None,
        IsGroupDescriptionStatLearnedInformationRefreshed=None,
        IsGroupFeatureStatLearnedInformationRefreshed=None,
        IsGroupStatLearnedInformationRefreshed=None,
        IsOfChannelLearnedInformationRefreshed=None,
        IsPortFeaturesLearnedInformationRefreshed=None,
        IsPortStatLearnedInformationRefreshed=None,
        IsQueueConfigLearnedInformationRefreshed=None,
        IsQueueStatLearnedInformationRefreshed=None,
        IsTableStatLearnedInformationRefreshed=None,
        IsVendorStatLearnedInformationRefreshed=None,
        PacketOutAuxiliaryId=None,
        PacketOutBufferId=None,
        PacketOutBufferIdInputMode=None,
        PacketOutData=None,
        PacketOutDataLength=None,
        PacketOutInPortInputMode=None,
        PacketOutInPortNumber=None,
        PortFeaturesResponseTimeOut=None,
        PortNumber=None,
        PortNumberInputMode=None,
        PortStatResponseTimeOut=None,
        QueueConfigPortNumber=None,
        QueueConfigResponseTimeOut=None,
        QueueId=None,
        QueueIdInputMode=None,
        QueueStatPortNumber=None,
        QueueStatPortNumberInputMode=None,
        QueueStatResponseTimeOut=None,
        RoleRequestGenerationId=None,
        RoleRequestType=None,
        SwitchConfigDropFragments=None,
        SwitchConfigMissSendLength=None,
        SwitchConfigReassembleFragments=None,
        SwitchConfigResponseTimeOut=None,
        TableFeatureConfig=None,
        TableFeatureMaxEntries=None,
        TableFeatureMetadataMatch=None,
        TableFeatureMetadataWrite=None,
        TableFeatureName=None,
        TableFeatureResponseTimeOut=None,
        TableFeatureTableId=None,
        TableStatResponseTimeOut=None,
        TriggeredVendorMessage=None,
        TriggeredVendorMessageId=None,
        TriggeredVendorMessageLength=None,
        VendorId=None,
        VendorMessage=None,
        VendorMessageLength=None,
        VendorStateResponseTimeOut=None,
    ):
        # type: (int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, str, str, str, str, str, str, str, int, str, int, str, str, str, str, str, str, str, str, str, str, str, str, str, int, str, int, str, str, str, str, int, int, int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, str, int, str, int, int, int, str, int, int, int, int, str, int, str, int, str, str, bool, int, bool, int, int, int, str, str, str, int, int, int, str, int, int, int, str, int, int) -> LearnedInformation
        """Finds and retrieves learnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInformation resources from the server.

        Args
        ----
        - AsyncConfStatResponseTimeOut (number): NOT DEFINED
        - DescriptionStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.
        - EnableAsyncConfMasterFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.
        - EnableAsyncConfMasterFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.
        - EnableAsyncConfMasterFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.
        - EnableAsyncConfMasterFlowRemovedIdleTimeOut (bool): NOT DEFINED
        - EnableAsyncConfMasterPacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.
        - EnableAsyncConfMasterPacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.
        - EnableAsyncConfMasterPacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.
        - EnableAsyncConfMasterPortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.
        - EnableAsyncConfMasterPortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.
        - EnableAsyncConfMasterPortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        - EnableAsyncConfSlaveFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.
        - EnableAsyncConfSlaveFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.
        - EnableAsyncConfSlaveFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.
        - EnableAsyncConfSlaveFlowRemovedIdleTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.
        - EnableAsyncConfSlavePacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.
        - EnableAsyncConfSlavePacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.
        - EnableAsyncConfSlavePacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.
        - EnableAsyncConfSlavePortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.
        - EnableAsyncConfSlavePortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        - EnableAsyncConfSlavePortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.
        - EnableFlowAggregatedStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Aggregated Statistics
        - EnableFlowStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Statistics
        - EnableGroupStatMatchCapability (bool): If enabled,it denotes that the enable Group Statistics Match Capability is received.
        - EnablePortStatMatchCapability (bool): Checks to see if the switch has the capability to publish Port Statistics
        - EnableQueueStatMatchCapability (bool): If true, the switch has the capability to publish Queue Statistics.
        - EnableSendTableFeaturesTrigger (bool): If enabled,it denotes that the enable Send Table Features Trigger is received.
        - EnableSendTriggerPortFeaturesLearnedInformation (bool): Enables Trigger for port features learned information.
        - EnableSendTriggeredAsyncConfStatLearnedInformation (bool): If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.
        - EnableSendTriggeredBarrierRequestMessage (bool): If true, enables trigger for barrier request message
        - EnableSendTriggeredDescriptionStatLearnedInformation (bool): If true, the description statistic trigger configuration parameters are available.
        - EnableSendTriggeredFlowAggregatedStatLearnedInformation (bool): If true, the flow aggregated statistic trigger configuration parameters are available.
        - EnableSendTriggeredFlowStatLearnedInformation (bool): If true, the flow statistic trigger configuration parameters are available.
        - EnableSendTriggeredGroupDescriptionStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.
        - EnableSendTriggeredGroupFeatureStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.
        - EnableSendTriggeredGroupStatLearnedInformation (bool): If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.
        - EnableSendTriggeredPacketOutMessage (bool): If enabled,it denotes that the enable Send Triggered Packet Out Message is received.
        - EnableSendTriggeredPortModificationMessage (bool): If enabled,it denotes that the enable Send Triggered Port Modification Message is received.
        - EnableSendTriggeredPortStatLearnedInformation (bool): If true, the port statistic trigger configuration parameters are available.
        - EnableSendTriggeredQueueConfigLearnedInformation (bool): If true, the queue config trigger configuration parameters are available.
        - EnableSendTriggeredQueueStatLearnedInformation (bool): If true, the queue statistic trigger configuration parameters are available.
        - EnableSendTriggeredRoleRequestMessage (bool): If enabled,it denotes that the Triggered Role Request Message is received.
        - EnableSendTriggeredSwitchConfigLearnedInformation (bool): If enabled,it denotes that the enable Switch Configuration Learned Information is received.
        - EnableSendTriggeredTableStatLearnedInformation (bool): If true, the table statistic trigger configuration parameters are available.
        - EnableSendTriggeredVendorStatLearnedInformation (bool): If true, the vendor statistic trigger configuration parameters are available.
        - EnableSetAsyncConfig (bool): If enabled,it denotes that the Set Asynchronous Configuration is received.
        - EnableSetSwitchConfig (bool): If enabled,it denotes that the enable Set Switch Configuration is received.
        - EnableSetTableFeatures (bool): NOT DEFINED
        - EnableTableStatMatchCapability (bool): If true, the switch has the capability to publish Table Statistics.
        - EnableTriggeredVendorMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - FlowAggregatedStatEthernetDestination (str): Signifies the ethernet destination address.
        - FlowAggregatedStatEthernetSource (str): Signifies the ethernet source address.
        - FlowAggregatedStatEthernetType (str): Signifies the type of Ethernet used.
        - FlowAggregatedStatInPort (str): Signifies the input port used.
        - FlowAggregatedStatIpDscp (str): Signifies the IP DSCP value for advertising.
        - FlowAggregatedStatIpProtocol (str): Signifies the IP protocol used.
        - FlowAggregatedStatIpv4Destination (str): Signifies the IPv4 destination address.
        - FlowAggregatedStatIpv4Source (str): Signifies the IPv4 source address.
        - FlowAggregatedStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): Signifies the identifier output mode of the aggregated flow statistics table.
        - FlowAggregatedStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.
        - FlowAggregatedStatTableIdInputMode (str(allTables | emergency | custom)): Signifies the identifier input mode of the flow aggregated statistics table.
        - FlowAggregatedStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow aggregated statistics table.
        - FlowAggregatedStatTransportDestination (str): Signifies the Transport destination address.
        - FlowAggregatedStatTransportSource (str): Signifies the Transport source address.
        - FlowAggregatedStatVlanId (str): Signifies the unique VLAN Identifier.
        - FlowAggregatedStatVlanPriority (str): Signifies the User Priority for this VLAN.
        - FlowStatEthernetDestination (str): Specifies the Ethernet destination address.
        - FlowStatEthernetSource (str): Specifies the Ethernet source address.
        - FlowStatEthernetType (str): Specifies the type of Ethernet used.
        - FlowStatInPort (str): Specifies the input port used.
        - FlowStatIpDscp (str): Specifies the IP DSCP value for advertising.
        - FlowStatIpProtocol (str): Specifies the IP protocol used.
        - FlowStatIpv4Destination (str): Specifies the The IPv4 destination address.
        - FlowStatIpv4Source (str): Specifies the The IPv4 source address.
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): Specifies the output mode of the Table identifier.
        - FlowStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no response is received.
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): Specifies the input mode of the Table identifier.
        - FlowStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow statistics table.
        - FlowStatTransportDestination (str): Specifies the Transport destination address.
        - FlowStatTransportSource (str): Specifies the Transport source address.
        - FlowStatVlanId (str): Specifies the unique VLAN Identifier.
        - FlowStatVlanPriority (str): Specifies the User Priority for this VLAN.
        - GroupDescriptionStatResponseTimeOut (number): NOT DEFINED
        - GroupFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - GroupId (number): The ID of the group used. .
        - GroupIdType (str(ofpgAll | ofpgAny | manual)): NOT DEFINED
        - GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - IsAsyncConfStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Queue Statistics is received.
        - IsDescriptionStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Description Statistics is received.
        - IsFlowAggregatedStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Flow Aggregated Statistics is received.
        - IsFlowStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Flow Statistics is received.
        - IsGroupDescriptionStatLearnedInformationRefreshed (bool): NOT DEFINED
        - IsGroupFeatureStatLearnedInformationRefreshed (bool): NOT DEFINED
        - IsGroupStatLearnedInformationRefreshed (bool): NOT DEFINED
        - IsOfChannelLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the OF Channels is received.
        - IsPortFeaturesLearnedInformationRefreshed (bool): Checks if the learned information for the port feature Learned Information is refreshed.
        - IsPortStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Port Statistics is received.
        - IsQueueConfigLearnedInformationRefreshed (bool): If true, it denotes that the reply for the queue config request is received.
        - IsQueueStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Queue Statistics is received.
        - IsTableStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Table Statistics is received.
        - IsVendorStatLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the Vendor Statistics is received
        - PacketOutAuxiliaryId (number): NOT DEFINED
        - PacketOutBufferId (number): NOT DEFINED
        - PacketOutBufferIdInputMode (str(opfNoBuffer | manual)): NOT DEFINED
        - PacketOutData (str): NOT DEFINED
        - PacketOutDataLength (number): NOT DEFINED
        - PacketOutInPortInputMode (str(ofppController | ofppLocal | manual)): NOT DEFINED
        - PacketOutInPortNumber (number): NOT DEFINED
        - PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - PortNumber (number): Specifies the port number.
        - PortNumberInputMode (str(ofppNone | custom)): Specifies the input mode for the Port number.
        - PortStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.
        - QueueConfigPortNumber (number): Indicates the Port for which the queue config request is sought.
        - QueueConfigResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.
        - QueueId (number): Indicates the queue ID for which queue statistics is being sought.
        - QueueIdInputMode (str(ofpqAll | custom)): Request queue statistics for the queues belonging to the specified ports.
        - QueueStatPortNumber (number): Specifies the port number for which queue statistics is sought.
        - QueueStatPortNumberInputMode (str(ofppAll | custom)): Indicates the ports for which queue statistics is sought.
        - QueueStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.
        - RoleRequestGenerationId (str): The generation ID number.
        - RoleRequestType (str(equal | master | slave | noChange)): Select the type of role for the controller.
        - SwitchConfigDropFragments (bool): NOT DEFINED
        - SwitchConfigMissSendLength (number): NOT DEFINED
        - SwitchConfigReassembleFragments (bool): NOT DEFINED
        - SwitchConfigResponseTimeOut (number): NOT DEFINED
        - TableFeatureConfig (number): The bitmap of OFPTC_* values.
        - TableFeatureMaxEntries (number): The maximum number of entries supported.
        - TableFeatureMetadataMatch (str): The bits of metadata which the table can match.
        - TableFeatureMetadataWrite (str): MetaData Write The bits of metadata which the table can write.
        - TableFeatureName (str): The table name.
        - TableFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - TableFeatureTableId (number): The table identifier.
        - TableStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.
        - TriggeredVendorMessage (str): Indicates the vendor data of the vendor message trigger.
        - TriggeredVendorMessageId (number): Indicates the ID of the vendor for which vendor message is triggered.
        - TriggeredVendorMessageLength (number): Indicates the length of vendor data of the vendor message trigger.
        - VendorId (number): Specifies the unique Vendor identifier.
        - VendorMessage (str): Speciifes the vendor message value.
        - VendorMessageLength (number): Specifies the length of the message being transmitted.
        - VendorStateResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.

        Returns
        -------
        - self: This instance with matching learnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearRecordsForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the clearRecordsForTrigger operation on the server.

        This describes the record cleared for trigger settings.

        clearRecordsForTrigger(async_operation=bool)bool
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearRecordsForTrigger", payload=payload, response_object=None
        )

    def RefreshLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInformation operation on the server.

        This describes the learned information is refreshed.

        refreshLearnedInformation(async_operation=bool)bool
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "refreshLearnedInformation", payload=payload, response_object=None
        )

    def Trigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the trigger operation on the server.

        This describes the learned info trigger settings.

        trigger(async_operation=bool)number
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("trigger", payload=payload, response_object=None)

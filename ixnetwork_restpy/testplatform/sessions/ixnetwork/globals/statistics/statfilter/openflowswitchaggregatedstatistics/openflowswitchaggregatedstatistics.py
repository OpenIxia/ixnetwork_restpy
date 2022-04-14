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


class OpenflowSwitchAggregatedStatistics(Base):
    """Represents stats of OpenFlow Switch Aggregated Statistics
    The OpenflowSwitchAggregatedStatistics class encapsulates a required openflowSwitchAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "openflowSwitchAggregatedStatistics"
    _SDM_ATT_MAP = {
        "ActionErrorsTx": "actionErrorsTx",
        "AuxiliaryConnectionsConfigured": "auxiliaryConnectionsConfigured",
        "AuxiliaryConnectionsUp": "auxiliaryConnectionsUp",
        "BarrierRepliesTx": "barrierRepliesTx",
        "BarrierRequestsRx": "barrierRequestsRx",
        "DescriptionStatRepliesTx": "descriptionStatRepliesTx",
        "DescriptionStatRequestsRx": "descriptionStatRequestsRx",
        "EchoRepliesRx": "echoRepliesRx",
        "EchoRepliesTx": "echoRepliesTx",
        "EchoRequestsRx": "echoRequestsRx",
        "EchoRequestsTx": "echoRequestsTx",
        "ErrorsTx": "errorsTx",
        "ExperimenterErrorsTx": "experimenterErrorsTx",
        "FeatureRepliesTx": "featureRepliesTx",
        "FeatureRequestsRx": "featureRequestsRx",
        "FlowAddsRx": "flowAddsRx",
        "FlowAggregateStatRepliesTx": "flowAggregateStatRepliesTx",
        "FlowAggregateStatRequestsRx": "flowAggregateStatRequestsRx",
        "FlowDelsRx": "flowDelsRx",
        "FlowModErrorsTx": "flowModErrorsTx",
        "FlowModsRx": "flowModsRx",
        "FlowRemovesTx": "flowRemovesTx",
        "FlowStatRepliesTx": "flowStatRepliesTx",
        "FlowStatRequestsRx": "flowStatRequestsRx",
        "FlowTxRateflowssec": "flowTxRateflowssec",
        "GetAsynchronousConfigRepliesTx": "getAsynchronousConfigRepliesTx",
        "GetAsynchronousConfigRequestsRx": "getAsynchronousConfigRequestsRx",
        "GetConfigRepliesTx": "getConfigRepliesTx",
        "GetConfigRequestsRx": "getConfigRequestsRx",
        "GetQueueConfigRepliesTx": "getQueueConfigRepliesTx",
        "GetQueueConfigRequestsRx": "getQueueConfigRequestsRx",
        "GroupAddsRx": "groupAddsRx",
        "GroupDelsRx": "groupDelsRx",
        "GroupDescRepliesTx": "groupDescRepliesTx",
        "GroupDescRequestsRx": "groupDescRequestsRx",
        "GroupFeatureRepliesTx": "groupFeatureRepliesTx",
        "GroupFeatureRequestsRx": "groupFeatureRequestsRx",
        "GroupModErrorsTx": "groupModErrorsTx",
        "GroupModsRx": "groupModsRx",
        "GroupStatRepliesTx": "groupStatRepliesTx",
        "GroupStatRequestsRx": "groupStatRequestsRx",
        "HelloErrorsTx": "helloErrorsTx",
        "HellosRx": "hellosRx",
        "HellosTx": "hellosTx",
        "InstructionErrorsTx": "instructionErrorsTx",
        "MatchErrorsTx": "matchErrorsTx",
        "MeterAddsRx": "meterAddsRx",
        "MeterConfigRepliesTx": "meterConfigRepliesTx",
        "MeterConfigRequestsRx": "meterConfigRequestsRx",
        "MeterDelsRx": "meterDelsRx",
        "MeterFeatureRepliesTx": "meterFeatureRepliesTx",
        "MeterFeatureRequestsRx": "meterFeatureRequestsRx",
        "MeterModErrorsTx": "meterModErrorsTx",
        "MeterModsRx": "meterModsRx",
        "MeterStatRepliesTx": "meterStatRepliesTx",
        "MeterStatRequestsRx": "meterStatRequestsRx",
        "OfChannelConfigured": "ofChannelConfigured",
        "OfChannelConfiguredUp": "ofChannelConfiguredUp",
        "OfChannelFlapCount": "ofChannelFlapCount",
        "PacketInsTx": "packetInsTx",
        "PacketOutsRx": "packetOutsRx",
        "PacketinDelaymicrosec": "packetinDelaymicrosec",
        "PacketinReasonAction": "packetinReasonAction",
        "PacketinReasonInvalidTTL": "packetinReasonInvalidTTL",
        "PacketinReasonNoMatch": "packetinReasonNoMatch",
        "PacketinTxRatepacketssec": "packetinTxRatepacketssec",
        "PacketoutRxRatepacketssec": "packetoutRxRatepacketssec",
        "PortDescRepliesTx": "portDescRepliesTx",
        "PortDescRequestsRx": "portDescRequestsRx",
        "PortModErrorsTx": "portModErrorsTx",
        "PortModsRx": "portModsRx",
        "PortName": "portName",
        "PortStatRepliesTx": "portStatRepliesTx",
        "PortStatRequestsRx": "portStatRequestsRx",
        "PortStatusesTx": "portStatusesTx",
        "QueueOpErrorsTx": "queueOpErrorsTx",
        "QueueStatRepliesTx": "queueStatRepliesTx",
        "QueueStatRequestsRx": "queueStatRequestsRx",
        "RequestErrorsTx": "requestErrorsTx",
        "RoleRepliesTx": "roleRepliesTx",
        "RoleRequestErrorsTx": "roleRequestErrorsTx",
        "RoleRequestsRx": "roleRequestsRx",
        "SetAsynchronousConfigRx": "setAsynchronousConfigRx",
        "SetConfigRx": "setConfigRx",
        "StatRepliesTx": "statRepliesTx",
        "StatRequestsRx": "statRequestsRx",
        "SwitchConfigErrorsTx": "switchConfigErrorsTx",
        "TableFeatureErrorsTx": "tableFeatureErrorsTx",
        "TableFeatureRepliesTx": "tableFeatureRepliesTx",
        "TableFeatureRequestsRx": "tableFeatureRequestsRx",
        "TableModErrorsTx": "tableModErrorsTx",
        "TableModsRx": "tableModsRx",
        "TableStatRepliesTx": "tableStatRepliesTx",
        "TableStatRequestsRx": "tableStatRequestsRx",
        "VendorMessagesRx": "vendorMessagesRx",
        "VendorMessagesTx": "vendorMessagesTx",
        "VendorStatRepliesTx": "vendorStatRepliesTx",
        "VendorStatRequestsRx": "vendorStatRequestsRx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OpenflowSwitchAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def ActionErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Action Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActionErrorsTx"])

    @ActionErrorsTx.setter
    def ActionErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActionErrorsTx"], value)

    @property
    def AuxiliaryConnectionsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Auxiliary Connections Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuxiliaryConnectionsConfigured"])

    @AuxiliaryConnectionsConfigured.setter
    def AuxiliaryConnectionsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuxiliaryConnectionsConfigured"], value)

    @property
    def AuxiliaryConnectionsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Auxiliary Connections Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuxiliaryConnectionsUp"])

    @AuxiliaryConnectionsUp.setter
    def AuxiliaryConnectionsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuxiliaryConnectionsUp"], value)

    @property
    def BarrierRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Barrier Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BarrierRepliesTx"])

    @BarrierRepliesTx.setter
    def BarrierRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BarrierRepliesTx"], value)

    @property
    def BarrierRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Barrier Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BarrierRequestsRx"])

    @BarrierRequestsRx.setter
    def BarrierRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BarrierRequestsRx"], value)

    @property
    def DescriptionStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Description Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptionStatRepliesTx"])

    @DescriptionStatRepliesTx.setter
    def DescriptionStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DescriptionStatRepliesTx"], value)

    @property
    def DescriptionStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Description Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptionStatRequestsRx"])

    @DescriptionStatRequestsRx.setter
    def DescriptionStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DescriptionStatRequestsRx"], value)

    @property
    def EchoRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoRepliesRx"])

    @EchoRepliesRx.setter
    def EchoRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoRepliesRx"], value)

    @property
    def EchoRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoRepliesTx"])

    @EchoRepliesTx.setter
    def EchoRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoRepliesTx"], value)

    @property
    def EchoRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoRequestsRx"])

    @EchoRequestsRx.setter
    def EchoRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoRequestsRx"], value)

    @property
    def EchoRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Echo Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoRequestsTx"])

    @EchoRequestsTx.setter
    def EchoRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoRequestsTx"], value)

    @property
    def ErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorsTx"])

    @ErrorsTx.setter
    def ErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorsTx"], value)

    @property
    def ExperimenterErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Experimenter Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterErrorsTx"])

    @ExperimenterErrorsTx.setter
    def ExperimenterErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterErrorsTx"], value)

    @property
    def FeatureRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Feature Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureRepliesTx"])

    @FeatureRepliesTx.setter
    def FeatureRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureRepliesTx"], value)

    @property
    def FeatureRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Feature Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureRequestsRx"])

    @FeatureRequestsRx.setter
    def FeatureRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureRequestsRx"], value)

    @property
    def FlowAddsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Adds Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAddsRx"])

    @FlowAddsRx.setter
    def FlowAddsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAddsRx"], value)

    @property
    def FlowAggregateStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Aggregate Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregateStatRepliesTx"])

    @FlowAggregateStatRepliesTx.setter
    def FlowAggregateStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregateStatRepliesTx"], value)

    @property
    def FlowAggregateStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Aggregate Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregateStatRequestsRx"])

    @FlowAggregateStatRequestsRx.setter
    def FlowAggregateStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregateStatRequestsRx"], value)

    @property
    def FlowDelsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Dels Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowDelsRx"])

    @FlowDelsRx.setter
    def FlowDelsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowDelsRx"], value)

    @property
    def FlowModErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Mod Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowModErrorsTx"])

    @FlowModErrorsTx.setter
    def FlowModErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowModErrorsTx"], value)

    @property
    def FlowModsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Mods Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowModsRx"])

    @FlowModsRx.setter
    def FlowModsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowModsRx"], value)

    @property
    def FlowRemovesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Removes Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowRemovesTx"])

    @FlowRemovesTx.setter
    def FlowRemovesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowRemovesTx"], value)

    @property
    def FlowStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatRepliesTx"])

    @FlowStatRepliesTx.setter
    def FlowStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatRepliesTx"], value)

    @property
    def FlowStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatRequestsRx"])

    @FlowStatRequestsRx.setter
    def FlowStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatRequestsRx"], value)

    @property
    def FlowTxRateflowssec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Tx Rate (flows/sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowTxRateflowssec"])

    @FlowTxRateflowssec.setter
    def FlowTxRateflowssec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowTxRateflowssec"], value)

    @property
    def GetAsynchronousConfigRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Asynchronous Config Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRepliesTx"])

    @GetAsynchronousConfigRepliesTx.setter
    def GetAsynchronousConfigRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRepliesTx"], value)

    @property
    def GetAsynchronousConfigRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Asynchronous Config Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRequestsRx"])

    @GetAsynchronousConfigRequestsRx.setter
    def GetAsynchronousConfigRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRequestsRx"], value)

    @property
    def GetConfigRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Config Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetConfigRepliesTx"])

    @GetConfigRepliesTx.setter
    def GetConfigRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetConfigRepliesTx"], value)

    @property
    def GetConfigRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Config Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetConfigRequestsRx"])

    @GetConfigRequestsRx.setter
    def GetConfigRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetConfigRequestsRx"], value)

    @property
    def GetQueueConfigRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Queue Config Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetQueueConfigRepliesTx"])

    @GetQueueConfigRepliesTx.setter
    def GetQueueConfigRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetQueueConfigRepliesTx"], value)

    @property
    def GetQueueConfigRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Queue Config Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetQueueConfigRequestsRx"])

    @GetQueueConfigRequestsRx.setter
    def GetQueueConfigRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetQueueConfigRequestsRx"], value)

    @property
    def GroupAddsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Adds Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupAddsRx"])

    @GroupAddsRx.setter
    def GroupAddsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupAddsRx"], value)

    @property
    def GroupDelsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Dels Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDelsRx"])

    @GroupDelsRx.setter
    def GroupDelsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDelsRx"], value)

    @property
    def GroupDescRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Desc Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDescRepliesTx"])

    @GroupDescRepliesTx.setter
    def GroupDescRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDescRepliesTx"], value)

    @property
    def GroupDescRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Desc Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDescRequestsRx"])

    @GroupDescRequestsRx.setter
    def GroupDescRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDescRequestsRx"], value)

    @property
    def GroupFeatureRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Feature Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFeatureRepliesTx"])

    @GroupFeatureRepliesTx.setter
    def GroupFeatureRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFeatureRepliesTx"], value)

    @property
    def GroupFeatureRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Feature Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFeatureRequestsRx"])

    @GroupFeatureRequestsRx.setter
    def GroupFeatureRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFeatureRequestsRx"], value)

    @property
    def GroupModErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Mod Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupModErrorsTx"])

    @GroupModErrorsTx.setter
    def GroupModErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupModErrorsTx"], value)

    @property
    def GroupModsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Mods Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupModsRx"])

    @GroupModsRx.setter
    def GroupModsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupModsRx"], value)

    @property
    def GroupStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatRepliesTx"])

    @GroupStatRepliesTx.setter
    def GroupStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatRepliesTx"], value)

    @property
    def GroupStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatRequestsRx"])

    @GroupStatRequestsRx.setter
    def GroupStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatRequestsRx"], value)

    @property
    def HelloErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hello Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HelloErrorsTx"])

    @HelloErrorsTx.setter
    def HelloErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HelloErrorsTx"], value)

    @property
    def HellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosRx"])

    @HellosRx.setter
    def HellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosRx"], value)

    @property
    def HellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosTx"])

    @HellosTx.setter
    def HellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosTx"], value)

    @property
    def InstructionErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Instruction Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionErrorsTx"])

    @InstructionErrorsTx.setter
    def InstructionErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionErrorsTx"], value)

    @property
    def MatchErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Match Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchErrorsTx"])

    @MatchErrorsTx.setter
    def MatchErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchErrorsTx"], value)

    @property
    def MeterAddsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Adds Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterAddsRx"])

    @MeterAddsRx.setter
    def MeterAddsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterAddsRx"], value)

    @property
    def MeterConfigRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Config Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigRepliesTx"])

    @MeterConfigRepliesTx.setter
    def MeterConfigRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigRepliesTx"], value)

    @property
    def MeterConfigRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Config Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigRequestsRx"])

    @MeterConfigRequestsRx.setter
    def MeterConfigRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigRequestsRx"], value)

    @property
    def MeterDelsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Dels Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterDelsRx"])

    @MeterDelsRx.setter
    def MeterDelsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterDelsRx"], value)

    @property
    def MeterFeatureRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Feature Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterFeatureRepliesTx"])

    @MeterFeatureRepliesTx.setter
    def MeterFeatureRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterFeatureRepliesTx"], value)

    @property
    def MeterFeatureRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Feature Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterFeatureRequestsRx"])

    @MeterFeatureRequestsRx.setter
    def MeterFeatureRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterFeatureRequestsRx"], value)

    @property
    def MeterModErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Mod Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterModErrorsTx"])

    @MeterModErrorsTx.setter
    def MeterModErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterModErrorsTx"], value)

    @property
    def MeterModsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Mods Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterModsRx"])

    @MeterModsRx.setter
    def MeterModsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterModsRx"], value)

    @property
    def MeterStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatRepliesTx"])

    @MeterStatRepliesTx.setter
    def MeterStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatRepliesTx"], value)

    @property
    def MeterStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatRequestsRx"])

    @MeterStatRequestsRx.setter
    def MeterStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatRequestsRx"], value)

    @property
    def OfChannelConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OF Channel Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["OfChannelConfigured"])

    @OfChannelConfigured.setter
    def OfChannelConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OfChannelConfigured"], value)

    @property
    def OfChannelConfiguredUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OF Channel Configured Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["OfChannelConfiguredUp"])

    @OfChannelConfiguredUp.setter
    def OfChannelConfiguredUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OfChannelConfiguredUp"], value)

    @property
    def OfChannelFlapCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OF Channel Flap Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["OfChannelFlapCount"])

    @OfChannelFlapCount.setter
    def OfChannelFlapCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OfChannelFlapCount"], value)

    @property
    def PacketInsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packet Ins Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketInsTx"])

    @PacketInsTx.setter
    def PacketInsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketInsTx"], value)

    @property
    def PacketOutsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packet Outs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutsRx"])

    @PacketOutsRx.setter
    def PacketOutsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutsRx"], value)

    @property
    def PacketinDelaymicrosec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PacketIn Delay (micro sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketinDelaymicrosec"])

    @PacketinDelaymicrosec.setter
    def PacketinDelaymicrosec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketinDelaymicrosec"], value)

    @property
    def PacketinReasonAction(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PacketIn Reason Action
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketinReasonAction"])

    @PacketinReasonAction.setter
    def PacketinReasonAction(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketinReasonAction"], value)

    @property
    def PacketinReasonInvalidTTL(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PacketIn Reason Invalid TTL
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketinReasonInvalidTTL"])

    @PacketinReasonInvalidTTL.setter
    def PacketinReasonInvalidTTL(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketinReasonInvalidTTL"], value)

    @property
    def PacketinReasonNoMatch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PacketIn Reason No Match
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketinReasonNoMatch"])

    @PacketinReasonNoMatch.setter
    def PacketinReasonNoMatch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketinReasonNoMatch"], value)

    @property
    def PacketinTxRatepacketssec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PacketIn Tx Rate (packets/sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketinTxRatepacketssec"])

    @PacketinTxRatepacketssec.setter
    def PacketinTxRatepacketssec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketinTxRatepacketssec"], value)

    @property
    def PacketoutRxRatepacketssec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PacketOut Rx Rate (packets/sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketoutRxRatepacketssec"])

    @PacketoutRxRatepacketssec.setter
    def PacketoutRxRatepacketssec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketoutRxRatepacketssec"], value)

    @property
    def PortDescRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Desc Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDescRepliesTx"])

    @PortDescRepliesTx.setter
    def PortDescRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDescRepliesTx"], value)

    @property
    def PortDescRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Desc Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDescRequestsRx"])

    @PortDescRequestsRx.setter
    def PortDescRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDescRequestsRx"], value)

    @property
    def PortModErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Mod Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortModErrorsTx"])

    @PortModErrorsTx.setter
    def PortModErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortModErrorsTx"], value)

    @property
    def PortModsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Mods Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortModsRx"])

    @PortModsRx.setter
    def PortModsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortModsRx"], value)

    @property
    def PortName(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortName"])

    @PortName.setter
    def PortName(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortName"], value)

    @property
    def PortStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatRepliesTx"])

    @PortStatRepliesTx.setter
    def PortStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatRepliesTx"], value)

    @property
    def PortStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatRequestsRx"])

    @PortStatRequestsRx.setter
    def PortStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatRequestsRx"], value)

    @property
    def PortStatusesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Statuses Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatusesTx"])

    @PortStatusesTx.setter
    def PortStatusesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatusesTx"], value)

    @property
    def QueueOpErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queue Op Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueOpErrorsTx"])

    @QueueOpErrorsTx.setter
    def QueueOpErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueOpErrorsTx"], value)

    @property
    def QueueStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queue Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatRepliesTx"])

    @QueueStatRepliesTx.setter
    def QueueStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatRepliesTx"], value)

    @property
    def QueueStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queue Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatRequestsRx"])

    @QueueStatRequestsRx.setter
    def QueueStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatRequestsRx"], value)

    @property
    def RequestErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Request Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RequestErrorsTx"])

    @RequestErrorsTx.setter
    def RequestErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RequestErrorsTx"], value)

    @property
    def RoleRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Role Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRepliesTx"])

    @RoleRepliesTx.setter
    def RoleRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRepliesTx"], value)

    @property
    def RoleRequestErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Role Request Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRequestErrorsTx"])

    @RoleRequestErrorsTx.setter
    def RoleRequestErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRequestErrorsTx"], value)

    @property
    def RoleRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Role Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRequestsRx"])

    @RoleRequestsRx.setter
    def RoleRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRequestsRx"], value)

    @property
    def SetAsynchronousConfigRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set Asynchronous Config Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetAsynchronousConfigRx"])

    @SetAsynchronousConfigRx.setter
    def SetAsynchronousConfigRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetAsynchronousConfigRx"], value)

    @property
    def SetConfigRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set Config Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetConfigRx"])

    @SetConfigRx.setter
    def SetConfigRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetConfigRx"], value)

    @property
    def StatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatRepliesTx"])

    @StatRepliesTx.setter
    def StatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatRepliesTx"], value)

    @property
    def StatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatRequestsRx"])

    @StatRequestsRx.setter
    def StatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatRequestsRx"], value)

    @property
    def SwitchConfigErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Switch Config Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigErrorsTx"])

    @SwitchConfigErrorsTx.setter
    def SwitchConfigErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigErrorsTx"], value)

    @property
    def TableFeatureErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Feature Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureErrorsTx"])

    @TableFeatureErrorsTx.setter
    def TableFeatureErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureErrorsTx"], value)

    @property
    def TableFeatureRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Feature Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureRepliesTx"])

    @TableFeatureRepliesTx.setter
    def TableFeatureRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureRepliesTx"], value)

    @property
    def TableFeatureRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Feature Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureRequestsRx"])

    @TableFeatureRequestsRx.setter
    def TableFeatureRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureRequestsRx"], value)

    @property
    def TableModErrorsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Mod Errors Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableModErrorsTx"])

    @TableModErrorsTx.setter
    def TableModErrorsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableModErrorsTx"], value)

    @property
    def TableModsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Mods Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableModsRx"])

    @TableModsRx.setter
    def TableModsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableModsRx"], value)

    @property
    def TableStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatRepliesTx"])

    @TableStatRepliesTx.setter
    def TableStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatRepliesTx"], value)

    @property
    def TableStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatRequestsRx"])

    @TableStatRequestsRx.setter
    def TableStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatRequestsRx"], value)

    @property
    def VendorMessagesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vendor Messages Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMessagesRx"])

    @VendorMessagesRx.setter
    def VendorMessagesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMessagesRx"], value)

    @property
    def VendorMessagesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vendor Messages Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMessagesTx"])

    @VendorMessagesTx.setter
    def VendorMessagesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMessagesTx"], value)

    @property
    def VendorStatRepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vendor Stat Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatRepliesTx"])

    @VendorStatRepliesTx.setter
    def VendorStatRepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatRepliesTx"], value)

    @property
    def VendorStatRequestsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vendor Stat Requests Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatRequestsRx"])

    @VendorStatRequestsRx.setter
    def VendorStatRequestsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatRequestsRx"], value)

    def update(
        self,
        ActionErrorsTx=None,
        AuxiliaryConnectionsConfigured=None,
        AuxiliaryConnectionsUp=None,
        BarrierRepliesTx=None,
        BarrierRequestsRx=None,
        DescriptionStatRepliesTx=None,
        DescriptionStatRequestsRx=None,
        EchoRepliesRx=None,
        EchoRepliesTx=None,
        EchoRequestsRx=None,
        EchoRequestsTx=None,
        ErrorsTx=None,
        ExperimenterErrorsTx=None,
        FeatureRepliesTx=None,
        FeatureRequestsRx=None,
        FlowAddsRx=None,
        FlowAggregateStatRepliesTx=None,
        FlowAggregateStatRequestsRx=None,
        FlowDelsRx=None,
        FlowModErrorsTx=None,
        FlowModsRx=None,
        FlowRemovesTx=None,
        FlowStatRepliesTx=None,
        FlowStatRequestsRx=None,
        FlowTxRateflowssec=None,
        GetAsynchronousConfigRepliesTx=None,
        GetAsynchronousConfigRequestsRx=None,
        GetConfigRepliesTx=None,
        GetConfigRequestsRx=None,
        GetQueueConfigRepliesTx=None,
        GetQueueConfigRequestsRx=None,
        GroupAddsRx=None,
        GroupDelsRx=None,
        GroupDescRepliesTx=None,
        GroupDescRequestsRx=None,
        GroupFeatureRepliesTx=None,
        GroupFeatureRequestsRx=None,
        GroupModErrorsTx=None,
        GroupModsRx=None,
        GroupStatRepliesTx=None,
        GroupStatRequestsRx=None,
        HelloErrorsTx=None,
        HellosRx=None,
        HellosTx=None,
        InstructionErrorsTx=None,
        MatchErrorsTx=None,
        MeterAddsRx=None,
        MeterConfigRepliesTx=None,
        MeterConfigRequestsRx=None,
        MeterDelsRx=None,
        MeterFeatureRepliesTx=None,
        MeterFeatureRequestsRx=None,
        MeterModErrorsTx=None,
        MeterModsRx=None,
        MeterStatRepliesTx=None,
        MeterStatRequestsRx=None,
        OfChannelConfigured=None,
        OfChannelConfiguredUp=None,
        OfChannelFlapCount=None,
        PacketInsTx=None,
        PacketOutsRx=None,
        PacketinDelaymicrosec=None,
        PacketinReasonAction=None,
        PacketinReasonInvalidTTL=None,
        PacketinReasonNoMatch=None,
        PacketinTxRatepacketssec=None,
        PacketoutRxRatepacketssec=None,
        PortDescRepliesTx=None,
        PortDescRequestsRx=None,
        PortModErrorsTx=None,
        PortModsRx=None,
        PortName=None,
        PortStatRepliesTx=None,
        PortStatRequestsRx=None,
        PortStatusesTx=None,
        QueueOpErrorsTx=None,
        QueueStatRepliesTx=None,
        QueueStatRequestsRx=None,
        RequestErrorsTx=None,
        RoleRepliesTx=None,
        RoleRequestErrorsTx=None,
        RoleRequestsRx=None,
        SetAsynchronousConfigRx=None,
        SetConfigRx=None,
        StatRepliesTx=None,
        StatRequestsRx=None,
        SwitchConfigErrorsTx=None,
        TableFeatureErrorsTx=None,
        TableFeatureRepliesTx=None,
        TableFeatureRequestsRx=None,
        TableModErrorsTx=None,
        TableModsRx=None,
        TableStatRepliesTx=None,
        TableStatRequestsRx=None,
        VendorMessagesRx=None,
        VendorMessagesTx=None,
        VendorStatRepliesTx=None,
        VendorStatRequestsRx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> OpenflowSwitchAggregatedStatistics
        """Updates openflowSwitchAggregatedStatistics resource on the server.

        Args
        ----
        - ActionErrorsTx (bool): Action Errors Tx
        - AuxiliaryConnectionsConfigured (bool): Auxiliary Connections Configured
        - AuxiliaryConnectionsUp (bool): Auxiliary Connections Up
        - BarrierRepliesTx (bool): Barrier Replies Tx
        - BarrierRequestsRx (bool): Barrier Requests Rx
        - DescriptionStatRepliesTx (bool): Description Stat Replies Tx
        - DescriptionStatRequestsRx (bool): Description Stat Requests Rx
        - EchoRepliesRx (bool): Echo Replies Rx
        - EchoRepliesTx (bool): Echo Replies Tx
        - EchoRequestsRx (bool): Echo Requests Rx
        - EchoRequestsTx (bool): Echo Requests Tx
        - ErrorsTx (bool): Errors Tx
        - ExperimenterErrorsTx (bool): Experimenter Errors Tx
        - FeatureRepliesTx (bool): Feature Replies Tx
        - FeatureRequestsRx (bool): Feature Requests Rx
        - FlowAddsRx (bool): Flow Adds Rx
        - FlowAggregateStatRepliesTx (bool): Flow Aggregate Stat Replies Tx
        - FlowAggregateStatRequestsRx (bool): Flow Aggregate Stat Requests Rx
        - FlowDelsRx (bool): Flow Dels Rx
        - FlowModErrorsTx (bool): Flow Mod Errors Tx
        - FlowModsRx (bool): Flow Mods Rx
        - FlowRemovesTx (bool): Flow Removes Tx
        - FlowStatRepliesTx (bool): Flow Stat Replies Tx
        - FlowStatRequestsRx (bool): Flow Stat Requests Rx
        - FlowTxRateflowssec (bool): Flow Tx Rate (flows/sec)
        - GetAsynchronousConfigRepliesTx (bool): Get Asynchronous Config Replies Tx
        - GetAsynchronousConfigRequestsRx (bool): Get Asynchronous Config Requests Rx
        - GetConfigRepliesTx (bool): Get Config Replies Tx
        - GetConfigRequestsRx (bool): Get Config Requests Rx
        - GetQueueConfigRepliesTx (bool): Get Queue Config Replies Tx
        - GetQueueConfigRequestsRx (bool): Get Queue Config Requests Rx
        - GroupAddsRx (bool): Group Adds Rx
        - GroupDelsRx (bool): Group Dels Rx
        - GroupDescRepliesTx (bool): Group Desc Replies Tx
        - GroupDescRequestsRx (bool): Group Desc Requests Rx
        - GroupFeatureRepliesTx (bool): Group Feature Replies Tx
        - GroupFeatureRequestsRx (bool): Group Feature Requests Rx
        - GroupModErrorsTx (bool): Group Mod Errors Tx
        - GroupModsRx (bool): Group Mods Rx
        - GroupStatRepliesTx (bool): Group Stat Replies Tx
        - GroupStatRequestsRx (bool): Group Stat Requests Rx
        - HelloErrorsTx (bool): Hello Errors Tx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - InstructionErrorsTx (bool): Instruction Errors Tx
        - MatchErrorsTx (bool): Match Errors Tx
        - MeterAddsRx (bool): Meter Adds Rx
        - MeterConfigRepliesTx (bool): Meter Config Replies Tx
        - MeterConfigRequestsRx (bool): Meter Config Requests Rx
        - MeterDelsRx (bool): Meter Dels Rx
        - MeterFeatureRepliesTx (bool): Meter Feature Replies Tx
        - MeterFeatureRequestsRx (bool): Meter Feature Requests Rx
        - MeterModErrorsTx (bool): Meter Mod Errors Tx
        - MeterModsRx (bool): Meter Mods Rx
        - MeterStatRepliesTx (bool): Meter Stat Replies Tx
        - MeterStatRequestsRx (bool): Meter Stat Requests Rx
        - OfChannelConfigured (bool): OF Channel Configured
        - OfChannelConfiguredUp (bool): OF Channel Configured Up
        - OfChannelFlapCount (bool): OF Channel Flap Count
        - PacketInsTx (bool): Packet Ins Tx
        - PacketOutsRx (bool): Packet Outs Rx
        - PacketinDelaymicrosec (bool): PacketIn Delay (micro sec)
        - PacketinReasonAction (bool): PacketIn Reason Action
        - PacketinReasonInvalidTTL (bool): PacketIn Reason Invalid TTL
        - PacketinReasonNoMatch (bool): PacketIn Reason No Match
        - PacketinTxRatepacketssec (bool): PacketIn Tx Rate (packets/sec)
        - PacketoutRxRatepacketssec (bool): PacketOut Rx Rate (packets/sec)
        - PortDescRepliesTx (bool): Port Desc Replies Tx
        - PortDescRequestsRx (bool): Port Desc Requests Rx
        - PortModErrorsTx (bool): Port Mod Errors Tx
        - PortModsRx (bool): Port Mods Rx
        - PortName (bool): Port Name
        - PortStatRepliesTx (bool): Port Stat Replies Tx
        - PortStatRequestsRx (bool): Port Stat Requests Rx
        - PortStatusesTx (bool): Port Statuses Tx
        - QueueOpErrorsTx (bool): Queue Op Errors Tx
        - QueueStatRepliesTx (bool): Queue Stat Replies Tx
        - QueueStatRequestsRx (bool): Queue Stat Requests Rx
        - RequestErrorsTx (bool): Request Errors Tx
        - RoleRepliesTx (bool): Role Replies Tx
        - RoleRequestErrorsTx (bool): Role Request Errors Tx
        - RoleRequestsRx (bool): Role Requests Rx
        - SetAsynchronousConfigRx (bool): Set Asynchronous Config Rx
        - SetConfigRx (bool): Set Config Rx
        - StatRepliesTx (bool): Stat Replies Tx
        - StatRequestsRx (bool): Stat Requests Rx
        - SwitchConfigErrorsTx (bool): Switch Config Errors Tx
        - TableFeatureErrorsTx (bool): Table Feature Errors Tx
        - TableFeatureRepliesTx (bool): Table Feature Replies Tx
        - TableFeatureRequestsRx (bool): Table Feature Requests Rx
        - TableModErrorsTx (bool): Table Mod Errors Tx
        - TableModsRx (bool): Table Mods Rx
        - TableStatRepliesTx (bool): Table Stat Replies Tx
        - TableStatRequestsRx (bool): Table Stat Requests Rx
        - VendorMessagesRx (bool): Vendor Messages Rx
        - VendorMessagesTx (bool): Vendor Messages Tx
        - VendorStatRepliesTx (bool): Vendor Stat Replies Tx
        - VendorStatRequestsRx (bool): Vendor Stat Requests Rx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActionErrorsTx=None,
        AuxiliaryConnectionsConfigured=None,
        AuxiliaryConnectionsUp=None,
        BarrierRepliesTx=None,
        BarrierRequestsRx=None,
        DescriptionStatRepliesTx=None,
        DescriptionStatRequestsRx=None,
        EchoRepliesRx=None,
        EchoRepliesTx=None,
        EchoRequestsRx=None,
        EchoRequestsTx=None,
        ErrorsTx=None,
        ExperimenterErrorsTx=None,
        FeatureRepliesTx=None,
        FeatureRequestsRx=None,
        FlowAddsRx=None,
        FlowAggregateStatRepliesTx=None,
        FlowAggregateStatRequestsRx=None,
        FlowDelsRx=None,
        FlowModErrorsTx=None,
        FlowModsRx=None,
        FlowRemovesTx=None,
        FlowStatRepliesTx=None,
        FlowStatRequestsRx=None,
        FlowTxRateflowssec=None,
        GetAsynchronousConfigRepliesTx=None,
        GetAsynchronousConfigRequestsRx=None,
        GetConfigRepliesTx=None,
        GetConfigRequestsRx=None,
        GetQueueConfigRepliesTx=None,
        GetQueueConfigRequestsRx=None,
        GroupAddsRx=None,
        GroupDelsRx=None,
        GroupDescRepliesTx=None,
        GroupDescRequestsRx=None,
        GroupFeatureRepliesTx=None,
        GroupFeatureRequestsRx=None,
        GroupModErrorsTx=None,
        GroupModsRx=None,
        GroupStatRepliesTx=None,
        GroupStatRequestsRx=None,
        HelloErrorsTx=None,
        HellosRx=None,
        HellosTx=None,
        InstructionErrorsTx=None,
        MatchErrorsTx=None,
        MeterAddsRx=None,
        MeterConfigRepliesTx=None,
        MeterConfigRequestsRx=None,
        MeterDelsRx=None,
        MeterFeatureRepliesTx=None,
        MeterFeatureRequestsRx=None,
        MeterModErrorsTx=None,
        MeterModsRx=None,
        MeterStatRepliesTx=None,
        MeterStatRequestsRx=None,
        OfChannelConfigured=None,
        OfChannelConfiguredUp=None,
        OfChannelFlapCount=None,
        PacketInsTx=None,
        PacketOutsRx=None,
        PacketinDelaymicrosec=None,
        PacketinReasonAction=None,
        PacketinReasonInvalidTTL=None,
        PacketinReasonNoMatch=None,
        PacketinTxRatepacketssec=None,
        PacketoutRxRatepacketssec=None,
        PortDescRepliesTx=None,
        PortDescRequestsRx=None,
        PortModErrorsTx=None,
        PortModsRx=None,
        PortName=None,
        PortStatRepliesTx=None,
        PortStatRequestsRx=None,
        PortStatusesTx=None,
        QueueOpErrorsTx=None,
        QueueStatRepliesTx=None,
        QueueStatRequestsRx=None,
        RequestErrorsTx=None,
        RoleRepliesTx=None,
        RoleRequestErrorsTx=None,
        RoleRequestsRx=None,
        SetAsynchronousConfigRx=None,
        SetConfigRx=None,
        StatRepliesTx=None,
        StatRequestsRx=None,
        SwitchConfigErrorsTx=None,
        TableFeatureErrorsTx=None,
        TableFeatureRepliesTx=None,
        TableFeatureRequestsRx=None,
        TableModErrorsTx=None,
        TableModsRx=None,
        TableStatRepliesTx=None,
        TableStatRequestsRx=None,
        VendorMessagesRx=None,
        VendorMessagesTx=None,
        VendorStatRepliesTx=None,
        VendorStatRequestsRx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> OpenflowSwitchAggregatedStatistics
        """Finds and retrieves openflowSwitchAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openflowSwitchAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openflowSwitchAggregatedStatistics resources from the server.

        Args
        ----
        - ActionErrorsTx (bool): Action Errors Tx
        - AuxiliaryConnectionsConfigured (bool): Auxiliary Connections Configured
        - AuxiliaryConnectionsUp (bool): Auxiliary Connections Up
        - BarrierRepliesTx (bool): Barrier Replies Tx
        - BarrierRequestsRx (bool): Barrier Requests Rx
        - DescriptionStatRepliesTx (bool): Description Stat Replies Tx
        - DescriptionStatRequestsRx (bool): Description Stat Requests Rx
        - EchoRepliesRx (bool): Echo Replies Rx
        - EchoRepliesTx (bool): Echo Replies Tx
        - EchoRequestsRx (bool): Echo Requests Rx
        - EchoRequestsTx (bool): Echo Requests Tx
        - ErrorsTx (bool): Errors Tx
        - ExperimenterErrorsTx (bool): Experimenter Errors Tx
        - FeatureRepliesTx (bool): Feature Replies Tx
        - FeatureRequestsRx (bool): Feature Requests Rx
        - FlowAddsRx (bool): Flow Adds Rx
        - FlowAggregateStatRepliesTx (bool): Flow Aggregate Stat Replies Tx
        - FlowAggregateStatRequestsRx (bool): Flow Aggregate Stat Requests Rx
        - FlowDelsRx (bool): Flow Dels Rx
        - FlowModErrorsTx (bool): Flow Mod Errors Tx
        - FlowModsRx (bool): Flow Mods Rx
        - FlowRemovesTx (bool): Flow Removes Tx
        - FlowStatRepliesTx (bool): Flow Stat Replies Tx
        - FlowStatRequestsRx (bool): Flow Stat Requests Rx
        - FlowTxRateflowssec (bool): Flow Tx Rate (flows/sec)
        - GetAsynchronousConfigRepliesTx (bool): Get Asynchronous Config Replies Tx
        - GetAsynchronousConfigRequestsRx (bool): Get Asynchronous Config Requests Rx
        - GetConfigRepliesTx (bool): Get Config Replies Tx
        - GetConfigRequestsRx (bool): Get Config Requests Rx
        - GetQueueConfigRepliesTx (bool): Get Queue Config Replies Tx
        - GetQueueConfigRequestsRx (bool): Get Queue Config Requests Rx
        - GroupAddsRx (bool): Group Adds Rx
        - GroupDelsRx (bool): Group Dels Rx
        - GroupDescRepliesTx (bool): Group Desc Replies Tx
        - GroupDescRequestsRx (bool): Group Desc Requests Rx
        - GroupFeatureRepliesTx (bool): Group Feature Replies Tx
        - GroupFeatureRequestsRx (bool): Group Feature Requests Rx
        - GroupModErrorsTx (bool): Group Mod Errors Tx
        - GroupModsRx (bool): Group Mods Rx
        - GroupStatRepliesTx (bool): Group Stat Replies Tx
        - GroupStatRequestsRx (bool): Group Stat Requests Rx
        - HelloErrorsTx (bool): Hello Errors Tx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - InstructionErrorsTx (bool): Instruction Errors Tx
        - MatchErrorsTx (bool): Match Errors Tx
        - MeterAddsRx (bool): Meter Adds Rx
        - MeterConfigRepliesTx (bool): Meter Config Replies Tx
        - MeterConfigRequestsRx (bool): Meter Config Requests Rx
        - MeterDelsRx (bool): Meter Dels Rx
        - MeterFeatureRepliesTx (bool): Meter Feature Replies Tx
        - MeterFeatureRequestsRx (bool): Meter Feature Requests Rx
        - MeterModErrorsTx (bool): Meter Mod Errors Tx
        - MeterModsRx (bool): Meter Mods Rx
        - MeterStatRepliesTx (bool): Meter Stat Replies Tx
        - MeterStatRequestsRx (bool): Meter Stat Requests Rx
        - OfChannelConfigured (bool): OF Channel Configured
        - OfChannelConfiguredUp (bool): OF Channel Configured Up
        - OfChannelFlapCount (bool): OF Channel Flap Count
        - PacketInsTx (bool): Packet Ins Tx
        - PacketOutsRx (bool): Packet Outs Rx
        - PacketinDelaymicrosec (bool): PacketIn Delay (micro sec)
        - PacketinReasonAction (bool): PacketIn Reason Action
        - PacketinReasonInvalidTTL (bool): PacketIn Reason Invalid TTL
        - PacketinReasonNoMatch (bool): PacketIn Reason No Match
        - PacketinTxRatepacketssec (bool): PacketIn Tx Rate (packets/sec)
        - PacketoutRxRatepacketssec (bool): PacketOut Rx Rate (packets/sec)
        - PortDescRepliesTx (bool): Port Desc Replies Tx
        - PortDescRequestsRx (bool): Port Desc Requests Rx
        - PortModErrorsTx (bool): Port Mod Errors Tx
        - PortModsRx (bool): Port Mods Rx
        - PortName (bool): Port Name
        - PortStatRepliesTx (bool): Port Stat Replies Tx
        - PortStatRequestsRx (bool): Port Stat Requests Rx
        - PortStatusesTx (bool): Port Statuses Tx
        - QueueOpErrorsTx (bool): Queue Op Errors Tx
        - QueueStatRepliesTx (bool): Queue Stat Replies Tx
        - QueueStatRequestsRx (bool): Queue Stat Requests Rx
        - RequestErrorsTx (bool): Request Errors Tx
        - RoleRepliesTx (bool): Role Replies Tx
        - RoleRequestErrorsTx (bool): Role Request Errors Tx
        - RoleRequestsRx (bool): Role Requests Rx
        - SetAsynchronousConfigRx (bool): Set Asynchronous Config Rx
        - SetConfigRx (bool): Set Config Rx
        - StatRepliesTx (bool): Stat Replies Tx
        - StatRequestsRx (bool): Stat Requests Rx
        - SwitchConfigErrorsTx (bool): Switch Config Errors Tx
        - TableFeatureErrorsTx (bool): Table Feature Errors Tx
        - TableFeatureRepliesTx (bool): Table Feature Replies Tx
        - TableFeatureRequestsRx (bool): Table Feature Requests Rx
        - TableModErrorsTx (bool): Table Mod Errors Tx
        - TableModsRx (bool): Table Mods Rx
        - TableStatRepliesTx (bool): Table Stat Replies Tx
        - TableStatRequestsRx (bool): Table Stat Requests Rx
        - VendorMessagesRx (bool): Vendor Messages Rx
        - VendorMessagesTx (bool): Vendor Messages Tx
        - VendorStatRepliesTx (bool): Vendor Stat Replies Tx
        - VendorStatRequestsRx (bool): Vendor Stat Requests Rx

        Returns
        -------
        - self: This instance with matching openflowSwitchAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openflowSwitchAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openflowSwitchAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

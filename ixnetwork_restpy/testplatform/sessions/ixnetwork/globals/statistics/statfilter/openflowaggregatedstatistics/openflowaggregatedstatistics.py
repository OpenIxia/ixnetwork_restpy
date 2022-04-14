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


class OpenflowAggregatedStatistics(Base):
    """Represents stats of OpenFlow Aggregated Statistics
    The OpenflowAggregatedStatistics class encapsulates a required openflowAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "openflowAggregatedStatistics"
    _SDM_ATT_MAP = {
        "ActionErrorsRx": "actionErrorsRx",
        "AuxiliaryConnectionsUp": "auxiliaryConnectionsUp",
        "BarrierRepliesRx": "barrierRepliesRx",
        "BarrierRequestsTx": "barrierRequestsTx",
        "DescriptionStatRepliesRx": "descriptionStatRepliesRx",
        "DescriptionStatRequestsTx": "descriptionStatRequestsTx",
        "EchoRepliesRx": "echoRepliesRx",
        "EchoRepliesTx": "echoRepliesTx",
        "EchoRequestsRx": "echoRequestsRx",
        "EchoRequestsTx": "echoRequestsTx",
        "ErrorsRx": "errorsRx",
        "ExperimenterErrorsRx": "experimenterErrorsRx",
        "FeatureRepliesRx": "featureRepliesRx",
        "FeatureRequestsTx": "featureRequestsTx",
        "FlowAddsTx": "flowAddsTx",
        "FlowAggregateStatRepliesRx": "flowAggregateStatRepliesRx",
        "FlowAggregateStatRequestsTx": "flowAggregateStatRequestsTx",
        "FlowDelsTx": "flowDelsTx",
        "FlowModErrorsRx": "flowModErrorsRx",
        "FlowModsTx": "flowModsTx",
        "FlowRateflowssec": "flowRateflowssec",
        "FlowRemovesRx": "flowRemovesRx",
        "FlowStatRepliesRx": "flowStatRepliesRx",
        "FlowStatRequestsTx": "flowStatRequestsTx",
        "GetAsynchronousConfigRepliesRx": "getAsynchronousConfigRepliesRx",
        "GetAsynchronousConfigRequestsTx": "getAsynchronousConfigRequestsTx",
        "GetConfigRepliesRx": "getConfigRepliesRx",
        "GetConfigRequestsTx": "getConfigRequestsTx",
        "GetQueueConfigRepliesRx": "getQueueConfigRepliesRx",
        "GetQueueConfigRequestsTx": "getQueueConfigRequestsTx",
        "GroupAddsTx": "groupAddsTx",
        "GroupDelsTx": "groupDelsTx",
        "GroupDescRepliesRx": "groupDescRepliesRx",
        "GroupDescRequestsTx": "groupDescRequestsTx",
        "GroupFeatureRepliesRx": "groupFeatureRepliesRx",
        "GroupFeatureRequestsTx": "groupFeatureRequestsTx",
        "GroupModErrorsRx": "groupModErrorsRx",
        "GroupModsTx": "groupModsTx",
        "GroupStatRepliesRx": "groupStatRepliesRx",
        "GroupStatRequestsTx": "groupStatRequestsTx",
        "HelloErrorsRx": "helloErrorsRx",
        "HellosRx": "hellosRx",
        "HellosTx": "hellosTx",
        "InstructionErrorsRx": "instructionErrorsRx",
        "MatchErrorsRx": "matchErrorsRx",
        "MeterAddsTx": "meterAddsTx",
        "MeterConfigRepliesRx": "meterConfigRepliesRx",
        "MeterConfigRequestsTx": "meterConfigRequestsTx",
        "MeterDelsTx": "meterDelsTx",
        "MeterFeatureRepliesRx": "meterFeatureRepliesRx",
        "MeterFeatureRequestsTx": "meterFeatureRequestsTx",
        "MeterModErrorsRx": "meterModErrorsRx",
        "MeterModsTx": "meterModsTx",
        "MeterStatRepliesRx": "meterStatRepliesRx",
        "MeterStatRequestsTx": "meterStatRequestsTx",
        "OfChannelConfigured": "ofChannelConfigured",
        "OfChannelConfiguredUp": "ofChannelConfiguredUp",
        "OfChannelFlapCount": "ofChannelFlapCount",
        "OfChannelLearnedUp": "ofChannelLearnedUp",
        "PacketInsRx": "packetInsRx",
        "PacketOutsTx": "packetOutsTx",
        "PacketinReasonAction": "packetinReasonAction",
        "PacketinReasonInvalidTTL": "packetinReasonInvalidTTL",
        "PacketinReasonNoMatch": "packetinReasonNoMatch",
        "PortDescRepliesRx": "portDescRepliesRx",
        "PortDescRequestsTx": "portDescRequestsTx",
        "PortModErrorsRx": "portModErrorsRx",
        "PortModsTx": "portModsTx",
        "PortName": "portName",
        "PortStatRepliesRx": "portStatRepliesRx",
        "PortStatRequestsTx": "portStatRequestsTx",
        "PortStatusesRx": "portStatusesRx",
        "QueueOpErrorsRx": "queueOpErrorsRx",
        "QueueStatRepliesRx": "queueStatRepliesRx",
        "QueueStatRequestsTx": "queueStatRequestsTx",
        "RequestErrorsRx": "requestErrorsRx",
        "RoleRepliesRx": "roleRepliesRx",
        "RoleRequestErrorsRx": "roleRequestErrorsRx",
        "RoleRequestsTx": "roleRequestsTx",
        "SetAsynchronousConfigTx": "setAsynchronousConfigTx",
        "SetConfigTx": "setConfigTx",
        "StatRepliesRx": "statRepliesRx",
        "StatRequestsTx": "statRequestsTx",
        "SwitchConfigErrorsRx": "switchConfigErrorsRx",
        "TableFeatureErrorsRx": "tableFeatureErrorsRx",
        "TableFeatureRepliesRx": "tableFeatureRepliesRx",
        "TableFeatureRequestsTx": "tableFeatureRequestsTx",
        "TableModErrorsRx": "tableModErrorsRx",
        "TableModsTx": "tableModsTx",
        "TableStatRepliesRx": "tableStatRepliesRx",
        "TableStatRequestsTx": "tableStatRequestsTx",
        "VendorMessagesRx": "vendorMessagesRx",
        "VendorMessagesTx": "vendorMessagesTx",
        "VendorStatRepliesRx": "vendorStatRepliesRx",
        "VendorStatRequestsTx": "vendorStatRequestsTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OpenflowAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def ActionErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Action Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActionErrorsRx"])

    @ActionErrorsRx.setter
    def ActionErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActionErrorsRx"], value)

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
    def BarrierRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Barrier Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BarrierRepliesRx"])

    @BarrierRepliesRx.setter
    def BarrierRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BarrierRepliesRx"], value)

    @property
    def BarrierRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Barrier Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BarrierRequestsTx"])

    @BarrierRequestsTx.setter
    def BarrierRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BarrierRequestsTx"], value)

    @property
    def DescriptionStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Description Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptionStatRepliesRx"])

    @DescriptionStatRepliesRx.setter
    def DescriptionStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DescriptionStatRepliesRx"], value)

    @property
    def DescriptionStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Description Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptionStatRequestsTx"])

    @DescriptionStatRequestsTx.setter
    def DescriptionStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DescriptionStatRequestsTx"], value)

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
    def ErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorsRx"])

    @ErrorsRx.setter
    def ErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorsRx"], value)

    @property
    def ExperimenterErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Experimenter Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterErrorsRx"])

    @ExperimenterErrorsRx.setter
    def ExperimenterErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterErrorsRx"], value)

    @property
    def FeatureRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Feature Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureRepliesRx"])

    @FeatureRepliesRx.setter
    def FeatureRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureRepliesRx"], value)

    @property
    def FeatureRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Feature Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureRequestsTx"])

    @FeatureRequestsTx.setter
    def FeatureRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureRequestsTx"], value)

    @property
    def FlowAddsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Adds Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAddsTx"])

    @FlowAddsTx.setter
    def FlowAddsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAddsTx"], value)

    @property
    def FlowAggregateStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Aggregate Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregateStatRepliesRx"])

    @FlowAggregateStatRepliesRx.setter
    def FlowAggregateStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregateStatRepliesRx"], value)

    @property
    def FlowAggregateStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Aggregate Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggregateStatRequestsTx"])

    @FlowAggregateStatRequestsTx.setter
    def FlowAggregateStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggregateStatRequestsTx"], value)

    @property
    def FlowDelsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Dels Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowDelsTx"])

    @FlowDelsTx.setter
    def FlowDelsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowDelsTx"], value)

    @property
    def FlowModErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Mod Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowModErrorsRx"])

    @FlowModErrorsRx.setter
    def FlowModErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowModErrorsRx"], value)

    @property
    def FlowModsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Mods Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowModsTx"])

    @FlowModsTx.setter
    def FlowModsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowModsTx"], value)

    @property
    def FlowRateflowssec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Rate (flows/sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowRateflowssec"])

    @FlowRateflowssec.setter
    def FlowRateflowssec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowRateflowssec"], value)

    @property
    def FlowRemovesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Removes Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowRemovesRx"])

    @FlowRemovesRx.setter
    def FlowRemovesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowRemovesRx"], value)

    @property
    def FlowStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatRepliesRx"])

    @FlowStatRepliesRx.setter
    def FlowStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatRepliesRx"], value)

    @property
    def FlowStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatRequestsTx"])

    @FlowStatRequestsTx.setter
    def FlowStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatRequestsTx"], value)

    @property
    def GetAsynchronousConfigRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Asynchronous Config Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRepliesRx"])

    @GetAsynchronousConfigRepliesRx.setter
    def GetAsynchronousConfigRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRepliesRx"], value)

    @property
    def GetAsynchronousConfigRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Asynchronous Config Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRequestsTx"])

    @GetAsynchronousConfigRequestsTx.setter
    def GetAsynchronousConfigRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetAsynchronousConfigRequestsTx"], value)

    @property
    def GetConfigRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Config Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetConfigRepliesRx"])

    @GetConfigRepliesRx.setter
    def GetConfigRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetConfigRepliesRx"], value)

    @property
    def GetConfigRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Config Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetConfigRequestsTx"])

    @GetConfigRequestsTx.setter
    def GetConfigRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetConfigRequestsTx"], value)

    @property
    def GetQueueConfigRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Queue Config Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetQueueConfigRepliesRx"])

    @GetQueueConfigRepliesRx.setter
    def GetQueueConfigRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetQueueConfigRepliesRx"], value)

    @property
    def GetQueueConfigRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Get Queue Config Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GetQueueConfigRequestsTx"])

    @GetQueueConfigRequestsTx.setter
    def GetQueueConfigRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GetQueueConfigRequestsTx"], value)

    @property
    def GroupAddsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Adds Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupAddsTx"])

    @GroupAddsTx.setter
    def GroupAddsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupAddsTx"], value)

    @property
    def GroupDelsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Dels Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDelsTx"])

    @GroupDelsTx.setter
    def GroupDelsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDelsTx"], value)

    @property
    def GroupDescRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Desc Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDescRepliesRx"])

    @GroupDescRepliesRx.setter
    def GroupDescRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDescRepliesRx"], value)

    @property
    def GroupDescRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Desc Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDescRequestsTx"])

    @GroupDescRequestsTx.setter
    def GroupDescRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDescRequestsTx"], value)

    @property
    def GroupFeatureRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Feature Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFeatureRepliesRx"])

    @GroupFeatureRepliesRx.setter
    def GroupFeatureRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFeatureRepliesRx"], value)

    @property
    def GroupFeatureRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Feature Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFeatureRequestsTx"])

    @GroupFeatureRequestsTx.setter
    def GroupFeatureRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFeatureRequestsTx"], value)

    @property
    def GroupModErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Mod Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupModErrorsRx"])

    @GroupModErrorsRx.setter
    def GroupModErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupModErrorsRx"], value)

    @property
    def GroupModsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Mods Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupModsTx"])

    @GroupModsTx.setter
    def GroupModsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupModsTx"], value)

    @property
    def GroupStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatRepliesRx"])

    @GroupStatRepliesRx.setter
    def GroupStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatRepliesRx"], value)

    @property
    def GroupStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Group Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatRequestsTx"])

    @GroupStatRequestsTx.setter
    def GroupStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatRequestsTx"], value)

    @property
    def HelloErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hello Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HelloErrorsRx"])

    @HelloErrorsRx.setter
    def HelloErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HelloErrorsRx"], value)

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
    def InstructionErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Instruction Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionErrorsRx"])

    @InstructionErrorsRx.setter
    def InstructionErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionErrorsRx"], value)

    @property
    def MatchErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Match Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchErrorsRx"])

    @MatchErrorsRx.setter
    def MatchErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchErrorsRx"], value)

    @property
    def MeterAddsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Adds Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterAddsTx"])

    @MeterAddsTx.setter
    def MeterAddsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterAddsTx"], value)

    @property
    def MeterConfigRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Config Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigRepliesRx"])

    @MeterConfigRepliesRx.setter
    def MeterConfigRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigRepliesRx"], value)

    @property
    def MeterConfigRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Config Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigRequestsTx"])

    @MeterConfigRequestsTx.setter
    def MeterConfigRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigRequestsTx"], value)

    @property
    def MeterDelsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Dels Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterDelsTx"])

    @MeterDelsTx.setter
    def MeterDelsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterDelsTx"], value)

    @property
    def MeterFeatureRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Feature Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterFeatureRepliesRx"])

    @MeterFeatureRepliesRx.setter
    def MeterFeatureRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterFeatureRepliesRx"], value)

    @property
    def MeterFeatureRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Feature Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterFeatureRequestsTx"])

    @MeterFeatureRequestsTx.setter
    def MeterFeatureRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterFeatureRequestsTx"], value)

    @property
    def MeterModErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Mod Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterModErrorsRx"])

    @MeterModErrorsRx.setter
    def MeterModErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterModErrorsRx"], value)

    @property
    def MeterModsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Mods Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterModsTx"])

    @MeterModsTx.setter
    def MeterModsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterModsTx"], value)

    @property
    def MeterStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatRepliesRx"])

    @MeterStatRepliesRx.setter
    def MeterStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatRepliesRx"], value)

    @property
    def MeterStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Meter Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatRequestsTx"])

    @MeterStatRequestsTx.setter
    def MeterStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatRequestsTx"], value)

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
    def OfChannelLearnedUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OF Channel Learned Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["OfChannelLearnedUp"])

    @OfChannelLearnedUp.setter
    def OfChannelLearnedUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OfChannelLearnedUp"], value)

    @property
    def PacketInsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packet Ins Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketInsRx"])

    @PacketInsRx.setter
    def PacketInsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketInsRx"], value)

    @property
    def PacketOutsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packet Outs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutsTx"])

    @PacketOutsTx.setter
    def PacketOutsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutsTx"], value)

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
    def PortDescRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Desc Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDescRepliesRx"])

    @PortDescRepliesRx.setter
    def PortDescRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDescRepliesRx"], value)

    @property
    def PortDescRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Desc Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDescRequestsTx"])

    @PortDescRequestsTx.setter
    def PortDescRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDescRequestsTx"], value)

    @property
    def PortModErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Mod Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortModErrorsRx"])

    @PortModErrorsRx.setter
    def PortModErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortModErrorsRx"], value)

    @property
    def PortModsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Mods Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortModsTx"])

    @PortModsTx.setter
    def PortModsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortModsTx"], value)

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
    def PortStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatRepliesRx"])

    @PortStatRepliesRx.setter
    def PortStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatRepliesRx"], value)

    @property
    def PortStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatRequestsTx"])

    @PortStatRequestsTx.setter
    def PortStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatRequestsTx"], value)

    @property
    def PortStatusesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Statuses Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatusesRx"])

    @PortStatusesRx.setter
    def PortStatusesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatusesRx"], value)

    @property
    def QueueOpErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queue Op Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueOpErrorsRx"])

    @QueueOpErrorsRx.setter
    def QueueOpErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueOpErrorsRx"], value)

    @property
    def QueueStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queue Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatRepliesRx"])

    @QueueStatRepliesRx.setter
    def QueueStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatRepliesRx"], value)

    @property
    def QueueStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queue Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatRequestsTx"])

    @QueueStatRequestsTx.setter
    def QueueStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatRequestsTx"], value)

    @property
    def RequestErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Request Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RequestErrorsRx"])

    @RequestErrorsRx.setter
    def RequestErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RequestErrorsRx"], value)

    @property
    def RoleRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Role Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRepliesRx"])

    @RoleRepliesRx.setter
    def RoleRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRepliesRx"], value)

    @property
    def RoleRequestErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Role Request Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRequestErrorsRx"])

    @RoleRequestErrorsRx.setter
    def RoleRequestErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRequestErrorsRx"], value)

    @property
    def RoleRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Role Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleRequestsTx"])

    @RoleRequestsTx.setter
    def RoleRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleRequestsTx"], value)

    @property
    def SetAsynchronousConfigTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set Asynchronous Config Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetAsynchronousConfigTx"])

    @SetAsynchronousConfigTx.setter
    def SetAsynchronousConfigTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetAsynchronousConfigTx"], value)

    @property
    def SetConfigTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set Config Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetConfigTx"])

    @SetConfigTx.setter
    def SetConfigTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetConfigTx"], value)

    @property
    def StatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatRepliesRx"])

    @StatRepliesRx.setter
    def StatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatRepliesRx"], value)

    @property
    def StatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatRequestsTx"])

    @StatRequestsTx.setter
    def StatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatRequestsTx"], value)

    @property
    def SwitchConfigErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Switch Config Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigErrorsRx"])

    @SwitchConfigErrorsRx.setter
    def SwitchConfigErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigErrorsRx"], value)

    @property
    def TableFeatureErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Feature Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureErrorsRx"])

    @TableFeatureErrorsRx.setter
    def TableFeatureErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureErrorsRx"], value)

    @property
    def TableFeatureRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Feature Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureRepliesRx"])

    @TableFeatureRepliesRx.setter
    def TableFeatureRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureRepliesRx"], value)

    @property
    def TableFeatureRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Feature Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableFeatureRequestsTx"])

    @TableFeatureRequestsTx.setter
    def TableFeatureRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableFeatureRequestsTx"], value)

    @property
    def TableModErrorsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Mod Errors Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableModErrorsRx"])

    @TableModErrorsRx.setter
    def TableModErrorsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableModErrorsRx"], value)

    @property
    def TableModsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Mods Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableModsTx"])

    @TableModsTx.setter
    def TableModsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableModsTx"], value)

    @property
    def TableStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatRepliesRx"])

    @TableStatRepliesRx.setter
    def TableStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatRepliesRx"], value)

    @property
    def TableStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Table Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatRequestsTx"])

    @TableStatRequestsTx.setter
    def TableStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatRequestsTx"], value)

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
    def VendorStatRepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vendor Stat Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatRepliesRx"])

    @VendorStatRepliesRx.setter
    def VendorStatRepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatRepliesRx"], value)

    @property
    def VendorStatRequestsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vendor Stat Requests Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatRequestsTx"])

    @VendorStatRequestsTx.setter
    def VendorStatRequestsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatRequestsTx"], value)

    def update(
        self,
        ActionErrorsRx=None,
        AuxiliaryConnectionsUp=None,
        BarrierRepliesRx=None,
        BarrierRequestsTx=None,
        DescriptionStatRepliesRx=None,
        DescriptionStatRequestsTx=None,
        EchoRepliesRx=None,
        EchoRepliesTx=None,
        EchoRequestsRx=None,
        EchoRequestsTx=None,
        ErrorsRx=None,
        ExperimenterErrorsRx=None,
        FeatureRepliesRx=None,
        FeatureRequestsTx=None,
        FlowAddsTx=None,
        FlowAggregateStatRepliesRx=None,
        FlowAggregateStatRequestsTx=None,
        FlowDelsTx=None,
        FlowModErrorsRx=None,
        FlowModsTx=None,
        FlowRateflowssec=None,
        FlowRemovesRx=None,
        FlowStatRepliesRx=None,
        FlowStatRequestsTx=None,
        GetAsynchronousConfigRepliesRx=None,
        GetAsynchronousConfigRequestsTx=None,
        GetConfigRepliesRx=None,
        GetConfigRequestsTx=None,
        GetQueueConfigRepliesRx=None,
        GetQueueConfigRequestsTx=None,
        GroupAddsTx=None,
        GroupDelsTx=None,
        GroupDescRepliesRx=None,
        GroupDescRequestsTx=None,
        GroupFeatureRepliesRx=None,
        GroupFeatureRequestsTx=None,
        GroupModErrorsRx=None,
        GroupModsTx=None,
        GroupStatRepliesRx=None,
        GroupStatRequestsTx=None,
        HelloErrorsRx=None,
        HellosRx=None,
        HellosTx=None,
        InstructionErrorsRx=None,
        MatchErrorsRx=None,
        MeterAddsTx=None,
        MeterConfigRepliesRx=None,
        MeterConfigRequestsTx=None,
        MeterDelsTx=None,
        MeterFeatureRepliesRx=None,
        MeterFeatureRequestsTx=None,
        MeterModErrorsRx=None,
        MeterModsTx=None,
        MeterStatRepliesRx=None,
        MeterStatRequestsTx=None,
        OfChannelConfigured=None,
        OfChannelConfiguredUp=None,
        OfChannelFlapCount=None,
        OfChannelLearnedUp=None,
        PacketInsRx=None,
        PacketOutsTx=None,
        PacketinReasonAction=None,
        PacketinReasonInvalidTTL=None,
        PacketinReasonNoMatch=None,
        PortDescRepliesRx=None,
        PortDescRequestsTx=None,
        PortModErrorsRx=None,
        PortModsTx=None,
        PortName=None,
        PortStatRepliesRx=None,
        PortStatRequestsTx=None,
        PortStatusesRx=None,
        QueueOpErrorsRx=None,
        QueueStatRepliesRx=None,
        QueueStatRequestsTx=None,
        RequestErrorsRx=None,
        RoleRepliesRx=None,
        RoleRequestErrorsRx=None,
        RoleRequestsTx=None,
        SetAsynchronousConfigTx=None,
        SetConfigTx=None,
        StatRepliesRx=None,
        StatRequestsTx=None,
        SwitchConfigErrorsRx=None,
        TableFeatureErrorsRx=None,
        TableFeatureRepliesRx=None,
        TableFeatureRequestsTx=None,
        TableModErrorsRx=None,
        TableModsTx=None,
        TableStatRepliesRx=None,
        TableStatRequestsTx=None,
        VendorMessagesRx=None,
        VendorMessagesTx=None,
        VendorStatRepliesRx=None,
        VendorStatRequestsTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> OpenflowAggregatedStatistics
        """Updates openflowAggregatedStatistics resource on the server.

        Args
        ----
        - ActionErrorsRx (bool): Action Errors Rx
        - AuxiliaryConnectionsUp (bool): Auxiliary Connections Up
        - BarrierRepliesRx (bool): Barrier Replies Rx
        - BarrierRequestsTx (bool): Barrier Requests Tx
        - DescriptionStatRepliesRx (bool): Description Stat Replies Rx
        - DescriptionStatRequestsTx (bool): Description Stat Requests Tx
        - EchoRepliesRx (bool): Echo Replies Rx
        - EchoRepliesTx (bool): Echo Replies Tx
        - EchoRequestsRx (bool): Echo Requests Rx
        - EchoRequestsTx (bool): Echo Requests Tx
        - ErrorsRx (bool): Errors Rx
        - ExperimenterErrorsRx (bool): Experimenter Errors Rx
        - FeatureRepliesRx (bool): Feature Replies Rx
        - FeatureRequestsTx (bool): Feature Requests Tx
        - FlowAddsTx (bool): Flow Adds Tx
        - FlowAggregateStatRepliesRx (bool): Flow Aggregate Stat Replies Rx
        - FlowAggregateStatRequestsTx (bool): Flow Aggregate Stat Requests Tx
        - FlowDelsTx (bool): Flow Dels Tx
        - FlowModErrorsRx (bool): Flow Mod Errors Rx
        - FlowModsTx (bool): Flow Mods Tx
        - FlowRateflowssec (bool): Flow Rate (flows/sec)
        - FlowRemovesRx (bool): Flow Removes Rx
        - FlowStatRepliesRx (bool): Flow Stat Replies Rx
        - FlowStatRequestsTx (bool): Flow Stat Requests Tx
        - GetAsynchronousConfigRepliesRx (bool): Get Asynchronous Config Replies Rx
        - GetAsynchronousConfigRequestsTx (bool): Get Asynchronous Config Requests Tx
        - GetConfigRepliesRx (bool): Get Config Replies Rx
        - GetConfigRequestsTx (bool): Get Config Requests Tx
        - GetQueueConfigRepliesRx (bool): Get Queue Config Replies Rx
        - GetQueueConfigRequestsTx (bool): Get Queue Config Requests Tx
        - GroupAddsTx (bool): Group Adds Tx
        - GroupDelsTx (bool): Group Dels Tx
        - GroupDescRepliesRx (bool): Group Desc Replies Rx
        - GroupDescRequestsTx (bool): Group Desc Requests Tx
        - GroupFeatureRepliesRx (bool): Group Feature Replies Rx
        - GroupFeatureRequestsTx (bool): Group Feature Requests Tx
        - GroupModErrorsRx (bool): Group Mod Errors Rx
        - GroupModsTx (bool): Group Mods Tx
        - GroupStatRepliesRx (bool): Group Stat Replies Rx
        - GroupStatRequestsTx (bool): Group Stat Requests Tx
        - HelloErrorsRx (bool): Hello Errors Rx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - InstructionErrorsRx (bool): Instruction Errors Rx
        - MatchErrorsRx (bool): Match Errors Rx
        - MeterAddsTx (bool): Meter Adds Tx
        - MeterConfigRepliesRx (bool): Meter Config Replies Rx
        - MeterConfigRequestsTx (bool): Meter Config Requests Tx
        - MeterDelsTx (bool): Meter Dels Tx
        - MeterFeatureRepliesRx (bool): Meter Feature Replies Rx
        - MeterFeatureRequestsTx (bool): Meter Feature Requests Tx
        - MeterModErrorsRx (bool): Meter Mod Errors Rx
        - MeterModsTx (bool): Meter Mods Tx
        - MeterStatRepliesRx (bool): Meter Stat Replies Rx
        - MeterStatRequestsTx (bool): Meter Stat Requests Tx
        - OfChannelConfigured (bool): OF Channel Configured
        - OfChannelConfiguredUp (bool): OF Channel Configured Up
        - OfChannelFlapCount (bool): OF Channel Flap Count
        - OfChannelLearnedUp (bool): OF Channel Learned Up
        - PacketInsRx (bool): Packet Ins Rx
        - PacketOutsTx (bool): Packet Outs Tx
        - PacketinReasonAction (bool): PacketIn Reason Action
        - PacketinReasonInvalidTTL (bool): PacketIn Reason Invalid TTL
        - PacketinReasonNoMatch (bool): PacketIn Reason No Match
        - PortDescRepliesRx (bool): Port Desc Replies Rx
        - PortDescRequestsTx (bool): Port Desc Requests Tx
        - PortModErrorsRx (bool): Port Mod Errors Rx
        - PortModsTx (bool): Port Mods Tx
        - PortName (bool): Port Name
        - PortStatRepliesRx (bool): Port Stat Replies Rx
        - PortStatRequestsTx (bool): Port Stat Requests Tx
        - PortStatusesRx (bool): Port Statuses Rx
        - QueueOpErrorsRx (bool): Queue Op Errors Rx
        - QueueStatRepliesRx (bool): Queue Stat Replies Rx
        - QueueStatRequestsTx (bool): Queue Stat Requests Tx
        - RequestErrorsRx (bool): Request Errors Rx
        - RoleRepliesRx (bool): Role Replies Rx
        - RoleRequestErrorsRx (bool): Role Request Errors Rx
        - RoleRequestsTx (bool): Role Requests Tx
        - SetAsynchronousConfigTx (bool): Set Asynchronous Config Tx
        - SetConfigTx (bool): Set Config Tx
        - StatRepliesRx (bool): Stat Replies Rx
        - StatRequestsTx (bool): Stat Requests Tx
        - SwitchConfigErrorsRx (bool): Switch Config Errors Rx
        - TableFeatureErrorsRx (bool): Table Feature Errors Rx
        - TableFeatureRepliesRx (bool): Table Feature Replies Rx
        - TableFeatureRequestsTx (bool): Table Feature Requests Tx
        - TableModErrorsRx (bool): Table Mod Errors Rx
        - TableModsTx (bool): Table Mods Tx
        - TableStatRepliesRx (bool): Table Stat Replies Rx
        - TableStatRequestsTx (bool): Table Stat Requests Tx
        - VendorMessagesRx (bool): Vendor Messages Rx
        - VendorMessagesTx (bool): Vendor Messages Tx
        - VendorStatRepliesRx (bool): Vendor Stat Replies Rx
        - VendorStatRequestsTx (bool): Vendor Stat Requests Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActionErrorsRx=None,
        AuxiliaryConnectionsUp=None,
        BarrierRepliesRx=None,
        BarrierRequestsTx=None,
        DescriptionStatRepliesRx=None,
        DescriptionStatRequestsTx=None,
        EchoRepliesRx=None,
        EchoRepliesTx=None,
        EchoRequestsRx=None,
        EchoRequestsTx=None,
        ErrorsRx=None,
        ExperimenterErrorsRx=None,
        FeatureRepliesRx=None,
        FeatureRequestsTx=None,
        FlowAddsTx=None,
        FlowAggregateStatRepliesRx=None,
        FlowAggregateStatRequestsTx=None,
        FlowDelsTx=None,
        FlowModErrorsRx=None,
        FlowModsTx=None,
        FlowRateflowssec=None,
        FlowRemovesRx=None,
        FlowStatRepliesRx=None,
        FlowStatRequestsTx=None,
        GetAsynchronousConfigRepliesRx=None,
        GetAsynchronousConfigRequestsTx=None,
        GetConfigRepliesRx=None,
        GetConfigRequestsTx=None,
        GetQueueConfigRepliesRx=None,
        GetQueueConfigRequestsTx=None,
        GroupAddsTx=None,
        GroupDelsTx=None,
        GroupDescRepliesRx=None,
        GroupDescRequestsTx=None,
        GroupFeatureRepliesRx=None,
        GroupFeatureRequestsTx=None,
        GroupModErrorsRx=None,
        GroupModsTx=None,
        GroupStatRepliesRx=None,
        GroupStatRequestsTx=None,
        HelloErrorsRx=None,
        HellosRx=None,
        HellosTx=None,
        InstructionErrorsRx=None,
        MatchErrorsRx=None,
        MeterAddsTx=None,
        MeterConfigRepliesRx=None,
        MeterConfigRequestsTx=None,
        MeterDelsTx=None,
        MeterFeatureRepliesRx=None,
        MeterFeatureRequestsTx=None,
        MeterModErrorsRx=None,
        MeterModsTx=None,
        MeterStatRepliesRx=None,
        MeterStatRequestsTx=None,
        OfChannelConfigured=None,
        OfChannelConfiguredUp=None,
        OfChannelFlapCount=None,
        OfChannelLearnedUp=None,
        PacketInsRx=None,
        PacketOutsTx=None,
        PacketinReasonAction=None,
        PacketinReasonInvalidTTL=None,
        PacketinReasonNoMatch=None,
        PortDescRepliesRx=None,
        PortDescRequestsTx=None,
        PortModErrorsRx=None,
        PortModsTx=None,
        PortName=None,
        PortStatRepliesRx=None,
        PortStatRequestsTx=None,
        PortStatusesRx=None,
        QueueOpErrorsRx=None,
        QueueStatRepliesRx=None,
        QueueStatRequestsTx=None,
        RequestErrorsRx=None,
        RoleRepliesRx=None,
        RoleRequestErrorsRx=None,
        RoleRequestsTx=None,
        SetAsynchronousConfigTx=None,
        SetConfigTx=None,
        StatRepliesRx=None,
        StatRequestsTx=None,
        SwitchConfigErrorsRx=None,
        TableFeatureErrorsRx=None,
        TableFeatureRepliesRx=None,
        TableFeatureRequestsTx=None,
        TableModErrorsRx=None,
        TableModsTx=None,
        TableStatRepliesRx=None,
        TableStatRequestsTx=None,
        VendorMessagesRx=None,
        VendorMessagesTx=None,
        VendorStatRepliesRx=None,
        VendorStatRequestsTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> OpenflowAggregatedStatistics
        """Finds and retrieves openflowAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openflowAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openflowAggregatedStatistics resources from the server.

        Args
        ----
        - ActionErrorsRx (bool): Action Errors Rx
        - AuxiliaryConnectionsUp (bool): Auxiliary Connections Up
        - BarrierRepliesRx (bool): Barrier Replies Rx
        - BarrierRequestsTx (bool): Barrier Requests Tx
        - DescriptionStatRepliesRx (bool): Description Stat Replies Rx
        - DescriptionStatRequestsTx (bool): Description Stat Requests Tx
        - EchoRepliesRx (bool): Echo Replies Rx
        - EchoRepliesTx (bool): Echo Replies Tx
        - EchoRequestsRx (bool): Echo Requests Rx
        - EchoRequestsTx (bool): Echo Requests Tx
        - ErrorsRx (bool): Errors Rx
        - ExperimenterErrorsRx (bool): Experimenter Errors Rx
        - FeatureRepliesRx (bool): Feature Replies Rx
        - FeatureRequestsTx (bool): Feature Requests Tx
        - FlowAddsTx (bool): Flow Adds Tx
        - FlowAggregateStatRepliesRx (bool): Flow Aggregate Stat Replies Rx
        - FlowAggregateStatRequestsTx (bool): Flow Aggregate Stat Requests Tx
        - FlowDelsTx (bool): Flow Dels Tx
        - FlowModErrorsRx (bool): Flow Mod Errors Rx
        - FlowModsTx (bool): Flow Mods Tx
        - FlowRateflowssec (bool): Flow Rate (flows/sec)
        - FlowRemovesRx (bool): Flow Removes Rx
        - FlowStatRepliesRx (bool): Flow Stat Replies Rx
        - FlowStatRequestsTx (bool): Flow Stat Requests Tx
        - GetAsynchronousConfigRepliesRx (bool): Get Asynchronous Config Replies Rx
        - GetAsynchronousConfigRequestsTx (bool): Get Asynchronous Config Requests Tx
        - GetConfigRepliesRx (bool): Get Config Replies Rx
        - GetConfigRequestsTx (bool): Get Config Requests Tx
        - GetQueueConfigRepliesRx (bool): Get Queue Config Replies Rx
        - GetQueueConfigRequestsTx (bool): Get Queue Config Requests Tx
        - GroupAddsTx (bool): Group Adds Tx
        - GroupDelsTx (bool): Group Dels Tx
        - GroupDescRepliesRx (bool): Group Desc Replies Rx
        - GroupDescRequestsTx (bool): Group Desc Requests Tx
        - GroupFeatureRepliesRx (bool): Group Feature Replies Rx
        - GroupFeatureRequestsTx (bool): Group Feature Requests Tx
        - GroupModErrorsRx (bool): Group Mod Errors Rx
        - GroupModsTx (bool): Group Mods Tx
        - GroupStatRepliesRx (bool): Group Stat Replies Rx
        - GroupStatRequestsTx (bool): Group Stat Requests Tx
        - HelloErrorsRx (bool): Hello Errors Rx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - InstructionErrorsRx (bool): Instruction Errors Rx
        - MatchErrorsRx (bool): Match Errors Rx
        - MeterAddsTx (bool): Meter Adds Tx
        - MeterConfigRepliesRx (bool): Meter Config Replies Rx
        - MeterConfigRequestsTx (bool): Meter Config Requests Tx
        - MeterDelsTx (bool): Meter Dels Tx
        - MeterFeatureRepliesRx (bool): Meter Feature Replies Rx
        - MeterFeatureRequestsTx (bool): Meter Feature Requests Tx
        - MeterModErrorsRx (bool): Meter Mod Errors Rx
        - MeterModsTx (bool): Meter Mods Tx
        - MeterStatRepliesRx (bool): Meter Stat Replies Rx
        - MeterStatRequestsTx (bool): Meter Stat Requests Tx
        - OfChannelConfigured (bool): OF Channel Configured
        - OfChannelConfiguredUp (bool): OF Channel Configured Up
        - OfChannelFlapCount (bool): OF Channel Flap Count
        - OfChannelLearnedUp (bool): OF Channel Learned Up
        - PacketInsRx (bool): Packet Ins Rx
        - PacketOutsTx (bool): Packet Outs Tx
        - PacketinReasonAction (bool): PacketIn Reason Action
        - PacketinReasonInvalidTTL (bool): PacketIn Reason Invalid TTL
        - PacketinReasonNoMatch (bool): PacketIn Reason No Match
        - PortDescRepliesRx (bool): Port Desc Replies Rx
        - PortDescRequestsTx (bool): Port Desc Requests Tx
        - PortModErrorsRx (bool): Port Mod Errors Rx
        - PortModsTx (bool): Port Mods Tx
        - PortName (bool): Port Name
        - PortStatRepliesRx (bool): Port Stat Replies Rx
        - PortStatRequestsTx (bool): Port Stat Requests Tx
        - PortStatusesRx (bool): Port Statuses Rx
        - QueueOpErrorsRx (bool): Queue Op Errors Rx
        - QueueStatRepliesRx (bool): Queue Stat Replies Rx
        - QueueStatRequestsTx (bool): Queue Stat Requests Tx
        - RequestErrorsRx (bool): Request Errors Rx
        - RoleRepliesRx (bool): Role Replies Rx
        - RoleRequestErrorsRx (bool): Role Request Errors Rx
        - RoleRequestsTx (bool): Role Requests Tx
        - SetAsynchronousConfigTx (bool): Set Asynchronous Config Tx
        - SetConfigTx (bool): Set Config Tx
        - StatRepliesRx (bool): Stat Replies Rx
        - StatRequestsTx (bool): Stat Requests Tx
        - SwitchConfigErrorsRx (bool): Switch Config Errors Rx
        - TableFeatureErrorsRx (bool): Table Feature Errors Rx
        - TableFeatureRepliesRx (bool): Table Feature Replies Rx
        - TableFeatureRequestsTx (bool): Table Feature Requests Tx
        - TableModErrorsRx (bool): Table Mod Errors Rx
        - TableModsTx (bool): Table Mods Tx
        - TableStatRepliesRx (bool): Table Stat Replies Rx
        - TableStatRequestsTx (bool): Table Stat Requests Tx
        - VendorMessagesRx (bool): Vendor Messages Rx
        - VendorMessagesTx (bool): Vendor Messages Tx
        - VendorStatRepliesRx (bool): Vendor Stat Replies Rx
        - VendorStatRequestsTx (bool): Vendor Stat Requests Tx

        Returns
        -------
        - self: This instance with matching openflowAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openflowAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openflowAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

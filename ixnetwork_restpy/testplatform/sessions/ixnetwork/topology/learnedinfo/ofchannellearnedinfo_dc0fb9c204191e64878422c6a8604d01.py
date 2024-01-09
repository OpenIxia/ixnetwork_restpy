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


class OFChannelLearnedInfo(Base):
    """OF channel learned info
    The OFChannelLearnedInfo class encapsulates a list of oFChannelLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the OFChannelLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "oFChannelLearnedInfo"
    _SDM_ATT_MAP = {
        "AsyncConfigFlowRemovedMaster": "asyncConfigFlowRemovedMaster",
        "AsyncConfigFlowRemovedSlave": "asyncConfigFlowRemovedSlave",
        "AsyncConfigPktInMaster": "asyncConfigPktInMaster",
        "AsyncConfigPktInSlave": "asyncConfigPktInSlave",
        "AsyncConfigPortStatusMaster": "asyncConfigPortStatusMaster",
        "AsyncConfigPortStatusSlave": "asyncConfigPortStatusSlave",
        "AsyncConfigResTimeOut": "asyncConfigResTimeOut",
        "DescriptionStatResponseTimeOut": "descriptionStatResponseTimeOut",
        "FlowAggrStatCookie": "flowAggrStatCookie",
        "FlowAggrStatCookieMask": "flowAggrStatCookieMask",
        "FlowAggrStatMatchCap": "flowAggrStatMatchCap",
        "FlowAggrStatOutGroup": "flowAggrStatOutGroup",
        "FlowAggrStatOutGroupValue": "flowAggrStatOutGroupValue",
        "FlowAggrStatOutPort": "flowAggrStatOutPort",
        "FlowAggrStatOutPortValue": "flowAggrStatOutPortValue",
        "FlowAggrStatResTimeOut": "flowAggrStatResTimeOut",
        "FlowAggrStatTableId": "flowAggrStatTableId",
        "FlowAggrStatTableIdValue": "flowAggrStatTableIdValue",
        "FlowStatCookie": "flowStatCookie",
        "FlowStatCookieMask": "flowStatCookieMask",
        "FlowStatMatchCap": "flowStatMatchCap",
        "FlowStatOutGroup": "flowStatOutGroup",
        "FlowStatOutGroupValue": "flowStatOutGroupValue",
        "FlowStatOutPort": "flowStatOutPort",
        "FlowStatOutPortValue": "flowStatOutPortValue",
        "FlowStatResTimeOut": "flowStatResTimeOut",
        "FlowStatTableId": "flowStatTableId",
        "FlowStatTableIdValue": "flowStatTableIdValue",
        "GenerationId": "generationId",
        "GroupDescResponseTimeOut": "groupDescResponseTimeOut",
        "GroupFeatureResponseTimeOut": "groupFeatureResponseTimeOut",
        "GroupStatIDType": "groupStatIDType",
        "GroupStatIDValue": "groupStatIDValue",
        "GroupStatMatchCapability": "groupStatMatchCapability",
        "GroupStatResponseTimeOut": "groupStatResponseTimeOut",
        "MeterConfigMeterID": "meterConfigMeterID",
        "MeterConfigMeterIDManual": "meterConfigMeterIDManual",
        "MeterConfigResponseTimeOut": "meterConfigResponseTimeOut",
        "MeterFeatureStatResponseTimeOut": "meterFeatureStatResponseTimeOut",
        "MeterStatMeterID": "meterStatMeterID",
        "MeterStatMeterIDType": "meterStatMeterIDType",
        "MeterStatResponseTimeOut": "meterStatResponseTimeOut",
        "OnDemandMessages": "onDemandMessages",
        "PacketOutAuxiliaryID": "packetOutAuxiliaryID",
        "PacketOutBufferID": "packetOutBufferID",
        "PacketOutBufferIDType": "packetOutBufferIDType",
        "PacketOutData": "packetOutData",
        "PacketOutInPort": "packetOutInPort",
        "PacketOutInPortType": "packetOutInPortType",
        "PacketOutSendData": "packetOutSendData",
        "PortFeaturesResponseTimeOut": "portFeaturesResponseTimeOut",
        "PortStatMatchCapability": "portStatMatchCapability",
        "PortStatPortNumberType": "portStatPortNumberType",
        "PortStatPortNumberValue": "portStatPortNumberValue",
        "PortStatResponseTimeOut": "portStatResponseTimeOut",
        "QueueConfigPortNumberType": "queueConfigPortNumberType",
        "QueueConfigPortNumberValue": "queueConfigPortNumberValue",
        "QueueConfigResponseTimeOut": "queueConfigResponseTimeOut",
        "QueueStatIDType": "queueStatIDType",
        "QueueStatIDValue": "queueStatIDValue",
        "QueueStatMatchCapability": "queueStatMatchCapability",
        "QueueStatPortNumberType": "queueStatPortNumberType",
        "QueueStatPortNumberValue": "queueStatPortNumberValue",
        "QueueStatResponseTimeOut": "queueStatResponseTimeOut",
        "RoleType": "roleType",
        "SetAsyncConfig": "setAsyncConfig",
        "SetSwitchConfig": "setSwitchConfig",
        "SwitchConfigDropFragments": "switchConfigDropFragments",
        "SwitchConfigMissSendLength": "switchConfigMissSendLength",
        "SwitchConfigReassembleFragments": "switchConfigReassembleFragments",
        "SwitchConfigResTimeOut": "switchConfigResTimeOut",
        "TableStatMatchCap": "tableStatMatchCap",
        "TableStatResTimeOut": "tableStatResTimeOut",
        "VendorMsgExpType": "vendorMsgExpType",
        "VendorMsgId": "vendorMsgId",
        "VendorMsgMessage": "vendorMsgMessage",
        "VendorMsgSendData": "vendorMsgSendData",
        "VendorStatExpType": "vendorStatExpType",
        "VendorStatId": "vendorStatId",
        "VendorStatMessage": "vendorStatMessage",
        "VendorStatResponseTimeOut": "vendorStatResponseTimeOut",
        "VendorStatSendData": "vendorStatSendData",
    }
    _SDM_ENUM_MAP = {
        "flowAggrStatOutGroup": ["oFPGALL", "oFPGANY", "outGroupCustom"],
        "flowAggrStatOutPort": [
            "oFPP_IN_PORT",
            "oFPP_NORMAL",
            "oFPP_FLOOD",
            "oFPP_ALL",
            "oFPP_CONTROLLER",
            "oFPP_LOCAL",
            "oFPP_ANY",
            "outPortCustom",
        ],
        "flowAggrStatTableId": ["tableIdAllTables", "tableIdCustom"],
        "flowStatOutGroup": ["oFPGALL", "oFPGANY", "outGroupCustom"],
        "flowStatOutPort": [
            "oFPP_IN_PORT",
            "oFPP_NORMAL",
            "oFPP_FLOOD",
            "oFPP_ALL",
            "oFPP_CONTROLLER",
            "oFPP_LOCAL",
            "oFPP_ANY",
            "outPortCustom",
        ],
        "flowStatTableId": ["tableIdAllTables", "tableIdCustom"],
        "groupStatIDType": ["oFPG_ALL", "oFPG_ANY", "manual"],
        "meterConfigMeterID": ["oFPM_CONTROLLER", "oFPM_SLOWPATH", "all", "manual"],
        "meterStatMeterIDType": ["oFPM_CONTROLLER", "oFPM_SLOWPATH", "all", "manual"],
        "packetOutBufferIDType": ["oPF_NO_BUFFER", "manual"],
        "packetOutInPortType": ["oFPP_CONTROLLER", "oFPP_LOCAL", "manual"],
        "portStatPortNumberType": ["oFPP_ANY", "portNumberCustom"],
        "queueConfigPortNumberType": ["oFPP_ANY", "manual"],
        "queueStatIDType": ["oFPQ_ALL", "manual"],
        "queueStatPortNumberType": ["oFPP_ANY", "manual"],
        "roleType": ["noChange", "equal", "master", "slave"],
    }

    def __init__(self, parent, list_op=False):
        super(OFChannelLearnedInfo, self).__init__(parent, list_op)

    @property
    def FlowAggrMatchProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.flowaggrmatchprofile_2ba597be74523b48fa398c0fe5ce3acf.FlowAggrMatchProfile): An instance of the FlowAggrMatchProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.flowaggrmatchprofile_2ba597be74523b48fa398c0fe5ce3acf import (
            FlowAggrMatchProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlowAggrMatchProfile", None) is not None:
                return self._properties.get("FlowAggrMatchProfile")
        return FlowAggrMatchProfile(self)

    @property
    def FlowStatMatchProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.flowstatmatchprofile_d56a9c24805ae788ef01a9b7a86babf1.FlowStatMatchProfile): An instance of the FlowStatMatchProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.flowstatmatchprofile_d56a9c24805ae788ef01a9b7a86babf1 import (
            FlowStatMatchProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlowStatMatchProfile", None) is not None:
                return self._properties.get("FlowStatMatchProfile")
        return FlowStatMatchProfile(self)

    @property
    def PacketOutActionProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.packetoutactionprofile_7087734f0df99cfe7bfd9afab773a120.PacketOutActionProfile): An instance of the PacketOutActionProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.packetoutactionprofile_7087734f0df99cfe7bfd9afab773a120 import (
            PacketOutActionProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PacketOutActionProfile", None) is not None:
                return self._properties.get("PacketOutActionProfile")
        return PacketOutActionProfile(self)

    @property
    def AsyncConfigFlowRemovedMaster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the flow removed message types that can be configured in the asynchronous messages when the controller has the Master/Equal role. Options include: 1) Flow Idle Time 2) Hard Timeout 3) Flow Delete 4) Group Delete
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsyncConfigFlowRemovedMaster"])
        )

    @property
    def AsyncConfigFlowRemovedSlave(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the flow removed message types that can be configured in the asynchronous messages when the controller has the Slave role. Options include: 1) Flow Idle Time 2) Hard Timeout 3) Flow Delete 4) Group Delete
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsyncConfigFlowRemovedSlave"])
        )

    @property
    def AsyncConfigPktInMaster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the packet-in message types that will be received when the controller has the Master/Equal role. Options include: 1) No Match 2) Action Output 3) Invalid TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsyncConfigPktInMaster"])
        )

    @property
    def AsyncConfigPktInSlave(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the packet-in message types that will be received when the controller has the Slave role. Options include: 1) No Match 2) Action Output 3) Invalid TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsyncConfigPktInSlave"])
        )

    @property
    def AsyncConfigPortStatusMaster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the port status types that can be a part of the asynchronous messages when the controller has the Master/Equal role. Options include: 1) Port Add 2) Port Delete 3) Port Modify
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsyncConfigPortStatusMaster"])
        )

    @property
    def AsyncConfigPortStatusSlave(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the port status types that can be part of the asynchronous messages when the controller has the Slave role. Options include: 1) Port Add 2) Port Delete 3) Port Modify
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsyncConfigPortStatusSlave"])
        )

    @property
    def AsyncConfigResTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsyncConfigResTimeOut"])

    @AsyncConfigResTimeOut.setter
    def AsyncConfigResTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsyncConfigResTimeOut"], value)

    @property
    def DescriptionStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptionStatResponseTimeOut"])

    @DescriptionStatResponseTimeOut.setter
    def DescriptionStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DescriptionStatResponseTimeOut"], value)

    @property
    def FlowAggrStatCookie(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Cookie of the flow entry that was looked up.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatCookie"])
        )

    @property
    def FlowAggrStatCookieMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mask used to restrict the cookie bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatCookieMask"])
        )

    @property
    def FlowAggrStatMatchCap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, match capability is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatMatchCap"])

    @FlowAggrStatMatchCap.setter
    def FlowAggrStatMatchCap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatMatchCap"], value)

    @property
    def FlowAggrStatOutGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPGALL | oFPGANY | outGroupCustom): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatOutGroup"])

    @FlowAggrStatOutGroup.setter
    def FlowAggrStatOutGroup(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatOutGroup"], value)

    @property
    def FlowAggrStatOutGroupValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Out Group is Custom/Manual, type the output group value in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatOutGroupValue"])

    @FlowAggrStatOutGroupValue.setter
    def FlowAggrStatOutGroupValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatOutGroupValue"], value)

    @property
    def FlowAggrStatOutPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatOutPort"])

    @FlowAggrStatOutPort.setter
    def FlowAggrStatOutPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatOutPort"], value)

    @property
    def FlowAggrStatOutPortValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Out Port is Custom/Manual, type the output port value in the box provided.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatOutPortValue"])

    @FlowAggrStatOutPortValue.setter
    def FlowAggrStatOutPortValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatOutPortValue"], value)

    @property
    def FlowAggrStatResTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatResTimeOut"])

    @FlowAggrStatResTimeOut.setter
    def FlowAggrStatResTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatResTimeOut"], value)

    @property
    def FlowAggrStatTableId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tableIdAllTables | tableIdCustom): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatTableId"])

    @FlowAggrStatTableId.setter
    def FlowAggrStatTableId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatTableId"], value)

    @property
    def FlowAggrStatTableIdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Table ID is Custom/ Manual, type the Table ID Number in the box given
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowAggrStatTableIdValue"])

    @FlowAggrStatTableIdValue.setter
    def FlowAggrStatTableIdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowAggrStatTableIdValue"], value)

    @property
    def FlowStatCookie(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Cookie of the flow entry that was looked up.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlowStatCookie"])
        )

    @property
    def FlowStatCookieMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mask used to restrict the cookie bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlowStatCookieMask"])
        )

    @property
    def FlowStatMatchCap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, match capability is available
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatMatchCap"])

    @FlowStatMatchCap.setter
    def FlowStatMatchCap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatMatchCap"], value)

    @property
    def FlowStatOutGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPGALL | oFPGANY | outGroupCustom): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutGroup"])

    @FlowStatOutGroup.setter
    def FlowStatOutGroup(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutGroup"], value)

    @property
    def FlowStatOutGroupValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Out Group is Custom/Manual, type the output group value in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutGroupValue"])

    @FlowStatOutGroupValue.setter
    def FlowStatOutGroupValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutGroupValue"], value)

    @property
    def FlowStatOutPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutPort"])

    @FlowStatOutPort.setter
    def FlowStatOutPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutPort"], value)

    @property
    def FlowStatOutPortValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Out Port is Custom/Manual, type the output port value in the box provided.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatOutPortValue"])

    @FlowStatOutPortValue.setter
    def FlowStatOutPortValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatOutPortValue"], value)

    @property
    def FlowStatResTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatResTimeOut"])

    @FlowStatResTimeOut.setter
    def FlowStatResTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatResTimeOut"], value)

    @property
    def FlowStatTableId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tableIdAllTables | tableIdCustom): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTableId"])

    @FlowStatTableId.setter
    def FlowStatTableId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTableId"], value)

    @property
    def FlowStatTableIdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Table ID is Custom/ Manual, type the Table ID Number in the box given
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatTableIdValue"])

    @FlowStatTableIdValue.setter
    def FlowStatTableIdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatTableIdValue"], value)

    @property
    def GenerationId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 64-bit sequence number field that identifies a given mastership view.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GenerationId"]))

    @property
    def GroupDescResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDescResponseTimeOut"])

    @GroupDescResponseTimeOut.setter
    def GroupDescResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDescResponseTimeOut"], value)

    @property
    def GroupFeatureResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFeatureResponseTimeOut"])

    @GroupFeatureResponseTimeOut.setter
    def GroupFeatureResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFeatureResponseTimeOut"], value)

    @property
    def GroupStatIDType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPG_ALL | oFPG_ANY | manual): The ID of the group used. The options are: 1) OFPG_ALL 2) OFPG_ANY 3) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatIDType"])

    @GroupStatIDType.setter
    def GroupStatIDType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatIDType"], value)

    @property
    def GroupStatIDValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Group ID Type is selected as Manual, type the Group ID in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatIDValue"])

    @GroupStatIDValue.setter
    def GroupStatIDValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatIDValue"], value)

    @property
    def GroupStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, match capability is available
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatMatchCapability"])

    @GroupStatMatchCapability.setter
    def GroupStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatMatchCapability"], value)

    @property
    def GroupStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatResponseTimeOut"])

    @GroupStatResponseTimeOut.setter
    def GroupStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatResponseTimeOut"], value)

    @property
    def MeterConfigMeterID(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigMeterID"])

    @MeterConfigMeterID.setter
    def MeterConfigMeterID(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigMeterID"], value)

    @property
    def MeterConfigMeterIDManual(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Meter ID Type is selected as Manual, type the meter ID in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigMeterIDManual"])

    @MeterConfigMeterIDManual.setter
    def MeterConfigMeterIDManual(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigMeterIDManual"], value)

    @property
    def MeterConfigResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterConfigResponseTimeOut"])

    @MeterConfigResponseTimeOut.setter
    def MeterConfigResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterConfigResponseTimeOut"], value)

    @property
    def MeterFeatureStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterFeatureStatResponseTimeOut"])

    @MeterFeatureStatResponseTimeOut.setter
    def MeterFeatureStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterFeatureStatResponseTimeOut"], value)

    @property
    def MeterStatMeterID(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Meter ID Type is selected as Manual, type the meter ID in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatMeterID"])

    @MeterStatMeterID.setter
    def MeterStatMeterID(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatMeterID"], value)

    @property
    def MeterStatMeterIDType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatMeterIDType"])

    @MeterStatMeterIDType.setter
    def MeterStatMeterIDType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatMeterIDType"], value)

    @property
    def MeterStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterStatResponseTimeOut"])

    @MeterStatResponseTimeOut.setter
    def MeterStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeterStatResponseTimeOut"], value)

    @property
    def OnDemandMessages(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OnDemandMessages"])
        )

    @property
    def PacketOutAuxiliaryID(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier of the auxiliary connection.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutAuxiliaryID"])

    @PacketOutAuxiliaryID.setter
    def PacketOutAuxiliaryID(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutAuxiliaryID"], value)

    @property
    def PacketOutBufferID(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Buffer ID Type is selected as Manual, type the buffer ID in the box provided.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutBufferID"])

    @PacketOutBufferID.setter
    def PacketOutBufferID(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutBufferID"], value)

    @property
    def PacketOutBufferIDType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oPF_NO_BUFFER | manual): Specify the buffer identifier. The options are: 1) OPF_NO_BUFFER 2) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutBufferIDType"])

    @PacketOutBufferIDType.setter
    def PacketOutBufferIDType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutBufferIDType"], value)

    @property
    def PacketOutData(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The data of the packet out message in hexadecimal format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PacketOutData"]))

    @property
    def PacketOutInPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If In Port Type is selected as Manual, type the input port type in the box provided.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutInPort"])

    @PacketOutInPort.setter
    def PacketOutInPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutInPort"], value)

    @property
    def PacketOutInPortType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_CONTROLLER | oFPP_LOCAL | manual): Specify the Input Port Type. The options are: 1) OFPP_CONTROLLER 2) OFPP_LOCAL 3) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutInPortType"])

    @PacketOutInPortType.setter
    def PacketOutInPortType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutInPortType"], value)

    @property
    def PacketOutSendData(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected,the system sends packet out data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketOutSendData"])

    @PacketOutSendData.setter
    def PacketOutSendData(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketOutSendData"], value)

    @property
    def PortFeaturesResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortFeaturesResponseTimeOut"])

    @PortFeaturesResponseTimeOut.setter
    def PortFeaturesResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortFeaturesResponseTimeOut"], value)

    @property
    def PortStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, match capability is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatMatchCapability"])

    @PortStatMatchCapability.setter
    def PortStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatMatchCapability"], value)

    @property
    def PortStatPortNumberType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_ANY | portNumberCustom): Specify the port number. Options include: 1) OFPP_ANY 2) Manual/Custom
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatPortNumberType"])

    @PortStatPortNumberType.setter
    def PortStatPortNumberType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatPortNumberType"], value)

    @property
    def PortStatPortNumberValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Port Number Type is selected as Custom/Manual, type the port number in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatPortNumberValue"])

    @PortStatPortNumberValue.setter
    def PortStatPortNumberValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatPortNumberValue"], value)

    @property
    def PortStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatResponseTimeOut"])

    @PortStatResponseTimeOut.setter
    def PortStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatResponseTimeOut"], value)

    @property
    def QueueConfigPortNumberType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_ANY | manual): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigPortNumberType"])

    @QueueConfigPortNumberType.setter
    def QueueConfigPortNumberType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigPortNumberType"], value)

    @property
    def QueueConfigPortNumberValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Port Number Type is selected as Manual, type the port number in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigPortNumberValue"])

    @QueueConfigPortNumberValue.setter
    def QueueConfigPortNumberValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigPortNumberValue"], value)

    @property
    def QueueConfigResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueConfigResponseTimeOut"])

    @QueueConfigResponseTimeOut.setter
    def QueueConfigResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueConfigResponseTimeOut"], value)

    @property
    def QueueStatIDType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPQ_ALL | manual): The unique queue identifier. The options are: 1) OFPQ_ALL 2) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatIDType"])

    @QueueStatIDType.setter
    def QueueStatIDType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatIDType"], value)

    @property
    def QueueStatIDValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Queue ID Type is selected as Manual, type the queue ID in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatIDValue"])

    @QueueStatIDValue.setter
    def QueueStatIDValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatIDValue"], value)

    @property
    def QueueStatMatchCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, match capability is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatMatchCapability"])

    @QueueStatMatchCapability.setter
    def QueueStatMatchCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatMatchCapability"], value)

    @property
    def QueueStatPortNumberType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_ANY | manual): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatPortNumberType"])

    @QueueStatPortNumberType.setter
    def QueueStatPortNumberType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatPortNumberType"], value)

    @property
    def QueueStatPortNumberValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Port Number Type is selected as Manual, type the port number in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatPortNumberValue"])

    @QueueStatPortNumberValue.setter
    def QueueStatPortNumberValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatPortNumberValue"], value)

    @property
    def QueueStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatResponseTimeOut"])

    @QueueStatResponseTimeOut.setter
    def QueueStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatResponseTimeOut"], value)

    @property
    def RoleType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noChange | equal | master | slave): Specify the Role Type. The options are: 1) NoChange 2) Equal 3) Master 4) Slave
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoleType"])

    @RoleType.setter
    def RoleType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoleType"], value)

    @property
    def SetAsyncConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetAsyncConfig"])

    @SetAsyncConfig.setter
    def SetAsyncConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetAsyncConfig"], value)

    @property
    def SetSwitchConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the corresponding switch configuration parameters are available. This option is available only if Switch Config is selected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetSwitchConfig"])

    @SetSwitchConfig.setter
    def SetSwitchConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetSwitchConfig"], value)

    @property
    def SwitchConfigDropFragments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IP fragments are dropped.
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
        - number: The length of the table-miss message sent.
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
        - bool: If selected, IP fragments are reassembled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigReassembleFragments"])

    @SwitchConfigReassembleFragments.setter
    def SwitchConfigReassembleFragments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigReassembleFragments"], value)

    @property
    def SwitchConfigResTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchConfigResTimeOut"])

    @SwitchConfigResTimeOut.setter
    def SwitchConfigResTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchConfigResTimeOut"], value)

    @property
    def TableStatMatchCap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, match capability is available
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatMatchCap"])

    @TableStatMatchCap.setter
    def TableStatMatchCap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatMatchCap"], value)

    @property
    def TableStatResTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out, if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatResTimeOut"])

    @TableStatResTimeOut.setter
    def TableStatResTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatResTimeOut"], value)

    @property
    def VendorMsgExpType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of Experimenter
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMsgExpType"])

    @VendorMsgExpType.setter
    def VendorMsgExpType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMsgExpType"], value)

    @property
    def VendorMsgId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique Vendor/Experimenter identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMsgId"])

    @VendorMsgId.setter
    def VendorMsgId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMsgId"], value)

    @property
    def VendorMsgMessage(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Experimenter message value in hexadecimal format
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorMsgMessage"])
        )

    @property
    def VendorMsgSendData(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected,It sends vendor stat Data
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMsgSendData"])

    @VendorMsgSendData.setter
    def VendorMsgSendData(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMsgSendData"], value)

    @property
    def VendorStatExpType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of Experimenter
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatExpType"])

    @VendorStatExpType.setter
    def VendorStatExpType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatExpType"], value)

    @property
    def VendorStatId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique Vendor/Experimenter identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatId"])

    @VendorStatId.setter
    def VendorStatId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatId"], value)

    @property
    def VendorStatMessage(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Experimenter message value in hexadecimal format
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorStatMessage"])
        )

    @property
    def VendorStatResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatResponseTimeOut"])

    @VendorStatResponseTimeOut.setter
    def VendorStatResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatResponseTimeOut"], value)

    @property
    def VendorStatSendData(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the system sends vendor stat Data
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorStatSendData"])

    @VendorStatSendData.setter
    def VendorStatSendData(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorStatSendData"], value)

    def update(
        self,
        AsyncConfigResTimeOut=None,
        DescriptionStatResponseTimeOut=None,
        FlowAggrStatMatchCap=None,
        FlowAggrStatOutGroup=None,
        FlowAggrStatOutGroupValue=None,
        FlowAggrStatOutPort=None,
        FlowAggrStatOutPortValue=None,
        FlowAggrStatResTimeOut=None,
        FlowAggrStatTableId=None,
        FlowAggrStatTableIdValue=None,
        FlowStatMatchCap=None,
        FlowStatOutGroup=None,
        FlowStatOutGroupValue=None,
        FlowStatOutPort=None,
        FlowStatOutPortValue=None,
        FlowStatResTimeOut=None,
        FlowStatTableId=None,
        FlowStatTableIdValue=None,
        GroupDescResponseTimeOut=None,
        GroupFeatureResponseTimeOut=None,
        GroupStatIDType=None,
        GroupStatIDValue=None,
        GroupStatMatchCapability=None,
        GroupStatResponseTimeOut=None,
        MeterConfigMeterID=None,
        MeterConfigMeterIDManual=None,
        MeterConfigResponseTimeOut=None,
        MeterFeatureStatResponseTimeOut=None,
        MeterStatMeterID=None,
        MeterStatMeterIDType=None,
        MeterStatResponseTimeOut=None,
        PacketOutAuxiliaryID=None,
        PacketOutBufferID=None,
        PacketOutBufferIDType=None,
        PacketOutInPort=None,
        PacketOutInPortType=None,
        PacketOutSendData=None,
        PortFeaturesResponseTimeOut=None,
        PortStatMatchCapability=None,
        PortStatPortNumberType=None,
        PortStatPortNumberValue=None,
        PortStatResponseTimeOut=None,
        QueueConfigPortNumberType=None,
        QueueConfigPortNumberValue=None,
        QueueConfigResponseTimeOut=None,
        QueueStatIDType=None,
        QueueStatIDValue=None,
        QueueStatMatchCapability=None,
        QueueStatPortNumberType=None,
        QueueStatPortNumberValue=None,
        QueueStatResponseTimeOut=None,
        RoleType=None,
        SetAsyncConfig=None,
        SetSwitchConfig=None,
        SwitchConfigDropFragments=None,
        SwitchConfigMissSendLength=None,
        SwitchConfigReassembleFragments=None,
        SwitchConfigResTimeOut=None,
        TableStatMatchCap=None,
        TableStatResTimeOut=None,
        VendorMsgExpType=None,
        VendorMsgId=None,
        VendorMsgSendData=None,
        VendorStatExpType=None,
        VendorStatId=None,
        VendorStatResponseTimeOut=None,
        VendorStatSendData=None,
    ):
        # type: (int, int, bool, str, int, str, int, int, str, int, bool, str, int, str, int, int, str, int, int, int, str, int, bool, int, str, int, int, int, int, str, int, int, int, str, int, str, bool, int, bool, str, int, int, str, int, int, str, int, bool, str, int, int, str, bool, bool, bool, int, bool, int, bool, int, int, int, bool, int, int, int, bool) -> OFChannelLearnedInfo
        """Updates oFChannelLearnedInfo resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AsyncConfigResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - DescriptionStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - FlowAggrStatMatchCap (bool): If selected, match capability is available.
        - FlowAggrStatOutGroup (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowAggrStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowAggrStatOutPort (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowAggrStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value in the box provided.
        - FlowAggrStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - FlowAggrStatTableId (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        - FlowAggrStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number in the box given
        - FlowStatMatchCap (bool): If selected, match capability is available
        - FlowStatOutGroup (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowStatOutPort (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value in the box provided.
        - FlowStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - FlowStatTableId (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        - FlowStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number in the box given
        - GroupDescResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - GroupFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - GroupStatIDType (str(oFPG_ALL | oFPG_ANY | manual)): The ID of the group used. The options are: 1) OFPG_ALL 2) OFPG_ANY 3) Manual
        - GroupStatIDValue (number): If Group ID Type is selected as Manual, type the Group ID in the box provided
        - GroupStatMatchCapability (bool): If selected, match capability is available
        - GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - MeterConfigMeterID (str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual)): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        - MeterConfigMeterIDManual (number): If Meter ID Type is selected as Manual, type the meter ID in the box provided
        - MeterConfigResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - MeterFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - MeterStatMeterID (number): If Meter ID Type is selected as Manual, type the meter ID in the box provided
        - MeterStatMeterIDType (str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual)): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        - MeterStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - PacketOutAuxiliaryID (number): The identifier of the auxiliary connection.
        - PacketOutBufferID (number): If Buffer ID Type is selected as Manual, type the buffer ID in the box provided.
        - PacketOutBufferIDType (str(oPF_NO_BUFFER | manual)): Specify the buffer identifier. The options are: 1) OPF_NO_BUFFER 2) Manual
        - PacketOutInPort (number): If In Port Type is selected as Manual, type the input port type in the box provided.
        - PacketOutInPortType (str(oFPP_CONTROLLER | oFPP_LOCAL | manual)): Specify the Input Port Type. The options are: 1) OFPP_CONTROLLER 2) OFPP_LOCAL 3) Manual
        - PacketOutSendData (bool): If selected,the system sends packet out data.
        - PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - PortStatMatchCapability (bool): If selected, match capability is available.
        - PortStatPortNumberType (str(oFPP_ANY | portNumberCustom)): Specify the port number. Options include: 1) OFPP_ANY 2) Manual/Custom
        - PortStatPortNumberValue (number): If Port Number Type is selected as Custom/Manual, type the port number in the box provided
        - PortStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - QueueConfigPortNumberType (str(oFPP_ANY | manual)): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        - QueueConfigPortNumberValue (number): If Port Number Type is selected as Manual, type the port number in the box provided
        - QueueConfigResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - QueueStatIDType (str(oFPQ_ALL | manual)): The unique queue identifier. The options are: 1) OFPQ_ALL 2) Manual
        - QueueStatIDValue (number): If Queue ID Type is selected as Manual, type the queue ID in the box provided
        - QueueStatMatchCapability (bool): If selected, match capability is available.
        - QueueStatPortNumberType (str(oFPP_ANY | manual)): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        - QueueStatPortNumberValue (number): If Port Number Type is selected as Manual, type the port number in the box provided
        - QueueStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - RoleType (str(noChange | equal | master | slave)): Specify the Role Type. The options are: 1) NoChange 2) Equal 3) Master 4) Slave
        - SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - SetSwitchConfig (bool): If selected, the corresponding switch configuration parameters are available. This option is available only if Switch Config is selected.
        - SwitchConfigDropFragments (bool): If selected, IP fragments are dropped.
        - SwitchConfigMissSendLength (number): The length of the table-miss message sent.
        - SwitchConfigReassembleFragments (bool): If selected, IP fragments are reassembled.
        - SwitchConfigResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - TableStatMatchCap (bool): If selected, match capability is available
        - TableStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - VendorMsgExpType (number): The type of Experimenter
        - VendorMsgId (number): The unique Vendor/Experimenter identifier
        - VendorMsgSendData (bool): If selected,It sends vendor stat Data
        - VendorStatExpType (number): The type of Experimenter
        - VendorStatId (number): The unique Vendor/Experimenter identifier
        - VendorStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - VendorStatSendData (bool): If selected, the system sends vendor stat Data

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AsyncConfigResTimeOut=None,
        DescriptionStatResponseTimeOut=None,
        FlowAggrStatMatchCap=None,
        FlowAggrStatOutGroup=None,
        FlowAggrStatOutGroupValue=None,
        FlowAggrStatOutPort=None,
        FlowAggrStatOutPortValue=None,
        FlowAggrStatResTimeOut=None,
        FlowAggrStatTableId=None,
        FlowAggrStatTableIdValue=None,
        FlowStatMatchCap=None,
        FlowStatOutGroup=None,
        FlowStatOutGroupValue=None,
        FlowStatOutPort=None,
        FlowStatOutPortValue=None,
        FlowStatResTimeOut=None,
        FlowStatTableId=None,
        FlowStatTableIdValue=None,
        GroupDescResponseTimeOut=None,
        GroupFeatureResponseTimeOut=None,
        GroupStatIDType=None,
        GroupStatIDValue=None,
        GroupStatMatchCapability=None,
        GroupStatResponseTimeOut=None,
        MeterConfigMeterID=None,
        MeterConfigMeterIDManual=None,
        MeterConfigResponseTimeOut=None,
        MeterFeatureStatResponseTimeOut=None,
        MeterStatMeterID=None,
        MeterStatMeterIDType=None,
        MeterStatResponseTimeOut=None,
        PacketOutAuxiliaryID=None,
        PacketOutBufferID=None,
        PacketOutBufferIDType=None,
        PacketOutInPort=None,
        PacketOutInPortType=None,
        PacketOutSendData=None,
        PortFeaturesResponseTimeOut=None,
        PortStatMatchCapability=None,
        PortStatPortNumberType=None,
        PortStatPortNumberValue=None,
        PortStatResponseTimeOut=None,
        QueueConfigPortNumberType=None,
        QueueConfigPortNumberValue=None,
        QueueConfigResponseTimeOut=None,
        QueueStatIDType=None,
        QueueStatIDValue=None,
        QueueStatMatchCapability=None,
        QueueStatPortNumberType=None,
        QueueStatPortNumberValue=None,
        QueueStatResponseTimeOut=None,
        RoleType=None,
        SetAsyncConfig=None,
        SetSwitchConfig=None,
        SwitchConfigDropFragments=None,
        SwitchConfigMissSendLength=None,
        SwitchConfigReassembleFragments=None,
        SwitchConfigResTimeOut=None,
        TableStatMatchCap=None,
        TableStatResTimeOut=None,
        VendorMsgExpType=None,
        VendorMsgId=None,
        VendorMsgSendData=None,
        VendorStatExpType=None,
        VendorStatId=None,
        VendorStatResponseTimeOut=None,
        VendorStatSendData=None,
    ):
        # type: (int, int, bool, str, int, str, int, int, str, int, bool, str, int, str, int, int, str, int, int, int, str, int, bool, int, str, int, int, int, int, str, int, int, int, str, int, str, bool, int, bool, str, int, int, str, int, int, str, int, bool, str, int, int, str, bool, bool, bool, int, bool, int, bool, int, int, int, bool, int, int, int, bool) -> OFChannelLearnedInfo
        """Adds a new oFChannelLearnedInfo resource on the json, only valid with batch add utility

        Args
        ----
        - AsyncConfigResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - DescriptionStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - FlowAggrStatMatchCap (bool): If selected, match capability is available.
        - FlowAggrStatOutGroup (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowAggrStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowAggrStatOutPort (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowAggrStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value in the box provided.
        - FlowAggrStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - FlowAggrStatTableId (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        - FlowAggrStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number in the box given
        - FlowStatMatchCap (bool): If selected, match capability is available
        - FlowStatOutGroup (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowStatOutPort (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value in the box provided.
        - FlowStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - FlowStatTableId (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        - FlowStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number in the box given
        - GroupDescResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - GroupFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - GroupStatIDType (str(oFPG_ALL | oFPG_ANY | manual)): The ID of the group used. The options are: 1) OFPG_ALL 2) OFPG_ANY 3) Manual
        - GroupStatIDValue (number): If Group ID Type is selected as Manual, type the Group ID in the box provided
        - GroupStatMatchCapability (bool): If selected, match capability is available
        - GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - MeterConfigMeterID (str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual)): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        - MeterConfigMeterIDManual (number): If Meter ID Type is selected as Manual, type the meter ID in the box provided
        - MeterConfigResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - MeterFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - MeterStatMeterID (number): If Meter ID Type is selected as Manual, type the meter ID in the box provided
        - MeterStatMeterIDType (str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual)): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        - MeterStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - PacketOutAuxiliaryID (number): The identifier of the auxiliary connection.
        - PacketOutBufferID (number): If Buffer ID Type is selected as Manual, type the buffer ID in the box provided.
        - PacketOutBufferIDType (str(oPF_NO_BUFFER | manual)): Specify the buffer identifier. The options are: 1) OPF_NO_BUFFER 2) Manual
        - PacketOutInPort (number): If In Port Type is selected as Manual, type the input port type in the box provided.
        - PacketOutInPortType (str(oFPP_CONTROLLER | oFPP_LOCAL | manual)): Specify the Input Port Type. The options are: 1) OFPP_CONTROLLER 2) OFPP_LOCAL 3) Manual
        - PacketOutSendData (bool): If selected,the system sends packet out data.
        - PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - PortStatMatchCapability (bool): If selected, match capability is available.
        - PortStatPortNumberType (str(oFPP_ANY | portNumberCustom)): Specify the port number. Options include: 1) OFPP_ANY 2) Manual/Custom
        - PortStatPortNumberValue (number): If Port Number Type is selected as Custom/Manual, type the port number in the box provided
        - PortStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - QueueConfigPortNumberType (str(oFPP_ANY | manual)): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        - QueueConfigPortNumberValue (number): If Port Number Type is selected as Manual, type the port number in the box provided
        - QueueConfigResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - QueueStatIDType (str(oFPQ_ALL | manual)): The unique queue identifier. The options are: 1) OFPQ_ALL 2) Manual
        - QueueStatIDValue (number): If Queue ID Type is selected as Manual, type the queue ID in the box provided
        - QueueStatMatchCapability (bool): If selected, match capability is available.
        - QueueStatPortNumberType (str(oFPP_ANY | manual)): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        - QueueStatPortNumberValue (number): If Port Number Type is selected as Manual, type the port number in the box provided
        - QueueStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - RoleType (str(noChange | equal | master | slave)): Specify the Role Type. The options are: 1) NoChange 2) Equal 3) Master 4) Slave
        - SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - SetSwitchConfig (bool): If selected, the corresponding switch configuration parameters are available. This option is available only if Switch Config is selected.
        - SwitchConfigDropFragments (bool): If selected, IP fragments are dropped.
        - SwitchConfigMissSendLength (number): The length of the table-miss message sent.
        - SwitchConfigReassembleFragments (bool): If selected, IP fragments are reassembled.
        - SwitchConfigResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - TableStatMatchCap (bool): If selected, match capability is available
        - TableStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - VendorMsgExpType (number): The type of Experimenter
        - VendorMsgId (number): The unique Vendor/Experimenter identifier
        - VendorMsgSendData (bool): If selected,It sends vendor stat Data
        - VendorStatExpType (number): The type of Experimenter
        - VendorStatId (number): The unique Vendor/Experimenter identifier
        - VendorStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - VendorStatSendData (bool): If selected, the system sends vendor stat Data

        Returns
        -------
        - self: This instance with all currently retrieved oFChannelLearnedInfo resources using find and the newly added oFChannelLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AsyncConfigResTimeOut=None,
        DescriptionStatResponseTimeOut=None,
        FlowAggrStatMatchCap=None,
        FlowAggrStatOutGroup=None,
        FlowAggrStatOutGroupValue=None,
        FlowAggrStatOutPort=None,
        FlowAggrStatOutPortValue=None,
        FlowAggrStatResTimeOut=None,
        FlowAggrStatTableId=None,
        FlowAggrStatTableIdValue=None,
        FlowStatMatchCap=None,
        FlowStatOutGroup=None,
        FlowStatOutGroupValue=None,
        FlowStatOutPort=None,
        FlowStatOutPortValue=None,
        FlowStatResTimeOut=None,
        FlowStatTableId=None,
        FlowStatTableIdValue=None,
        GroupDescResponseTimeOut=None,
        GroupFeatureResponseTimeOut=None,
        GroupStatIDType=None,
        GroupStatIDValue=None,
        GroupStatMatchCapability=None,
        GroupStatResponseTimeOut=None,
        MeterConfigMeterID=None,
        MeterConfigMeterIDManual=None,
        MeterConfigResponseTimeOut=None,
        MeterFeatureStatResponseTimeOut=None,
        MeterStatMeterID=None,
        MeterStatMeterIDType=None,
        MeterStatResponseTimeOut=None,
        PacketOutAuxiliaryID=None,
        PacketOutBufferID=None,
        PacketOutBufferIDType=None,
        PacketOutInPort=None,
        PacketOutInPortType=None,
        PacketOutSendData=None,
        PortFeaturesResponseTimeOut=None,
        PortStatMatchCapability=None,
        PortStatPortNumberType=None,
        PortStatPortNumberValue=None,
        PortStatResponseTimeOut=None,
        QueueConfigPortNumberType=None,
        QueueConfigPortNumberValue=None,
        QueueConfigResponseTimeOut=None,
        QueueStatIDType=None,
        QueueStatIDValue=None,
        QueueStatMatchCapability=None,
        QueueStatPortNumberType=None,
        QueueStatPortNumberValue=None,
        QueueStatResponseTimeOut=None,
        RoleType=None,
        SetAsyncConfig=None,
        SetSwitchConfig=None,
        SwitchConfigDropFragments=None,
        SwitchConfigMissSendLength=None,
        SwitchConfigReassembleFragments=None,
        SwitchConfigResTimeOut=None,
        TableStatMatchCap=None,
        TableStatResTimeOut=None,
        VendorMsgExpType=None,
        VendorMsgId=None,
        VendorMsgSendData=None,
        VendorStatExpType=None,
        VendorStatId=None,
        VendorStatResponseTimeOut=None,
        VendorStatSendData=None,
    ):
        # type: (int, int, bool, str, int, str, int, int, str, int, bool, str, int, str, int, int, str, int, int, int, str, int, bool, int, str, int, int, int, int, str, int, int, int, str, int, str, bool, int, bool, str, int, int, str, int, int, str, int, bool, str, int, int, str, bool, bool, bool, int, bool, int, bool, int, int, int, bool, int, int, int, bool) -> OFChannelLearnedInfo
        """Finds and retrieves oFChannelLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve oFChannelLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all oFChannelLearnedInfo resources from the server.

        Args
        ----
        - AsyncConfigResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - DescriptionStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - FlowAggrStatMatchCap (bool): If selected, match capability is available.
        - FlowAggrStatOutGroup (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowAggrStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowAggrStatOutPort (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowAggrStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value in the box provided.
        - FlowAggrStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - FlowAggrStatTableId (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        - FlowAggrStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number in the box given
        - FlowStatMatchCap (bool): If selected, match capability is available
        - FlowStatOutGroup (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowStatOutPort (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value in the box provided.
        - FlowStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - FlowStatTableId (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual
        - FlowStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number in the box given
        - GroupDescResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - GroupFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - GroupStatIDType (str(oFPG_ALL | oFPG_ANY | manual)): The ID of the group used. The options are: 1) OFPG_ALL 2) OFPG_ANY 3) Manual
        - GroupStatIDValue (number): If Group ID Type is selected as Manual, type the Group ID in the box provided
        - GroupStatMatchCapability (bool): If selected, match capability is available
        - GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - MeterConfigMeterID (str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual)): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        - MeterConfigMeterIDManual (number): If Meter ID Type is selected as Manual, type the meter ID in the box provided
        - MeterConfigResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - MeterFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - MeterStatMeterID (number): If Meter ID Type is selected as Manual, type the meter ID in the box provided
        - MeterStatMeterIDType (str(oFPM_CONTROLLER | oFPM_SLOWPATH | all | manual)): The ID of the meter used. The options are: 1) OFPM_SLOWPATH 2) OFPM_CONTROLLER 3) OFPM_All 4) Manual
        - MeterStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - PacketOutAuxiliaryID (number): The identifier of the auxiliary connection.
        - PacketOutBufferID (number): If Buffer ID Type is selected as Manual, type the buffer ID in the box provided.
        - PacketOutBufferIDType (str(oPF_NO_BUFFER | manual)): Specify the buffer identifier. The options are: 1) OPF_NO_BUFFER 2) Manual
        - PacketOutInPort (number): If In Port Type is selected as Manual, type the input port type in the box provided.
        - PacketOutInPortType (str(oFPP_CONTROLLER | oFPP_LOCAL | manual)): Specify the Input Port Type. The options are: 1) OFPP_CONTROLLER 2) OFPP_LOCAL 3) Manual
        - PacketOutSendData (bool): If selected,the system sends packet out data.
        - PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - PortStatMatchCapability (bool): If selected, match capability is available.
        - PortStatPortNumberType (str(oFPP_ANY | portNumberCustom)): Specify the port number. Options include: 1) OFPP_ANY 2) Manual/Custom
        - PortStatPortNumberValue (number): If Port Number Type is selected as Custom/Manual, type the port number in the box provided
        - PortStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - QueueConfigPortNumberType (str(oFPP_ANY | manual)): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        - QueueConfigPortNumberValue (number): If Port Number Type is selected as Manual, type the port number in the box provided
        - QueueConfigResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received
        - QueueStatIDType (str(oFPQ_ALL | manual)): The unique queue identifier. The options are: 1) OFPQ_ALL 2) Manual
        - QueueStatIDValue (number): If Queue ID Type is selected as Manual, type the queue ID in the box provided
        - QueueStatMatchCapability (bool): If selected, match capability is available.
        - QueueStatPortNumberType (str(oFPP_ANY | manual)): The number of the port used. The options are: 1) OFPP_ANY 2) Manual
        - QueueStatPortNumberValue (number): If Port Number Type is selected as Manual, type the port number in the box provided
        - QueueStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - RoleType (str(noChange | equal | master | slave)): Specify the Role Type. The options are: 1) NoChange 2) Equal 3) Master 4) Slave
        - SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - SetSwitchConfig (bool): If selected, the corresponding switch configuration parameters are available. This option is available only if Switch Config is selected.
        - SwitchConfigDropFragments (bool): If selected, IP fragments are dropped.
        - SwitchConfigMissSendLength (number): The length of the table-miss message sent.
        - SwitchConfigReassembleFragments (bool): If selected, IP fragments are reassembled.
        - SwitchConfigResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - TableStatMatchCap (bool): If selected, match capability is available
        - TableStatResTimeOut (number): The time in milliseconds after which the trigger request times out, if no response is received.
        - VendorMsgExpType (number): The type of Experimenter
        - VendorMsgId (number): The unique Vendor/Experimenter identifier
        - VendorMsgSendData (bool): If selected,It sends vendor stat Data
        - VendorStatExpType (number): The type of Experimenter
        - VendorStatId (number): The unique Vendor/Experimenter identifier
        - VendorStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - VendorStatSendData (bool): If selected, the system sends vendor stat Data

        Returns
        -------
        - self: This instance with matching oFChannelLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of oFChannelLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the oFChannelLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def SendOnDemandMessage(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendOnDemandMessage operation on the server.

        Sends learned on demand messages for the OF Channels.

        sendOnDemandMessage(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of OF Channels into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "sendOnDemandMessage", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        AsyncConfigFlowRemovedMaster=None,
        AsyncConfigFlowRemovedSlave=None,
        AsyncConfigPktInMaster=None,
        AsyncConfigPktInSlave=None,
        AsyncConfigPortStatusMaster=None,
        AsyncConfigPortStatusSlave=None,
        FlowAggrStatCookie=None,
        FlowAggrStatCookieMask=None,
        FlowStatCookie=None,
        FlowStatCookieMask=None,
        GenerationId=None,
        OnDemandMessages=None,
        PacketOutData=None,
        VendorMsgMessage=None,
        VendorStatMessage=None,
    ):
        """Base class infrastructure that gets a list of oFChannelLearnedInfo device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AsyncConfigFlowRemovedMaster (str): optional regex of asyncConfigFlowRemovedMaster
        - AsyncConfigFlowRemovedSlave (str): optional regex of asyncConfigFlowRemovedSlave
        - AsyncConfigPktInMaster (str): optional regex of asyncConfigPktInMaster
        - AsyncConfigPktInSlave (str): optional regex of asyncConfigPktInSlave
        - AsyncConfigPortStatusMaster (str): optional regex of asyncConfigPortStatusMaster
        - AsyncConfigPortStatusSlave (str): optional regex of asyncConfigPortStatusSlave
        - FlowAggrStatCookie (str): optional regex of flowAggrStatCookie
        - FlowAggrStatCookieMask (str): optional regex of flowAggrStatCookieMask
        - FlowStatCookie (str): optional regex of flowStatCookie
        - FlowStatCookieMask (str): optional regex of flowStatCookieMask
        - GenerationId (str): optional regex of generationId
        - OnDemandMessages (str): optional regex of onDemandMessages
        - PacketOutData (str): optional regex of packetOutData
        - VendorMsgMessage (str): optional regex of vendorMsgMessage
        - VendorStatMessage (str): optional regex of vendorStatMessage

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

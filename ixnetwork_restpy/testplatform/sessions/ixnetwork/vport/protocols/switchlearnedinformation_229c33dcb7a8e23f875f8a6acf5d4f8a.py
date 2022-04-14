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


class SwitchLearnedInformation(Base):
    """This object allows to configure the switch learned information parameters.
    The SwitchLearnedInformation class encapsulates a required switchLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "switchLearnedInformation"
    _SDM_ATT_MAP = {
        "EnableVendorExperimenterMessage": "enableVendorExperimenterMessage",
        "EthernetDestination": "ethernetDestination",
        "EthernetSource": "ethernetSource",
        "EthernetType": "ethernetType",
        "InPort": "inPort",
        "IpDscp": "ipDscp",
        "IpProtocol": "ipProtocol",
        "Ipv4Source": "ipv4Source",
        "Ipv4destination": "ipv4destination",
        "IsOfChannelLearnedInformationRefreshed": "isOfChannelLearnedInformationRefreshed",
        "IsOfFlowsLearnedInformationRefreshed": "isOfFlowsLearnedInformationRefreshed",
        "OutPort": "outPort",
        "OutPortInputMode": "outPortInputMode",
        "TableId": "tableId",
        "TableIdInputMode": "tableIdInputMode",
        "TansportSource": "tansportSource",
        "TransportDestination": "transportDestination",
        "VendorExperimenterId": "vendorExperimenterId",
        "VendorExperimenterType": "vendorExperimenterType",
        "VendorMessage": "vendorMessage",
        "VendorMessageLength": "vendorMessageLength",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {
        "outPortInputMode": [
            "ofppMax",
            "ofppInPort",
            "ofppTable",
            "ofppNormal",
            "ofppFlood",
            "ofppAll",
            "ofppController",
            "ofppLocal",
            "ofppNone",
            "outPortCustom",
        ],
        "tableIdInputMode": ["allTables", "emergency", "tableIdCustom"],
    }

    def __init__(self, parent, list_op=False):
        super(SwitchLearnedInformation, self).__init__(parent, list_op)

    @property
    def OfChannelSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_b388ce0c4d70741ca769d564a7b8e654.OfChannelSwitchLearnedInfo): An instance of the OfChannelSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_b388ce0c4d70741ca769d564a7b8e654 import (
            OfChannelSwitchLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OfChannelSwitchLearnedInfo", None) is not None:
                return self._properties.get("OfChannelSwitchLearnedInfo")
        return OfChannelSwitchLearnedInfo(self)

    @property
    def SwitchFlow131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_e48e6a22f9f9bbf78e2684330b75a32e.SwitchFlow131TriggerAttributes): An instance of the SwitchFlow131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_e48e6a22f9f9bbf78e2684330b75a32e import (
            SwitchFlow131TriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchFlow131TriggerAttributes", None) is not None:
                return self._properties.get("SwitchFlow131TriggerAttributes")
        return SwitchFlow131TriggerAttributes(self)._select()

    @property
    def SwitchFlowLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_5f61b81a749e83192f2f0aba3723f328.SwitchFlowLearnedInfo): An instance of the SwitchFlowLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_5f61b81a749e83192f2f0aba3723f328 import (
            SwitchFlowLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchFlowLearnedInfo", None) is not None:
                return self._properties.get("SwitchFlowLearnedInfo")
        return SwitchFlowLearnedInfo(self)

    @property
    def SwitchFlowMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_bfd68967531928dd87f9224a41a38633.SwitchFlowMatchCriteria131TriggerAttributes): An instance of the SwitchFlowMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_bfd68967531928dd87f9224a41a38633 import (
            SwitchFlowMatchCriteria131TriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get(
                    "SwitchFlowMatchCriteria131TriggerAttributes", None
                )
                is not None
            ):
                return self._properties.get(
                    "SwitchFlowMatchCriteria131TriggerAttributes"
                )
        return SwitchFlowMatchCriteria131TriggerAttributes(self)._select()

    @property
    def SwitchGroupLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_1b0e7ca2c5c5bf68353402fcf910385f.SwitchGroupLearnedInfo): An instance of the SwitchGroupLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_1b0e7ca2c5c5bf68353402fcf910385f import (
            SwitchGroupLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchGroupLearnedInfo", None) is not None:
                return self._properties.get("SwitchGroupLearnedInfo")
        return SwitchGroupLearnedInfo(self)

    @property
    def SwitchMeterLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_912ee9c10af14a4526668258ad5851db.SwitchMeterLearnedInfo): An instance of the SwitchMeterLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_912ee9c10af14a4526668258ad5851db import (
            SwitchMeterLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchMeterLearnedInfo", None) is not None:
                return self._properties.get("SwitchMeterLearnedInfo")
        return SwitchMeterLearnedInfo(self)

    @property
    def SwitchTableFeaturesStatLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_1ae04328da2a331275401279fecdcbc9.SwitchTableFeaturesStatLearnedInfo): An instance of the SwitchTableFeaturesStatLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_1ae04328da2a331275401279fecdcbc9 import (
            SwitchTableFeaturesStatLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("SwitchTableFeaturesStatLearnedInfo", None)
                is not None
            ):
                return self._properties.get("SwitchTableFeaturesStatLearnedInfo")
        return SwitchTableFeaturesStatLearnedInfo(self)

    @property
    def EnableVendorExperimenterMessage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the vendor message trigger configuration parameters are available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVendorExperimenterMessage"])

    @EnableVendorExperimenterMessage.setter
    def EnableVendorExperimenterMessage(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVendorExperimenterMessage"], value)

    @property
    def EthernetDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for ethernet destination address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestination"])

    @EthernetDestination.setter
    def EthernetDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetDestination"], value)

    @property
    def EthernetSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for ethernet source address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSource"])

    @EthernetSource.setter
    def EthernetSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetSource"], value)

    @property
    def EthernetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the Ethernet type of the flow match.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @EthernetType.setter
    def EthernetType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetType"], value)

    @property
    def InPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for input port field
        """
        return self._get_attribute(self._SDM_ATT_MAP["InPort"])

    @InPort.setter
    def InPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InPort"], value)

    @property
    def IpDscp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for IP ToS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDscp"])

    @IpDscp.setter
    def IpDscp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpDscp"], value)

    @property
    def IpProtocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for IP Protocol field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpProtocol"])

    @IpProtocol.setter
    def IpProtocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpProtocol"], value)

    @property
    def Ipv4Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for IPv4 source address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Source"])

    @Ipv4Source.setter
    def Ipv4Source(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Source"], value)

    @property
    def Ipv4destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for IPv4 destination address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4destination"])

    @Ipv4destination.setter
    def Ipv4destination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4destination"], value)

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
    def IsOfFlowsLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Flow Learned Info for the OF Channels is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsOfFlowsLearnedInformationRefreshed"]
        )

    @property
    def OutPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the flow match value for output port field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutPort"])

    @OutPort.setter
    def OutPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutPort"], value)

    @property
    def OutPortInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom): This describes the output port type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutPortInputMode"])

    @OutPortInputMode.setter
    def OutPortInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutPortInputMode"], value)

    @property
    def TableId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the table identifier. It indicates the next table in the packet processing pipeline.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableId"])

    @TableId.setter
    def TableId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableId"], value)

    @property
    def TableIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allTables | emergency | tableIdCustom): This describes the type of table from which flow statistics will be sought.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableIdInputMode"])

    @TableIdInputMode.setter
    def TableIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableIdInputMode"], value)

    @property
    def TansportSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for transport source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TansportSource"])

    @TansportSource.setter
    def TansportSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TansportSource"], value)

    @property
    def TransportDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for transport destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransportDestination"])

    @TransportDestination.setter
    def TransportDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransportDestination"], value)

    @property
    def VendorExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the ID of the vendor for which vendor message is triggered.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorExperimenterId"])

    @VendorExperimenterId.setter
    def VendorExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorExperimenterId"], value)

    @property
    def VendorExperimenterType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the Type of experimenter only for v 1.3.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorExperimenterType"])

    @VendorExperimenterType.setter
    def VendorExperimenterType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorExperimenterType"], value)

    @property
    def VendorMessage(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the vendor data of the vendor message trigger.
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
        - number: This describes the length of vendor data of the vendor message trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorMessageLength"])

    @VendorMessageLength.setter
    def VendorMessageLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorMessageLength"], value)

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for VLAN ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the flow match value for VLAN Priority field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        EnableVendorExperimenterMessage=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        InPort=None,
        IpDscp=None,
        IpProtocol=None,
        Ipv4Source=None,
        Ipv4destination=None,
        OutPort=None,
        OutPortInputMode=None,
        TableId=None,
        TableIdInputMode=None,
        TansportSource=None,
        TransportDestination=None,
        VendorExperimenterId=None,
        VendorExperimenterType=None,
        VendorMessage=None,
        VendorMessageLength=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, str, str, str, str, str, str, str, str, int, str, int, str, str, str, int, int, str, int, str, str) -> SwitchLearnedInformation
        """Updates switchLearnedInformation resource on the server.

        Args
        ----
        - EnableVendorExperimenterMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - EthernetDestination (str): This describes the flow match value for ethernet destination address field.
        - EthernetSource (str): This describes the flow match value for ethernet source address field.
        - EthernetType (str): This describes the Ethernet type of the flow match.
        - InPort (str): This describes the flow match value for input port field
        - IpDscp (str): This describes the flow match value for IP ToS field.
        - IpProtocol (str): This describes the flow match value for IP Protocol field.
        - Ipv4Source (str): This describes the flow match value for IPv4 source address field.
        - Ipv4destination (str): This describes the flow match value for IPv4 destination address field.
        - OutPort (number): This describes the flow match value for output port field.
        - OutPortInputMode (str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom)): This describes the output port type.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | tableIdCustom)): This describes the type of table from which flow statistics will be sought.
        - TansportSource (str): This describes the flow match value for transport source field.
        - TransportDestination (str): This describes the flow match value for transport destination field.
        - VendorExperimenterId (number): This describes the ID of the vendor for which vendor message is triggered.
        - VendorExperimenterType (number): This describes the Type of experimenter only for v 1.3.
        - VendorMessage (str): This describes the vendor data of the vendor message trigger.
        - VendorMessageLength (number): This describes the length of vendor data of the vendor message trigger.
        - VlanId (str): This describes the flow match value for VLAN ID field.
        - VlanPriority (str): This describes the flow match value for VLAN Priority field.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableVendorExperimenterMessage=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        InPort=None,
        IpDscp=None,
        IpProtocol=None,
        Ipv4Source=None,
        Ipv4destination=None,
        IsOfChannelLearnedInformationRefreshed=None,
        IsOfFlowsLearnedInformationRefreshed=None,
        OutPort=None,
        OutPortInputMode=None,
        TableId=None,
        TableIdInputMode=None,
        TansportSource=None,
        TransportDestination=None,
        VendorExperimenterId=None,
        VendorExperimenterType=None,
        VendorMessage=None,
        VendorMessageLength=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, str, str, str, str, str, str, str, str, bool, bool, int, str, int, str, str, str, int, int, str, int, str, str) -> SwitchLearnedInformation
        """Finds and retrieves switchLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchLearnedInformation resources from the server.

        Args
        ----
        - EnableVendorExperimenterMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - EthernetDestination (str): This describes the flow match value for ethernet destination address field.
        - EthernetSource (str): This describes the flow match value for ethernet source address field.
        - EthernetType (str): This describes the Ethernet type of the flow match.
        - InPort (str): This describes the flow match value for input port field
        - IpDscp (str): This describes the flow match value for IP ToS field.
        - IpProtocol (str): This describes the flow match value for IP Protocol field.
        - Ipv4Source (str): This describes the flow match value for IPv4 source address field.
        - Ipv4destination (str): This describes the flow match value for IPv4 destination address field.
        - IsOfChannelLearnedInformationRefreshed (bool): If true, it denotes that the Learned Info for the OF Channels is received.
        - IsOfFlowsLearnedInformationRefreshed (bool): If true, it denotes that the Flow Learned Info for the OF Channels is received.
        - OutPort (number): This describes the flow match value for output port field.
        - OutPortInputMode (str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom)): This describes the output port type.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | tableIdCustom)): This describes the type of table from which flow statistics will be sought.
        - TansportSource (str): This describes the flow match value for transport source field.
        - TransportDestination (str): This describes the flow match value for transport destination field.
        - VendorExperimenterId (number): This describes the ID of the vendor for which vendor message is triggered.
        - VendorExperimenterType (number): This describes the Type of experimenter only for v 1.3.
        - VendorMessage (str): This describes the vendor data of the vendor message trigger.
        - VendorMessageLength (number): This describes the length of vendor data of the vendor message trigger.
        - VlanId (str): This describes the flow match value for VLAN ID field.
        - VlanPriority (str): This describes the flow match value for VLAN Priority field.

        Returns
        -------
        - self: This instance with matching switchLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearRecordsForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the clearRecordsForTrigger operation on the server.

        API to clear records for any trigger.

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

    def RefreshFlows(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshFlows operation on the server.

        This describes that the flows learned information is refreshed.

        refreshFlows(async_operation=bool)bool
        --------------------------------------
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
        return self._execute("refreshFlows", payload=payload, response_object=None)

    def RefreshGroupLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshGroupLearnedInformation operation on the server.

        NOT DEFINED

        refreshGroupLearnedInformation(async_operation=bool)bool
        --------------------------------------------------------
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
            "refreshGroupLearnedInformation", payload=payload, response_object=None
        )

    def RefreshMeterLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshMeterLearnedInformation operation on the server.

        NOT DEFINED

        refreshMeterLearnedInformation(async_operation=bool)bool
        --------------------------------------------------------
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
            "refreshMeterLearnedInformation", payload=payload, response_object=None
        )

    def RefreshOfChannelLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshOfChannelLearnedInformation operation on the server.

        This describes that the ofChannellearned information is refreshed.

        refreshOfChannelLearnedInformation(async_operation=bool)bool
        ------------------------------------------------------------
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
            "refreshOfChannelLearnedInformation", payload=payload, response_object=None
        )

    def RefreshTableFeature(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshTableFeature operation on the server.

        NOT DEFINED

        refreshTableFeature(async_operation=bool)bool
        ---------------------------------------------
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
            "refreshTableFeature", payload=payload, response_object=None
        )

    def Trigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the trigger operation on the server.

        API to send Trigger.

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

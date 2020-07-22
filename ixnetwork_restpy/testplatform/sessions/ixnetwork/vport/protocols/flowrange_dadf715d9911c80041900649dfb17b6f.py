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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FlowRange(Base):
    """This object allows you to define the number of Flow Ranges for this Interface.
    The FlowRange class encapsulates a list of flowRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the FlowRange.find() method.
    The list can be managed by using the FlowRange.add() and FlowRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'flowRange'
    _SDM_ATT_MAP = {
        'CheckOverlap': 'checkOverlap',
        'Description': 'description',
        'DontAddOnChannelUp': 'dontAddOnChannelUp',
        'EmergencyFlow': 'emergencyFlow',
        'Enabled': 'enabled',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'EthernetType': 'ethernetType',
        'FlowModStatus': 'flowModStatus',
        'HardTimeout': 'hardTimeout',
        'IdleTimeout': 'idleTimeout',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpProtocol': 'ipProtocol',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
        'MatchType': 'matchType',
        'Priority': 'priority',
        'SendFlowRemoved': 'sendFlowRemoved',
        'TotalFlowCount': 'totalFlowCount',
        'TransportDestinationIcmpCode': 'transportDestinationIcmpCode',
        'TransportSourceIcmpType': 'transportSourceIcmpType',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(FlowRange, self).__init__(parent)

    @property
    def FlowRangeAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowrangeaction_79d179d105734bb8378d7e2614b0c17e.FlowRangeAction): An instance of the FlowRangeAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowrangeaction_79d179d105734bb8378d7e2614b0c17e import FlowRangeAction
        return FlowRangeAction(self)

    @property
    def CheckOverlap(self):
        """
        Returns
        -------
        - bool: If true, Ixia enables the Check Overlap flag while sending OpenFlow flow modification messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CheckOverlap'])
    @CheckOverlap.setter
    def CheckOverlap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CheckOverlap'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A name that describes the Flow Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def DontAddOnChannelUp(self):
        """
        Returns
        -------
        - bool: If true, no flow add or delete packet is sent out when OpenFlow channel comes up or when flow entry is enabled/disabled in the IxNetwork GUI. This facility is useful to send flow add,delete, and modify for ad-hoc flows through Test Composer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DontAddOnChannelUp'])
    @DontAddOnChannelUp.setter
    def DontAddOnChannelUp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DontAddOnChannelUp'], value)

    @property
    def EmergencyFlow(self):
        """
        Returns
        -------
        - bool: If true, Ixia enables the Emergency flag while sending OpenFlow flow modification messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EmergencyFlow'])
    @EmergencyFlow.setter
    def EmergencyFlow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EmergencyFlow'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the flow Range object in the protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: Indicates the Ethernet destination address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestination'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: Indicates the Ethernet source address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: Indicates the type of Ethernet to be used. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetType'], value)

    @property
    def FlowModStatus(self):
        """
        Returns
        -------
        - str: Reflects the status of the selected flow range which is modified at runtime.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowModStatus'])

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - number: Indicates the inactive time in seconds after which the Flow range will hard timeout and close.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardTimeout'])
    @HardTimeout.setter
    def HardTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HardTimeout'], value)

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - number: Indicates the inactive time in seconds after which the Flow range will timeout and become idle.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IdleTimeout'])
    @IdleTimeout.setter
    def IdleTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IdleTimeout'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: Indicates the In port value for flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])
    @InPort.setter
    def InPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPort'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: Specifies the IP DSCP value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: Specifies the IP Protocol to be used for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: Indicates the IPv4 destination address mask value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Destination'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: Indicates the IPv4 source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def MatchType(self):
        """
        Returns
        -------
        - str(strict | loose): Indicates the type of match to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchType'])
    @MatchType.setter
    def MatchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchType'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: Indicates the priority level for the Flow Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def SendFlowRemoved(self):
        """
        Returns
        -------
        - bool: If true, Ixia enables the Send Flow Removed flag while sending OpenFlow flow modification messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendFlowRemoved'])
    @SendFlowRemoved.setter
    def SendFlowRemoved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendFlowRemoved'], value)

    @property
    def TotalFlowCount(self):
        """
        Returns
        -------
        - number: Specifies the number of flows.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalFlowCount'])
    @TotalFlowCount.setter
    def TotalFlowCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TotalFlowCount'], value)

    @property
    def TransportDestinationIcmpCode(self):
        """
        Returns
        -------
        - str: Specifies the Transport destination address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestinationIcmpCode'])
    @TransportDestinationIcmpCode.setter
    def TransportDestinationIcmpCode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportDestinationIcmpCode'], value)

    @property
    def TransportSourceIcmpType(self):
        """
        Returns
        -------
        - str: Specifies the Transport Source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportSourceIcmpType'])
    @TransportSourceIcmpType.setter
    def TransportSourceIcmpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportSourceIcmpType'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: Indicates the VLAN identifier value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: Indicates the VLAN priority value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, CheckOverlap=None, Description=None, DontAddOnChannelUp=None, EmergencyFlow=None, Enabled=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, HardTimeout=None, IdleTimeout=None, InPort=None, IpDscp=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, MatchType=None, Priority=None, SendFlowRemoved=None, TotalFlowCount=None, TransportDestinationIcmpCode=None, TransportSourceIcmpType=None, VlanId=None, VlanPriority=None):
        """Updates flowRange resource on the server.

        Args
        ----
        - CheckOverlap (bool): If true, Ixia enables the Check Overlap flag while sending OpenFlow flow modification messages.
        - Description (str): A name that describes the Flow Range.
        - DontAddOnChannelUp (bool): If true, no flow add or delete packet is sent out when OpenFlow channel comes up or when flow entry is enabled/disabled in the IxNetwork GUI. This facility is useful to send flow add,delete, and modify for ad-hoc flows through Test Composer.
        - EmergencyFlow (bool): If true, Ixia enables the Emergency flag while sending OpenFlow flow modification messages.
        - Enabled (bool): If true, enables the flow Range object in the protocol.
        - EthernetDestination (str): Indicates the Ethernet destination address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EthernetSource (str): Indicates the Ethernet source address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EthernetType (str): Indicates the type of Ethernet to be used. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - HardTimeout (number): Indicates the inactive time in seconds after which the Flow range will hard timeout and close.
        - IdleTimeout (number): Indicates the inactive time in seconds after which the Flow range will timeout and become idle.
        - InPort (str): Indicates the In port value for flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpDscp (str): Specifies the IP DSCP value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpProtocol (str): Specifies the IP Protocol to be used for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Destination (str): Indicates the IPv4 destination address mask value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Source (str): Indicates the IPv4 source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MatchType (str(strict | loose)): Indicates the type of match to be configured.
        - Priority (number): Indicates the priority level for the Flow Range.
        - SendFlowRemoved (bool): If true, Ixia enables the Send Flow Removed flag while sending OpenFlow flow modification messages.
        - TotalFlowCount (number): Specifies the number of flows.
        - TransportDestinationIcmpCode (str): Specifies the Transport destination address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - TransportSourceIcmpType (str): Specifies the Transport Source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanId (str): Indicates the VLAN identifier value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Indicates the VLAN priority value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CheckOverlap=None, Description=None, DontAddOnChannelUp=None, EmergencyFlow=None, Enabled=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, HardTimeout=None, IdleTimeout=None, InPort=None, IpDscp=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, MatchType=None, Priority=None, SendFlowRemoved=None, TotalFlowCount=None, TransportDestinationIcmpCode=None, TransportSourceIcmpType=None, VlanId=None, VlanPriority=None):
        """Adds a new flowRange resource on the server and adds it to the container.

        Args
        ----
        - CheckOverlap (bool): If true, Ixia enables the Check Overlap flag while sending OpenFlow flow modification messages.
        - Description (str): A name that describes the Flow Range.
        - DontAddOnChannelUp (bool): If true, no flow add or delete packet is sent out when OpenFlow channel comes up or when flow entry is enabled/disabled in the IxNetwork GUI. This facility is useful to send flow add,delete, and modify for ad-hoc flows through Test Composer.
        - EmergencyFlow (bool): If true, Ixia enables the Emergency flag while sending OpenFlow flow modification messages.
        - Enabled (bool): If true, enables the flow Range object in the protocol.
        - EthernetDestination (str): Indicates the Ethernet destination address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EthernetSource (str): Indicates the Ethernet source address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EthernetType (str): Indicates the type of Ethernet to be used. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - HardTimeout (number): Indicates the inactive time in seconds after which the Flow range will hard timeout and close.
        - IdleTimeout (number): Indicates the inactive time in seconds after which the Flow range will timeout and become idle.
        - InPort (str): Indicates the In port value for flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpDscp (str): Specifies the IP DSCP value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpProtocol (str): Specifies the IP Protocol to be used for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Destination (str): Indicates the IPv4 destination address mask value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Source (str): Indicates the IPv4 source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MatchType (str(strict | loose)): Indicates the type of match to be configured.
        - Priority (number): Indicates the priority level for the Flow Range.
        - SendFlowRemoved (bool): If true, Ixia enables the Send Flow Removed flag while sending OpenFlow flow modification messages.
        - TotalFlowCount (number): Specifies the number of flows.
        - TransportDestinationIcmpCode (str): Specifies the Transport destination address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - TransportSourceIcmpType (str): Specifies the Transport Source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanId (str): Indicates the VLAN identifier value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Indicates the VLAN priority value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Returns
        -------
        - self: This instance with all currently retrieved flowRange resources using find and the newly added flowRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained flowRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CheckOverlap=None, Description=None, DontAddOnChannelUp=None, EmergencyFlow=None, Enabled=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, FlowModStatus=None, HardTimeout=None, IdleTimeout=None, InPort=None, IpDscp=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, MatchType=None, Priority=None, SendFlowRemoved=None, TotalFlowCount=None, TransportDestinationIcmpCode=None, TransportSourceIcmpType=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves flowRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowRange resources from the server.

        Args
        ----
        - CheckOverlap (bool): If true, Ixia enables the Check Overlap flag while sending OpenFlow flow modification messages.
        - Description (str): A name that describes the Flow Range.
        - DontAddOnChannelUp (bool): If true, no flow add or delete packet is sent out when OpenFlow channel comes up or when flow entry is enabled/disabled in the IxNetwork GUI. This facility is useful to send flow add,delete, and modify for ad-hoc flows through Test Composer.
        - EmergencyFlow (bool): If true, Ixia enables the Emergency flag while sending OpenFlow flow modification messages.
        - Enabled (bool): If true, enables the flow Range object in the protocol.
        - EthernetDestination (str): Indicates the Ethernet destination address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EthernetSource (str): Indicates the Ethernet source address for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EthernetType (str): Indicates the type of Ethernet to be used. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - FlowModStatus (str): Reflects the status of the selected flow range which is modified at runtime.
        - HardTimeout (number): Indicates the inactive time in seconds after which the Flow range will hard timeout and close.
        - IdleTimeout (number): Indicates the inactive time in seconds after which the Flow range will timeout and become idle.
        - InPort (str): Indicates the In port value for flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpDscp (str): Specifies the IP DSCP value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpProtocol (str): Specifies the IP Protocol to be used for the flow range. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Destination (str): Indicates the IPv4 destination address mask value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Source (str): Indicates the IPv4 source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MatchType (str(strict | loose)): Indicates the type of match to be configured.
        - Priority (number): Indicates the priority level for the Flow Range.
        - SendFlowRemoved (bool): If true, Ixia enables the Send Flow Removed flag while sending OpenFlow flow modification messages.
        - TotalFlowCount (number): Specifies the number of flows.
        - TransportDestinationIcmpCode (str): Specifies the Transport destination address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - TransportSourceIcmpType (str): Specifies the Transport Source address. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanId (str): Indicates the VLAN identifier value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Indicates the VLAN priority value. This attribute is of string type and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Returns
        -------
        - self: This instance with matching flowRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flowRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateFlowMod(self, *args, **kwargs):
        """Executes the updateFlowMod operation on the server.

        NOT DEFINED

        updateFlowMod(Arg2=enum)bool
        ----------------------------
        - Arg2 (str(sendFlowAdd | sendFlowModify | sendFlowRemove)): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('updateFlowMod', payload=payload, response_object=None)

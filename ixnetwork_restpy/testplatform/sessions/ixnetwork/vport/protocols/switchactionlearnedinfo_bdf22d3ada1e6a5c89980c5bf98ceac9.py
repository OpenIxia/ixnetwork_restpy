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


class SwitchActionLearnedInfo(Base):
    """This object allows to configure the switch action parameters.
    The SwitchActionLearnedInfo class encapsulates a list of switchActionLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchActionLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchActionLearnedInfo'
    _SDM_ATT_MAP = {
        'ActionType': 'actionType',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'IpDscp': 'ipDscp',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
        'MaxByteLength': 'maxByteLength',
        'OutputPort': 'outputPort',
        'QueueId': 'queueId',
        'TransportDestination': 'transportDestination',
        'TransportSource': 'transportSource',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(SwitchActionLearnedInfo, self).__init__(parent)

    @property
    def ActionType(self):
        """
        Returns
        -------
        - str: This describes the action associated with the flow entry
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionType'])

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: This describes Ethernet destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: This describes Ethernet source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: This describes the IP DSCP value for advertising.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: This describes the IPv4 destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: This describes the IPv4 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])

    @property
    def MaxByteLength(self):
        """
        Returns
        -------
        - number: This describes the maximum amount of data from a packet that should be sent when the port is OFPP_CONTROLLER.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxByteLength'])

    @property
    def OutputPort(self):
        """
        Returns
        -------
        - number: This describes the output port through which the packet should be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPort'])

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: This describes the queue of the port in which the packet should be enqueued.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])

    @property
    def TransportDestination(self):
        """
        Returns
        -------
        - number: This describes the transport destination address
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestination'])

    @property
    def TransportSource(self):
        """
        Returns
        -------
        - number: This describes the transport source address
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportSource'])

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: This describes the Value of the VLAN ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: This describes the VLAN priority
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])

    def find(self, ActionType=None, EthernetDestination=None, EthernetSource=None, IpDscp=None, Ipv4Destination=None, Ipv4Source=None, MaxByteLength=None, OutputPort=None, QueueId=None, TransportDestination=None, TransportSource=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves switchActionLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchActionLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchActionLearnedInfo resources from the server.

        Args
        ----
        - ActionType (str): This describes the action associated with the flow entry
        - EthernetDestination (str): This describes Ethernet destination address.
        - EthernetSource (str): This describes Ethernet source address.
        - IpDscp (str): This describes the IP DSCP value for advertising.
        - Ipv4Destination (str): This describes the IPv4 destination address.
        - Ipv4Source (str): This describes the IPv4 source address.
        - MaxByteLength (number): This describes the maximum amount of data from a packet that should be sent when the port is OFPP_CONTROLLER.
        - OutputPort (number): This describes the output port through which the packet should be sent.
        - QueueId (number): This describes the queue of the port in which the packet should be enqueued.
        - TransportDestination (number): This describes the transport destination address
        - TransportSource (number): This describes the transport source address
        - VlanId (number): This describes the Value of the VLAN ID field.
        - VlanPriority (number): This describes the VLAN priority

        Returns
        -------
        - self: This instance with matching switchActionLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchActionLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchActionLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class SupportedActions(Base):
    """This object allows to define the Bitmap of supported actions.
    The SupportedActions class encapsulates a required supportedActions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'supportedActions'
    _SDM_ATT_MAP = {
        'Enqueue': 'enqueue',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'IpDscp': 'ipDscp',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
        'Output': 'output',
        'StripVlanHeader': 'stripVlanHeader',
        'TransportDestination': 'transportDestination',
        'TransportSource': 'transportSource',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(SupportedActions, self).__init__(parent)

    @property
    def Enqueue(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes Output to queue.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enqueue'])
    @Enqueue.setter
    def Enqueue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enqueue'], value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes setting Ethernet destination address.
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
        - bool: Indicates that the supported action of the switch includes setting Ethernet source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes setting IP ToS, DSCP field, 6 bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes setting IP destination address.
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
        - bool: Indicates that the supported action of the switch includes setting IP source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def Output(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes Output to switch port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Output'])
    @Output.setter
    def Output(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Output'], value)

    @property
    def StripVlanHeader(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes stripping the 802.1q header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StripVlanHeader'])
    @StripVlanHeader.setter
    def StripVlanHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StripVlanHeader'], value)

    @property
    def TransportDestination(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes setting TCP/UDP destination port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestination'])
    @TransportDestination.setter
    def TransportDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportDestination'], value)

    @property
    def TransportSource(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes setting TCP/UDP source port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportSource'])
    @TransportSource.setter
    def TransportSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportSource'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - bool: Indicates that the supported action of the switch includes setting the 802.1q VLAN id.
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
        - bool: Indicates that the supported action of the switch includes setting the 802.1q priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, Enqueue=None, EthernetDestination=None, EthernetSource=None, IpDscp=None, Ipv4Destination=None, Ipv4Source=None, Output=None, StripVlanHeader=None, TransportDestination=None, TransportSource=None, VlanId=None, VlanPriority=None):
        """Updates supportedActions resource on the server.

        Args
        ----
        - Enqueue (bool): Indicates that the supported action of the switch includes Output to queue.
        - EthernetDestination (bool): Indicates that the supported action of the switch includes setting Ethernet destination address.
        - EthernetSource (bool): Indicates that the supported action of the switch includes setting Ethernet source address.
        - IpDscp (bool): Indicates that the supported action of the switch includes setting IP ToS, DSCP field, 6 bits.
        - Ipv4Destination (bool): Indicates that the supported action of the switch includes setting IP destination address.
        - Ipv4Source (bool): Indicates that the supported action of the switch includes setting IP source address.
        - Output (bool): Indicates that the supported action of the switch includes Output to switch port.
        - StripVlanHeader (bool): Indicates that the supported action of the switch includes stripping the 802.1q header.
        - TransportDestination (bool): Indicates that the supported action of the switch includes setting TCP/UDP destination port.
        - TransportSource (bool): Indicates that the supported action of the switch includes setting TCP/UDP source port.
        - VlanId (bool): Indicates that the supported action of the switch includes setting the 802.1q VLAN id.
        - VlanPriority (bool): Indicates that the supported action of the switch includes setting the 802.1q priority.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

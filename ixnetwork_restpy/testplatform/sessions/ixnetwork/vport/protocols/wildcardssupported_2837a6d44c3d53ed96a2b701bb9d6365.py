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


class WildcardsSupported(Base):
    """Indicates the Bitmap of OFPFW_* wildcards that are supported by the table.
    The WildcardsSupported class encapsulates a required wildcardsSupported resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "wildcardsSupported"
    _SDM_ATT_MAP = {
        "EthernetDestinationAddress": "ethernetDestinationAddress",
        "EthernetFrameType": "ethernetFrameType",
        "EthernetSourceAddress": "ethernetSourceAddress",
        "IpDestinationAddress": "ipDestinationAddress",
        "IpProtocol": "ipProtocol",
        "IpSourceAddress": "ipSourceAddress",
        "IpTos": "ipTos",
        "SwitchInputPort": "switchInputPort",
        "TcpUdpDestinationPort": "tcpUdpDestinationPort",
        "TcpUdpSourcePort": "tcpUdpSourcePort",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(WildcardsSupported, self).__init__(parent, list_op)

    @property
    def EthernetDestinationAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the Ethernet destination address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestinationAddress"])

    @EthernetDestinationAddress.setter
    def EthernetDestinationAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetDestinationAddress"], value)

    @property
    def EthernetFrameType(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the Ethernet frame type is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetFrameType"])

    @EthernetFrameType.setter
    def EthernetFrameType(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetFrameType"], value)

    @property
    def EthernetSourceAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the Ethernet source address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSourceAddress"])

    @EthernetSourceAddress.setter
    def EthernetSourceAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetSourceAddress"], value)

    @property
    def IpDestinationAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the IP destination address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDestinationAddress"])

    @IpDestinationAddress.setter
    def IpDestinationAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpDestinationAddress"], value)

    @property
    def IpProtocol(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the IP protocol is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpProtocol"])

    @IpProtocol.setter
    def IpProtocol(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpProtocol"], value)

    @property
    def IpSourceAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the IP source address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpSourceAddress"])

    @IpSourceAddress.setter
    def IpSourceAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpSourceAddress"], value)

    @property
    def IpTos(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the IP ToS (DSCP field, 6 bits) is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpTos"])

    @IpTos.setter
    def IpTos(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpTos"], value)

    @property
    def SwitchInputPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the Switch input port is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchInputPort"])

    @SwitchInputPort.setter
    def SwitchInputPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchInputPort"], value)

    @property
    def TcpUdpDestinationPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the TCP/UDP destination port is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpUdpDestinationPort"])

    @TcpUdpDestinationPort.setter
    def TcpUdpDestinationPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpUdpDestinationPort"], value)

    @property
    def TcpUdpSourcePort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the TCP/UDP source port is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpUdpSourcePort"])

    @TcpUdpSourcePort.setter
    def TcpUdpSourcePort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpUdpSourcePort"], value)

    @property
    def VlanId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the VLAN id is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the VLAN priority is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        EthernetDestinationAddress=None,
        EthernetFrameType=None,
        EthernetSourceAddress=None,
        IpDestinationAddress=None,
        IpProtocol=None,
        IpSourceAddress=None,
        IpTos=None,
        SwitchInputPort=None,
        TcpUdpDestinationPort=None,
        TcpUdpSourcePort=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> WildcardsSupported
        """Updates wildcardsSupported resource on the server.

        Args
        ----
        - EthernetDestinationAddress (bool): Indicates that the Ethernet destination address is supported.
        - EthernetFrameType (bool): Indicates that the Ethernet frame type is supported.
        - EthernetSourceAddress (bool): Indicates that the Ethernet source address is supported.
        - IpDestinationAddress (bool): Indicates that the IP destination address is supported.
        - IpProtocol (bool): Indicates that the IP protocol is supported.
        - IpSourceAddress (bool): Indicates that the IP source address is supported.
        - IpTos (bool): Indicates that the IP ToS (DSCP field, 6 bits) is supported.
        - SwitchInputPort (bool): Indicates that the Switch input port is supported.
        - TcpUdpDestinationPort (bool): Indicates that the TCP/UDP destination port is supported.
        - TcpUdpSourcePort (bool): Indicates that the TCP/UDP source port is supported.
        - VlanId (bool): Indicates that the VLAN id is supported.
        - VlanPriority (bool): Indicates that the VLAN priority is supported.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EthernetDestinationAddress=None,
        EthernetFrameType=None,
        EthernetSourceAddress=None,
        IpDestinationAddress=None,
        IpProtocol=None,
        IpSourceAddress=None,
        IpTos=None,
        SwitchInputPort=None,
        TcpUdpDestinationPort=None,
        TcpUdpSourcePort=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> WildcardsSupported
        """Finds and retrieves wildcardsSupported resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve wildcardsSupported resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all wildcardsSupported resources from the server.

        Args
        ----
        - EthernetDestinationAddress (bool): Indicates that the Ethernet destination address is supported.
        - EthernetFrameType (bool): Indicates that the Ethernet frame type is supported.
        - EthernetSourceAddress (bool): Indicates that the Ethernet source address is supported.
        - IpDestinationAddress (bool): Indicates that the IP destination address is supported.
        - IpProtocol (bool): Indicates that the IP protocol is supported.
        - IpSourceAddress (bool): Indicates that the IP source address is supported.
        - IpTos (bool): Indicates that the IP ToS (DSCP field, 6 bits) is supported.
        - SwitchInputPort (bool): Indicates that the Switch input port is supported.
        - TcpUdpDestinationPort (bool): Indicates that the TCP/UDP destination port is supported.
        - TcpUdpSourcePort (bool): Indicates that the TCP/UDP source port is supported.
        - VlanId (bool): Indicates that the VLAN id is supported.
        - VlanPriority (bool): Indicates that the VLAN priority is supported.

        Returns
        -------
        - self: This instance with matching wildcardsSupported resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of wildcardsSupported data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the wildcardsSupported resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

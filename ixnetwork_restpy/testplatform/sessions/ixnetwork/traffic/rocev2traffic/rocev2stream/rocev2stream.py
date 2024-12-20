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


class RoceV2Stream(Base):
    """A Flow Group that is generated from the RoCEv2 Traffic Item. Each RoCEv2 Traffic Item generates one or more Flow Groups, which in turn map to hardware streams on the port.  Each Flow Group/roceV2Stream picks up its Rate, Frame size properties/attributes from its corresponding RoCEv2 configuration under the Traffic Item.
    The RoceV2Stream class encapsulates a list of roceV2Stream resources that are managed by the system.
    A list of resources can be retrieved from the server using the RoceV2Stream.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "roceV2Stream"
    _SDM_ATT_MAP = {
        "BurstCount": "burstCount",
        "DestIp": "destIp",
        "DestIpv4": "destIpv4",
        "DestMac": "destMac",
        "DestQP": "destQP",
        "Enabled": "enabled",
        "FrameSizeInBytes": "frameSizeInBytes",
        "IpDscp": "ipDscp",
        "Name": "name",
        "Packets": "packets",
        "RxPort": "rxPort",
        "SourceIp": "sourceIp",
        "SourceIpv4": "sourceIpv4",
        "SourceMac": "sourceMac",
        "SourceQP": "sourceQP",
        "TxPort": "txPort",
        "Type": "type",
        "UdpSource": "udpSource",
    }
    _SDM_ENUM_MAP = {
        "type": ["continuous", "fixed"],
    }

    def __init__(self, parent, list_op=False):
        super(RoceV2Stream, self).__init__(parent, list_op)

    @property
    def BurstCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Burst Count when Tx Mode is Fixed mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstCount"])

    @BurstCount.setter
    def BurstCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstCount"], value)

    @property
    def DestIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Destination IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestIp"])

    @property
    def DestIpv4(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Destination IPv4
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestIpv4"])

    @property
    def DestMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Destination MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestMac"])

    @property
    def DestQP(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Destination QP
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestQP"])

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FrameSizeInBytes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The FrameSize Details for this Flowgroup
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeInBytes"])

    @property
    def IpDscp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: IP DSCP
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDscp"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: An alphanumeric string that returns the name of the flow group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def Packets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The RDMA Packets in this Flowgroup
        """
        return self._get_attribute(self._SDM_ATT_MAP["Packets"])

    @property
    def RxPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Receiving Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPort"])

    @property
    def SourceIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Source IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceIp"])

    @property
    def SourceIpv4(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Source IPv4
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceIpv4"])

    @property
    def SourceMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Source MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceMac"])

    @property
    def SourceQP(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Source QP
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceQP"])

    @property
    def TxPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Transmitting Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxPort"])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(continuous | fixed): The Transmission Control types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    @property
    def UdpSource(self):
        # type: () -> int
        """
        Returns
        -------
        - number: UDP Source Port
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSource"])

    def update(self, BurstCount=None, Enabled=None, Name=None, Type=None):
        # type: (int, bool, str, str) -> RoceV2Stream
        """Updates roceV2Stream resource on the server.

        Args
        ----
        - BurstCount (number): Burst Count when Tx Mode is Fixed mode.
        - Enabled (bool):
        - Name (str): An alphanumeric string that returns the name of the flow group.
        - Type (str(continuous | fixed)): The Transmission Control types.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BurstCount=None, Enabled=None, Name=None, Type=None):
        # type: (int, bool, str, str) -> RoceV2Stream
        """Adds a new roceV2Stream resource on the json, only valid with batch add utility

        Args
        ----
        - BurstCount (number): Burst Count when Tx Mode is Fixed mode.
        - Enabled (bool):
        - Name (str): An alphanumeric string that returns the name of the flow group.
        - Type (str(continuous | fixed)): The Transmission Control types.

        Returns
        -------
        - self: This instance with all currently retrieved roceV2Stream resources using find and the newly added roceV2Stream resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BurstCount=None,
        DestIp=None,
        DestIpv4=None,
        DestMac=None,
        DestQP=None,
        Enabled=None,
        FrameSizeInBytes=None,
        IpDscp=None,
        Name=None,
        Packets=None,
        RxPort=None,
        SourceIp=None,
        SourceIpv4=None,
        SourceMac=None,
        SourceQP=None,
        TxPort=None,
        Type=None,
        UdpSource=None,
    ):
        # type: (int, str, str, str, int, bool, str, int, str, str, str, str, str, str, int, str, str, int) -> RoceV2Stream
        """Finds and retrieves roceV2Stream resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve roceV2Stream resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all roceV2Stream resources from the server.

        Args
        ----
        - BurstCount (number): Burst Count when Tx Mode is Fixed mode.
        - DestIp (str): Destination IP
        - DestIpv4 (str): Destination IPv4
        - DestMac (str): Destination MAC
        - DestQP (number): Destination QP
        - Enabled (bool):
        - FrameSizeInBytes (str): The FrameSize Details for this Flowgroup
        - IpDscp (number): IP DSCP
        - Name (str): An alphanumeric string that returns the name of the flow group.
        - Packets (str): The RDMA Packets in this Flowgroup
        - RxPort (str): The Receiving Port Name
        - SourceIp (str): Source IP
        - SourceIpv4 (str): Source IPv4
        - SourceMac (str): Source MAC
        - SourceQP (number): Source QP
        - TxPort (str): The Transmitting Port Name
        - Type (str(continuous | fixed)): The Transmission Control types.
        - UdpSource (number): UDP Source Port

        Returns
        -------
        - self: This instance with matching roceV2Stream resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of roceV2Stream data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the roceV2Stream resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

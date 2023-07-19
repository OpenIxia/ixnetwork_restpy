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


class Dhcpv4client(Base):
    """IPv4 global and per-port settings
    The Dhcpv4client class encapsulates a required dhcpv4client resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dhcpv4client"
    _SDM_ATT_MAP = {
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Dhcp4ArpGw": "dhcp4ArpGw",
        "Dhcp4ClientPort": "dhcp4ClientPort",
        "Dhcp4MaxDiscoverTimeout": "dhcp4MaxDiscoverTimeout",
        "Dhcp4NumRetry": "dhcp4NumRetry",
        "Dhcp4ResponseTimeout": "dhcp4ResponseTimeout",
        "Dhcp4ResponseTimeoutFactor": "dhcp4ResponseTimeoutFactor",
        "Dhcp4ServerPort": "dhcp4ServerPort",
        "Name": "name",
        "RenewOnLinkUp": "renewOnLinkUp",
        "RowNames": "rowNames",
        "SkipReleaseOnStop": "skipReleaseOnStop",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Dhcpv4client, self).__init__(parent, list_op)

    @property
    def SessionLifetime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.sessionlifetime.sessionlifetime_c56c3cca82dcd438a26eb5e7980bb00a.SessionLifetime): An instance of the SessionLifetime class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.sessionlifetime.sessionlifetime_c56c3cca82dcd438a26eb5e7980bb00a import (
            SessionLifetime,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SessionLifetime", None) is not None:
                return self._properties.get("SessionLifetime")
        return SessionLifetime(self)._select()

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.startrate.startrate_1bba90e9b5242a924a45ce8454358006.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.startrate.startrate_1bba90e9b5242a924a45ce8454358006 import (
            StartRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StartRate", None) is not None:
                return self._properties.get("StartRate")
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.stoprate.stoprate_e57c921a314c7c4a39ab432f5e2970a0.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.stoprate.stoprate_e57c921a314c7c4a39ab432f5e2970a0 import (
            StopRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StopRate", None) is not None:
                return self._properties.get("StopRate")
        return StopRate(self)._select()

    @property
    def TlvEditor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor_9737bec75dbac826009c3374be76c5f7.TlvEditor): An instance of the TlvEditor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor_9737bec75dbac826009c3374be76c5f7 import (
            TlvEditor,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TlvEditor", None) is not None:
                return self._properties.get("TlvEditor")
        return TlvEditor(self)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def Dhcp4ArpGw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, DHCP clients ARP to find their Gateway MAC Addresses.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4ArpGw"]))

    @property
    def Dhcp4ClientPort(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP port that the client listens on for DHCP and BOOTP responses.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4ClientPort"])
        )

    @property
    def Dhcp4MaxDiscoverTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The max value, in seconds, that the discover timeout can reach though Discover Timeout Factor.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4MaxDiscoverTimeout"])
        )

    @property
    def Dhcp4NumRetry(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of times that the client will retransmit a request for which it has not received a response. When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4NumRetry"]))

    @property
    def Dhcp4ResponseTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4ResponseTimeout"])
        )

    @property
    def Dhcp4ResponseTimeoutFactor(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The factor by which the timeout will be multiplied each time the response timeout has been reached.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4ResponseTimeoutFactor"])
        )

    @property
    def Dhcp4ServerPort(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP port that the client addresses server requests to.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Dhcp4ServerPort"])
        )

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def RenewOnLinkUp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicate to renew the active DHCP sessions after link status goes down and up.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RenewOnLinkUp"]))

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowNames"])

    @property
    def SkipReleaseOnStop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SkipReleaseOnStop"])
        )

    def update(self, Name=None):
        # type: (str) -> Dhcpv4client
        """Updates dhcpv4client resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
        # type: (int, str, str, List[str]) -> Dhcpv4client
        """Finds and retrieves dhcpv4client resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv4client resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv4client resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching dhcpv4client resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv4client data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv4client resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self,
        PortNames=None,
        Dhcp4ArpGw=None,
        Dhcp4ClientPort=None,
        Dhcp4MaxDiscoverTimeout=None,
        Dhcp4NumRetry=None,
        Dhcp4ResponseTimeout=None,
        Dhcp4ResponseTimeoutFactor=None,
        Dhcp4ServerPort=None,
        RenewOnLinkUp=None,
        SkipReleaseOnStop=None,
    ):
        """Base class infrastructure that gets a list of dhcpv4client device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Dhcp4ArpGw (str): optional regex of dhcp4ArpGw
        - Dhcp4ClientPort (str): optional regex of dhcp4ClientPort
        - Dhcp4MaxDiscoverTimeout (str): optional regex of dhcp4MaxDiscoverTimeout
        - Dhcp4NumRetry (str): optional regex of dhcp4NumRetry
        - Dhcp4ResponseTimeout (str): optional regex of dhcp4ResponseTimeout
        - Dhcp4ResponseTimeoutFactor (str): optional regex of dhcp4ResponseTimeoutFactor
        - Dhcp4ServerPort (str): optional regex of dhcp4ServerPort
        - RenewOnLinkUp (str): optional regex of renewOnLinkUp
        - SkipReleaseOnStop (str): optional regex of skipReleaseOnStop

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

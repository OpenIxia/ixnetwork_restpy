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


class Dhcpv6client(Base):
    """IPv6 global and per-port settings
    The Dhcpv6client class encapsulates a required dhcpv6client resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6client'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Dhcp6EchoIAInfo': 'dhcp6EchoIAInfo',
        'Dhcp6InfoReqMaxRc': 'dhcp6InfoReqMaxRc',
        'Dhcp6InfoReqMaxRt': 'dhcp6InfoReqMaxRt',
        'Dhcp6InfoReqTimeout': 'dhcp6InfoReqTimeout',
        'Dhcp6NsGw': 'dhcp6NsGw',
        'Dhcp6RebMaxRt': 'dhcp6RebMaxRt',
        'Dhcp6RebTimeout': 'dhcp6RebTimeout',
        'Dhcp6RelMaxRc': 'dhcp6RelMaxRc',
        'Dhcp6RelTimeout': 'dhcp6RelTimeout',
        'Dhcp6RenMaxRt': 'dhcp6RenMaxRt',
        'Dhcp6RenTimeout': 'dhcp6RenTimeout',
        'Dhcp6ReqMaxRc': 'dhcp6ReqMaxRc',
        'Dhcp6ReqMaxRt': 'dhcp6ReqMaxRt',
        'Dhcp6ReqTimeout': 'dhcp6ReqTimeout',
        'Dhcp6SolMaxRc': 'dhcp6SolMaxRc',
        'Dhcp6SolMaxRt': 'dhcp6SolMaxRt',
        'Dhcp6SolTimeout': 'dhcp6SolTimeout',
        'ImmediateResponse': 'immediateResponse',
        'Name': 'name',
        'RenewOnLinkUp': 'renewOnLinkUp',
        'RowNames': 'rowNames',
        'SkipReleaseOnStop': 'skipReleaseOnStop',
    }

    def __init__(self, parent):
        super(Dhcpv6client, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.sessionlifetime.sessionlifetime_c56c3cca82dcd438a26eb5e7980bb00a import SessionLifetime
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.startrate.startrate_1bba90e9b5242a924a45ce8454358006 import StartRate
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.stoprate.stoprate_e57c921a314c7c4a39ab432f5e2970a0 import StopRate
        return StopRate(self)._select()

    @property
    def TlvEditor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor_d66c1061f4b3bb902b0e5e76ee632657.TlvEditor): An instance of the TlvEditor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor_d66c1061f4b3bb902b0e5e76ee632657 import TlvEditor
        return TlvEditor(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Dhcp6EchoIAInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, the DHCPv6 client will request the exact address as advertised by server.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6EchoIAInfo']))

    @property
    def Dhcp6InfoReqMaxRc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Info Request Attempts
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfoReqMaxRc']))

    @property
    def Dhcp6InfoReqMaxRt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Information-request timeout value in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfoReqMaxRt']))

    @property
    def Dhcp6InfoReqTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Initial Information-request timeout value in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfoReqTimeout']))

    @property
    def Dhcp6NsGw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, DHCP clients NS to find their Gateway MAC Addresses.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6NsGw']))

    @property
    def Dhcp6RebMaxRt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Rebind timeout value in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6RebMaxRt']))

    @property
    def Dhcp6RebTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Initial Rebind timeout seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6RebTimeout']))

    @property
    def Dhcp6RelMaxRc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Release attempts
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6RelMaxRc']))

    @property
    def Dhcp6RelTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Initial Release timeout in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6RelTimeout']))

    @property
    def Dhcp6RenMaxRt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Renew timeout value in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6RenMaxRt']))

    @property
    def Dhcp6RenTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Initial Renew timeout in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6RenTimeout']))

    @property
    def Dhcp6ReqMaxRc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Request retry attempts
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6ReqMaxRc']))

    @property
    def Dhcp6ReqMaxRt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Request timeout value in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6ReqMaxRt']))

    @property
    def Dhcp6ReqTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Initial Request timeout in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6ReqTimeout']))

    @property
    def Dhcp6SolMaxRc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Solicit retry attempts
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6SolMaxRc']))

    @property
    def Dhcp6SolMaxRt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Max Solicit timeout value in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6SolMaxRt']))

    @property
    def Dhcp6SolTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RFC 3315 Initial Solicit timeout in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6SolTimeout']))

    @property
    def ImmediateResponse(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables DHCP client to send Request immediately after receiving Advertise irrespective of Initial Solicit Timeout.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ImmediateResponse']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def RenewOnLinkUp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicate to renew the active DHCP sessions after link status goes down and up.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RenewOnLinkUp']))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def SkipReleaseOnStop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SkipReleaseOnStop']))

    def update(self, Name=None):
        """Updates dhcpv6client resource on the server.

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

    def get_device_ids(self, PortNames=None, Dhcp6EchoIAInfo=None, Dhcp6InfoReqMaxRc=None, Dhcp6InfoReqMaxRt=None, Dhcp6InfoReqTimeout=None, Dhcp6NsGw=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, ImmediateResponse=None, RenewOnLinkUp=None, SkipReleaseOnStop=None):
        """Base class infrastructure that gets a list of dhcpv6client device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Dhcp6EchoIAInfo (str): optional regex of dhcp6EchoIAInfo
        - Dhcp6InfoReqMaxRc (str): optional regex of dhcp6InfoReqMaxRc
        - Dhcp6InfoReqMaxRt (str): optional regex of dhcp6InfoReqMaxRt
        - Dhcp6InfoReqTimeout (str): optional regex of dhcp6InfoReqTimeout
        - Dhcp6NsGw (str): optional regex of dhcp6NsGw
        - Dhcp6RebMaxRt (str): optional regex of dhcp6RebMaxRt
        - Dhcp6RebTimeout (str): optional regex of dhcp6RebTimeout
        - Dhcp6RelMaxRc (str): optional regex of dhcp6RelMaxRc
        - Dhcp6RelTimeout (str): optional regex of dhcp6RelTimeout
        - Dhcp6RenMaxRt (str): optional regex of dhcp6RenMaxRt
        - Dhcp6RenTimeout (str): optional regex of dhcp6RenTimeout
        - Dhcp6ReqMaxRc (str): optional regex of dhcp6ReqMaxRc
        - Dhcp6ReqMaxRt (str): optional regex of dhcp6ReqMaxRt
        - Dhcp6ReqTimeout (str): optional regex of dhcp6ReqTimeout
        - Dhcp6SolMaxRc (str): optional regex of dhcp6SolMaxRc
        - Dhcp6SolMaxRt (str): optional regex of dhcp6SolMaxRt
        - Dhcp6SolTimeout (str): optional regex of dhcp6SolTimeout
        - ImmediateResponse (str): optional regex of immediateResponse
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

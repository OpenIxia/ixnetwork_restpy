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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Ipv6(Base):
    """IPv6 global and per-port settings
    The Ipv6 class encapsulates a required ipv6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv6'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableNaRouterBit': 'enableNaRouterBit',
        'InitialRaCount': 'initialRaCount',
        'MaxInitialRaInterval': 'maxInitialRaInterval',
        'MaxRaInterval': 'maxRaInterval',
        'Name': 'name',
        'PermanentMacForGateway': 'permanentMacForGateway',
        'RaRtrLifetime': 'raRtrLifetime',
        'ReSendNsOnLinkUp': 'reSendNsOnLinkUp',
        'RowNames': 'rowNames',
        'SuppressNsForDuplicateGateway': 'suppressNsForDuplicateGateway',
    }

    def __init__(self, parent):
        super(Ipv6, self).__init__(parent)

    @property
    def NsRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.nsrate.nsrate_2743e8b1b7c27242856a5d009e73521d.NsRate): An instance of the NsRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.nsrate.nsrate_2743e8b1b7c27242856a5d009e73521d import NsRate
        return NsRate(self)._select()

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        return StopRate(self)._select()

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
    def EnableNaRouterBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, Router bit will be set in Neighbor Advertisement.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNaRouterBit']))

    @property
    def InitialRaCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Initial Router Advertisement sent count. Values can range from 0 to 10.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitialRaCount']))

    @property
    def MaxInitialRaInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Initial Router Advertisement interval. Values can range from 3 to 16.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxInitialRaInterval']))

    @property
    def MaxRaInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Periodic Router Advertisement interval. Values can range from 9 to 1800.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxRaInterval']))

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
    def PermanentMacForGateway(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): When enabled, adds permanent entries for Gateways with manual MAC.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PermanentMacForGateway']))

    @property
    def RaRtrLifetime(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Router lifetime in Router Advertisement. Values can range from 0 to 9000.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RaRtrLifetime']))

    @property
    def ReSendNsOnLinkUp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Resends neighbor solicitation after link up.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReSendNsOnLinkUp']))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def SuppressNsForDuplicateGateway(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Optimizes the gateway MAC discovery by sending a single NS request for each unique destination.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SuppressNsForDuplicateGateway']))

    def update(self, Name=None):
        """Updates ipv6 resource on the server.

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

    def get_device_ids(self, PortNames=None, EnableNaRouterBit=None, InitialRaCount=None, MaxInitialRaInterval=None, MaxRaInterval=None, PermanentMacForGateway=None, RaRtrLifetime=None, ReSendNsOnLinkUp=None, SuppressNsForDuplicateGateway=None):
        """Base class infrastructure that gets a list of ipv6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - EnableNaRouterBit (str): optional regex of enableNaRouterBit
        - InitialRaCount (str): optional regex of initialRaCount
        - MaxInitialRaInterval (str): optional regex of maxInitialRaInterval
        - MaxRaInterval (str): optional regex of maxRaInterval
        - PermanentMacForGateway (str): optional regex of permanentMacForGateway
        - RaRtrLifetime (str): optional regex of raRtrLifetime
        - ReSendNsOnLinkUp (str): optional regex of reSendNsOnLinkUp
        - SuppressNsForDuplicateGateway (str): optional regex of suppressNsForDuplicateGateway

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

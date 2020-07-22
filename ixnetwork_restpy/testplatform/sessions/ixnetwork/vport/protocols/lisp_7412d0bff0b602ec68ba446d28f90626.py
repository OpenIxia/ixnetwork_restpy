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


class Lisp(Base):
    """Details about the list processing are provided here
    The Lisp class encapsulates a required lisp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'lisp'
    _SDM_ATT_MAP = {
        'BurstIntervalInMs': 'burstIntervalInMs',
        'Enabled': 'enabled',
        'Ipv4MapRegisterPacketsPerBurst': 'ipv4MapRegisterPacketsPerBurst',
        'Ipv4MapRequestPacketsPerBurst': 'ipv4MapRequestPacketsPerBurst',
        'Ipv4SmrPacketsPerBurst': 'ipv4SmrPacketsPerBurst',
        'Ipv6MapRegisterPacketsPerBurst': 'ipv6MapRegisterPacketsPerBurst',
        'Ipv6MapRequestPacketsPerBurst': 'ipv6MapRequestPacketsPerBurst',
        'Ipv6SmrPacketsPerBurst': 'ipv6SmrPacketsPerBurst',
        'ProtocolState': 'protocolState',
    }

    def __init__(self, parent):
        super(Lisp, self).__init__(parent)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_460cd981ff6408d3ef21002172a567e2.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_460cd981ff6408d3ef21002172a567e2 import Router
        return Router(self)

    @property
    def SiteEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.siteeidrange_05797de8ac7278cb990c0a2b3de1a225.SiteEidRange): An instance of the SiteEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.siteeidrange_05797de8ac7278cb990c0a2b3de1a225 import SiteEidRange
        return SiteEidRange(self)

    @property
    def BurstIntervalInMs(self):
        """
        Returns
        -------
        - number: It shows the details abou the burst interval in micro seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstIntervalInMs'])
    @BurstIntervalInMs.setter
    def BurstIntervalInMs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstIntervalInMs'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it shows enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Ipv4MapRegisterPacketsPerBurst(self):
        """
        Returns
        -------
        - number: It gives details about the ip v4 map register packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapRegisterPacketsPerBurst'])
    @Ipv4MapRegisterPacketsPerBurst.setter
    def Ipv4MapRegisterPacketsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4MapRegisterPacketsPerBurst'], value)

    @property
    def Ipv4MapRequestPacketsPerBurst(self):
        """
        Returns
        -------
        - number: It gives details about the ip v4 map requests packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapRequestPacketsPerBurst'])
    @Ipv4MapRequestPacketsPerBurst.setter
    def Ipv4MapRequestPacketsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4MapRequestPacketsPerBurst'], value)

    @property
    def Ipv4SmrPacketsPerBurst(self):
        """
        Returns
        -------
        - number: It gives details about the Ip v4 Smr packets per bursts
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4SmrPacketsPerBurst'])
    @Ipv4SmrPacketsPerBurst.setter
    def Ipv4SmrPacketsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4SmrPacketsPerBurst'], value)

    @property
    def Ipv6MapRegisterPacketsPerBurst(self):
        """
        Returns
        -------
        - number: It gives details about the ip v6 map register packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapRegisterPacketsPerBurst'])
    @Ipv6MapRegisterPacketsPerBurst.setter
    def Ipv6MapRegisterPacketsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6MapRegisterPacketsPerBurst'], value)

    @property
    def Ipv6MapRequestPacketsPerBurst(self):
        """
        Returns
        -------
        - number: It gives details about the ip v6 map requests packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapRequestPacketsPerBurst'])
    @Ipv6MapRequestPacketsPerBurst.setter
    def Ipv6MapRequestPacketsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6MapRequestPacketsPerBurst'], value)

    @property
    def Ipv6SmrPacketsPerBurst(self):
        """
        Returns
        -------
        - number: It gives details about the Ip v6 Smr packets per bursts
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6SmrPacketsPerBurst'])
    @Ipv6SmrPacketsPerBurst.setter
    def Ipv6SmrPacketsPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6SmrPacketsPerBurst'], value)

    @property
    def ProtocolState(self):
        """
        Returns
        -------
        - str(stopped | unknown | stopping | started | starting): Shows different protocol states (read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolState'])

    def update(self, BurstIntervalInMs=None, Enabled=None, Ipv4MapRegisterPacketsPerBurst=None, Ipv4MapRequestPacketsPerBurst=None, Ipv4SmrPacketsPerBurst=None, Ipv6MapRegisterPacketsPerBurst=None, Ipv6MapRequestPacketsPerBurst=None, Ipv6SmrPacketsPerBurst=None):
        """Updates lisp resource on the server.

        Args
        ----
        - BurstIntervalInMs (number): It shows the details abou the burst interval in micro seconds
        - Enabled (bool): If true, it shows enabled.
        - Ipv4MapRegisterPacketsPerBurst (number): It gives details about the ip v4 map register packets per burst
        - Ipv4MapRequestPacketsPerBurst (number): It gives details about the ip v4 map requests packets per burst
        - Ipv4SmrPacketsPerBurst (number): It gives details about the Ip v4 Smr packets per bursts
        - Ipv6MapRegisterPacketsPerBurst (number): It gives details about the ip v6 map register packets per burst
        - Ipv6MapRequestPacketsPerBurst (number): It gives details about the ip v6 map requests packets per burst
        - Ipv6SmrPacketsPerBurst (number): It gives details about the Ip v6 Smr packets per bursts

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self):
        """Executes the start operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

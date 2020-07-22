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


class CustomTopology(Base):
    """NOT DEFINED
    The CustomTopology class encapsulates a list of customTopology resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopology.find() method.
    The list can be managed by using the CustomTopology.add() and CustomTopology.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopology'
    _SDM_ATT_MAP = {
        'CapRouterId': 'capRouterId',
        'EnableHostname': 'enableHostname',
        'Enabled': 'enabled',
        'HostNamePrefix': 'hostNamePrefix',
        'InterfaceMetric': 'interfaceMetric',
        'StartSysId': 'startSysId',
        'SysIdInc': 'sysIdInc',
    }

    def __init__(self, parent):
        super(CustomTopology, self).__init__(parent)

    @property
    def CustomTopologyMulticastIpv4GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv4grouprange_a15b6ec5846f1ddab31235f1d562c55c.CustomTopologyMulticastIpv4GroupRange): An instance of the CustomTopologyMulticastIpv4GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv4grouprange_a15b6ec5846f1ddab31235f1d562c55c import CustomTopologyMulticastIpv4GroupRange
        return CustomTopologyMulticastIpv4GroupRange(self)

    @property
    def CustomTopologyMulticastIpv6GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv6grouprange_febe5392db46dbf816f07785a75a5a5d.CustomTopologyMulticastIpv6GroupRange): An instance of the CustomTopologyMulticastIpv6GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv6grouprange_febe5392db46dbf816f07785a75a5a5d import CustomTopologyMulticastIpv6GroupRange
        return CustomTopologyMulticastIpv6GroupRange(self)

    @property
    def CustomTopologyMulticastMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastmacrange_8c759596f197c960a0a5f985205516a4.CustomTopologyMulticastMacRange): An instance of the CustomTopologyMulticastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastmacrange_8c759596f197c960a0a5f985205516a4 import CustomTopologyMulticastMacRange
        return CustomTopologyMulticastMacRange(self)

    @property
    def CustomTopologyNode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynode_8129a1649705353aa11e5c05b0e43d74.CustomTopologyNode): An instance of the CustomTopologyNode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynode_8129a1649705353aa11e5c05b0e43d74 import CustomTopologyNode
        return CustomTopologyNode(self)

    @property
    def CustomTopologyNodeTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynodetopologyrange_181026171b26292c0aa2d8d9e8a7c0f9.CustomTopologyNodeTopologyRange): An instance of the CustomTopologyNodeTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynodetopologyrange_181026171b26292c0aa2d8d9e8a7c0f9 import CustomTopologyNodeTopologyRange
        return CustomTopologyNodeTopologyRange(self)

    @property
    def CustomTopologyRbLinks(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyrblinks_1ff82933a2cfb3381c1a218bb1f15478.CustomTopologyRbLinks): An instance of the CustomTopologyRbLinks class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyrblinks_1ff82933a2cfb3381c1a218bb1f15478 import CustomTopologyRbLinks
        return CustomTopologyRbLinks(self)

    @property
    def CustomTopologySpbNodeTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodetopologyrange_07ced20538fd8f8fea38a783c9448fb6.CustomTopologySpbNodeTopologyRange): An instance of the CustomTopologySpbNodeTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodetopologyrange_07ced20538fd8f8fea38a783c9448fb6 import CustomTopologySpbNodeTopologyRange
        return CustomTopologySpbNodeTopologyRange(self)

    @property
    def CustomTopologyUnicastMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyunicastmacrange_0273c2983b0c58ba52e6d2c06548f60d.CustomTopologyUnicastMacRange): An instance of the CustomTopologyUnicastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyunicastmacrange_0273c2983b0c58ba52e6d2c06548f60d import CustomTopologyUnicastMacRange
        return CustomTopologyUnicastMacRange(self)

    @property
    def CapRouterId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CapRouterId'])
    @CapRouterId.setter
    def CapRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CapRouterId'], value)

    @property
    def EnableHostname(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHostname'])
    @EnableHostname.setter
    def EnableHostname(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHostname'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def HostNamePrefix(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostNamePrefix'])
    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostNamePrefix'], value)

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric'])
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceMetric'], value)

    @property
    def StartSysId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSysId'])
    @StartSysId.setter
    def StartSysId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSysId'], value)

    @property
    def SysIdInc(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SysIdInc'])
    @SysIdInc.setter
    def SysIdInc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SysIdInc'], value)

    def update(self, CapRouterId=None, EnableHostname=None, Enabled=None, HostNamePrefix=None, InterfaceMetric=None, StartSysId=None, SysIdInc=None):
        """Updates customTopology resource on the server.

        Args
        ----
        - CapRouterId (str): NOT DEFINED
        - EnableHostname (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - HostNamePrefix (str): NOT DEFINED
        - InterfaceMetric (number): NOT DEFINED
        - StartSysId (str): NOT DEFINED
        - SysIdInc (str): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CapRouterId=None, EnableHostname=None, Enabled=None, HostNamePrefix=None, InterfaceMetric=None, StartSysId=None, SysIdInc=None):
        """Adds a new customTopology resource on the server and adds it to the container.

        Args
        ----
        - CapRouterId (str): NOT DEFINED
        - EnableHostname (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - HostNamePrefix (str): NOT DEFINED
        - InterfaceMetric (number): NOT DEFINED
        - StartSysId (str): NOT DEFINED
        - SysIdInc (str): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopology resources using find and the newly added customTopology resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopology resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CapRouterId=None, EnableHostname=None, Enabled=None, HostNamePrefix=None, InterfaceMetric=None, StartSysId=None, SysIdInc=None):
        """Finds and retrieves customTopology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopology resources from the server.

        Args
        ----
        - CapRouterId (str): NOT DEFINED
        - EnableHostname (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - HostNamePrefix (str): NOT DEFINED
        - InterfaceMetric (number): NOT DEFINED
        - StartSysId (str): NOT DEFINED
        - SysIdInc (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

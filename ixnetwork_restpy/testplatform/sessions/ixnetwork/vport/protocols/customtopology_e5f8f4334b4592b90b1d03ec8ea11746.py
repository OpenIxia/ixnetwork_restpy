# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
    The CustomTopology class encapsulates a list of customTopology resources that is be managed by the user.
    A list of resources can be retrieved from the server using the CustomTopology.find() method.
    The list can be managed by the user by using the CustomTopology.add() and CustomTopology.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopology'

    def __init__(self, parent):
        super(CustomTopology, self).__init__(parent)

    @property
    def CustomTopologyMulticastIpv4GroupRange(self):
        """An instance of the CustomTopologyMulticastIpv4GroupRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv4grouprange_8b7ebcb58d6e011e48e4311a2a4edb4a.CustomTopologyMulticastIpv4GroupRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv4grouprange_8b7ebcb58d6e011e48e4311a2a4edb4a import CustomTopologyMulticastIpv4GroupRange
        return CustomTopologyMulticastIpv4GroupRange(self)

    @property
    def CustomTopologyMulticastIpv6GroupRange(self):
        """An instance of the CustomTopologyMulticastIpv6GroupRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv6grouprange_dec631743816cb4bf5e074fff9534f91.CustomTopologyMulticastIpv6GroupRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv6grouprange_dec631743816cb4bf5e074fff9534f91 import CustomTopologyMulticastIpv6GroupRange
        return CustomTopologyMulticastIpv6GroupRange(self)

    @property
    def CustomTopologyMulticastMacRange(self):
        """An instance of the CustomTopologyMulticastMacRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastmacrange_7e8248f2611b55649e9d5f59c62b9277.CustomTopologyMulticastMacRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastmacrange_7e8248f2611b55649e9d5f59c62b9277 import CustomTopologyMulticastMacRange
        return CustomTopologyMulticastMacRange(self)

    @property
    def CustomTopologyNode(self):
        """An instance of the CustomTopologyNode class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynode_7c4c2bb71601960bb46af685c2460bf0.CustomTopologyNode)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynode_7c4c2bb71601960bb46af685c2460bf0 import CustomTopologyNode
        return CustomTopologyNode(self)

    @property
    def CustomTopologyNodeTopologyRange(self):
        """An instance of the CustomTopologyNodeTopologyRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynodetopologyrange_99163c414d695fc043ba0ea600b48720.CustomTopologyNodeTopologyRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynodetopologyrange_99163c414d695fc043ba0ea600b48720 import CustomTopologyNodeTopologyRange
        return CustomTopologyNodeTopologyRange(self)

    @property
    def CustomTopologyRbLinks(self):
        """An instance of the CustomTopologyRbLinks class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyrblinks_d3f6765ac561b29351d942b45e7510a0.CustomTopologyRbLinks)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyrblinks_d3f6765ac561b29351d942b45e7510a0 import CustomTopologyRbLinks
        return CustomTopologyRbLinks(self)

    @property
    def CustomTopologySpbNodeTopologyRange(self):
        """An instance of the CustomTopologySpbNodeTopologyRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodetopologyrange_78dc15df4bc5698ff6aa5bb7e6119d48.CustomTopologySpbNodeTopologyRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodetopologyrange_78dc15df4bc5698ff6aa5bb7e6119d48 import CustomTopologySpbNodeTopologyRange
        return CustomTopologySpbNodeTopologyRange(self)

    @property
    def CustomTopologyUnicastMacRange(self):
        """An instance of the CustomTopologyUnicastMacRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyunicastmacrange_7d5b9c4d26a6e7c7990447ee7b5b1819.CustomTopologyUnicastMacRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyunicastmacrange_7d5b9c4d26a6e7c7990447ee7b5b1819 import CustomTopologyUnicastMacRange
        return CustomTopologyUnicastMacRange(self)

    @property
    def CapRouterId(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('capRouterId')
    @CapRouterId.setter
    def CapRouterId(self, value):
        self._set_attribute('capRouterId', value)

    @property
    def EnableHostname(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableHostname')
    @EnableHostname.setter
    def EnableHostname(self, value):
        self._set_attribute('enableHostname', value)

    @property
    def Enabled(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def HostNamePrefix(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('hostNamePrefix')
    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        self._set_attribute('hostNamePrefix', value)

    @property
    def InterfaceMetric(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('interfaceMetric')
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute('interfaceMetric', value)

    @property
    def StartSysId(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('startSysId')
    @StartSysId.setter
    def StartSysId(self, value):
        self._set_attribute('startSysId', value)

    @property
    def SysIdInc(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('sysIdInc')
    @SysIdInc.setter
    def SysIdInc(self, value):
        self._set_attribute('sysIdInc', value)

    def update(self, CapRouterId=None, EnableHostname=None, Enabled=None, HostNamePrefix=None, InterfaceMetric=None, StartSysId=None, SysIdInc=None):
        """Updates a child instance of customTopology on the server.

        Args:
            CapRouterId (str): NOT DEFINED
            EnableHostname (bool): NOT DEFINED
            Enabled (bool): NOT DEFINED
            HostNamePrefix (str): NOT DEFINED
            InterfaceMetric (number): NOT DEFINED
            StartSysId (str): NOT DEFINED
            SysIdInc (str): NOT DEFINED

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, CapRouterId=None, EnableHostname=None, Enabled=None, HostNamePrefix=None, InterfaceMetric=None, StartSysId=None, SysIdInc=None):
        """Adds a new customTopology node on the server and retrieves it in this instance.

        Args:
            CapRouterId (str): NOT DEFINED
            EnableHostname (bool): NOT DEFINED
            Enabled (bool): NOT DEFINED
            HostNamePrefix (str): NOT DEFINED
            InterfaceMetric (number): NOT DEFINED
            StartSysId (str): NOT DEFINED
            SysIdInc (str): NOT DEFINED

        Returns:
            self: This instance with all currently retrieved customTopology data using find and the newly added customTopology data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the customTopology data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CapRouterId=None, EnableHostname=None, Enabled=None, HostNamePrefix=None, InterfaceMetric=None, StartSysId=None, SysIdInc=None):
        """Finds and retrieves customTopology data from the server.

        All named parameters support regex and can be used to selectively retrieve customTopology data from the server.
        By default the find method takes no parameters and will retrieve all customTopology data from the server.

        Args:
            CapRouterId (str): NOT DEFINED
            EnableHostname (bool): NOT DEFINED
            Enabled (bool): NOT DEFINED
            HostNamePrefix (str): NOT DEFINED
            InterfaceMetric (number): NOT DEFINED
            StartSysId (str): NOT DEFINED
            SysIdInc (str): NOT DEFINED

        Returns:
            self: This instance with matching customTopology data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of customTopology data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the customTopology data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class MacPools(Base):
    """Represents an Ethernet device set
    The MacPools class encapsulates a list of macPools resources that are managed by the user.
    A list of resources can be retrieved from the server using the MacPools.find() method.
    The list can be managed by using the MacPools.add() and MacPools.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macPools'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableVlans': 'enableVlans',
        'LastMacAddress': 'lastMacAddress',
        'Mac': 'mac',
        'Name': 'name',
        'NumberOfAddresses': 'numberOfAddresses',
        'NumberOfAddressesAsy': 'numberOfAddressesAsy',
        'PrefixLength': 'prefixLength',
        'UseVlans': 'useVlans',
        'VlanCount': 'vlanCount',
    }

    def __init__(self, parent):
        super(MacPools, self).__init__(parent)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        return CMacProperties(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        return EvpnIPv6PrefixRange(self)

    @property
    def Ipv4PrefixPools(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools_2d6f2aedde61c058965d4e1b21741352.Ipv4PrefixPools): An instance of the Ipv4PrefixPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools_2d6f2aedde61c058965d4e1b21741352 import Ipv4PrefixPools
        return Ipv4PrefixPools(self)

    @property
    def Ipv6PrefixPools(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools_f83aba85ff769655b348dc60ddcb30f2.Ipv6PrefixPools): An instance of the Ipv6PrefixPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools_f83aba85ff769655b348dc60ddcb30f2 import Ipv6PrefixPools
        return Ipv6PrefixPools(self)

    @property
    def IsisSpbMacCloudConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig_791b0bf61c8f6877cabfa2621478ab8a.IsisSpbMacCloudConfig): An instance of the IsisSpbMacCloudConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig_791b0bf61c8f6877cabfa2621478ab8a import IsisSpbMacCloudConfig
        return IsisSpbMacCloudConfig(self)

    @property
    def IsisTrillUCastMacConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig_a91c5b3e28b2bee04ff08d2e22fad1e2.IsisTrillUCastMacConfig): An instance of the IsisTrillUCastMacConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig_a91c5b3e28b2bee04ff08d2e22fad1e2 import IsisTrillUCastMacConfig
        return IsisTrillUCastMacConfig(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def Vlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vlan_a3ff17a54eb8b0ce450fbc0fd0191f37.Vlan): An instance of the Vlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vlan_a3ff17a54eb8b0ce450fbc0fd0191f37 import Vlan
        return Vlan(self)

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
    def EnableVlans(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables VLANs for the sessions
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVlans']))

    @property
    def LastMacAddress(self):
        """
        Returns
        -------
        - list(str): Last Address of network addresses in the simulated MAC network range
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastMacAddress'])

    @property
    def Mac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MAC addresses of the devices
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mac']))

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
    def NumberOfAddresses(self):
        """DEPRECATED 
        Returns
        -------
        - number: Number of MAC addresses in the simulated MAC range
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfAddresses'])
    @NumberOfAddresses.setter
    def NumberOfAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfAddresses'], value)

    @property
    def NumberOfAddressesAsy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of MAC addresses in the simulated MAC range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfAddressesAsy']))

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def UseVlans(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Flag to determine whether VLANs are enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseVlans'])
    @UseVlans.setter
    def UseVlans(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseVlans'], value)

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - number: Number of active VLANs
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanCount'])
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanCount'], value)

    def update(self, Name=None, NumberOfAddresses=None, UseVlans=None, VlanCount=None):
        """Updates macPools resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAddresses (number): Number of MAC addresses in the simulated MAC range
        - UseVlans (bool): Flag to determine whether VLANs are enabled
        - VlanCount (number): Number of active VLANs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, NumberOfAddresses=None, UseVlans=None, VlanCount=None):
        """Adds a new macPools resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAddresses (number): Number of MAC addresses in the simulated MAC range
        - UseVlans (bool): Flag to determine whether VLANs are enabled
        - VlanCount (number): Number of active VLANs

        Returns
        -------
        - self: This instance with all currently retrieved macPools resources using find and the newly added macPools resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macPools resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, LastMacAddress=None, Name=None, NumberOfAddresses=None, UseVlans=None, VlanCount=None):
        """Finds and retrieves macPools resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macPools resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macPools resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - LastMacAddress (list(str)): Last Address of network addresses in the simulated MAC network range
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAddresses (number): Number of MAC addresses in the simulated MAC range
        - UseVlans (bool): Flag to determine whether VLANs are enabled
        - VlanCount (number): Number of active VLANs

        Returns
        -------
        - self: This instance with matching macPools resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macPools data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macPools resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, EnableVlans=None, Mac=None, NumberOfAddressesAsy=None, PrefixLength=None):
        """Base class infrastructure that gets a list of macPools device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - EnableVlans (str): optional regex of enableVlans
        - Mac (str): optional regex of mac
        - NumberOfAddressesAsy (str): optional regex of numberOfAddressesAsy
        - PrefixLength (str): optional regex of prefixLength

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)

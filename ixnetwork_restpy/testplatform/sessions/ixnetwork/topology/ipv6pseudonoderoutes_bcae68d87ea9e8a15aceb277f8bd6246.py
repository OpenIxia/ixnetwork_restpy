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


class IPv6PseudoNodeRoutes(Base):
    """Isis IPv6 pseudo node routes
    The IPv6PseudoNodeRoutes class encapsulates a list of IPv6PseudoNodeRoutes resources that are managed by the system.
    A list of resources can be retrieved from the server using the IPv6PseudoNodeRoutes.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'IPv6PseudoNodeRoutes'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Algorithm': 'algorithm',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableBit4': 'enableBit4',
        'EnableBit5': 'enableBit5',
        'EnableBit6': 'enableBit6',
        'EnableBit7': 'enableBit7',
        'EnableBit8': 'enableBit8',
        'EnableNFlag': 'enableNFlag',
        'EnableRFlag': 'enableRFlag',
        'EnableXFlag': 'enableXFlag',
        'IPv6SourceRouterID': 'iPv6SourceRouterID',
        'IncludePrefixAttrFlags': 'includePrefixAttrFlags',
        'IncludeSourceRouterID': 'includeSourceRouterID',
        'Ipv4SourceRouterID': 'ipv4SourceRouterID',
        'Ipv6EFlag': 'ipv6EFlag',
        'Ipv6LFlag': 'ipv6LFlag',
        'Ipv6Metric': 'ipv6Metric',
        'Ipv6NFlag': 'ipv6NFlag',
        'Ipv6PFlag': 'ipv6PFlag',
        'Ipv6RFlag': 'ipv6RFlag',
        'Ipv6Redistribution': 'ipv6Redistribution',
        'Ipv6RouteOrigin': 'ipv6RouteOrigin',
        'Ipv6Srh': 'ipv6Srh',
        'Ipv6VFlag': 'ipv6VFlag',
        'Name': 'name',
        'NetworkAddress': 'networkAddress',
        'NoOfMtIds': 'noOfMtIds',
        'NoOfSidPerNodeRoutes': 'noOfSidPerNodeRoutes',
        'OverWriteRoutersMt': 'overWriteRoutersMt',
        'Prefix': 'prefix',
        'RangeSize': 'rangeSize',
        'SIDIndexLabel': 'sIDIndexLabel',
    }

    def __init__(self, parent):
        super(IPv6PseudoNodeRoutes, self).__init__(parent)

    @property
    def IsisL3PseudoRouteMtIdIPv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoroutemtidipv6_652a2ad7bd5f910e0b5af8caa70a77b7.IsisL3PseudoRouteMtIdIPv6): An instance of the IsisL3PseudoRouteMtIdIPv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoroutemtidipv6_652a2ad7bd5f910e0b5af8caa70a77b7 import IsisL3PseudoRouteMtIdIPv6
        return IsisL3PseudoRouteMtIdIPv6(self)._select()

    @property
    def PseudoRoutesSid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pseudoroutessid_2945568b93e033040e1720a03e86ab6f.PseudoRoutesSid): An instance of the PseudoRoutesSid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pseudoroutessid_2945568b93e033040e1720a03e86ab6f import PseudoRoutesSid
        return PseudoRoutesSid(self)._select()

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
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether this is to be advertised or not
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Algorithm(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def ConfigureSIDIndexLabel(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

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
    def EnableBit4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 4th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit4']))

    @property
    def EnableBit5(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 5th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit5']))

    @property
    def EnableBit6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 6th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit6']))

    @property
    def EnableBit7(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 7th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit7']))

    @property
    def EnableBit8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 8th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit8']))

    @property
    def EnableNFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables node flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNFlag']))

    @property
    def EnableRFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables redistribution flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRFlag']))

    @property
    def EnableXFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables external flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableXFlag']))

    @property
    def IPv6SourceRouterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This takes the value of the ipv6 source router id.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv6SourceRouterID']))

    @property
    def IncludePrefixAttrFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to include the prefix attribute flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludePrefixAttrFlags']))

    @property
    def IncludeSourceRouterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This drop box is provided to select ipv4 or ipv6 source id or none of them.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSourceRouterID']))

    @property
    def Ipv4SourceRouterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This takes the value of the ipv4 source router id.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4SourceRouterID']))

    @property
    def Ipv6EFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit NULL flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6EFlag']))

    @property
    def Ipv6LFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6LFlag']))

    @property
    def Ipv6Metric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Metric']))

    @property
    def Ipv6NFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nodal prefix flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NFlag']))

    @property
    def Ipv6PFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6PFlag']))

    @property
    def Ipv6RFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6RFlag']))

    @property
    def Ipv6Redistribution(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Redistribution']))

    @property
    def Ipv6RouteOrigin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6RouteOrigin']))

    @property
    def Ipv6Srh(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Srh']))

    @property
    def Ipv6VFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6VFlag']))

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
    def NetworkAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefixes of the simulated IPv6 network
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkAddress']))

    @property
    def NoOfMtIds(self):
        """
        Returns
        -------
        - number: Number of MTIDs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfMtIds'])
    @NoOfMtIds.setter
    def NoOfMtIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfMtIds'], value)

    @property
    def NoOfSidPerNodeRoutes(self):
        """
        Returns
        -------
        - number: Number of SID per node routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSidPerNodeRoutes'])
    @NoOfSidPerNodeRoutes.setter
    def NoOfSidPerNodeRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfSidPerNodeRoutes'], value)

    @property
    def OverWriteRoutersMt(self):
        """
        Returns
        -------
        - bool: If false, routers MT IDs which is union of all interfaces MTIDs would be used. If true, configured MT IDs in route range would be used
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverWriteRoutersMt'])
    @OverWriteRoutersMt.setter
    def OverWriteRoutersMt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverWriteRoutersMt'], value)

    @property
    def Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Prefix']))

    @property
    def RangeSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Range Size
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RangeSize']))

    @property
    def SIDIndexLabel(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SIDIndexLabel']))

    def update(self, Name=None, NoOfMtIds=None, NoOfSidPerNodeRoutes=None, OverWriteRoutersMt=None):
        """Updates IPv6PseudoNodeRoutes resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMtIds (number): Number of MTIDs
        - NoOfSidPerNodeRoutes (number): Number of SID per node routes
        - OverWriteRoutersMt (bool): If false, routers MT IDs which is union of all interfaces MTIDs would be used. If true, configured MT IDs in route range would be used

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, NoOfMtIds=None, NoOfSidPerNodeRoutes=None, OverWriteRoutersMt=None):
        """Finds and retrieves IPv6PseudoNodeRoutes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve IPv6PseudoNodeRoutes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all IPv6PseudoNodeRoutes resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMtIds (number): Number of MTIDs
        - NoOfSidPerNodeRoutes (number): Number of SID per node routes
        - OverWriteRoutersMt (bool): If false, routers MT IDs which is union of all interfaces MTIDs would be used. If true, configured MT IDs in route range would be used

        Returns
        -------
        - self: This instance with matching IPv6PseudoNodeRoutes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of IPv6PseudoNodeRoutes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the IPv6PseudoNodeRoutes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, ConfigureSIDIndexLabel=None, EnableBit4=None, EnableBit5=None, EnableBit6=None, EnableBit7=None, EnableBit8=None, EnableNFlag=None, EnableRFlag=None, EnableXFlag=None, IPv6SourceRouterID=None, IncludePrefixAttrFlags=None, IncludeSourceRouterID=None, Ipv4SourceRouterID=None, Ipv6EFlag=None, Ipv6LFlag=None, Ipv6Metric=None, Ipv6NFlag=None, Ipv6PFlag=None, Ipv6RFlag=None, Ipv6Redistribution=None, Ipv6RouteOrigin=None, Ipv6Srh=None, Ipv6VFlag=None, NetworkAddress=None, Prefix=None, RangeSize=None, SIDIndexLabel=None):
        """Base class infrastructure that gets a list of IPv6PseudoNodeRoutes device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Algorithm (str): optional regex of algorithm
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - EnableBit4 (str): optional regex of enableBit4
        - EnableBit5 (str): optional regex of enableBit5
        - EnableBit6 (str): optional regex of enableBit6
        - EnableBit7 (str): optional regex of enableBit7
        - EnableBit8 (str): optional regex of enableBit8
        - EnableNFlag (str): optional regex of enableNFlag
        - EnableRFlag (str): optional regex of enableRFlag
        - EnableXFlag (str): optional regex of enableXFlag
        - IPv6SourceRouterID (str): optional regex of iPv6SourceRouterID
        - IncludePrefixAttrFlags (str): optional regex of includePrefixAttrFlags
        - IncludeSourceRouterID (str): optional regex of includeSourceRouterID
        - Ipv4SourceRouterID (str): optional regex of ipv4SourceRouterID
        - Ipv6EFlag (str): optional regex of ipv6EFlag
        - Ipv6LFlag (str): optional regex of ipv6LFlag
        - Ipv6Metric (str): optional regex of ipv6Metric
        - Ipv6NFlag (str): optional regex of ipv6NFlag
        - Ipv6PFlag (str): optional regex of ipv6PFlag
        - Ipv6RFlag (str): optional regex of ipv6RFlag
        - Ipv6Redistribution (str): optional regex of ipv6Redistribution
        - Ipv6RouteOrigin (str): optional regex of ipv6RouteOrigin
        - Ipv6Srh (str): optional regex of ipv6Srh
        - Ipv6VFlag (str): optional regex of ipv6VFlag
        - NetworkAddress (str): optional regex of networkAddress
        - Prefix (str): optional regex of prefix
        - RangeSize (str): optional regex of rangeSize
        - SIDIndexLabel (str): optional regex of sIDIndexLabel

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

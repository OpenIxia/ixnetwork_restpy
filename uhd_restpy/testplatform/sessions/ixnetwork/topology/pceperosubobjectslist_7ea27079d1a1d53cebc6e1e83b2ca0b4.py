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


class PcepEroSubObjectsList(Base):
    """
    The PcepEroSubObjectsList class encapsulates a list of pcepEroSubObjectsList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PcepEroSubObjectsList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pcepEroSubObjectsList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AsNumber': 'asNumber',
        'Bos': 'bos',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FBit': 'fBit',
        'Ipv4NodeId': 'ipv4NodeId',
        'Ipv4Prefix': 'ipv4Prefix',
        'Ipv6NodeId': 'ipv6NodeId',
        'Ipv6Prefix': 'ipv6Prefix',
        'LocalInterfaceId': 'localInterfaceId',
        'LocalIpv4Address': 'localIpv4Address',
        'LocalIpv6Address': 'localIpv6Address',
        'LocalNodeId': 'localNodeId',
        'LooseHop': 'looseHop',
        'MplsLabel': 'mplsLabel',
        'NaiType': 'naiType',
        'Name': 'name',
        'PrefixLength': 'prefixLength',
        'RemoteInterfaceId': 'remoteInterfaceId',
        'RemoteIpv4Address': 'remoteIpv4Address',
        'RemoteIpv6Address': 'remoteIpv6Address',
        'RemoteNodeId': 'remoteNodeId',
        'Sid': 'sid',
        'SidType': 'sidType',
        'Srv6FunctionCode': 'srv6FunctionCode',
        'Srv6Identifier': 'srv6Identifier',
        'Srv6NaiType': 'srv6NaiType',
        'SubObjectType': 'subObjectType',
        'Tc': 'tc',
        'Ttl': 'ttl',
    }

    def __init__(self, parent):
        super(PcepEroSubObjectsList, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Controls whether the ERO sub-object will be sent in the PCInitiate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AsNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumber']))

    @property
    def Bos(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This bit is set to true for the last entry in the label stack i.e., for the bottom of the stack, and false for all other label stack entries. This control will be editable only if SID Type is MPLS Label 32bit.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bos']))

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
    def FBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FBit']))

    @property
    def Ipv4NodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Node ID is specified as an IPv4 address. This control can be configured if NAI Type is set to IPv4 Node ID and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NodeId']))

    @property
    def Ipv4Prefix(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Prefix is specified as an IPv4 address.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4Prefix']))

    @property
    def Ipv6NodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Node ID is specified as an IPv6 address. This control can be configured if NAI Type is set to IPv6 Node ID and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NodeId']))

    @property
    def Ipv6Prefix(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Prefix is specified as an IPv6 address.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Prefix']))

    @property
    def LocalInterfaceId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the Local Interface ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalInterfaceId']))

    @property
    def LocalIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This Control can be configured if NAI Type is set to IPv4 Adjacency and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalIpv4Address']))

    @property
    def LocalIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalIpv6Address']))

    @property
    def LocalNodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the Local Node ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalNodeId']))

    @property
    def LooseHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates if user wants to represent a loose-hop sub object in the LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LooseHop']))

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This control will be editable if the SID Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MplsLabel']))

    @property
    def NaiType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): NAI (Node or Adjacency Identifier) contains the NAI associated with the SID. Depending on the value of SID Type, the NAI can have different formats such as, Not Applicable IPv4 Node ID IPv6 Node ID IPv4 Adjacency IPv6 Adjacency Unnumbered Adjacency with IPv4 NodeIDs
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NaiType']))

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
    def PrefixLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Prefix Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def RemoteInterfaceId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the Remote Interface ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteInterfaceId']))

    @property
    def RemoteIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This Control can be configured if NAI Type is set to IPv4 Adjacency and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIpv4Address']))

    @property
    def RemoteIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIpv6Address']))

    @property
    def RemoteNodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the Remote Node ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteNodeId']))

    @property
    def Sid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SID is the Segment Identifier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sid']))

    @property
    def SidType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Using the Segment Identifier Type control user can configure whether to include SID or not and if included what is its type. Types are as follows: Null SID 20bit MPLS Label 32bit MPLS Label. If it is Null then S bit is set in the packet. Default value is 20bit MPLS Label.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidType']))

    @property
    def Srv6FunctionCode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Function Code is is the 16 bit field representing supported functions associated with SRv6 SIDs. This information is optional and included only for maintainability. Following function codes are currently defined - 0: Reserved 1: End Function 2: End.DX6 Function 3: End.DT6 Function 4: End.X Function
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6FunctionCode']))

    @property
    def Srv6Identifier(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 Identifier is the 128 bit IPv6 addresses representing SRv6 segment.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6Identifier']))

    @property
    def Srv6NaiType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The SRv6 NAI Type which indicates the interpretation for NAI (Node or Adjacency Identifier).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6NaiType']))

    @property
    def SubObjectType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: Not Applicable IPv4 Prefix IPv6 Prefix AS Number.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubObjectType']))

    @property
    def Tc(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This field is used to carry traffic class information. This control will be editable only if SID Type is MPLS Label 32bit.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Tc']))

    @property
    def Ttl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This field is used to encode a time-to-live value. This control will be editable only if SID Type is MPLS Label 32bit.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ttl']))

    def update(self, Name=None):
        """Updates pcepEroSubObjectsList resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None):
        """Finds and retrieves pcepEroSubObjectsList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pcepEroSubObjectsList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pcepEroSubObjectsList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching pcepEroSubObjectsList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pcepEroSubObjectsList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pcepEroSubObjectsList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AsNumber=None, Bos=None, FBit=None, Ipv4NodeId=None, Ipv4Prefix=None, Ipv6NodeId=None, Ipv6Prefix=None, LocalInterfaceId=None, LocalIpv4Address=None, LocalIpv6Address=None, LocalNodeId=None, LooseHop=None, MplsLabel=None, NaiType=None, PrefixLength=None, RemoteInterfaceId=None, RemoteIpv4Address=None, RemoteIpv6Address=None, RemoteNodeId=None, Sid=None, SidType=None, Srv6FunctionCode=None, Srv6Identifier=None, Srv6NaiType=None, SubObjectType=None, Tc=None, Ttl=None):
        """Base class infrastructure that gets a list of pcepEroSubObjectsList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AsNumber (str): optional regex of asNumber
        - Bos (str): optional regex of bos
        - FBit (str): optional regex of fBit
        - Ipv4NodeId (str): optional regex of ipv4NodeId
        - Ipv4Prefix (str): optional regex of ipv4Prefix
        - Ipv6NodeId (str): optional regex of ipv6NodeId
        - Ipv6Prefix (str): optional regex of ipv6Prefix
        - LocalInterfaceId (str): optional regex of localInterfaceId
        - LocalIpv4Address (str): optional regex of localIpv4Address
        - LocalIpv6Address (str): optional regex of localIpv6Address
        - LocalNodeId (str): optional regex of localNodeId
        - LooseHop (str): optional regex of looseHop
        - MplsLabel (str): optional regex of mplsLabel
        - NaiType (str): optional regex of naiType
        - PrefixLength (str): optional regex of prefixLength
        - RemoteInterfaceId (str): optional regex of remoteInterfaceId
        - RemoteIpv4Address (str): optional regex of remoteIpv4Address
        - RemoteIpv6Address (str): optional regex of remoteIpv6Address
        - RemoteNodeId (str): optional regex of remoteNodeId
        - Sid (str): optional regex of sid
        - SidType (str): optional regex of sidType
        - Srv6FunctionCode (str): optional regex of srv6FunctionCode
        - Srv6Identifier (str): optional regex of srv6Identifier
        - Srv6NaiType (str): optional regex of srv6NaiType
        - SubObjectType (str): optional regex of subObjectType
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

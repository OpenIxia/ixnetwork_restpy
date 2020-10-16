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


class PceUpdateSrEroSubObjectList(Base):
    """
    The PceUpdateSrEroSubObjectList class encapsulates a list of pceUpdateSrEroSubObjectList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateSrEroSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceUpdateSrEroSubObjectList'
    _SDM_ATT_MAP = {
        'ActiveThisEro': 'activeThisEro',
        'Bos': 'bos',
        'FBit': 'fBit',
        'Ipv4NodeId': 'ipv4NodeId',
        'Ipv6NodeId': 'ipv6NodeId',
        'LocalInterfaceId': 'localInterfaceId',
        'LocalIpv4Address': 'localIpv4Address',
        'LocalIpv6Address': 'localIpv6Address',
        'LocalNodeId': 'localNodeId',
        'LooseHop': 'looseHop',
        'MplsLabel': 'mplsLabel',
        'MplsLabel32': 'mplsLabel32',
        'NaiType': 'naiType',
        'RemoteInterfaceId': 'remoteInterfaceId',
        'RemoteIpv4Address': 'remoteIpv4Address',
        'RemoteIpv6Address': 'remoteIpv6Address',
        'RemoteNodeId': 'remoteNodeId',
        'Sid': 'sid',
        'SidType': 'sidType',
        'Tc': 'tc',
        'Ttl': 'ttl',
    }

    def __init__(self, parent):
        super(PceUpdateSrEroSubObjectList, self).__init__(parent)

    @property
    def ActiveThisEro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Controls whether the ERO sub-object will be sent in the PCInitiate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveThisEro']))

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
    def Ipv6NodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Node ID is specified as an IPv6 address. This control can be configured if NAI Type is set to IPv6 Node ID and F bit is disabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NodeId']))

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
    def MplsLabel32(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MPLS Label 32 Bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MplsLabel32']))

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

    def find(self):
        """Finds and retrieves pceUpdateSrEroSubObjectList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceUpdateSrEroSubObjectList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceUpdateSrEroSubObjectList resources from the server.

        Returns
        -------
        - self: This instance with matching pceUpdateSrEroSubObjectList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceUpdateSrEroSubObjectList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceUpdateSrEroSubObjectList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveThisEro=None, Bos=None, FBit=None, Ipv4NodeId=None, Ipv6NodeId=None, LocalInterfaceId=None, LocalIpv4Address=None, LocalIpv6Address=None, LocalNodeId=None, LooseHop=None, MplsLabel=None, MplsLabel32=None, NaiType=None, RemoteInterfaceId=None, RemoteIpv4Address=None, RemoteIpv6Address=None, RemoteNodeId=None, Sid=None, SidType=None, Tc=None, Ttl=None):
        """Base class infrastructure that gets a list of pceUpdateSrEroSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveThisEro (str): optional regex of activeThisEro
        - Bos (str): optional regex of bos
        - FBit (str): optional regex of fBit
        - Ipv4NodeId (str): optional regex of ipv4NodeId
        - Ipv6NodeId (str): optional regex of ipv6NodeId
        - LocalInterfaceId (str): optional regex of localInterfaceId
        - LocalIpv4Address (str): optional regex of localIpv4Address
        - LocalIpv6Address (str): optional regex of localIpv6Address
        - LocalNodeId (str): optional regex of localNodeId
        - LooseHop (str): optional regex of looseHop
        - MplsLabel (str): optional regex of mplsLabel
        - MplsLabel32 (str): optional regex of mplsLabel32
        - NaiType (str): optional regex of naiType
        - RemoteInterfaceId (str): optional regex of remoteInterfaceId
        - RemoteIpv4Address (str): optional regex of remoteIpv4Address
        - RemoteIpv6Address (str): optional regex of remoteIpv6Address
        - RemoteNodeId (str): optional regex of remoteNodeId
        - Sid (str): optional regex of sid
        - SidType (str): optional regex of sidType
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

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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class PccLearnedLspDb(Base):
    """PCC Learned LSPs Information Database
    The PccLearnedLspDb class encapsulates a required pccLearnedLspDb resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pccLearnedLspDb'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(PccLearnedLspDb, self).__init__(parent, list_op)

    @property
    def DestIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.destipv4address_82bc6a41b9337a2dedf7e396720959e4.DestIpv4Address): An instance of the DestIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.destipv4address_82bc6a41b9337a2dedf7e396720959e4 import DestIpv4Address
        if len(self._object_properties) > 0:
            if self._properties.get('DestIpv4Address', None) is not None:
                return self._properties.get('DestIpv4Address')
        return DestIpv4Address(self)._select()

    @property
    def DestIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.destipv6address_6333f28bd3662f5a8f83aabc7ece2d2a.DestIpv6Address): An instance of the DestIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.destipv6address_6333f28bd3662f5a8f83aabc7ece2d2a import DestIpv6Address
        if len(self._object_properties) > 0:
            if self._properties.get('DestIpv6Address', None) is not None:
                return self._properties.get('DestIpv6Address')
        return DestIpv6Address(self)._select()

    @property
    def ErrorInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.errorinfo_d1a52084750f6e3362b71d1591073670.ErrorInfo): An instance of the ErrorInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.errorinfo_d1a52084750f6e3362b71d1591073670 import ErrorInfo
        if len(self._object_properties) > 0:
            if self._properties.get('ErrorInfo', None) is not None:
                return self._properties.get('ErrorInfo')
        return ErrorInfo(self)._select()

    @property
    def IpVersion(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ipversion_f8376a4cfcc15328a4fe9a3fb44f6670.IpVersion): An instance of the IpVersion class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ipversion_f8376a4cfcc15328a4fe9a3fb44f6670 import IpVersion
        if len(self._object_properties) > 0:
            if self._properties.get('IpVersion', None) is not None:
                return self._properties.get('IpVersion')
        return IpVersion(self)._select()

    @property
    def Ipv4NodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv4nodeid_0058dcb0072bd8ec4de31da83d10b96a.Ipv4NodeId): An instance of the Ipv4NodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv4nodeid_0058dcb0072bd8ec4de31da83d10b96a import Ipv4NodeId
        if len(self._object_properties) > 0:
            if self._properties.get('Ipv4NodeId', None) is not None:
                return self._properties.get('Ipv4NodeId')
        return Ipv4NodeId(self)._select()

    @property
    def Ipv6NodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv6nodeid_4387c92ac6681abc984b1a38400183c9.Ipv6NodeId): An instance of the Ipv6NodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv6nodeid_4387c92ac6681abc984b1a38400183c9 import Ipv6NodeId
        if len(self._object_properties) > 0:
            if self._properties.get('Ipv6NodeId', None) is not None:
                return self._properties.get('Ipv6NodeId')
        return Ipv6NodeId(self)._select()

    @property
    def LearnedLspIndex(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedlspindex_c701313bed13ee8aba049d45e00b1355.LearnedLspIndex): An instance of the LearnedLspIndex class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedlspindex_c701313bed13ee8aba049d45e00b1355 import LearnedLspIndex
        if len(self._object_properties) > 0:
            if self._properties.get('LearnedLspIndex', None) is not None:
                return self._properties.get('LearnedLspIndex')
        return LearnedLspIndex(self)._select()

    @property
    def LearnedMsgDbType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedmsgdbtype_d3eeda9354841cd7f27654332e67c26b.LearnedMsgDbType): An instance of the LearnedMsgDbType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedmsgdbtype_d3eeda9354841cd7f27654332e67c26b import LearnedMsgDbType
        if len(self._object_properties) > 0:
            if self._properties.get('LearnedMsgDbType', None) is not None:
                return self._properties.get('LearnedMsgDbType')
        return LearnedMsgDbType(self)._select()

    @property
    def LocalIntefaceId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.localintefaceid_ae40044a30782cee0087b08a288efe1d.LocalIntefaceId): An instance of the LocalIntefaceId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.localintefaceid_ae40044a30782cee0087b08a288efe1d import LocalIntefaceId
        if len(self._object_properties) > 0:
            if self._properties.get('LocalIntefaceId', None) is not None:
                return self._properties.get('LocalIntefaceId')
        return LocalIntefaceId(self)._select()

    @property
    def LocalIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.localipv4address_b81d048af8b00be0fd4fded7e4d28574.LocalIpv4Address): An instance of the LocalIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.localipv4address_b81d048af8b00be0fd4fded7e4d28574 import LocalIpv4Address
        if len(self._object_properties) > 0:
            if self._properties.get('LocalIpv4Address', None) is not None:
                return self._properties.get('LocalIpv4Address')
        return LocalIpv4Address(self)._select()

    @property
    def LocalIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.localipv6address_db0b032b0167051f08ee1b875f3bb0d5.LocalIpv6Address): An instance of the LocalIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.localipv6address_db0b032b0167051f08ee1b875f3bb0d5 import LocalIpv6Address
        if len(self._object_properties) > 0:
            if self._properties.get('LocalIpv6Address', None) is not None:
                return self._properties.get('LocalIpv6Address')
        return LocalIpv6Address(self)._select()

    @property
    def LocalNodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.localnodeid_a2150e20db7b7e8a73277c2b4581702d.LocalNodeId): An instance of the LocalNodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.localnodeid_a2150e20db7b7e8a73277c2b4581702d import LocalNodeId
        if len(self._object_properties) > 0:
            if self._properties.get('LocalNodeId', None) is not None:
                return self._properties.get('LocalNodeId')
        return LocalNodeId(self)._select()

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.mplslabel_f0b733862256902b721f5de4e5a0c542.MplsLabel): An instance of the MplsLabel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.mplslabel_f0b733862256902b721f5de4e5a0c542 import MplsLabel
        if len(self._object_properties) > 0:
            if self._properties.get('MplsLabel', None) is not None:
                return self._properties.get('MplsLabel')
        return MplsLabel(self)._select()

    @property
    def NaiType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.naitype_53c2cdf91ca50e9351d06a63484d2cf1.NaiType): An instance of the NaiType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.naitype_53c2cdf91ca50e9351d06a63484d2cf1 import NaiType
        if len(self._object_properties) > 0:
            if self._properties.get('NaiType', None) is not None:
                return self._properties.get('NaiType')
        return NaiType(self)._select()

    @property
    def PlspId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.plspid_051d75d17e1fb1b13dc5de62dda1109d.PlspId): An instance of the PlspId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.plspid_051d75d17e1fb1b13dc5de62dda1109d import PlspId
        if len(self._object_properties) > 0:
            if self._properties.get('PlspId', None) is not None:
                return self._properties.get('PlspId')
        return PlspId(self)._select()

    @property
    def RemoteInterfaceId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.remoteinterfaceid_c8d71be034f0bce6f7e7fee6fc575d5a.RemoteInterfaceId): An instance of the RemoteInterfaceId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.remoteinterfaceid_c8d71be034f0bce6f7e7fee6fc575d5a import RemoteInterfaceId
        if len(self._object_properties) > 0:
            if self._properties.get('RemoteInterfaceId', None) is not None:
                return self._properties.get('RemoteInterfaceId')
        return RemoteInterfaceId(self)._select()

    @property
    def RemoteIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.remoteipv4address_ce13915019bdc07322aaeadd4f34e428.RemoteIpv4Address): An instance of the RemoteIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.remoteipv4address_ce13915019bdc07322aaeadd4f34e428 import RemoteIpv4Address
        if len(self._object_properties) > 0:
            if self._properties.get('RemoteIpv4Address', None) is not None:
                return self._properties.get('RemoteIpv4Address')
        return RemoteIpv4Address(self)._select()

    @property
    def RemoteIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.remoteipv6address_4387d585717913933b818a169b61aa59.RemoteIpv6Address): An instance of the RemoteIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.remoteipv6address_4387d585717913933b818a169b61aa59 import RemoteIpv6Address
        if len(self._object_properties) > 0:
            if self._properties.get('RemoteIpv6Address', None) is not None:
                return self._properties.get('RemoteIpv6Address')
        return RemoteIpv6Address(self)._select()

    @property
    def RemoteNodeId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.remotenodeid_26967b9b8d67f080911a80d276776a63.RemoteNodeId): An instance of the RemoteNodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.remotenodeid_26967b9b8d67f080911a80d276776a63 import RemoteNodeId
        if len(self._object_properties) > 0:
            if self._properties.get('RemoteNodeId', None) is not None:
                return self._properties.get('RemoteNodeId')
        return RemoteNodeId(self)._select()

    @property
    def RequestId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.requestid_4bb823de2302ea46c48b53652c8059b5.RequestId): An instance of the RequestId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.requestid_4bb823de2302ea46c48b53652c8059b5 import RequestId
        if len(self._object_properties) > 0:
            if self._properties.get('RequestId', None) is not None:
                return self._properties.get('RequestId')
        return RequestId(self)._select()

    @property
    def Sid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.sid_8c2f535b036e46b302b17150b1058608.Sid): An instance of the Sid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.sid_8c2f535b036e46b302b17150b1058608 import Sid
        if len(self._object_properties) > 0:
            if self._properties.get('Sid', None) is not None:
                return self._properties.get('Sid')
        return Sid(self)._select()

    @property
    def SidType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.sidtype_579b966f4e4c3d833da37f5f97dc08ee.SidType): An instance of the SidType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.sidtype_579b966f4e4c3d833da37f5f97dc08ee import SidType
        if len(self._object_properties) > 0:
            if self._properties.get('SidType', None) is not None:
                return self._properties.get('SidType')
        return SidType(self)._select()

    @property
    def SourceIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.sourceipv4address_707bf2f3cc4230a0651eaf5afdefe498.SourceIpv4Address): An instance of the SourceIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.sourceipv4address_707bf2f3cc4230a0651eaf5afdefe498 import SourceIpv4Address
        if len(self._object_properties) > 0:
            if self._properties.get('SourceIpv4Address', None) is not None:
                return self._properties.get('SourceIpv4Address')
        return SourceIpv4Address(self)._select()

    @property
    def SourceIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.sourceipv6address_37f328eecbea00714a96da2c073f4428.SourceIpv6Address): An instance of the SourceIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.sourceipv6address_37f328eecbea00714a96da2c073f4428 import SourceIpv6Address
        if len(self._object_properties) > 0:
            if self._properties.get('SourceIpv6Address', None) is not None:
                return self._properties.get('SourceIpv6Address')
        return SourceIpv6Address(self)._select()

    @property
    def SymbolicPathName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.symbolicpathname_ed1c62d2f4f0680292dada315970feea.SymbolicPathName): An instance of the SymbolicPathName class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.symbolicpathname_ed1c62d2f4f0680292dada315970feea import SymbolicPathName
        if len(self._object_properties) > 0:
            if self._properties.get('SymbolicPathName', None) is not None:
                return self._properties.get('SymbolicPathName')
        return SymbolicPathName(self)._select()

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Name=None):
        # type: (str) -> PccLearnedLspDb
        """Updates pccLearnedLspDb resource on the server.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> PccLearnedLspDb
        """Finds and retrieves pccLearnedLspDb resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pccLearnedLspDb resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pccLearnedLspDb resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching pccLearnedLspDb resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pccLearnedLspDb data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pccLearnedLspDb resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

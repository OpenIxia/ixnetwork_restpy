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


class PccLearnedLspDb(Base):
    """PCC Learned LSPs Information Database
    The PccLearnedLspDb class encapsulates a required pccLearnedLspDb resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pccLearnedLspDb'

    def __init__(self, parent):
        super(PccLearnedLspDb, self).__init__(parent)

    @property
    def DestIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.destipv4address.DestIpv4Address): An instance of the DestIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.destipv4address import DestIpv4Address
        return DestIpv4Address(self)._select()

    @property
    def DestIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.destipv6address.DestIpv6Address): An instance of the DestIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.destipv6address import DestIpv6Address
        return DestIpv6Address(self)._select()

    @property
    def ErrorInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.errorinfo.ErrorInfo): An instance of the ErrorInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.errorinfo import ErrorInfo
        return ErrorInfo(self)._select()

    @property
    def IpVersion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipversion.IpVersion): An instance of the IpVersion class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipversion import IpVersion
        return IpVersion(self)._select()

    @property
    def Ipv4NodeId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4nodeid.Ipv4NodeId): An instance of the Ipv4NodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4nodeid import Ipv4NodeId
        return Ipv4NodeId(self)._select()

    @property
    def Ipv6NodeId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6nodeid.Ipv6NodeId): An instance of the Ipv6NodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6nodeid import Ipv6NodeId
        return Ipv6NodeId(self)._select()

    @property
    def LearnedLspIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedlspindex.LearnedLspIndex): An instance of the LearnedLspIndex class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedlspindex import LearnedLspIndex
        return LearnedLspIndex(self)._select()

    @property
    def LearnedMsgDbType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedmsgdbtype.LearnedMsgDbType): An instance of the LearnedMsgDbType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedmsgdbtype import LearnedMsgDbType
        return LearnedMsgDbType(self)._select()

    @property
    def LocalIntefaceId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localintefaceid.LocalIntefaceId): An instance of the LocalIntefaceId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localintefaceid import LocalIntefaceId
        return LocalIntefaceId(self)._select()

    @property
    def LocalIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localipv4address.LocalIpv4Address): An instance of the LocalIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localipv4address import LocalIpv4Address
        return LocalIpv4Address(self)._select()

    @property
    def LocalIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localipv6address.LocalIpv6Address): An instance of the LocalIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localipv6address import LocalIpv6Address
        return LocalIpv6Address(self)._select()

    @property
    def LocalNodeId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localnodeid.LocalNodeId): An instance of the LocalNodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.localnodeid import LocalNodeId
        return LocalNodeId(self)._select()

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplslabel.MplsLabel): An instance of the MplsLabel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplslabel import MplsLabel
        return MplsLabel(self)._select()

    @property
    def PlspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.plspid.PlspId): An instance of the PlspId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.plspid import PlspId
        return PlspId(self)._select()

    @property
    def RemoteInterfaceId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remoteinterfaceid.RemoteInterfaceId): An instance of the RemoteInterfaceId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remoteinterfaceid import RemoteInterfaceId
        return RemoteInterfaceId(self)._select()

    @property
    def RemoteIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remoteipv4address.RemoteIpv4Address): An instance of the RemoteIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remoteipv4address import RemoteIpv4Address
        return RemoteIpv4Address(self)._select()

    @property
    def RemoteIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remoteipv6address.RemoteIpv6Address): An instance of the RemoteIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remoteipv6address import RemoteIpv6Address
        return RemoteIpv6Address(self)._select()

    @property
    def RemoteNodeId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remotenodeid.RemoteNodeId): An instance of the RemoteNodeId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.remotenodeid import RemoteNodeId
        return RemoteNodeId(self)._select()

    @property
    def RequestId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.requestid.RequestId): An instance of the RequestId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.requestid import RequestId
        return RequestId(self)._select()

    @property
    def Sid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sid.Sid): An instance of the Sid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sid import Sid
        return Sid(self)._select()

    @property
    def SidType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sidtype.SidType): An instance of the SidType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sidtype import SidType
        return SidType(self)._select()

    @property
    def SidType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sidtype.SidType): An instance of the SidType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sidtype import SidType
        return SidType(self)._select()

    @property
    def SourceIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sourceipv4address.SourceIpv4Address): An instance of the SourceIpv4Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sourceipv4address import SourceIpv4Address
        return SourceIpv4Address(self)._select()

    @property
    def SourceIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sourceipv6address.SourceIpv6Address): An instance of the SourceIpv6Address class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sourceipv6address import SourceIpv6Address
        return SourceIpv6Address(self)._select()

    @property
    def SymbolicPathName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.symbolicpathname.SymbolicPathName): An instance of the SymbolicPathName class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.symbolicpathname import SymbolicPathName
        return SymbolicPathName(self)._select()

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    def update(self, Name=None):
        """Updates pccLearnedLspDb resource on the server.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

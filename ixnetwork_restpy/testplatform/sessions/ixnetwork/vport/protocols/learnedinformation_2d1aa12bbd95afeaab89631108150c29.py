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


class LearnedInformation(Base):
    """The ISISL2/L3 Learned Information option fetches and shows the information learned by ISIS.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInformation'

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def Ipv4Multicast(self):
        """An instance of the Ipv4Multicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_bcb51ecb4be120e340e6db69c054d9e4.Ipv4Multicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_bcb51ecb4be120e340e6db69c054d9e4 import Ipv4Multicast
        return Ipv4Multicast(self)

    @property
    def Ipv4Prefixes(self):
        """An instance of the Ipv4Prefixes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_24b107d33fa9185991e698d4a7924ad8.Ipv4Prefixes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_24b107d33fa9185991e698d4a7924ad8 import Ipv4Prefixes
        return Ipv4Prefixes(self)

    @property
    def Ipv6Multicast(self):
        """An instance of the Ipv6Multicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_37ea0a85dd55049c28cde943a8e8127c.Ipv6Multicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_37ea0a85dd55049c28cde943a8e8127c import Ipv6Multicast
        return Ipv6Multicast(self)

    @property
    def Ipv6Prefixes(self):
        """An instance of the Ipv6Prefixes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_7ce1da3b3781885289e17d9c53c826fe.Ipv6Prefixes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_7ce1da3b3781885289e17d9c53c826fe import Ipv6Prefixes
        return Ipv6Prefixes(self)

    @property
    def MacMulticast(self):
        """An instance of the MacMulticast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_806a2d0b9628b3391d0c73f48b313a5c.MacMulticast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_806a2d0b9628b3391d0c73f48b313a5c import MacMulticast
        return MacMulticast(self)

    @property
    def RBridges(self):
        """An instance of the RBridges class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_88b46433c1a36dbc302403b28c40ebda.RBridges)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_88b46433c1a36dbc302403b28c40ebda import RBridges
        return RBridges(self)

    @property
    def SpbRbridges(self):
        """An instance of the SpbRbridges class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_dcb0b1dd5750ac01fc1e15cffc6ec5b0.SpbRbridges)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_dcb0b1dd5750ac01fc1e15cffc6ec5b0 import SpbRbridges
        return SpbRbridges(self)

    @property
    def TrillMacUnicast(self):
        """An instance of the TrillMacUnicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_c1b6220b293b815f476300e9d2db6caf.TrillMacUnicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_c1b6220b293b815f476300e9d2db6caf import TrillMacUnicast
        return TrillMacUnicast(self)

    @property
    def TrillOamPing(self):
        """An instance of the TrillOamPing class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_58069223eb1b548f5e6bff7d253f087e.TrillOamPing)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_58069223eb1b548f5e6bff7d253f087e import TrillOamPing
        return TrillOamPing(self)

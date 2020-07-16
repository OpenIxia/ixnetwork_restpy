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


class LearnedInformation(Base):
    """The ISISL2/L3 Learned Information option fetches and shows the information learned by ISIS.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInformation'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def Ipv4Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_10a4379979b6506eb349de25887e2e38.Ipv4Multicast): An instance of the Ipv4Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_10a4379979b6506eb349de25887e2e38 import Ipv4Multicast
        return Ipv4Multicast(self)

    @property
    def Ipv4Prefixes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_9a3bf961681bc0cbf455302154b26917.Ipv4Prefixes): An instance of the Ipv4Prefixes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_9a3bf961681bc0cbf455302154b26917 import Ipv4Prefixes
        return Ipv4Prefixes(self)

    @property
    def Ipv6Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_e5e209725397b0a0f784d398f082eda0.Ipv6Multicast): An instance of the Ipv6Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_e5e209725397b0a0f784d398f082eda0 import Ipv6Multicast
        return Ipv6Multicast(self)

    @property
    def Ipv6Prefixes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_c177f4d9bea9094ba2cc6f15470cd1b2.Ipv6Prefixes): An instance of the Ipv6Prefixes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_c177f4d9bea9094ba2cc6f15470cd1b2 import Ipv6Prefixes
        return Ipv6Prefixes(self)

    @property
    def MacMulticast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_4657479088be8ae0ce145407826c2664.MacMulticast): An instance of the MacMulticast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_4657479088be8ae0ce145407826c2664 import MacMulticast
        return MacMulticast(self)

    @property
    def RBridges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_5ce66d3e71a71da81c831e5004a9dcd9.RBridges): An instance of the RBridges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_5ce66d3e71a71da81c831e5004a9dcd9 import RBridges
        return RBridges(self)

    @property
    def SpbRbridges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_e17c520e3dfc11aba98087bf23532644.SpbRbridges): An instance of the SpbRbridges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_e17c520e3dfc11aba98087bf23532644 import SpbRbridges
        return SpbRbridges(self)

    @property
    def TrillMacUnicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_efd8df32a1caa34df792e44c556fcdd5.TrillMacUnicast): An instance of the TrillMacUnicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_efd8df32a1caa34df792e44c556fcdd5 import TrillMacUnicast
        return TrillMacUnicast(self)

    @property
    def TrillOamPing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_094ce4fc14cf8066982dbcc3c0c11845.TrillOamPing): An instance of the TrillOamPing class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_094ce4fc14cf8066982dbcc3c0c11845 import TrillOamPing
        return TrillOamPing(self)

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


class Protocols(Base):
    """Allows the user to select a set of protocols that are enabled for a newly added port.
    The Protocols class encapsulates a list of protocols resources that is managed by the system.
    A list of resources can be retrieved from the server using the Protocols.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'protocols'

    def __init__(self, parent):
        super(Protocols, self).__init__(parent)

    @property
    def Arp(self):
        """An instance of the Arp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_4fee329103832d33634d1078aa4a0310.Arp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_4fee329103832d33634d1078aa4a0310 import Arp
        return Arp(self)

    @property
    def Bfd(self):
        """An instance of the Bfd class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_e23ab09912a2ef91e2ded2720f525774.Bfd)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_e23ab09912a2ef91e2ded2720f525774 import Bfd
        return Bfd(self)._select()

    @property
    def Bgp(self):
        """An instance of the Bgp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_0e8a1570b831f6d92cd7ed1a8442257b.Bgp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_0e8a1570b831f6d92cd7ed1a8442257b import Bgp
        return Bgp(self)._select()

    @property
    def Cfm(self):
        """An instance of the Cfm class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_c1742b75736db9d1da0fb731317ab337.Cfm)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_c1742b75736db9d1da0fb731317ab337 import Cfm
        return Cfm(self)._select()

    @property
    def Eigrp(self):
        """An instance of the Eigrp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_6949e2b033460aaef78ccb1fa44a7ab4.Eigrp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_6949e2b033460aaef78ccb1fa44a7ab4 import Eigrp
        return Eigrp(self)._select()

    @property
    def Elmi(self):
        """An instance of the Elmi class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_de57cbdbc7817247497259f99ad1071f.Elmi)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_de57cbdbc7817247497259f99ad1071f import Elmi
        return Elmi(self)._select()

    @property
    def Igmp(self):
        """An instance of the Igmp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_97e223b0e4a22ccebe603523da1eea72.Igmp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_97e223b0e4a22ccebe603523da1eea72 import Igmp
        return Igmp(self)._select()

    @property
    def Isis(self):
        """An instance of the Isis class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_29ce49fd418e8cbafce46cc31d9c2c49.Isis)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_29ce49fd418e8cbafce46cc31d9c2c49 import Isis
        return Isis(self)._select()

    @property
    def Lacp(self):
        """An instance of the Lacp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_68f2c8c0edab1d36491ddbc7d38749a9.Lacp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_68f2c8c0edab1d36491ddbc7d38749a9 import Lacp
        return Lacp(self)._select()

    @property
    def Ldp(self):
        """An instance of the Ldp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_ebb85dc5fabc8c5084139b88b2c606bb.Ldp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_ebb85dc5fabc8c5084139b88b2c606bb import Ldp
        return Ldp(self)._select()

    @property
    def LinkOam(self):
        """An instance of the LinkOam class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_818ab0363cf206da8ed88b16971f57ad.LinkOam)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_818ab0363cf206da8ed88b16971f57ad import LinkOam
        return LinkOam(self)._select()

    @property
    def Lisp(self):
        """An instance of the Lisp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_d301cfea7233ed11239d812f92e92eb2.Lisp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_d301cfea7233ed11239d812f92e92eb2 import Lisp
        return Lisp(self)._select()

    @property
    def Mld(self):
        """An instance of the Mld class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_1265ede4da37798141cbe0c7663d6baf.Mld)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_1265ede4da37798141cbe0c7663d6baf import Mld
        return Mld(self)._select()

    @property
    def MplsOam(self):
        """An instance of the MplsOam class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_b9d0135a0213e9f8f0788c2977da02f1.MplsOam)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_b9d0135a0213e9f8f0788c2977da02f1 import MplsOam
        return MplsOam(self)._select()

    @property
    def MplsTp(self):
        """An instance of the MplsTp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_bbaf10c4b7d4a48cf2e24e573b52dff7.MplsTp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_bbaf10c4b7d4a48cf2e24e573b52dff7 import MplsTp
        return MplsTp(self)._select()

    @property
    def OpenFlow(self):
        """An instance of the OpenFlow class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_1359f2d189d73f1cb1204f83bd22ec2d.OpenFlow)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_1359f2d189d73f1cb1204f83bd22ec2d import OpenFlow
        return OpenFlow(self)._select()

    @property
    def Ospf(self):
        """An instance of the Ospf class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_41d7626c630d7a6559bcd053aa7e500e.Ospf)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_41d7626c630d7a6559bcd053aa7e500e import Ospf
        return Ospf(self)._select()

    @property
    def OspfV3(self):
        """An instance of the OspfV3 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_05c8bf0b9b983dc682c0862ff2aced73.OspfV3)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_05c8bf0b9b983dc682c0862ff2aced73 import OspfV3
        return OspfV3(self)._select()

    @property
    def Pimsm(self):
        """An instance of the Pimsm class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_82b0a1932030387a2e02e3ac4c4b4b4f.Pimsm)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_82b0a1932030387a2e02e3ac4c4b4b4f import Pimsm
        return Pimsm(self)._select()

    @property
    def Ping(self):
        """An instance of the Ping class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_66825393e94292078b55be3ee95ac5c4.Ping)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_66825393e94292078b55be3ee95ac5c4 import Ping
        return Ping(self)

    @property
    def Rip(self):
        """An instance of the Rip class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_2af6cc81c0016359731788b96d21a306.Rip)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_2af6cc81c0016359731788b96d21a306 import Rip
        return Rip(self)._select()

    @property
    def Ripng(self):
        """An instance of the Ripng class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_1d16516d9110a83b1d310b4a1523fbf7.Ripng)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_1d16516d9110a83b1d310b4a1523fbf7 import Ripng
        return Ripng(self)._select()

    @property
    def Rsvp(self):
        """An instance of the Rsvp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_a2c25e4facabe86f4f47a1790af24f9f.Rsvp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_a2c25e4facabe86f4f47a1790af24f9f import Rsvp
        return Rsvp(self)._select()

    @property
    def Static(self):
        """An instance of the Static class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_e25e6f710e8423e8461ee5383ae00065.Static)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_e25e6f710e8423e8461ee5383ae00065 import Static
        return Static(self)._select()

    @property
    def Stp(self):
        """An instance of the Stp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_4b39b48c36395c2f6a8db957f0f6f7c5.Stp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_4b39b48c36395c2f6a8db957f0f6f7c5 import Stp
        return Stp(self)._select()

    @property
    def ProtocolMaxNodeCount(self):
        """Shows maximum number of node.

        Returns:
            number
        """
        return self._get_attribute('protocolMaxNodeCount')

    def find(self, ProtocolMaxNodeCount=None):
        """Finds and retrieves protocols data from the server.

        All named parameters support regex and can be used to selectively retrieve protocols data from the server.
        By default the find method takes no parameters and will retrieve all protocols data from the server.

        Args:
            ProtocolMaxNodeCount (number): Shows maximum number of node.

        Returns:
            self: This instance with matching protocols data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of protocols data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the protocols data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class Protocols(Base):
    """Allows the user to select a set of protocols that are enabled for a newly added port.
    The Protocols class encapsulates a list of protocols resources that are managed by the system.
    A list of resources can be retrieved from the server using the Protocols.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'protocols'
    _SDM_ATT_MAP = {
        'ProtocolMaxNodeCount': 'protocolMaxNodeCount',
    }

    def __init__(self, parent):
        super(Protocols, self).__init__(parent)

    @property
    def Arp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_067eba21ef07a3fc09f15f554aa27f62.Arp): An instance of the Arp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_067eba21ef07a3fc09f15f554aa27f62 import Arp
        return Arp(self)

    @property
    def Bfd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_13635869671ecd9754ea8412fc59454e.Bfd): An instance of the Bfd class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_13635869671ecd9754ea8412fc59454e import Bfd
        return Bfd(self)._select()

    @property
    def Bgp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_3e6d8e0b1b17db8a0c58ab51996aae2b.Bgp): An instance of the Bgp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_3e6d8e0b1b17db8a0c58ab51996aae2b import Bgp
        return Bgp(self)._select()

    @property
    def Cfm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_f86ba26f5f0b238d459dfdf495bb75c0.Cfm): An instance of the Cfm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_f86ba26f5f0b238d459dfdf495bb75c0 import Cfm
        return Cfm(self)._select()

    @property
    def Eigrp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_87f33acf176dcbe78849cf8e8791c70d.Eigrp): An instance of the Eigrp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_87f33acf176dcbe78849cf8e8791c70d import Eigrp
        return Eigrp(self)._select()

    @property
    def Elmi(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_701893b9b99429bda254793bfb384df2.Elmi): An instance of the Elmi class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_701893b9b99429bda254793bfb384df2 import Elmi
        return Elmi(self)._select()

    @property
    def Igmp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_5181803aa94412c9279b9f387c23a716.Igmp): An instance of the Igmp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_5181803aa94412c9279b9f387c23a716 import Igmp
        return Igmp(self)._select()

    @property
    def Isis(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_050bb4482a1df0a3d61c7b64496e330d.Isis): An instance of the Isis class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_050bb4482a1df0a3d61c7b64496e330d import Isis
        return Isis(self)._select()

    @property
    def Lacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_2de629e1f1c006bff7fad33825e4d91b.Lacp): An instance of the Lacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_2de629e1f1c006bff7fad33825e4d91b import Lacp
        return Lacp(self)._select()

    @property
    def Ldp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_da338dbe787e89d2068f6bd186367c37.Ldp): An instance of the Ldp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_da338dbe787e89d2068f6bd186367c37 import Ldp
        return Ldp(self)._select()

    @property
    def LinkOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_efc27e762f17d4ddecbc0652ec4c7ac4.LinkOam): An instance of the LinkOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_efc27e762f17d4ddecbc0652ec4c7ac4 import LinkOam
        return LinkOam(self)._select()

    @property
    def Lisp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_cfcf8310ab534e86e05d76bfc192cb8f.Lisp): An instance of the Lisp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_cfcf8310ab534e86e05d76bfc192cb8f import Lisp
        return Lisp(self)._select()

    @property
    def Mld(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_addc243f110a2e6cdaa60cfde19d5efe.Mld): An instance of the Mld class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_addc243f110a2e6cdaa60cfde19d5efe import Mld
        return Mld(self)._select()

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_e3ac69344e2bf92870f02216ee81dec3.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_e3ac69344e2bf92870f02216ee81dec3 import MplsOam
        return MplsOam(self)._select()

    @property
    def MplsTp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_8fb90eb694dc0efb0ff6a231453357c5.MplsTp): An instance of the MplsTp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_8fb90eb694dc0efb0ff6a231453357c5 import MplsTp
        return MplsTp(self)._select()

    @property
    def OpenFlow(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_81b0892fb793919c2b8ec714a09eb3dc.OpenFlow): An instance of the OpenFlow class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_81b0892fb793919c2b8ec714a09eb3dc import OpenFlow
        return OpenFlow(self)._select()

    @property
    def Ospf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_e7cbc892bf16b0ebe7b056298a38b949.Ospf): An instance of the Ospf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_e7cbc892bf16b0ebe7b056298a38b949 import Ospf
        return Ospf(self)._select()

    @property
    def OspfV3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_fd46b6ab89f8ad7a237ac12140f8a863.OspfV3): An instance of the OspfV3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_fd46b6ab89f8ad7a237ac12140f8a863 import OspfV3
        return OspfV3(self)._select()

    @property
    def Pimsm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_5b2c0eab6298f36b1362558022b2d248.Pimsm): An instance of the Pimsm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_5b2c0eab6298f36b1362558022b2d248 import Pimsm
        return Pimsm(self)._select()

    @property
    def Ping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_95a393f5ad3a6b0c563501c39f382cae.Ping): An instance of the Ping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_95a393f5ad3a6b0c563501c39f382cae import Ping
        return Ping(self)

    @property
    def Rip(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_e819d24fd3ca51fc2aa4d2bb9ad9b9e2.Rip): An instance of the Rip class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_e819d24fd3ca51fc2aa4d2bb9ad9b9e2 import Rip
        return Rip(self)._select()

    @property
    def Ripng(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_ba15454897784b789bbbbfa92adc4ccd.Ripng): An instance of the Ripng class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_ba15454897784b789bbbbfa92adc4ccd import Ripng
        return Ripng(self)._select()

    @property
    def Rsvp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_1a88cb229a9aae7ce8ea61139e8fb910.Rsvp): An instance of the Rsvp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_1a88cb229a9aae7ce8ea61139e8fb910 import Rsvp
        return Rsvp(self)._select()

    @property
    def Static(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_5795de030fada71c167436cb330786b5.Static): An instance of the Static class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_5795de030fada71c167436cb330786b5 import Static
        return Static(self)._select()

    @property
    def Stp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_af850ad90f47656e0033090898ef0f0c.Stp): An instance of the Stp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_af850ad90f47656e0033090898ef0f0c import Stp
        return Stp(self)._select()

    @property
    def ProtocolMaxNodeCount(self):
        """
        Returns
        -------
        - number: Shows maximum number of node.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolMaxNodeCount'])

    def find(self, ProtocolMaxNodeCount=None):
        """Finds and retrieves protocols resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve protocols resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all protocols resources from the server.

        Args
        ----
        - ProtocolMaxNodeCount (number): Shows maximum number of node.

        Returns
        -------
        - self: This instance with matching protocols resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of protocols data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the protocols resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

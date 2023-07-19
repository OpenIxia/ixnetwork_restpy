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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Protocols(Base):
    """Allows the user to select a set of protocols that are enabled for a newly added port.
    The Protocols class encapsulates a list of protocols resources that are managed by the system.
    A list of resources can be retrieved from the server using the Protocols.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "protocols"
    _SDM_ATT_MAP = {
        "ProtocolMaxNodeCount": "protocolMaxNodeCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Protocols, self).__init__(parent, list_op)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_067eba21ef07a3fc09f15f554aa27f62 import (
            Arp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Arp", None) is not None:
                return self._properties.get("Arp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_13635869671ecd9754ea8412fc59454e import (
            Bfd,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bfd", None) is not None:
                return self._properties.get("Bfd")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_3e6d8e0b1b17db8a0c58ab51996aae2b import (
            Bgp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bgp", None) is not None:
                return self._properties.get("Bgp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_f86ba26f5f0b238d459dfdf495bb75c0 import (
            Cfm,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Cfm", None) is not None:
                return self._properties.get("Cfm")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_87f33acf176dcbe78849cf8e8791c70d import (
            Eigrp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Eigrp", None) is not None:
                return self._properties.get("Eigrp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_701893b9b99429bda254793bfb384df2 import (
            Elmi,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Elmi", None) is not None:
                return self._properties.get("Elmi")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_5181803aa94412c9279b9f387c23a716 import (
            Igmp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Igmp", None) is not None:
                return self._properties.get("Igmp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_050bb4482a1df0a3d61c7b64496e330d import (
            Isis,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Isis", None) is not None:
                return self._properties.get("Isis")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_2de629e1f1c006bff7fad33825e4d91b import (
            Lacp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lacp", None) is not None:
                return self._properties.get("Lacp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_da338dbe787e89d2068f6bd186367c37 import (
            Ldp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ldp", None) is not None:
                return self._properties.get("Ldp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_efc27e762f17d4ddecbc0652ec4c7ac4 import (
            LinkOam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LinkOam", None) is not None:
                return self._properties.get("LinkOam")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_cfcf8310ab534e86e05d76bfc192cb8f import (
            Lisp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lisp", None) is not None:
                return self._properties.get("Lisp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_addc243f110a2e6cdaa60cfde19d5efe import (
            Mld,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Mld", None) is not None:
                return self._properties.get("Mld")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_e3ac69344e2bf92870f02216ee81dec3 import (
            MplsOam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MplsOam", None) is not None:
                return self._properties.get("MplsOam")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_8fb90eb694dc0efb0ff6a231453357c5 import (
            MplsTp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MplsTp", None) is not None:
                return self._properties.get("MplsTp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_81b0892fb793919c2b8ec714a09eb3dc import (
            OpenFlow,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlow", None) is not None:
                return self._properties.get("OpenFlow")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_e7cbc892bf16b0ebe7b056298a38b949 import (
            Ospf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospf", None) is not None:
                return self._properties.get("Ospf")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_fd46b6ab89f8ad7a237ac12140f8a863 import (
            OspfV3,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OspfV3", None) is not None:
                return self._properties.get("OspfV3")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_5b2c0eab6298f36b1362558022b2d248 import (
            Pimsm,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pimsm", None) is not None:
                return self._properties.get("Pimsm")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_95a393f5ad3a6b0c563501c39f382cae import (
            Ping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ping", None) is not None:
                return self._properties.get("Ping")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_e819d24fd3ca51fc2aa4d2bb9ad9b9e2 import (
            Rip,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rip", None) is not None:
                return self._properties.get("Rip")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_ba15454897784b789bbbbfa92adc4ccd import (
            Ripng,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ripng", None) is not None:
                return self._properties.get("Ripng")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_1a88cb229a9aae7ce8ea61139e8fb910 import (
            Rsvp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rsvp", None) is not None:
                return self._properties.get("Rsvp")
        return Rsvp(self)._select()

    @property
    def Static(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_e79f48c67dc04c4349a4bfc7549f0778.Static): An instance of the Static class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_e79f48c67dc04c4349a4bfc7549f0778 import (
            Static,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Static", None) is not None:
                return self._properties.get("Static")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_af850ad90f47656e0033090898ef0f0c import (
            Stp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Stp", None) is not None:
                return self._properties.get("Stp")
        return Stp(self)._select()

    @property
    def ProtocolMaxNodeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Shows maximum number of node.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolMaxNodeCount"])

    def add(self):
        """Adds a new protocols resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved protocols resources using find and the newly added protocols resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ProtocolMaxNodeCount=None):
        # type: (int) -> Protocols
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

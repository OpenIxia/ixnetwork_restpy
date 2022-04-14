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


class ProtocolStack(Base):
    """PortGroup represents the concept of a stack of layers which are to be configured on a group of ports.
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "protocolStack"
    _SDM_ATT_MAP = {
        "ObjectId": "objectId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ProtocolStack, self).__init__(parent, list_op)

    @property
    def AmtOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_b8687d0aa450eedabad5937a3dd0d921.AmtOptions): An instance of the AmtOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_b8687d0aa450eedabad5937a3dd0d921 import (
            AmtOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AmtOptions", None) is not None:
                return self._properties.get("AmtOptions")
        return AmtOptions(self)

    @property
    def AncpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_60d2d5e33cccc1428aa5ab66090e545f.AncpOptions): An instance of the AncpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_60d2d5e33cccc1428aa5ab66090e545f import (
            AncpOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AncpOptions", None) is not None:
                return self._properties.get("AncpOptions")
        return AncpOptions(self)

    @property
    def DhcpHostsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_191fedb8ef50cd521c12d7ded5cc3bc5.DhcpHostsOptions): An instance of the DhcpHostsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_191fedb8ef50cd521c12d7ded5cc3bc5 import (
            DhcpHostsOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpHostsOptions", None) is not None:
                return self._properties.get("DhcpHostsOptions")
        return DhcpHostsOptions(self)

    @property
    def DhcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_9729e8bd162874e29097793e120e81b6.DhcpOptions): An instance of the DhcpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_9729e8bd162874e29097793e120e81b6 import (
            DhcpOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpOptions", None) is not None:
                return self._properties.get("DhcpOptions")
        return DhcpOptions(self)

    @property
    def Dhcpv6ClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_132f5e3e6310e86ccbbac482ccd94671.Dhcpv6ClientOptions): An instance of the Dhcpv6ClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_132f5e3e6310e86ccbbac482ccd94671 import (
            Dhcpv6ClientOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6ClientOptions", None) is not None:
                return self._properties.get("Dhcpv6ClientOptions")
        return Dhcpv6ClientOptions(self)

    @property
    def Dhcpv6PdClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_bd222f1628f075889e823bc4a6e1f541.Dhcpv6PdClientOptions): An instance of the Dhcpv6PdClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_bd222f1628f075889e823bc4a6e1f541 import (
            Dhcpv6PdClientOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6PdClientOptions", None) is not None:
                return self._properties.get("Dhcpv6PdClientOptions")
        return Dhcpv6PdClientOptions(self)

    @property
    def Dhcpv6ServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_53ee0b2472ff273e656afeded14cc6a7.Dhcpv6ServerOptions): An instance of the Dhcpv6ServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_53ee0b2472ff273e656afeded14cc6a7 import (
            Dhcpv6ServerOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6ServerOptions", None) is not None:
                return self._properties.get("Dhcpv6ServerOptions")
        return Dhcpv6ServerOptions(self)

    @property
    def Dot1xOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_c27d674f9a6209c0c34607209e0a9bac.Dot1xOptions): An instance of the Dot1xOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_c27d674f9a6209c0c34607209e0a9bac import (
            Dot1xOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dot1xOptions", None) is not None:
                return self._properties.get("Dot1xOptions")
        return Dot1xOptions(self)

    @property
    def EapoUdpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_f04b43d99a8c8e63cc9e7d622d06bfd6.EapoUdpOptions): An instance of the EapoUdpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_f04b43d99a8c8e63cc9e7d622d06bfd6 import (
            EapoUdpOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EapoUdpOptions", None) is not None:
                return self._properties.get("EapoUdpOptions")
        return EapoUdpOptions(self)

    @property
    def EgtpClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_31e0757ccf11d7e1c6855fdd46442542.EgtpClientOptions): An instance of the EgtpClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_31e0757ccf11d7e1c6855fdd46442542 import (
            EgtpClientOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgtpClientOptions", None) is not None:
                return self._properties.get("EgtpClientOptions")
        return EgtpClientOptions(self)

    @property
    def EgtpOptionsBase(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_32e4941bfba82166b4f883cdd51ee159.EgtpOptionsBase): An instance of the EgtpOptionsBase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_32e4941bfba82166b4f883cdd51ee159 import (
            EgtpOptionsBase,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgtpOptionsBase", None) is not None:
                return self._properties.get("EgtpOptionsBase")
        return EgtpOptionsBase(self)

    @property
    def EgtpS5S8PgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_dadee44b5f7ce54b3b4f2cf31bab949e.EgtpS5S8PgwOptions): An instance of the EgtpS5S8PgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_dadee44b5f7ce54b3b4f2cf31bab949e import (
            EgtpS5S8PgwOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgtpS5S8PgwOptions", None) is not None:
                return self._properties.get("EgtpS5S8PgwOptions")
        return EgtpS5S8PgwOptions(self)

    @property
    def EgtpS5S8SgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_9c9b6793368b14b5dae66276ece6b8df.EgtpS5S8SgwOptions): An instance of the EgtpS5S8SgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_9c9b6793368b14b5dae66276ece6b8df import (
            EgtpS5S8SgwOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgtpS5S8SgwOptions", None) is not None:
                return self._properties.get("EgtpS5S8SgwOptions")
        return EgtpS5S8SgwOptions(self)

    @property
    def EgtpServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_f4463e6fa600456177448ed49c1d5b23.EgtpServerOptions): An instance of the EgtpServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_f4463e6fa600456177448ed49c1d5b23 import (
            EgtpServerOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgtpServerOptions", None) is not None:
                return self._properties.get("EgtpServerOptions")
        return EgtpServerOptions(self)

    @property
    def EgtpSgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_d547c3e160d4f868199b7631c4804e68.EgtpSgwOptions): An instance of the EgtpSgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_d547c3e160d4f868199b7631c4804e68 import (
            EgtpSgwOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgtpSgwOptions", None) is not None:
                return self._properties.get("EgtpSgwOptions")
        return EgtpSgwOptions(self)

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_d38c7e88fb6f87dcc64e871cf7fb904c.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_d38c7e88fb6f87dcc64e871cf7fb904c import (
            Ethernet,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ethernet", None) is not None:
                return self._properties.get("Ethernet")
        return Ethernet(self)

    @property
    def EthernetEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_07ba999c5a07ba0fd133662d8bd1eae1.EthernetEndpoint): An instance of the EthernetEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_07ba999c5a07ba0fd133662d8bd1eae1 import (
            EthernetEndpoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EthernetEndpoint", None) is not None:
                return self._properties.get("EthernetEndpoint")
        return EthernetEndpoint(self)

    @property
    def EthernetOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_99c7302b2004441d3a0f14c74b218a11.EthernetOptions): An instance of the EthernetOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_99c7302b2004441d3a0f14c74b218a11 import (
            EthernetOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EthernetOptions", None) is not None:
                return self._properties.get("EthernetOptions")
        return EthernetOptions(self)

    @property
    def FcClientEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_0bb27e24785b640285fd4c28890701c0.FcClientEndpoint): An instance of the FcClientEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_0bb27e24785b640285fd4c28890701c0 import (
            FcClientEndpoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcClientEndpoint", None) is not None:
                return self._properties.get("FcClientEndpoint")
        return FcClientEndpoint(self)

    @property
    def FcClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_27e93046b19664cb9a7956d0ce172eda.FcClientOptions): An instance of the FcClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_27e93046b19664cb9a7956d0ce172eda import (
            FcClientOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcClientOptions", None) is not None:
                return self._properties.get("FcClientOptions")
        return FcClientOptions(self)

    @property
    def FcFportFwdEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_a42123f17fd448b552a019e1e0aaa650.FcFportFwdEndpoint): An instance of the FcFportFwdEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_a42123f17fd448b552a019e1e0aaa650 import (
            FcFportFwdEndpoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcFportFwdEndpoint", None) is not None:
                return self._properties.get("FcFportFwdEndpoint")
        return FcFportFwdEndpoint(self)

    @property
    def FcFportOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_a1c0042e98ef427e823313e5fbd2ff5c.FcFportOptions): An instance of the FcFportOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_a1c0042e98ef427e823313e5fbd2ff5c import (
            FcFportOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcFportOptions", None) is not None:
                return self._properties.get("FcFportOptions")
        return FcFportOptions(self)

    @property
    def FcoeClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_ddeb39bc9d33553718e9d9d5c5615515.FcoeClientOptions): An instance of the FcoeClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_ddeb39bc9d33553718e9d9d5c5615515 import (
            FcoeClientOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeClientOptions", None) is not None:
                return self._properties.get("FcoeClientOptions")
        return FcoeClientOptions(self)

    @property
    def FcoeFwdOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_bc0e3c0717da470b08da39ad2c23c3e9.FcoeFwdOptions): An instance of the FcoeFwdOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_bc0e3c0717da470b08da39ad2c23c3e9 import (
            FcoeFwdOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeFwdOptions", None) is not None:
                return self._properties.get("FcoeFwdOptions")
        return FcoeFwdOptions(self)

    @property
    def IgmpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_058462c51a289a750bb5b00d4485513a.IgmpOptions): An instance of the IgmpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_058462c51a289a750bb5b00d4485513a import (
            IgmpOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpOptions", None) is not None:
                return self._properties.get("IgmpOptions")
        return IgmpOptions(self)

    @property
    def IpRangeOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_54247ca6e830355df00053fbf4e307d5.IpRangeOptions): An instance of the IpRangeOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_54247ca6e830355df00053fbf4e307d5 import (
            IpRangeOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpRangeOptions", None) is not None:
                return self._properties.get("IpRangeOptions")
        return IpRangeOptions(self)

    @property
    def L2tpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_eeef014542cbd357c0dcccccc57550fc.L2tpOptions): An instance of the L2tpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_eeef014542cbd357c0dcccccc57550fc import (
            L2tpOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2tpOptions", None) is not None:
                return self._properties.get("L2tpOptions")
        return L2tpOptions(self)

    @property
    def Options(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_b95a6091b48575c48d8806df541b4653.Options): An instance of the Options class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_b95a6091b48575c48d8806df541b4653 import (
            Options,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Options", None) is not None:
                return self._properties.get("Options")
        return Options(self)._select()

    @property
    def PppoxOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_339cf64ae99c79e1d1492d14520ab152.PppoxOptions): An instance of the PppoxOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_339cf64ae99c79e1d1492d14520ab152 import (
            PppoxOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxOptions", None) is not None:
                return self._properties.get("PppoxOptions")
        return PppoxOptions(self)

    @property
    def PtpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_4431aed535b415be014c5a79217aa3be.PtpOptions): An instance of the PtpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_4431aed535b415be014c5a79217aa3be import (
            PtpOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PtpOptions", None) is not None:
                return self._properties.get("PtpOptions")
        return PtpOptions(self)

    @property
    def SmDnsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_100fbc7c6145703d8f1639aa93d794c3.SmDnsOptions): An instance of the SmDnsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_100fbc7c6145703d8f1639aa93d794c3 import (
            SmDnsOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SmDnsOptions", None) is not None:
                return self._properties.get("SmDnsOptions")
        return SmDnsOptions(self)

    @property
    def StaticHostsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_6108d519c1b8726625e78e54ace41b4d.StaticHostsOptions): An instance of the StaticHostsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_6108d519c1b8726625e78e54ace41b4d import (
            StaticHostsOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StaticHostsOptions", None) is not None:
                return self._properties.get("StaticHostsOptions")
        return StaticHostsOptions(self)

    @property
    def TwampOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_7b39fa6f24cf29a2ce58f94dd349a195.TwampOptions): An instance of the TwampOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_7b39fa6f24cf29a2ce58f94dd349a195 import (
            TwampOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TwampOptions", None) is not None:
                return self._properties.get("TwampOptions")
        return TwampOptions(self)

    @property
    def TwampServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_b3351876a5276da5b361125d722f4b5a.TwampServerOptions): An instance of the TwampServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_b3351876a5276da5b361125d722f4b5a import (
            TwampServerOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TwampServerOptions", None) is not None:
                return self._properties.get("TwampServerOptions")
        return TwampServerOptions(self)

    @property
    def VepaOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_bf2ac7071874877a35a42a8b0e4ce52c.VepaOptions): An instance of the VepaOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_bf2ac7071874877a35a42a8b0e4ce52c import (
            VepaOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VepaOptions", None) is not None:
                return self._properties.get("VepaOptions")
        return VepaOptions(self)

    @property
    def WebAuthOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_57296c855047b64842a042992661d642.WebAuthOptions): An instance of the WebAuthOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_57296c855047b64842a042992661d642 import (
            WebAuthOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WebAuthOptions", None) is not None:
                return self._properties.get("WebAuthOptions")
        return WebAuthOptions(self)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    def find(self, ObjectId=None):
        # type: (str) -> ProtocolStack
        """Finds and retrieves protocolStack resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve protocolStack resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all protocolStack resources from the server.

        Args
        ----
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching protocolStack resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of protocolStack data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the protocolStack resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )

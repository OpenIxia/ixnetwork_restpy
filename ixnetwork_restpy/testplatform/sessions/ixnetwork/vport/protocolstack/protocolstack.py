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


class ProtocolStack(Base):
    """PortGroup represents the concept of a stack of layers which are to be configured on a group of ports.
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'protocolStack'

    def __init__(self, parent):
        super(ProtocolStack, self).__init__(parent)

    @property
    def AmtOptions(self):
        """An instance of the AmtOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_b646bc082770c4988c4d2f0f299f9f6d.AmtOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_b646bc082770c4988c4d2f0f299f9f6d import AmtOptions
        return AmtOptions(self)

    @property
    def AncpOptions(self):
        """An instance of the AncpOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_775b2b31ca2d469bf827983edc2d44f4.AncpOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_775b2b31ca2d469bf827983edc2d44f4 import AncpOptions
        return AncpOptions(self)

    @property
    def DhcpHostsOptions(self):
        """An instance of the DhcpHostsOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_2d59a25fc778dfad35150a76049d737e.DhcpHostsOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_2d59a25fc778dfad35150a76049d737e import DhcpHostsOptions
        return DhcpHostsOptions(self)

    @property
    def DhcpOptions(self):
        """An instance of the DhcpOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_5cee0d2828b2f8132b1576b3b950790f.DhcpOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_5cee0d2828b2f8132b1576b3b950790f import DhcpOptions
        return DhcpOptions(self)

    @property
    def Dhcpv6ClientOptions(self):
        """An instance of the Dhcpv6ClientOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_f3411d592addcd6c2c725418af47e789.Dhcpv6ClientOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_f3411d592addcd6c2c725418af47e789 import Dhcpv6ClientOptions
        return Dhcpv6ClientOptions(self)

    @property
    def Dhcpv6PdClientOptions(self):
        """An instance of the Dhcpv6PdClientOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_1b9b1bff29370c2e959b20a26c83c0bc.Dhcpv6PdClientOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_1b9b1bff29370c2e959b20a26c83c0bc import Dhcpv6PdClientOptions
        return Dhcpv6PdClientOptions(self)

    @property
    def Dhcpv6ServerOptions(self):
        """An instance of the Dhcpv6ServerOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_d397523e63af2c4095b8905285fc4078.Dhcpv6ServerOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_d397523e63af2c4095b8905285fc4078 import Dhcpv6ServerOptions
        return Dhcpv6ServerOptions(self)

    @property
    def Dot1xOptions(self):
        """An instance of the Dot1xOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_d41ad0a4594139de13fe0c3059c2d3ab.Dot1xOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_d41ad0a4594139de13fe0c3059c2d3ab import Dot1xOptions
        return Dot1xOptions(self)

    @property
    def EapoUdpOptions(self):
        """An instance of the EapoUdpOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_4d410273dc845d295e6c3b2d66fcf643.EapoUdpOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_4d410273dc845d295e6c3b2d66fcf643 import EapoUdpOptions
        return EapoUdpOptions(self)

    @property
    def EgtpClientOptions(self):
        """An instance of the EgtpClientOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_26be109de742fbbd2addc5dc7d2f7440.EgtpClientOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_26be109de742fbbd2addc5dc7d2f7440 import EgtpClientOptions
        return EgtpClientOptions(self)

    @property
    def EgtpMmeOptions(self):
        """An instance of the EgtpMmeOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpmmeoptions_088d53457523cc0d57fee246b8506b02.EgtpMmeOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpmmeoptions_088d53457523cc0d57fee246b8506b02 import EgtpMmeOptions
        return EgtpMmeOptions(self)

    @property
    def EgtpOptionsBase(self):
        """An instance of the EgtpOptionsBase class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_b2a29181914e15bef14a3a6470d73f66.EgtpOptionsBase)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_b2a29181914e15bef14a3a6470d73f66 import EgtpOptionsBase
        return EgtpOptionsBase(self)

    @property
    def EgtpS5S8PgwOptions(self):
        """An instance of the EgtpS5S8PgwOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_f2a752987ad848aaeb754929885998a8.EgtpS5S8PgwOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_f2a752987ad848aaeb754929885998a8 import EgtpS5S8PgwOptions
        return EgtpS5S8PgwOptions(self)

    @property
    def EgtpS5S8SgwOptions(self):
        """An instance of the EgtpS5S8SgwOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_af8b6a8bfd46dac0f7182c206c093626.EgtpS5S8SgwOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_af8b6a8bfd46dac0f7182c206c093626 import EgtpS5S8SgwOptions
        return EgtpS5S8SgwOptions(self)

    @property
    def EgtpServerOptions(self):
        """An instance of the EgtpServerOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_156a7f39f1e18eabe77d17b18b76554d.EgtpServerOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_156a7f39f1e18eabe77d17b18b76554d import EgtpServerOptions
        return EgtpServerOptions(self)

    @property
    def EgtpSgwOptions(self):
        """An instance of the EgtpSgwOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_8acf4fd964e27f25d1eb28083861b317.EgtpSgwOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_8acf4fd964e27f25d1eb28083861b317 import EgtpSgwOptions
        return EgtpSgwOptions(self)

    @property
    def Ethernet(self):
        """An instance of the Ethernet class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_47d860f4202298975799160e360bdc2f.Ethernet)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_47d860f4202298975799160e360bdc2f import Ethernet
        return Ethernet(self)

    @property
    def EthernetEndpoint(self):
        """An instance of the EthernetEndpoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_12fe1eb917bd42db4d9a3ab9d5dd9b1d.EthernetEndpoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_12fe1eb917bd42db4d9a3ab9d5dd9b1d import EthernetEndpoint
        return EthernetEndpoint(self)

    @property
    def EthernetOptions(self):
        """An instance of the EthernetOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_06e2bb5c7fda213e408ccbe774be709b.EthernetOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_06e2bb5c7fda213e408ccbe774be709b import EthernetOptions
        return EthernetOptions(self)

    @property
    def FcClientEndpoint(self):
        """An instance of the FcClientEndpoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_15b63c043d88e0339f3a6424fce2cc15.FcClientEndpoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_15b63c043d88e0339f3a6424fce2cc15 import FcClientEndpoint
        return FcClientEndpoint(self)

    @property
    def FcClientOptions(self):
        """An instance of the FcClientOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_ec477e4b4ab8c58a590f38ceca9700c1.FcClientOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_ec477e4b4ab8c58a590f38ceca9700c1 import FcClientOptions
        return FcClientOptions(self)

    @property
    def FcFportFwdEndpoint(self):
        """An instance of the FcFportFwdEndpoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_90afcd7dccdb699e033406f7ec50ab1c.FcFportFwdEndpoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_90afcd7dccdb699e033406f7ec50ab1c import FcFportFwdEndpoint
        return FcFportFwdEndpoint(self)

    @property
    def FcFportOptions(self):
        """An instance of the FcFportOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_1a30ad982ff8d477ebb2e3444ef46e28.FcFportOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_1a30ad982ff8d477ebb2e3444ef46e28 import FcFportOptions
        return FcFportOptions(self)

    @property
    def FcoeClientOptions(self):
        """An instance of the FcoeClientOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_27897c246178b8c5ffcd7671576dbbec.FcoeClientOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_27897c246178b8c5ffcd7671576dbbec import FcoeClientOptions
        return FcoeClientOptions(self)

    @property
    def FcoeFwdOptions(self):
        """An instance of the FcoeFwdOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_45854bbf6e3e44e3be8090a8a1e9d3e9.FcoeFwdOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_45854bbf6e3e44e3be8090a8a1e9d3e9 import FcoeFwdOptions
        return FcoeFwdOptions(self)

    @property
    def IgmpOptions(self):
        """An instance of the IgmpOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_19b7396d8fd4e7cee58a17dd2c4b9a2f.IgmpOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_19b7396d8fd4e7cee58a17dd2c4b9a2f import IgmpOptions
        return IgmpOptions(self)

    @property
    def IpRangeOptions(self):
        """An instance of the IpRangeOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_5a24844b6ec44045bf630e29a9adfac6.IpRangeOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_5a24844b6ec44045bf630e29a9adfac6 import IpRangeOptions
        return IpRangeOptions(self)

    @property
    def L2tpOptions(self):
        """An instance of the L2tpOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_13564158f3fd55c3ba447076f3915d62.L2tpOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_13564158f3fd55c3ba447076f3915d62 import L2tpOptions
        return L2tpOptions(self)

    @property
    def Options(self):
        """An instance of the Options class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_002d01acd6e74f4e451280aebc42f3b9.Options)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_002d01acd6e74f4e451280aebc42f3b9 import Options
        return Options(self)._select()

    @property
    def PppoxOptions(self):
        """An instance of the PppoxOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_0b07a85896f36c6c8a9374cf836eab3a.PppoxOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_0b07a85896f36c6c8a9374cf836eab3a import PppoxOptions
        return PppoxOptions(self)

    @property
    def PtpOptions(self):
        """An instance of the PtpOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_638c9e02bdceb37e7493e82721c430eb.PtpOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_638c9e02bdceb37e7493e82721c430eb import PtpOptions
        return PtpOptions(self)

    @property
    def SmDnsOptions(self):
        """An instance of the SmDnsOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_f49ecbe351a8b3e3ae901a1ccff5f104.SmDnsOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_f49ecbe351a8b3e3ae901a1ccff5f104 import SmDnsOptions
        return SmDnsOptions(self)

    @property
    def StaticHostsOptions(self):
        """An instance of the StaticHostsOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_4505ac787255a166d6c17903f2efa30d.StaticHostsOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_4505ac787255a166d6c17903f2efa30d import StaticHostsOptions
        return StaticHostsOptions(self)

    @property
    def TwampOptions(self):
        """An instance of the TwampOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_2c24e573c15265927ae230f649e8193b.TwampOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_2c24e573c15265927ae230f649e8193b import TwampOptions
        return TwampOptions(self)

    @property
    def TwampServerOptions(self):
        """An instance of the TwampServerOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_61893ea50e275552ce7c4ead818930f4.TwampServerOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_61893ea50e275552ce7c4ead818930f4 import TwampServerOptions
        return TwampServerOptions(self)

    @property
    def VepaOptions(self):
        """An instance of the VepaOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_74c9d45a8d3787468ff6d93e58a83be4.VepaOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_74c9d45a8d3787468ff6d93e58a83be4 import VepaOptions
        return VepaOptions(self)

    @property
    def WebAuthOptions(self):
        """An instance of the WebAuthOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_c23789bfd84eb40cee6047c9bcf4b175.WebAuthOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_c23789bfd84eb40cee6047c9bcf4b175 import WebAuthOptions
        return WebAuthOptions(self)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

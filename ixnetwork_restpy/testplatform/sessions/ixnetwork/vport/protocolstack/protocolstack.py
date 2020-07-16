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


class ProtocolStack(Base):
    """PortGroup represents the concept of a stack of layers which are to be configured on a group of ports.
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'protocolStack'
    _SDM_ATT_MAP = {
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(ProtocolStack, self).__init__(parent)

    @property
    def AmtOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_920d5afd3e8b6201245458975a82c0db.AmtOptions): An instance of the AmtOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_920d5afd3e8b6201245458975a82c0db import AmtOptions
        return AmtOptions(self)

    @property
    def AncpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_f260f6494b4e2ad033aeceec23cac54c.AncpOptions): An instance of the AncpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_f260f6494b4e2ad033aeceec23cac54c import AncpOptions
        return AncpOptions(self)

    @property
    def DhcpHostsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_1aa84c4d3616ee0c49f129eb60e368f5.DhcpHostsOptions): An instance of the DhcpHostsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_1aa84c4d3616ee0c49f129eb60e368f5 import DhcpHostsOptions
        return DhcpHostsOptions(self)

    @property
    def DhcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_26f3d4f3f49721f70d8d3209df521d26.DhcpOptions): An instance of the DhcpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_26f3d4f3f49721f70d8d3209df521d26 import DhcpOptions
        return DhcpOptions(self)

    @property
    def Dhcpv6ClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_b7c7438f131dab8b0781a2aab896c6bf.Dhcpv6ClientOptions): An instance of the Dhcpv6ClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_b7c7438f131dab8b0781a2aab896c6bf import Dhcpv6ClientOptions
        return Dhcpv6ClientOptions(self)

    @property
    def Dhcpv6PdClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_ca2a2ece3298de61d5b8bdd7a850035f.Dhcpv6PdClientOptions): An instance of the Dhcpv6PdClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_ca2a2ece3298de61d5b8bdd7a850035f import Dhcpv6PdClientOptions
        return Dhcpv6PdClientOptions(self)

    @property
    def Dhcpv6ServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_a3f49164e013779eb52f1890d0a76869.Dhcpv6ServerOptions): An instance of the Dhcpv6ServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_a3f49164e013779eb52f1890d0a76869 import Dhcpv6ServerOptions
        return Dhcpv6ServerOptions(self)

    @property
    def Dot1xOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_8a46299312ed9582fb7d7b160232f3c4.Dot1xOptions): An instance of the Dot1xOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_8a46299312ed9582fb7d7b160232f3c4 import Dot1xOptions
        return Dot1xOptions(self)

    @property
    def EapoUdpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_c637c5c5d1e6ed49fb44ea5297e78110.EapoUdpOptions): An instance of the EapoUdpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_c637c5c5d1e6ed49fb44ea5297e78110 import EapoUdpOptions
        return EapoUdpOptions(self)

    @property
    def EgtpClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_faed49d1cd6032d1d86c972d66b3a5fe.EgtpClientOptions): An instance of the EgtpClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_faed49d1cd6032d1d86c972d66b3a5fe import EgtpClientOptions
        return EgtpClientOptions(self)

    @property
    def EgtpOptionsBase(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_2c116dc95d43ffef03c94ddbd3b750be.EgtpOptionsBase): An instance of the EgtpOptionsBase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_2c116dc95d43ffef03c94ddbd3b750be import EgtpOptionsBase
        return EgtpOptionsBase(self)

    @property
    def EgtpS5S8PgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_0ecee2b136b9e205c98c111ae43d2529.EgtpS5S8PgwOptions): An instance of the EgtpS5S8PgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_0ecee2b136b9e205c98c111ae43d2529 import EgtpS5S8PgwOptions
        return EgtpS5S8PgwOptions(self)

    @property
    def EgtpS5S8SgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_85e0aea713fb798872e1eb8bc6544fe9.EgtpS5S8SgwOptions): An instance of the EgtpS5S8SgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_85e0aea713fb798872e1eb8bc6544fe9 import EgtpS5S8SgwOptions
        return EgtpS5S8SgwOptions(self)

    @property
    def EgtpServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_0da9d0ef7484fcc78603ede124e9e586.EgtpServerOptions): An instance of the EgtpServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_0da9d0ef7484fcc78603ede124e9e586 import EgtpServerOptions
        return EgtpServerOptions(self)

    @property
    def EgtpSgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_a815efe97f0053663dab2a194220b27f.EgtpSgwOptions): An instance of the EgtpSgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_a815efe97f0053663dab2a194220b27f import EgtpSgwOptions
        return EgtpSgwOptions(self)

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_9270cf428cd566d0179a6cc2d36c2c51.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_9270cf428cd566d0179a6cc2d36c2c51 import Ethernet
        return Ethernet(self)

    @property
    def EthernetEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_d505a70c25c539a0f7f57c724fbbdc10.EthernetEndpoint): An instance of the EthernetEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_d505a70c25c539a0f7f57c724fbbdc10 import EthernetEndpoint
        return EthernetEndpoint(self)

    @property
    def EthernetOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_e2afbb391332ae673b33d4fa99666abc.EthernetOptions): An instance of the EthernetOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_e2afbb391332ae673b33d4fa99666abc import EthernetOptions
        return EthernetOptions(self)

    @property
    def FcClientEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_7e5e9b26d670e7a4f77b28623de3f69a.FcClientEndpoint): An instance of the FcClientEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_7e5e9b26d670e7a4f77b28623de3f69a import FcClientEndpoint
        return FcClientEndpoint(self)

    @property
    def FcClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_2888c6e9e7f909b50d27f503bbdee6af.FcClientOptions): An instance of the FcClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_2888c6e9e7f909b50d27f503bbdee6af import FcClientOptions
        return FcClientOptions(self)

    @property
    def FcFportFwdEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_f28ea5fd1bf83950a4aadd0d7a886489.FcFportFwdEndpoint): An instance of the FcFportFwdEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_f28ea5fd1bf83950a4aadd0d7a886489 import FcFportFwdEndpoint
        return FcFportFwdEndpoint(self)

    @property
    def FcFportOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_b1c1714bd27605ce452575322dc2d18e.FcFportOptions): An instance of the FcFportOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_b1c1714bd27605ce452575322dc2d18e import FcFportOptions
        return FcFportOptions(self)

    @property
    def FcoeClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_38e2c7ce6db993624d36fe2016760c4c.FcoeClientOptions): An instance of the FcoeClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_38e2c7ce6db993624d36fe2016760c4c import FcoeClientOptions
        return FcoeClientOptions(self)

    @property
    def FcoeFwdOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_c1ebfa7451c0fd226b21ca6a670f698a.FcoeFwdOptions): An instance of the FcoeFwdOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_c1ebfa7451c0fd226b21ca6a670f698a import FcoeFwdOptions
        return FcoeFwdOptions(self)

    @property
    def IgmpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_af97dc2d88fdcb59ef3bcbc0c5ee0383.IgmpOptions): An instance of the IgmpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_af97dc2d88fdcb59ef3bcbc0c5ee0383 import IgmpOptions
        return IgmpOptions(self)

    @property
    def IpRangeOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_e4c02903f7662a5dbdcd1ee5fc01c49d.IpRangeOptions): An instance of the IpRangeOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_e4c02903f7662a5dbdcd1ee5fc01c49d import IpRangeOptions
        return IpRangeOptions(self)

    @property
    def L2tpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_6924c5a1bebdbcd90ceed331b2bf3fa8.L2tpOptions): An instance of the L2tpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_6924c5a1bebdbcd90ceed331b2bf3fa8 import L2tpOptions
        return L2tpOptions(self)

    @property
    def Options(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_7469b94cd33b4b06719f0dd4ecfb6f8b.Options): An instance of the Options class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_7469b94cd33b4b06719f0dd4ecfb6f8b import Options
        return Options(self)._select()

    @property
    def PppoxOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_f7eed5ece8c8b093f410f4b19e5321ba.PppoxOptions): An instance of the PppoxOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_f7eed5ece8c8b093f410f4b19e5321ba import PppoxOptions
        return PppoxOptions(self)

    @property
    def PtpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_016c148d29be122b4ff63935e1a40089.PtpOptions): An instance of the PtpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_016c148d29be122b4ff63935e1a40089 import PtpOptions
        return PtpOptions(self)

    @property
    def SmDnsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_653d7eba98b73b1fad589c57df4e06db.SmDnsOptions): An instance of the SmDnsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_653d7eba98b73b1fad589c57df4e06db import SmDnsOptions
        return SmDnsOptions(self)

    @property
    def StaticHostsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_b856e92d38cfb4c7f8e76ffd5c970154.StaticHostsOptions): An instance of the StaticHostsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_b856e92d38cfb4c7f8e76ffd5c970154 import StaticHostsOptions
        return StaticHostsOptions(self)

    @property
    def TwampOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_76cd16af4e6a3457023c413b90dc09b1.TwampOptions): An instance of the TwampOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_76cd16af4e6a3457023c413b90dc09b1 import TwampOptions
        return TwampOptions(self)

    @property
    def TwampServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_d9df2e536efe64ac2a79662f006efe5c.TwampServerOptions): An instance of the TwampServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_d9df2e536efe64ac2a79662f006efe5c import TwampServerOptions
        return TwampServerOptions(self)

    @property
    def VepaOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_61de8697309d02e26cfdcfe37470fa44.VepaOptions): An instance of the VepaOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_61de8697309d02e26cfdcfe37470fa44 import VepaOptions
        return VepaOptions(self)

    @property
    def WebAuthOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_53051bd801054f33723505dcef43b2b7.WebAuthOptions): An instance of the WebAuthOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_53051bd801054f33723505dcef43b2b7 import WebAuthOptions
        return WebAuthOptions(self)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

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
    """
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'protocolStack'

    def __init__(self, parent):
        super(ProtocolStack, self).__init__(parent)

    @property
    def AmtGlobals(self):
        """An instance of the AmtGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.amtglobals.amtglobals.AmtGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.amtglobals.amtglobals import AmtGlobals
        return AmtGlobals(self)

    @property
    def AncpGlobals(self):
        """An instance of the AncpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpglobals.AncpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpglobals import AncpGlobals
        return AncpGlobals(self)

    @property
    def DcbxGlobals(self):
        """An instance of the DcbxGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dcbxglobals.dcbxglobals.DcbxGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dcbxglobals.dcbxglobals import DcbxGlobals
        return DcbxGlobals(self)

    @property
    def DhcpGlobals(self):
        """An instance of the DhcpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpglobals.DhcpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpglobals import DhcpGlobals
        return DhcpGlobals(self)

    @property
    def DhcpHostsGlobals(self):
        """An instance of the DhcpHostsGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcphostsglobals.dhcphostsglobals.DhcpHostsGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcphostsglobals.dhcphostsglobals import DhcpHostsGlobals
        return DhcpHostsGlobals(self)

    @property
    def DhcpServerGlobals(self):
        """An instance of the DhcpServerGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpserverglobals.dhcpserverglobals.DhcpServerGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpserverglobals.dhcpserverglobals import DhcpServerGlobals
        return DhcpServerGlobals(self)

    @property
    def Dhcpv6ClientGlobals(self):
        """An instance of the Dhcpv6ClientGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6clientglobals.dhcpv6clientglobals.Dhcpv6ClientGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6clientglobals.dhcpv6clientglobals import Dhcpv6ClientGlobals
        return Dhcpv6ClientGlobals(self)

    @property
    def Dhcpv6PdClientGlobals(self):
        """An instance of the Dhcpv6PdClientGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdclientglobals.Dhcpv6PdClientGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdclientglobals import Dhcpv6PdClientGlobals
        return Dhcpv6PdClientGlobals(self)

    @property
    def Dhcpv6ServerGlobals(self):
        """An instance of the Dhcpv6ServerGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6serverglobals.dhcpv6serverglobals.Dhcpv6ServerGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6serverglobals.dhcpv6serverglobals import Dhcpv6ServerGlobals
        return Dhcpv6ServerGlobals(self)

    @property
    def Dot1xGlobals(self):
        """An instance of the Dot1xGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.dot1xglobals.Dot1xGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.dot1xglobals import Dot1xGlobals
        return Dot1xGlobals(self)

    @property
    def EapoUdpGlobals(self):
        """An instance of the EapoUdpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.eapoudpglobals.EapoUdpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.eapoudpglobals import EapoUdpGlobals
        return EapoUdpGlobals(self)

    @property
    def EgtpClientGlobals(self):
        """An instance of the EgtpClientGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpclientglobals.egtpclientglobals.EgtpClientGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpclientglobals.egtpclientglobals import EgtpClientGlobals
        return EgtpClientGlobals(self)

    @property
    def EgtpGlobalsBase(self):
        """An instance of the EgtpGlobalsBase class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpglobalsbase.egtpglobalsbase.EgtpGlobalsBase)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpglobalsbase.egtpglobalsbase import EgtpGlobalsBase
        return EgtpGlobalsBase(self)

    @property
    def EgtpMmeGlobals(self):
        """An instance of the EgtpMmeGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpmmeglobals.egtpmmeglobals.EgtpMmeGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpmmeglobals.egtpmmeglobals import EgtpMmeGlobals
        return EgtpMmeGlobals(self)

    @property
    def EgtpS5S8PgwGlobals(self):
        """An instance of the EgtpS5S8PgwGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8pgwglobals.egtps5s8pgwglobals.EgtpS5S8PgwGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8pgwglobals.egtps5s8pgwglobals import EgtpS5S8PgwGlobals
        return EgtpS5S8PgwGlobals(self)

    @property
    def EgtpS5S8SgwGlobals(self):
        """An instance of the EgtpS5S8SgwGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.egtps5s8sgwglobals.EgtpS5S8SgwGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.egtps5s8sgwglobals import EgtpS5S8SgwGlobals
        return EgtpS5S8SgwGlobals(self)

    @property
    def EgtpSgwGlobals(self):
        """An instance of the EgtpSgwGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpsgwglobals.egtpsgwglobals.EgtpSgwGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpsgwglobals.egtpsgwglobals import EgtpSgwGlobals
        return EgtpSgwGlobals(self)

    @property
    def FcClientGlobals(self):
        """An instance of the FcClientGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcclientglobals.fcclientglobals.FcClientGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcclientglobals.fcclientglobals import FcClientGlobals
        return FcClientGlobals(self)

    @property
    def FcFportGlobals(self):
        """An instance of the FcFportGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcfportglobals.fcfportglobals.FcFportGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcfportglobals.fcfportglobals import FcFportGlobals
        return FcFportGlobals(self)

    @property
    def FcoeClientGlobals(self):
        """An instance of the FcoeClientGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientglobals.FcoeClientGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientglobals import FcoeClientGlobals
        return FcoeClientGlobals(self)

    @property
    def FcoeFwdGlobals(self):
        """An instance of the FcoeFwdGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoefwdglobals.fcoefwdglobals.FcoeFwdGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoefwdglobals.fcoefwdglobals import FcoeFwdGlobals
        return FcoeFwdGlobals(self)

    @property
    def IgmpGlobals(self):
        """An instance of the IgmpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpglobals.IgmpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpglobals import IgmpGlobals
        return IgmpGlobals(self)

    @property
    def IpGlobals(self):
        """An instance of the IpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ipglobals.ipglobals.IpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ipglobals.ipglobals import IpGlobals
        return IpGlobals(self)

    @property
    def IptvGlobals(self):
        """An instance of the IptvGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvglobals.IptvGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvglobals import IptvGlobals
        return IptvGlobals(self)

    @property
    def L2tpGlobals(self):
        """An instance of the L2tpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.l2tpglobals.l2tpglobals.L2tpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.l2tpglobals.l2tpglobals import L2tpGlobals
        return L2tpGlobals(self)

    @property
    def PppoxGlobals(self):
        """An instance of the PppoxGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.pppoxglobals.pppoxglobals.PppoxGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.pppoxglobals.pppoxglobals import PppoxGlobals
        return PppoxGlobals(self)

    @property
    def PtpGlobals(self):
        """An instance of the PtpGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ptpglobals.ptpglobals.PtpGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ptpglobals.ptpglobals import PtpGlobals
        return PtpGlobals(self)

    @property
    def RadiusGlobals(self):
        """An instance of the RadiusGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.radiusglobals.radiusglobals.RadiusGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.radiusglobals.radiusglobals import RadiusGlobals
        return RadiusGlobals(self)

    @property
    def StaticHostsGlobals(self):
        """An instance of the StaticHostsGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.statichostsglobals.statichostsglobals.StaticHostsGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.statichostsglobals.statichostsglobals import StaticHostsGlobals
        return StaticHostsGlobals(self)

    @property
    def TwampGlobals(self):
        """An instance of the TwampGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.twampglobals.twampglobals.TwampGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.twampglobals.twampglobals import TwampGlobals
        return TwampGlobals(self)

    @property
    def VepaGlobals(self):
        """An instance of the VepaGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vepaglobals.vepaglobals.VepaGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vepaglobals.vepaglobals import VepaGlobals
        return VepaGlobals(self)

    @property
    def VicClientGlobals(self):
        """An instance of the VicClientGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicclientglobals.VicClientGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicclientglobals import VicClientGlobals
        return VicClientGlobals(self)

    @property
    def WebAuthGlobals(self):
        """An instance of the WebAuthGlobals class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.webauthglobals.webauthglobals.WebAuthGlobals)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.webauthglobals.webauthglobals import WebAuthGlobals
        return WebAuthGlobals(self)

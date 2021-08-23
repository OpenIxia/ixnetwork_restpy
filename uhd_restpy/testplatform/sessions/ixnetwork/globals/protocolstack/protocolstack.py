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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class ProtocolStack(Base):
    """
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'protocolStack'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(ProtocolStack, self).__init__(parent, list_op)

    @property
    def AmtGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.amtglobals.amtglobals.AmtGlobals): An instance of the AmtGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.amtglobals.amtglobals import AmtGlobals
        if self._properties.get('AmtGlobals', None) is not None:
            return self._properties.get('AmtGlobals')
        else:
            return AmtGlobals(self)

    @property
    def AncpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpglobals.AncpGlobals): An instance of the AncpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpglobals import AncpGlobals
        if self._properties.get('AncpGlobals', None) is not None:
            return self._properties.get('AncpGlobals')
        else:
            return AncpGlobals(self)

    @property
    def DcbxGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dcbxglobals.dcbxglobals.DcbxGlobals): An instance of the DcbxGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dcbxglobals.dcbxglobals import DcbxGlobals
        if self._properties.get('DcbxGlobals', None) is not None:
            return self._properties.get('DcbxGlobals')
        else:
            return DcbxGlobals(self)

    @property
    def DhcpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpglobals.DhcpGlobals): An instance of the DhcpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpglobals import DhcpGlobals
        if self._properties.get('DhcpGlobals', None) is not None:
            return self._properties.get('DhcpGlobals')
        else:
            return DhcpGlobals(self)

    @property
    def DhcpHostsGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcphostsglobals.dhcphostsglobals.DhcpHostsGlobals): An instance of the DhcpHostsGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcphostsglobals.dhcphostsglobals import DhcpHostsGlobals
        if self._properties.get('DhcpHostsGlobals', None) is not None:
            return self._properties.get('DhcpHostsGlobals')
        else:
            return DhcpHostsGlobals(self)

    @property
    def DhcpServerGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpserverglobals.dhcpserverglobals.DhcpServerGlobals): An instance of the DhcpServerGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpserverglobals.dhcpserverglobals import DhcpServerGlobals
        if self._properties.get('DhcpServerGlobals', None) is not None:
            return self._properties.get('DhcpServerGlobals')
        else:
            return DhcpServerGlobals(self)

    @property
    def Dhcpv6ClientGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6clientglobals.dhcpv6clientglobals.Dhcpv6ClientGlobals): An instance of the Dhcpv6ClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6clientglobals.dhcpv6clientglobals import Dhcpv6ClientGlobals
        if self._properties.get('Dhcpv6ClientGlobals', None) is not None:
            return self._properties.get('Dhcpv6ClientGlobals')
        else:
            return Dhcpv6ClientGlobals(self)

    @property
    def Dhcpv6PdClientGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdclientglobals.Dhcpv6PdClientGlobals): An instance of the Dhcpv6PdClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdclientglobals import Dhcpv6PdClientGlobals
        if self._properties.get('Dhcpv6PdClientGlobals', None) is not None:
            return self._properties.get('Dhcpv6PdClientGlobals')
        else:
            return Dhcpv6PdClientGlobals(self)

    @property
    def Dhcpv6ServerGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6serverglobals.dhcpv6serverglobals.Dhcpv6ServerGlobals): An instance of the Dhcpv6ServerGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6serverglobals.dhcpv6serverglobals import Dhcpv6ServerGlobals
        if self._properties.get('Dhcpv6ServerGlobals', None) is not None:
            return self._properties.get('Dhcpv6ServerGlobals')
        else:
            return Dhcpv6ServerGlobals(self)

    @property
    def Dot1xGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.dot1xglobals.Dot1xGlobals): An instance of the Dot1xGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.dot1xglobals import Dot1xGlobals
        if self._properties.get('Dot1xGlobals', None) is not None:
            return self._properties.get('Dot1xGlobals')
        else:
            return Dot1xGlobals(self)

    @property
    def EapoUdpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.eapoudpglobals.EapoUdpGlobals): An instance of the EapoUdpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.eapoudpglobals import EapoUdpGlobals
        if self._properties.get('EapoUdpGlobals', None) is not None:
            return self._properties.get('EapoUdpGlobals')
        else:
            return EapoUdpGlobals(self)

    @property
    def EgtpClientGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpclientglobals.egtpclientglobals.EgtpClientGlobals): An instance of the EgtpClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpclientglobals.egtpclientglobals import EgtpClientGlobals
        if self._properties.get('EgtpClientGlobals', None) is not None:
            return self._properties.get('EgtpClientGlobals')
        else:
            return EgtpClientGlobals(self)

    @property
    def EgtpGlobalsBase(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpglobalsbase.egtpglobalsbase.EgtpGlobalsBase): An instance of the EgtpGlobalsBase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpglobalsbase.egtpglobalsbase import EgtpGlobalsBase
        if self._properties.get('EgtpGlobalsBase', None) is not None:
            return self._properties.get('EgtpGlobalsBase')
        else:
            return EgtpGlobalsBase(self)

    @property
    def EgtpS5S8PgwGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8pgwglobals.egtps5s8pgwglobals.EgtpS5S8PgwGlobals): An instance of the EgtpS5S8PgwGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8pgwglobals.egtps5s8pgwglobals import EgtpS5S8PgwGlobals
        if self._properties.get('EgtpS5S8PgwGlobals', None) is not None:
            return self._properties.get('EgtpS5S8PgwGlobals')
        else:
            return EgtpS5S8PgwGlobals(self)

    @property
    def EgtpS5S8SgwGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.egtps5s8sgwglobals.EgtpS5S8SgwGlobals): An instance of the EgtpS5S8SgwGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.egtps5s8sgwglobals import EgtpS5S8SgwGlobals
        if self._properties.get('EgtpS5S8SgwGlobals', None) is not None:
            return self._properties.get('EgtpS5S8SgwGlobals')
        else:
            return EgtpS5S8SgwGlobals(self)

    @property
    def EgtpSgwGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpsgwglobals.egtpsgwglobals.EgtpSgwGlobals): An instance of the EgtpSgwGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpsgwglobals.egtpsgwglobals import EgtpSgwGlobals
        if self._properties.get('EgtpSgwGlobals', None) is not None:
            return self._properties.get('EgtpSgwGlobals')
        else:
            return EgtpSgwGlobals(self)

    @property
    def FcClientGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcclientglobals.fcclientglobals.FcClientGlobals): An instance of the FcClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcclientglobals.fcclientglobals import FcClientGlobals
        if self._properties.get('FcClientGlobals', None) is not None:
            return self._properties.get('FcClientGlobals')
        else:
            return FcClientGlobals(self)

    @property
    def FcFportGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcfportglobals.fcfportglobals.FcFportGlobals): An instance of the FcFportGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcfportglobals.fcfportglobals import FcFportGlobals
        if self._properties.get('FcFportGlobals', None) is not None:
            return self._properties.get('FcFportGlobals')
        else:
            return FcFportGlobals(self)

    @property
    def FcoeClientGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientglobals.FcoeClientGlobals): An instance of the FcoeClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientglobals import FcoeClientGlobals
        if self._properties.get('FcoeClientGlobals', None) is not None:
            return self._properties.get('FcoeClientGlobals')
        else:
            return FcoeClientGlobals(self)

    @property
    def FcoeFwdGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoefwdglobals.fcoefwdglobals.FcoeFwdGlobals): An instance of the FcoeFwdGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoefwdglobals.fcoefwdglobals import FcoeFwdGlobals
        if self._properties.get('FcoeFwdGlobals', None) is not None:
            return self._properties.get('FcoeFwdGlobals')
        else:
            return FcoeFwdGlobals(self)

    @property
    def IgmpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpglobals.IgmpGlobals): An instance of the IgmpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpglobals import IgmpGlobals
        if self._properties.get('IgmpGlobals', None) is not None:
            return self._properties.get('IgmpGlobals')
        else:
            return IgmpGlobals(self)

    @property
    def IpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ipglobals.ipglobals.IpGlobals): An instance of the IpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ipglobals.ipglobals import IpGlobals
        if self._properties.get('IpGlobals', None) is not None:
            return self._properties.get('IpGlobals')
        else:
            return IpGlobals(self)

    @property
    def IptvGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvglobals.IptvGlobals): An instance of the IptvGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvglobals import IptvGlobals
        if self._properties.get('IptvGlobals', None) is not None:
            return self._properties.get('IptvGlobals')
        else:
            return IptvGlobals(self)

    @property
    def L2tpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.l2tpglobals.l2tpglobals.L2tpGlobals): An instance of the L2tpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.l2tpglobals.l2tpglobals import L2tpGlobals
        if self._properties.get('L2tpGlobals', None) is not None:
            return self._properties.get('L2tpGlobals')
        else:
            return L2tpGlobals(self)

    @property
    def PppoxGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.pppoxglobals.pppoxglobals.PppoxGlobals): An instance of the PppoxGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.pppoxglobals.pppoxglobals import PppoxGlobals
        if self._properties.get('PppoxGlobals', None) is not None:
            return self._properties.get('PppoxGlobals')
        else:
            return PppoxGlobals(self)

    @property
    def PtpGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ptpglobals.ptpglobals.PtpGlobals): An instance of the PtpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ptpglobals.ptpglobals import PtpGlobals
        if self._properties.get('PtpGlobals', None) is not None:
            return self._properties.get('PtpGlobals')
        else:
            return PtpGlobals(self)

    @property
    def RadiusGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.radiusglobals.radiusglobals.RadiusGlobals): An instance of the RadiusGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.radiusglobals.radiusglobals import RadiusGlobals
        if self._properties.get('RadiusGlobals', None) is not None:
            return self._properties.get('RadiusGlobals')
        else:
            return RadiusGlobals(self)

    @property
    def StaticHostsGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.statichostsglobals.statichostsglobals.StaticHostsGlobals): An instance of the StaticHostsGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.statichostsglobals.statichostsglobals import StaticHostsGlobals
        if self._properties.get('StaticHostsGlobals', None) is not None:
            return self._properties.get('StaticHostsGlobals')
        else:
            return StaticHostsGlobals(self)

    @property
    def TwampGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.twampglobals.twampglobals.TwampGlobals): An instance of the TwampGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.twampglobals.twampglobals import TwampGlobals
        if self._properties.get('TwampGlobals', None) is not None:
            return self._properties.get('TwampGlobals')
        else:
            return TwampGlobals(self)

    @property
    def VepaGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vepaglobals.vepaglobals.VepaGlobals): An instance of the VepaGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vepaglobals.vepaglobals import VepaGlobals
        if self._properties.get('VepaGlobals', None) is not None:
            return self._properties.get('VepaGlobals')
        else:
            return VepaGlobals(self)

    @property
    def VicClientGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicclientglobals.VicClientGlobals): An instance of the VicClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicclientglobals import VicClientGlobals
        if self._properties.get('VicClientGlobals', None) is not None:
            return self._properties.get('VicClientGlobals')
        else:
            return VicClientGlobals(self)

    @property
    def WebAuthGlobals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.webauthglobals.webauthglobals.WebAuthGlobals): An instance of the WebAuthGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.webauthglobals.webauthglobals import WebAuthGlobals
        if self._properties.get('WebAuthGlobals', None) is not None:
            return self._properties.get('WebAuthGlobals')
        else:
            return WebAuthGlobals(self)

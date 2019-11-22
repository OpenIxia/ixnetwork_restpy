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


class Range(Base):
    """
    The Range class encapsulates a list of range resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Range.find() method.
    The list can be managed by the user by using the Range.add() and Range.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'range'

    def __init__(self, parent):
        super(Range, self).__init__(parent)

    @property
    def AmtRange(self):
        """An instance of the AmtRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtrange_302750c07121c019adc1773d38a87c13.AmtRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtrange_302750c07121c019adc1773d38a87c13 import AmtRange
        return AmtRange(self)

    @property
    def AncpRange(self):
        """An instance of the AncpRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancprange_1844fc105fa0f6c7fb3b5970b1f3cf9a.AncpRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancprange_1844fc105fa0f6c7fb3b5970b1f3cf9a import AncpRange
        return AncpRange(self)

    @property
    def Dot1xRange(self):
        """An instance of the Dot1xRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_425c5d7a87d37864f6c87cf1ad4c2374.Dot1xRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_425c5d7a87d37864f6c87cf1ad4c2374 import Dot1xRange
        return Dot1xRange(self)

    @property
    def EapoUdpRange(self):
        """An instance of the EapoUdpRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudprange_480c6c4fa784b5422b18cca8132bb9ba.EapoUdpRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudprange_480c6c4fa784b5422b18cca8132bb9ba import EapoUdpRange
        return EapoUdpRange(self)

    @property
    def EgtpSgw5S8Range(self):
        """An instance of the EgtpSgw5S8Range class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgw5s8range_4e751bb15160865db6a3d645c638a3ca.EgtpSgw5S8Range)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgw5s8range_4e751bb15160865db6a3d645c638a3ca import EgtpSgw5S8Range
        return EgtpSgw5S8Range(self)._select()

    @property
    def EmulatedRouterRange(self):
        """An instance of the EmulatedRouterRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.emulatedrouterrange_2e11368e0e60179b1a271ce524b8710e.EmulatedRouterRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.emulatedrouterrange_2e11368e0e60179b1a271ce524b8710e import EmulatedRouterRange
        return EmulatedRouterRange(self)._select()

    @property
    def EsmcRange(self):
        """An instance of the EsmcRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_9ee5b45fe363b9c3c63bfb331d136e59.EsmcRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_9ee5b45fe363b9c3c63bfb331d136e59 import EsmcRange
        return EsmcRange(self)

    @property
    def IgmpMldRange(self):
        """An instance of the IgmpMldRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpmldrange_f31d2452a94693e8d4ff3cbb496f0d14.IgmpMldRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpmldrange_f31d2452a94693e8d4ff3cbb496f0d14 import IgmpMldRange
        return IgmpMldRange(self)

    @property
    def IgmpQuerierRange(self):
        """An instance of the IgmpQuerierRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpquerierrange_af9a60d98510108c624a01b10d8dbb39.IgmpQuerierRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpquerierrange_af9a60d98510108c624a01b10d8dbb39 import IgmpQuerierRange
        return IgmpQuerierRange(self)

    @property
    def IpRange(self):
        """An instance of the IpRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprange_431a1190ac17952c200124079192c41a.IpRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprange_431a1190ac17952c200124079192c41a import IpRange
        return IpRange(self)._select()

    @property
    def IptvRange(self):
        """An instance of the IptvRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvrange_f37d63e8c8760ea8abb45510d7be9fbd.IptvRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvrange_f37d63e8c8760ea8abb45510d7be9fbd import IptvRange
        return IptvRange(self)

    @property
    def MacRange(self):
        """An instance of the MacRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_e43ada6df4aad3df20b512aaf8394ac9.MacRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_e43ada6df4aad3df20b512aaf8394ac9 import MacRange
        return MacRange(self)._select()

    @property
    def PtpRangeOverIp(self):
        """An instance of the PtpRangeOverIp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeoverip_090dc0807c4d14cbe3ba1afba4c1b790.PtpRangeOverIp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeoverip_090dc0807c4d14cbe3ba1afba4c1b790 import PtpRangeOverIp
        return PtpRangeOverIp(self)

    @property
    def PtpRangeOverMac(self):
        """An instance of the PtpRangeOverMac class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_05aceb1280388c3d84f076a3de96490b.PtpRangeOverMac)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_05aceb1280388c3d84f076a3de96490b import PtpRangeOverMac
        return PtpRangeOverMac(self)

    @property
    def TwampControlRange(self):
        """An instance of the TwampControlRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampcontrolrange_98486def088f6fb65ec8173630d92f6e.TwampControlRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampcontrolrange_98486def088f6fb65ec8173630d92f6e import TwampControlRange
        return TwampControlRange(self)

    @property
    def TwampServerRange(self):
        """An instance of the TwampServerRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserverrange_f32fb006527e2d3d896ebe331845a044.TwampServerRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserverrange_f32fb006527e2d3d896ebe331845a044 import TwampServerRange
        return TwampServerRange(self)

    @property
    def TwampTestRange(self):
        """An instance of the TwampTestRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twamptestrange_a217c915312a9874ce09cc77985e2b34.TwampTestRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twamptestrange_a217c915312a9874ce09cc77985e2b34 import TwampTestRange
        return TwampTestRange(self)

    @property
    def VicClientRange(self):
        """An instance of the VicClientRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_36a9f5784c27faef1192a7cd66019697.VicClientRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_36a9f5784c27faef1192a7cd66019697 import VicClientRange
        return VicClientRange(self)

    @property
    def VlanRange(self):
        """An instance of the VlanRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_51007ce93457e9137bd6a2dc67e0ae1a.VlanRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_51007ce93457e9137bd6a2dc67e0ae1a import VlanRange
        return VlanRange(self)._select()

    @property
    def WebAuthRange(self):
        """An instance of the WebAuthRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthrange_3395e4e16aa9c73c66cf8bd4d18d7618.WebAuthRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthrange_3395e4e16aa9c73c66cf8bd4d18d7618 import WebAuthRange
        return WebAuthRange(self)

    def add(self):
        """Adds a new range node on the server and retrieves it in this instance.

        Returns:
            self: This instance with all currently retrieved range data using find and the newly added range data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the range data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves range data from the server.

        All named parameters support regex and can be used to selectively retrieve range data from the server.
        By default the find method takes no parameters and will retrieve all range data from the server.

        Returns:
            self: This instance with matching range data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of range data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the range data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def Ipv6SendNdpNS(self, *args, **kwargs):
        """Executes the ipv6SendNdpNS operation on the server.

        Send NS on NDP for IPv6 ports.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ipv6SendNdpNS(Arg2:number)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]

        ipv6SendNdpNS(Arg2:number, Arg3:enum)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
                args[1] is Arg3 (str(async|sync)): IPv6 NDP rate for NS messages.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ipv6SendNdpNS', payload=payload, response_object=None)

    def Ipv6SendNdpRS(self, *args, **kwargs):
        """Executes the ipv6SendNdpRS operation on the server.

        Send RS on NDP for IPv6 ports.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ipv6SendNdpRS(Arg2:number)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]

        ipv6SendNdpRS(Arg2:number, Arg3:enum)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
                args[1] is Arg3 (str(async|sync)): IPv6 NDP rate for RS messages.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ipv6SendNdpRS', payload=payload, response_object=None)

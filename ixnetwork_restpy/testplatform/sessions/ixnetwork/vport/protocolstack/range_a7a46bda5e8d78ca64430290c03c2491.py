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


class Range(Base):
    """
    The Range class encapsulates a list of range resources that are managed by the user.
    A list of resources can be retrieved from the server using the Range.find() method.
    The list can be managed by using the Range.add() and Range.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "range"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Range, self).__init__(parent, list_op)

    @property
    def AmtRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtrange_9964a448a08a161cec65777e7ed9b3cb.AmtRange): An instance of the AmtRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtrange_9964a448a08a161cec65777e7ed9b3cb import (
            AmtRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AmtRange", None) is not None:
                return self._properties.get("AmtRange")
        return AmtRange(self)

    @property
    def Dot1xRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_90d7dde1956f718a653befe0fe9e37d8.Dot1xRange): An instance of the Dot1xRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_90d7dde1956f718a653befe0fe9e37d8 import (
            Dot1xRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dot1xRange", None) is not None:
                return self._properties.get("Dot1xRange")
        return Dot1xRange(self)

    @property
    def EmulatedRouterRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.emulatedrouterrange_65f988a39cd56d0f1889fb207da823d8.EmulatedRouterRange): An instance of the EmulatedRouterRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.emulatedrouterrange_65f988a39cd56d0f1889fb207da823d8 import (
            EmulatedRouterRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EmulatedRouterRange", None) is not None:
                return self._properties.get("EmulatedRouterRange")
        return EmulatedRouterRange(self)._select()

    @property
    def EsmcRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_ffcf8b5e7715f448f70327b2a2d61a7a.EsmcRange): An instance of the EsmcRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_ffcf8b5e7715f448f70327b2a2d61a7a import (
            EsmcRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EsmcRange", None) is not None:
                return self._properties.get("EsmcRange")
        return EsmcRange(self)

    @property
    def MacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_92d5cdbd5b520a44b3acef3cde220624.MacRange): An instance of the MacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_92d5cdbd5b520a44b3acef3cde220624 import (
            MacRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MacRange", None) is not None:
                return self._properties.get("MacRange")
        return MacRange(self)._select()

    @property
    def PtpRangeOverMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_5607d28c3a293f88969906e336cff06f.PtpRangeOverMac): An instance of the PtpRangeOverMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_5607d28c3a293f88969906e336cff06f import (
            PtpRangeOverMac,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PtpRangeOverMac", None) is not None:
                return self._properties.get("PtpRangeOverMac")
        return PtpRangeOverMac(self)

    @property
    def VicClientRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_602826acb0e2c96884c01f27517806af.VicClientRange): An instance of the VicClientRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_602826acb0e2c96884c01f27517806af import (
            VicClientRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VicClientRange", None) is not None:
                return self._properties.get("VicClientRange")
        return VicClientRange(self)

    @property
    def VlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_efaa975cddab1aa9354951af05e865f9.VlanRange): An instance of the VlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_efaa975cddab1aa9354951af05e865f9 import (
            VlanRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VlanRange", None) is not None:
                return self._properties.get("VlanRange")
        return VlanRange(self)._select()

    def add(self):
        """Adds a new range resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved range resources using find and the newly added range resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained range resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all range resources from the server.

        Returns
        -------
        - self: This instance with matching range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the range resources from the server available through an iterator or index

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

    def Ipv6SendNdpNS(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ipv6SendNdpNS operation on the server.

        Send NS on NDP for IPv6 ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ipv6SendNdpNS(Arg2=number, async_operation=bool)
        ------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ipv6SendNdpNS(Arg2=number, Arg3=enum, async_operation=bool)
        -----------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
        - Arg3 (str(async | sync)): IPv6 NDP rate for NS messages.
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
        return self._execute("ipv6SendNdpNS", payload=payload, response_object=None)

    def Ipv6SendNdpRS(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ipv6SendNdpRS operation on the server.

        Send RS on NDP for IPv6 ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ipv6SendNdpRS(Arg2=number, async_operation=bool)
        ------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ipv6SendNdpRS(Arg2=number, Arg3=enum, async_operation=bool)
        -----------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
        - Arg3 (str(async | sync)): IPv6 NDP rate for RS messages.
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
        return self._execute("ipv6SendNdpRS", payload=payload, response_object=None)

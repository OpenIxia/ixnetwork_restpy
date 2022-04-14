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


class EsmcRange(Base):
    """
    The EsmcRange class encapsulates a list of esmcRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the EsmcRange.find() method.
    The list can be managed by using the EsmcRange.add() and EsmcRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "esmcRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "FlagMode": "flagMode",
        "Name": "name",
        "ObjectId": "objectId",
        "Ql": "ql",
        "Rate": "rate",
        "WaitId": "waitId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EsmcRange, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FlagMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The operation of the SSM header Event flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlagMode"])

    @FlagMode.setter
    def FlagMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlagMode"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def Ql(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The SSM clock quality level(QL) code.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ql"])

    @Ql.setter
    def Ql(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ql"], value)

    @property
    def Rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SSM message transmit rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rate"])

    @Rate.setter
    def Rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rate"], value)

    @property
    def WaitId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This value is true if supplicant is waiting for RequestId from DUT part.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WaitId"])

    @WaitId.setter
    def WaitId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WaitId"], value)

    def update(
        self, Enabled=None, FlagMode=None, Name=None, Ql=None, Rate=None, WaitId=None
    ):
        # type: (bool, str, str, str, int, bool) -> EsmcRange
        """Updates esmcRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FlagMode (str): The operation of the SSM header Event flag.
        - Name (str): Name of range
        - Ql (str): The SSM clock quality level(QL) code.
        - Rate (number): SSM message transmit rate.
        - WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self, Enabled=None, FlagMode=None, Name=None, Ql=None, Rate=None, WaitId=None
    ):
        # type: (bool, str, str, str, int, bool) -> EsmcRange
        """Adds a new esmcRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FlagMode (str): The operation of the SSM header Event flag.
        - Name (str): Name of range
        - Ql (str): The SSM clock quality level(QL) code.
        - Rate (number): SSM message transmit rate.
        - WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Returns
        -------
        - self: This instance with all currently retrieved esmcRange resources using find and the newly added esmcRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained esmcRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        FlagMode=None,
        Name=None,
        ObjectId=None,
        Ql=None,
        Rate=None,
        WaitId=None,
    ):
        # type: (bool, str, str, str, str, int, bool) -> EsmcRange
        """Finds and retrieves esmcRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve esmcRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all esmcRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FlagMode (str): The operation of the SSM header Event flag.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Ql (str): The SSM clock quality level(QL) code.
        - Rate (number): SSM message transmit rate.
        - WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Returns
        -------
        - self: This instance with matching esmcRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of esmcRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the esmcRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        apply(async_operation=bool)
        ---------------------------
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
        return self._execute("apply", payload=payload, response_object=None)

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

    def ESMCStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the eSMCStart operation on the server.

        Start ESMC

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        eSMCStart(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        eSMCStart(Arg2=enum, async_operation=bool)
        ------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/esmcRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/vepaEndpoint/range/esmcRange,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/ethernetEndpoint/range/esmcRange]
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
        return self._execute("eSMCStart", payload=payload, response_object=None)

    def ESMCStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the eSMCStop operation on the server.

        Stop ESMC

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        eSMCStop(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        eSMCStop(Arg2=enum, async_operation=bool)
        -----------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/esmcRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/vepaEndpoint/range/esmcRange,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/ethernetEndpoint/range/esmcRange]
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
        return self._execute("eSMCStop", payload=payload, response_object=None)

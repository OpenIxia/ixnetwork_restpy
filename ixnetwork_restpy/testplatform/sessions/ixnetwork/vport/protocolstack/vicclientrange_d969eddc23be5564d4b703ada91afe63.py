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


class VicClientRange(Base):
    """Range settings for VIC protocol
    The VicClientRange class encapsulates a list of vicClientRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the VicClientRange.find() method.
    The list can be managed by using the VicClientRange.add() and VicClientRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "vicClientRange"
    _SDM_ATT_MAP = {
        "ChannelIdIncrement": "channelIdIncrement",
        "ChannelIdStart": "channelIdStart",
        "Enabled": "enabled",
        "MacsPerVif": "macsPerVif",
        "Name": "name",
        "ObjectId": "objectId",
        "ProvInfoOui": "provInfoOui",
        "ProvInfoTlvs": "provInfoTlvs",
        "ProvInfoType": "provInfoType",
        "TlvOffset": "tlvOffset",
        "VifActive": "vifActive",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(VicClientRange, self).__init__(parent, list_op)

    @property
    def ChannelIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for channel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChannelIdIncrement"])

    @ChannelIdIncrement.setter
    def ChannelIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChannelIdIncrement"], value)

    @property
    def ChannelIdStart(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The channel ID within VIC session.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChannelIdStart"])

    @ChannelIdStart.setter
    def ChannelIdStart(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChannelIdStart"], value)

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
    def MacsPerVif(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of MAC interfaces managed by a single VIF object.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacsPerVif"])

    @MacsPerVif.setter
    def MacsPerVif(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacsPerVif"], value)

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
    def ProvInfoOui(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IEEE OUI owning the provisioning information type space.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProvInfoOui"])

    @ProvInfoOui.setter
    def ProvInfoOui(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProvInfoOui"], value)

    @property
    def ProvInfoTlvs(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/vicClientGlobals/vicOptionSet): The provisioning TLVs associated with this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProvInfoTlvs"])

    @ProvInfoTlvs.setter
    def ProvInfoTlvs(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProvInfoTlvs"], value)

    @property
    def ProvInfoType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of the provisioning information (defined in each namespace).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProvInfoType"])

    @ProvInfoType.setter
    def ProvInfoType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProvInfoType"], value)

    @property
    def TlvOffset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of TLV increments to apply before using the TLV values for this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TlvOffset"])

    @TlvOffset.setter
    def TlvOffset(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TlvOffset"], value)

    @property
    def VifActive(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The initial state of this interface set: true for Active, false for Standby.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VifActive"])

    @VifActive.setter
    def VifActive(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VifActive"], value)

    def update(
        self,
        ChannelIdIncrement=None,
        ChannelIdStart=None,
        Enabled=None,
        MacsPerVif=None,
        Name=None,
        ProvInfoOui=None,
        ProvInfoTlvs=None,
        ProvInfoType=None,
        TlvOffset=None,
        VifActive=None,
    ):
        # type: (int, int, bool, int, str, str, str, int, int, bool) -> VicClientRange
        """Updates vicClientRange resource on the server.

        Args
        ----
        - ChannelIdIncrement (number): The increment step for channel ID.
        - ChannelIdStart (number): The channel ID within VIC session.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - MacsPerVif (number): Number of MAC interfaces managed by a single VIF object.
        - Name (str): Name of range
        - ProvInfoOui (str): IEEE OUI owning the provisioning information type space.
        - ProvInfoTlvs (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/vicClientGlobals/vicOptionSet)): The provisioning TLVs associated with this range.
        - ProvInfoType (number): The type of the provisioning information (defined in each namespace).
        - TlvOffset (number): The number of TLV increments to apply before using the TLV values for this range.
        - VifActive (bool): The initial state of this interface set: true for Active, false for Standby.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ChannelIdIncrement=None,
        ChannelIdStart=None,
        Enabled=None,
        MacsPerVif=None,
        Name=None,
        ProvInfoOui=None,
        ProvInfoTlvs=None,
        ProvInfoType=None,
        TlvOffset=None,
        VifActive=None,
    ):
        # type: (int, int, bool, int, str, str, str, int, int, bool) -> VicClientRange
        """Adds a new vicClientRange resource on the server and adds it to the container.

        Args
        ----
        - ChannelIdIncrement (number): The increment step for channel ID.
        - ChannelIdStart (number): The channel ID within VIC session.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - MacsPerVif (number): Number of MAC interfaces managed by a single VIF object.
        - Name (str): Name of range
        - ProvInfoOui (str): IEEE OUI owning the provisioning information type space.
        - ProvInfoTlvs (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/vicClientGlobals/vicOptionSet)): The provisioning TLVs associated with this range.
        - ProvInfoType (number): The type of the provisioning information (defined in each namespace).
        - TlvOffset (number): The number of TLV increments to apply before using the TLV values for this range.
        - VifActive (bool): The initial state of this interface set: true for Active, false for Standby.

        Returns
        -------
        - self: This instance with all currently retrieved vicClientRange resources using find and the newly added vicClientRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vicClientRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ChannelIdIncrement=None,
        ChannelIdStart=None,
        Enabled=None,
        MacsPerVif=None,
        Name=None,
        ObjectId=None,
        ProvInfoOui=None,
        ProvInfoTlvs=None,
        ProvInfoType=None,
        TlvOffset=None,
        VifActive=None,
    ):
        # type: (int, int, bool, int, str, str, str, str, int, int, bool) -> VicClientRange
        """Finds and retrieves vicClientRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vicClientRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vicClientRange resources from the server.

        Args
        ----
        - ChannelIdIncrement (number): The increment step for channel ID.
        - ChannelIdStart (number): The channel ID within VIC session.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - MacsPerVif (number): Number of MAC interfaces managed by a single VIF object.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - ProvInfoOui (str): IEEE OUI owning the provisioning information type space.
        - ProvInfoTlvs (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/vicClientGlobals/vicOptionSet)): The provisioning TLVs associated with this range.
        - ProvInfoType (number): The type of the provisioning information (defined in each namespace).
        - TlvOffset (number): The number of TLV increments to apply before using the TLV values for this range.
        - VifActive (bool): The initial state of this interface set: true for Active, false for Standby.

        Returns
        -------
        - self: This instance with matching vicClientRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vicClientRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vicClientRange resources from the server available through an iterator or index

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

    def VicClientActivate(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientActivate operation on the server.

        Send VIF-ACTIVATE for selected ranges

        vicClientActivate(async_operation=bool)
        ---------------------------------------
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
        return self._execute("vicClientActivate", payload=payload, response_object=None)

    def VicClientCreate(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientCreate operation on the server.

        Send VIF-CREATE for selected ranges

        vicClientCreate(async_operation=bool)
        -------------------------------------
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
        return self._execute("vicClientCreate", payload=payload, response_object=None)

    def VicClientDeactivate(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientDeactivate operation on the server.

        Send VIF-DEACTIVATE for selected ranges

        vicClientDeactivate(async_operation=bool)
        -----------------------------------------
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
            "vicClientDeactivate", payload=payload, response_object=None
        )

    def VicClientDelete(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientDelete operation on the server.

        Send VIF-DELETE for selected ranges

        vicClientDelete(async_operation=bool)
        -------------------------------------
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
        return self._execute("vicClientDelete", payload=payload, response_object=None)

    def VicClientDisable(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientDisable operation on the server.

        Send VIF-DISABLE for selected ranges

        vicClientDisable(async_operation=bool)
        --------------------------------------
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
        return self._execute("vicClientDisable", payload=payload, response_object=None)

    def VicClientEnable(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientEnable operation on the server.

        Send VIF-ENABLE for selected ranges

        vicClientEnable(async_operation=bool)
        -------------------------------------
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
        return self._execute("vicClientEnable", payload=payload, response_object=None)

    def VicClientStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientStart operation on the server.

        Negotiate VIC sessions for selected ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        vicClientStart(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        vicClientStart(Arg2=enum, async_operation=bool)
        -----------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vepaEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vicClient,/vport/protocolStack/ethernetEndpoint/range/vicClientRange,/vport/protocolStack/ethernetEndpoint/vicClient]
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
        return self._execute("vicClientStart", payload=payload, response_object=None)

    def VicClientStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the vicClientStop operation on the server.

        Teardown VIC sessions for selected ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        vicClientStop(async_operation=bool)
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        vicClientStop(Arg2=enum, async_operation=bool)
        ----------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vepaEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vicClient,/vport/protocolStack/ethernetEndpoint/range/vicClientRange,/vport/protocolStack/ethernetEndpoint/vicClient]
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
        return self._execute("vicClientStop", payload=payload, response_object=None)

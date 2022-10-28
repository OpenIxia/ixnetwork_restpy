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


class VsiRange(Base):
    """Manages a range of Virtual Station Interfaces.
    The VsiRange class encapsulates a list of vsiRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the VsiRange.find() method.
    The list can be managed by using the VsiRange.add() and VsiRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "vsiRange"
    _SDM_ATT_MAP = {
        "Count": "count",
        "Enabled": "enabled",
        "FilterInfoFormat": "filterInfoFormat",
        "GatewayAddress": "gatewayAddress",
        "GatewayIncrement": "gatewayIncrement",
        "IpAddress": "ipAddress",
        "IpIncrementBy": "ipIncrementBy",
        "Name": "name",
        "ObjectId": "objectId",
        "PreAssociateMode": "preAssociateMode",
        "Prefix": "prefix",
        "Suspended": "suspended",
        "Uuid": "uuid",
        "UuidIncrementBy": "uuidIncrementBy",
        "VsiFormat": "vsiFormat",
        "VsiIdFormat": "vsiIdFormat",
        "VsiManagerId": "vsiManagerId",
        "VsiTypeId": "vsiTypeId",
        "VsiTypeVersion": "vsiTypeVersion",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(VsiRange, self).__init__(parent, list_op)

    @property
    def VsiFiltersInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vsifiltersinfo_aaa9868e9b18d75d2379e981b80d0b96.VsiFiltersInfo): An instance of the VsiFiltersInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vsifiltersinfo_aaa9868e9b18d75d2379e981b80d0b96 import (
            VsiFiltersInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VsiFiltersInfo", None) is not None:
                return self._properties.get("VsiFiltersInfo")
        return VsiFiltersInfo(self)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of VSIs in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

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
    def FilterInfoFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Dropdown box containing all the possible Filter Info Formats.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterInfoFormat"])

    @FilterInfoFormat.setter
    def FilterInfoFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterInfoFormat"], value)

    @property
    def GatewayAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The start IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayAddress"])

    @GatewayAddress.setter
    def GatewayAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayAddress"], value)

    @property
    def GatewayIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayIncrement"])

    @GatewayIncrement.setter
    def GatewayIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayIncrement"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The start IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpIncrementBy"])

    @IpIncrementBy.setter
    def IpIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpIncrementBy"], value)

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
    def PreAssociateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Dropdown box containing the possible pre-associate modes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PreAssociateMode"])

    @PreAssociateMode.setter
    def PreAssociateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PreAssociateMode"], value)

    @property
    def Prefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Prefix"])

    @Prefix.setter
    def Prefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Prefix"], value)

    @property
    def Suspended(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this is true, the VSI will have the Suspended Flag set in the VDP TLVs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Suspended"])

    @Suspended.setter
    def Suspended(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Suspended"], value)

    @property
    def Uuid(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The UUID for the interface. It is available only when the VSIID format is set to UUID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Uuid"])

    @Uuid.setter
    def Uuid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Uuid"], value)

    @property
    def UuidIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The UUID increment for the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UuidIncrementBy"])

    @UuidIncrementBy.setter
    def UuidIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UuidIncrementBy"], value)

    @property
    def VsiFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This field indicates the type of underlying VSI interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiFormat"])

    @VsiFormat.setter
    def VsiFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiFormat"], value)

    @property
    def VsiIdFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Dropdown box containing the possible VSIID Formats.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiIdFormat"])

    @VsiIdFormat.setter
    def VsiIdFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiIdFormat"], value)

    @property
    def VsiManagerId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Field exposing an IPv6 address identifying the VSI manager ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiManagerId"])

    @VsiManagerId.setter
    def VsiManagerId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiManagerId"], value)

    @property
    def VsiTypeId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: VSI Type ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiTypeId"])

    @VsiTypeId.setter
    def VsiTypeId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiTypeId"], value)

    @property
    def VsiTypeVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: VSI Type Version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VsiTypeVersion"])

    @VsiTypeVersion.setter
    def VsiTypeVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VsiTypeVersion"], value)

    def update(
        self,
        Count=None,
        Enabled=None,
        FilterInfoFormat=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        IpAddress=None,
        IpIncrementBy=None,
        Name=None,
        PreAssociateMode=None,
        Prefix=None,
        Suspended=None,
        Uuid=None,
        UuidIncrementBy=None,
        VsiFormat=None,
        VsiIdFormat=None,
        VsiManagerId=None,
        VsiTypeId=None,
        VsiTypeVersion=None,
    ):
        # type: (int, bool, str, str, str, str, str, str, str, int, bool, str, str, str, str, str, int, int) -> VsiRange
        """Updates vsiRange resource on the server.

        Args
        ----
        - Count (number): The number of VSIs in the range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FilterInfoFormat (str): Dropdown box containing all the possible Filter Info Formats.
        - GatewayAddress (str): The start IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        - GatewayIncrement (str): The increment IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        - IpAddress (str): The start IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        - IpIncrementBy (str): The increment IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        - Name (str): Name of range
        - PreAssociateMode (str): Dropdown box containing the possible pre-associate modes.
        - Prefix (number): Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.
        - Suspended (bool): If this is true, the VSI will have the Suspended Flag set in the VDP TLVs.
        - Uuid (str): The UUID for the interface. It is available only when the VSIID format is set to UUID.
        - UuidIncrementBy (str): The UUID increment for the interface.
        - VsiFormat (str): This field indicates the type of underlying VSI interface.
        - VsiIdFormat (str): Dropdown box containing the possible VSIID Formats.
        - VsiManagerId (str): Field exposing an IPv6 address identifying the VSI manager ID.
        - VsiTypeId (number): VSI Type ID.
        - VsiTypeVersion (number): VSI Type Version.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Count=None,
        Enabled=None,
        FilterInfoFormat=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        IpAddress=None,
        IpIncrementBy=None,
        Name=None,
        PreAssociateMode=None,
        Prefix=None,
        Suspended=None,
        Uuid=None,
        UuidIncrementBy=None,
        VsiFormat=None,
        VsiIdFormat=None,
        VsiManagerId=None,
        VsiTypeId=None,
        VsiTypeVersion=None,
    ):
        # type: (int, bool, str, str, str, str, str, str, str, int, bool, str, str, str, str, str, int, int) -> VsiRange
        """Adds a new vsiRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The number of VSIs in the range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FilterInfoFormat (str): Dropdown box containing all the possible Filter Info Formats.
        - GatewayAddress (str): The start IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        - GatewayIncrement (str): The increment IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        - IpAddress (str): The start IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        - IpIncrementBy (str): The increment IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        - Name (str): Name of range
        - PreAssociateMode (str): Dropdown box containing the possible pre-associate modes.
        - Prefix (number): Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.
        - Suspended (bool): If this is true, the VSI will have the Suspended Flag set in the VDP TLVs.
        - Uuid (str): The UUID for the interface. It is available only when the VSIID format is set to UUID.
        - UuidIncrementBy (str): The UUID increment for the interface.
        - VsiFormat (str): This field indicates the type of underlying VSI interface.
        - VsiIdFormat (str): Dropdown box containing the possible VSIID Formats.
        - VsiManagerId (str): Field exposing an IPv6 address identifying the VSI manager ID.
        - VsiTypeId (number): VSI Type ID.
        - VsiTypeVersion (number): VSI Type Version.

        Returns
        -------
        - self: This instance with all currently retrieved vsiRange resources using find and the newly added vsiRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vsiRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Count=None,
        Enabled=None,
        FilterInfoFormat=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        IpAddress=None,
        IpIncrementBy=None,
        Name=None,
        ObjectId=None,
        PreAssociateMode=None,
        Prefix=None,
        Suspended=None,
        Uuid=None,
        UuidIncrementBy=None,
        VsiFormat=None,
        VsiIdFormat=None,
        VsiManagerId=None,
        VsiTypeId=None,
        VsiTypeVersion=None,
    ):
        # type: (int, bool, str, str, str, str, str, str, str, str, int, bool, str, str, str, str, str, int, int) -> VsiRange
        """Finds and retrieves vsiRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vsiRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vsiRange resources from the server.

        Args
        ----
        - Count (number): The number of VSIs in the range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FilterInfoFormat (str): Dropdown box containing all the possible Filter Info Formats.
        - GatewayAddress (str): The start IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        - GatewayIncrement (str): The increment IP address for the interface gateway. It is available when the VSIID Format or the VSI Format are set to IP.
        - IpAddress (str): The start IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        - IpIncrementBy (str): The increment IP address for the interface. It is available when the VSIID Format or the VSI Format are set to IP.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - PreAssociateMode (str): Dropdown box containing the possible pre-associate modes.
        - Prefix (number): Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.
        - Suspended (bool): If this is true, the VSI will have the Suspended Flag set in the VDP TLVs.
        - Uuid (str): The UUID for the interface. It is available only when the VSIID format is set to UUID.
        - UuidIncrementBy (str): The UUID increment for the interface.
        - VsiFormat (str): This field indicates the type of underlying VSI interface.
        - VsiIdFormat (str): Dropdown box containing the possible VSIID Formats.
        - VsiManagerId (str): Field exposing an IPv6 address identifying the VSI manager ID.
        - VsiTypeId (number): VSI Type ID.
        - VsiTypeVersion (number): VSI Type Version.

        Returns
        -------
        - self: This instance with matching vsiRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vsiRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vsiRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ChangeParentRange(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the changeParentRange operation on the server.

        changeParentRange(Target=href, async_operation=bool)
        ----------------------------------------------------
        - Target (str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/vepaEndpoint/range/evbStationRange/erRange)):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("changeParentRange", payload=payload, response_object=None)

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

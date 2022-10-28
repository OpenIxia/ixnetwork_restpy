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


class RadiusRange(Base):
    """Represents a RADIUS range.
    The RadiusRange class encapsulates a list of radiusRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the RadiusRange.find() method.
    The list can be managed by using the RadiusRange.add() and RadiusRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "radiusRange"
    _SDM_ATT_MAP = {
        "AccountingPort": "accountingPort",
        "AccountingServer": "accountingServer",
        "AuthenticationPort": "authenticationPort",
        "AuthenticationServer": "authenticationServer",
        "EnableAccounting": "enableAccounting",
        "Enabled": "enabled",
        "Name": "name",
        "ObjectId": "objectId",
        "Retries": "retries",
        "Secret": "secret",
        "Timeout": "timeout",
        "TunnelAttributeSet": "tunnelAttributeSet",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RadiusRange, self).__init__(parent, list_op)

    @property
    def AccountingPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Accounting UDP port
        """
        return self._get_attribute(self._SDM_ATT_MAP["AccountingPort"])

    @AccountingPort.setter
    def AccountingPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AccountingPort"], value)

    @property
    def AccountingServer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: RADIUS Accounting Server, specified as IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP["AccountingServer"])

    @AccountingServer.setter
    def AccountingServer(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AccountingServer"], value)

    @property
    def AuthenticationPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Authentication UDP port
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuthenticationPort"])

    @AuthenticationPort.setter
    def AuthenticationPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuthenticationPort"], value)

    @property
    def AuthenticationServer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: RADIUS Authentication Server, specified as IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuthenticationServer"])

    @AuthenticationServer.setter
    def AuthenticationServer(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuthenticationServer"], value)

    @property
    def EnableAccounting(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables support for RADIUS accounting
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAccounting"])

    @EnableAccounting.setter
    def EnableAccounting(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAccounting"], value)

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
    def Retries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: RADIUS retry value
        """
        return self._get_attribute(self._SDM_ATT_MAP["Retries"])

    @Retries.setter
    def Retries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Retries"], value)

    @property
    def Secret(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Shared secret used by Ixia RADIUS client and RADIUS server
        """
        return self._get_attribute(self._SDM_ATT_MAP["Secret"])

    @Secret.setter
    def Secret(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Secret"], value)

    @property
    def Timeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: RADIUS timeout value
        """
        return self._get_attribute(self._SDM_ATT_MAP["Timeout"])

    @Timeout.setter
    def Timeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Timeout"], value)

    @property
    def TunnelAttributeSet(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/radiusGlobals/dhcpOptionSet): Defines the RADIUS tunnel attributes
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelAttributeSet"])

    @TunnelAttributeSet.setter
    def TunnelAttributeSet(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TunnelAttributeSet"], value)

    def update(
        self,
        AccountingPort=None,
        AccountingServer=None,
        AuthenticationPort=None,
        AuthenticationServer=None,
        EnableAccounting=None,
        Enabled=None,
        Name=None,
        Retries=None,
        Secret=None,
        Timeout=None,
        TunnelAttributeSet=None,
    ):
        # type: (int, str, int, str, bool, bool, str, int, str, int, str) -> RadiusRange
        """Updates radiusRange resource on the server.

        Args
        ----
        - AccountingPort (number): Accounting UDP port
        - AccountingServer (str): RADIUS Accounting Server, specified as IP address
        - AuthenticationPort (number): Authentication UDP port
        - AuthenticationServer (str): RADIUS Authentication Server, specified as IP address
        - EnableAccounting (bool): Enables support for RADIUS accounting
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - Retries (number): RADIUS retry value
        - Secret (str): Shared secret used by Ixia RADIUS client and RADIUS server
        - Timeout (number): RADIUS timeout value
        - TunnelAttributeSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/radiusGlobals/dhcpOptionSet)): Defines the RADIUS tunnel attributes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AccountingPort=None,
        AccountingServer=None,
        AuthenticationPort=None,
        AuthenticationServer=None,
        EnableAccounting=None,
        Enabled=None,
        Name=None,
        Retries=None,
        Secret=None,
        Timeout=None,
        TunnelAttributeSet=None,
    ):
        # type: (int, str, int, str, bool, bool, str, int, str, int, str) -> RadiusRange
        """Adds a new radiusRange resource on the server and adds it to the container.

        Args
        ----
        - AccountingPort (number): Accounting UDP port
        - AccountingServer (str): RADIUS Accounting Server, specified as IP address
        - AuthenticationPort (number): Authentication UDP port
        - AuthenticationServer (str): RADIUS Authentication Server, specified as IP address
        - EnableAccounting (bool): Enables support for RADIUS accounting
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - Retries (number): RADIUS retry value
        - Secret (str): Shared secret used by Ixia RADIUS client and RADIUS server
        - Timeout (number): RADIUS timeout value
        - TunnelAttributeSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/radiusGlobals/dhcpOptionSet)): Defines the RADIUS tunnel attributes

        Returns
        -------
        - self: This instance with all currently retrieved radiusRange resources using find and the newly added radiusRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained radiusRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AccountingPort=None,
        AccountingServer=None,
        AuthenticationPort=None,
        AuthenticationServer=None,
        EnableAccounting=None,
        Enabled=None,
        Name=None,
        ObjectId=None,
        Retries=None,
        Secret=None,
        Timeout=None,
        TunnelAttributeSet=None,
    ):
        # type: (int, str, int, str, bool, bool, str, str, int, str, int, str) -> RadiusRange
        """Finds and retrieves radiusRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve radiusRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all radiusRange resources from the server.

        Args
        ----
        - AccountingPort (number): Accounting UDP port
        - AccountingServer (str): RADIUS Accounting Server, specified as IP address
        - AuthenticationPort (number): Authentication UDP port
        - AuthenticationServer (str): RADIUS Authentication Server, specified as IP address
        - EnableAccounting (bool): Enables support for RADIUS accounting
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Retries (number): RADIUS retry value
        - Secret (str): Shared secret used by Ixia RADIUS client and RADIUS server
        - Timeout (number): RADIUS timeout value
        - TunnelAttributeSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/radiusGlobals/dhcpOptionSet)): Defines the RADIUS tunnel attributes

        Returns
        -------
        - self: This instance with matching radiusRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of radiusRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the radiusRange resources from the server available through an iterator or index

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

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


class WebAuthRange(Base):
    """Web Authentication Range Options
    The WebAuthRange class encapsulates a list of webAuthRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the WebAuthRange.find() method.
    The list can be managed by using the WebAuthRange.add() and WebAuthRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "webAuthRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "Expect": "expect",
        "InputValue1": "inputValue1",
        "InputValue2": "inputValue2",
        "InputValue3": "inputValue3",
        "Name": "name",
        "ObjectId": "objectId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(WebAuthRange, self).__init__(parent, list_op)

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
    def Expect(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Statistics will be maintained for expected/actual success/failure
        """
        return self._get_attribute(self._SDM_ATT_MAP["Expect"])

    @Expect.setter
    def Expect(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Expect"], value)

    @property
    def InputValue1(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputValue1"])

    @InputValue1.setter
    def InputValue1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InputValue1"], value)

    @property
    def InputValue2(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputValue2"])

    @InputValue2.setter
    def InputValue2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InputValue2"], value)

    @property
    def InputValue3(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputValue3"])

    @InputValue3.setter
    def InputValue3(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InputValue3"], value)

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

    def update(
        self,
        Enabled=None,
        Expect=None,
        InputValue1=None,
        InputValue2=None,
        InputValue3=None,
        Name=None,
    ):
        # type: (bool, str, str, str, str, str) -> WebAuthRange
        """Updates webAuthRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Expect (str): Statistics will be maintained for expected/actual success/failure
        - InputValue1 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - InputValue2 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - InputValue3 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        Expect=None,
        InputValue1=None,
        InputValue2=None,
        InputValue3=None,
        Name=None,
    ):
        # type: (bool, str, str, str, str, str) -> WebAuthRange
        """Adds a new webAuthRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Expect (str): Statistics will be maintained for expected/actual success/failure
        - InputValue1 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - InputValue2 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - InputValue3 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - Name (str): Name of range

        Returns
        -------
        - self: This instance with all currently retrieved webAuthRange resources using find and the newly added webAuthRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained webAuthRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        Expect=None,
        InputValue1=None,
        InputValue2=None,
        InputValue3=None,
        Name=None,
        ObjectId=None,
    ):
        # type: (bool, str, str, str, str, str, str) -> WebAuthRange
        """Finds and retrieves webAuthRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve webAuthRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all webAuthRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Expect (str): Statistics will be maintained for expected/actual success/failure
        - InputValue1 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - InputValue2 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - InputValue3 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching webAuthRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of webAuthRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the webAuthRange resources from the server available through an iterator or index

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

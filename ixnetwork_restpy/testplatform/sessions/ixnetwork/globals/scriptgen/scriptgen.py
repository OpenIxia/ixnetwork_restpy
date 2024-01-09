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


class Scriptgen(Base):
    """Container for scriptgen options
    The Scriptgen class encapsulates a required scriptgen resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "scriptgen"
    _SDM_ATT_MAP = {
        "ConnectHostname": "connectHostname",
        "ConnectPort": "connectPort",
        "ConnectVersion": "connectVersion",
        "IncludeAPIKey": "includeAPIKey",
        "IncludeConnect": "includeConnect",
        "IncludeSessionId": "includeSessionId",
        "IncludeTestComposer": "includeTestComposer",
        "IncludeUsernamePasswd": "includeUsernamePasswd",
        "Language": "language",
        "LinePerAttribute": "linePerAttribute",
        "OverwriteScriptFilename": "overwriteScriptFilename",
        "ScriptFilename": "scriptFilename",
        "SerializationType": "serializationType",
    }
    _SDM_ENUM_MAP = {
        "language": ["perl", "python", "ruby", "tcl"],
        "serializationType": ["base64", "ixNet"],
    }

    def __init__(self, parent, list_op=False):
        super(Scriptgen, self).__init__(parent, list_op)

    @property
    def Base64CodeOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.scriptgen.base64codeoptions.base64codeoptions.Base64CodeOptions): An instance of the Base64CodeOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.scriptgen.base64codeoptions.base64codeoptions import (
            Base64CodeOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Base64CodeOptions", None) is not None:
                return self._properties.get("Base64CodeOptions")
        return Base64CodeOptions(self)._select()

    @property
    def IxNetCodeOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.scriptgen.ixnetcodeoptions.ixnetcodeoptions.IxNetCodeOptions): An instance of the IxNetCodeOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.scriptgen.ixnetcodeoptions.ixnetcodeoptions import (
            IxNetCodeOptions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IxNetCodeOptions", None) is not None:
                return self._properties.get("IxNetCodeOptions")
        return IxNetCodeOptions(self)._select()

    @property
    def ConnectHostname(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The hostname to be used in the connect command
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectHostname"])

    @ConnectHostname.setter
    def ConnectHostname(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectHostname"], value)

    @property
    def ConnectPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The port number to be used in the connect command
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectPort"])

    @ConnectPort.setter
    def ConnectPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectPort"], value)

    @property
    def ConnectVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The version number to be used in the connect command
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectVersion"])

    @ConnectVersion.setter
    def ConnectVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectVersion"], value)

    @property
    def IncludeAPIKey(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: API-Key argument will be generated as part of HLT connect call
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeAPIKey"])

    @IncludeAPIKey.setter
    def IncludeAPIKey(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeAPIKey"], value)

    @property
    def IncludeConnect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include the connect command
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeConnect"])

    @IncludeConnect.setter
    def IncludeConnect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeConnect"], value)

    @property
    def IncludeSessionId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Session-ID argument will be generated as part of HLT connect call
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeSessionId"])

    @IncludeSessionId.setter
    def IncludeSessionId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeSessionId"], value)

    @property
    def IncludeTestComposer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include test composer code
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTestComposer"])

    @IncludeTestComposer.setter
    def IncludeTestComposer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTestComposer"], value)

    @property
    def IncludeUsernamePasswd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Username-password argument will be generated as part of HLT connect call
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeUsernamePasswd"])

    @IncludeUsernamePasswd.setter
    def IncludeUsernamePasswd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeUsernamePasswd"], value)

    @property
    def Language(self):
        # type: () -> str
        """
        Returns
        -------
        - str(perl | python | ruby | tcl): Select the target scriptgen language
        """
        return self._get_attribute(self._SDM_ATT_MAP["Language"])

    @Language.setter
    def Language(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Language"], value)

    @property
    def LinePerAttribute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the scriptgen output will show each attribute on a separate line
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinePerAttribute"])

    @LinePerAttribute.setter
    def LinePerAttribute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinePerAttribute"], value)

    @property
    def OverwriteScriptFilename(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the file indicated by the script filename will be overwritten
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverwriteScriptFilename"])

    @OverwriteScriptFilename.setter
    def OverwriteScriptFilename(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverwriteScriptFilename"], value)

    @property
    def ScriptFilename(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the target scriptgen file
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScriptFilename"])

    @ScriptFilename.setter
    def ScriptFilename(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScriptFilename"], value)

    @property
    def SerializationType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(base64 | ixNet): The scriptgen serialization type
        """
        return self._get_attribute(self._SDM_ATT_MAP["SerializationType"])

    @SerializationType.setter
    def SerializationType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SerializationType"], value)

    def update(
        self,
        ConnectHostname=None,
        ConnectPort=None,
        ConnectVersion=None,
        IncludeAPIKey=None,
        IncludeConnect=None,
        IncludeSessionId=None,
        IncludeTestComposer=None,
        IncludeUsernamePasswd=None,
        Language=None,
        LinePerAttribute=None,
        OverwriteScriptFilename=None,
        ScriptFilename=None,
        SerializationType=None,
    ):
        # type: (str, int, str, bool, bool, bool, bool, bool, str, bool, bool, str, str) -> Scriptgen
        """Updates scriptgen resource on the server.

        Args
        ----
        - ConnectHostname (str): The hostname to be used in the connect command
        - ConnectPort (number): The port number to be used in the connect command
        - ConnectVersion (str): The version number to be used in the connect command
        - IncludeAPIKey (bool): API-Key argument will be generated as part of HLT connect call
        - IncludeConnect (bool): Flag to include the connect command
        - IncludeSessionId (bool): Session-ID argument will be generated as part of HLT connect call
        - IncludeTestComposer (bool): Flag to include test composer code
        - IncludeUsernamePasswd (bool): Username-password argument will be generated as part of HLT connect call
        - Language (str(perl | python | ruby | tcl)): Select the target scriptgen language
        - LinePerAttribute (bool): If true the scriptgen output will show each attribute on a separate line
        - OverwriteScriptFilename (bool): If true the file indicated by the script filename will be overwritten
        - ScriptFilename (str): The name of the target scriptgen file
        - SerializationType (str(base64 | ixNet)): The scriptgen serialization type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ConnectHostname=None,
        ConnectPort=None,
        ConnectVersion=None,
        IncludeAPIKey=None,
        IncludeConnect=None,
        IncludeSessionId=None,
        IncludeTestComposer=None,
        IncludeUsernamePasswd=None,
        Language=None,
        LinePerAttribute=None,
        OverwriteScriptFilename=None,
        ScriptFilename=None,
        SerializationType=None,
    ):
        # type: (str, int, str, bool, bool, bool, bool, bool, str, bool, bool, str, str) -> Scriptgen
        """Finds and retrieves scriptgen resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve scriptgen resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all scriptgen resources from the server.

        Args
        ----
        - ConnectHostname (str): The hostname to be used in the connect command
        - ConnectPort (number): The port number to be used in the connect command
        - ConnectVersion (str): The version number to be used in the connect command
        - IncludeAPIKey (bool): API-Key argument will be generated as part of HLT connect call
        - IncludeConnect (bool): Flag to include the connect command
        - IncludeSessionId (bool): Session-ID argument will be generated as part of HLT connect call
        - IncludeTestComposer (bool): Flag to include test composer code
        - IncludeUsernamePasswd (bool): Username-password argument will be generated as part of HLT connect call
        - Language (str(perl | python | ruby | tcl)): Select the target scriptgen language
        - LinePerAttribute (bool): If true the scriptgen output will show each attribute on a separate line
        - OverwriteScriptFilename (bool): If true the file indicated by the script filename will be overwritten
        - ScriptFilename (str): The name of the target scriptgen file
        - SerializationType (str(base64 | ixNet)): The scriptgen serialization type

        Returns
        -------
        - self: This instance with matching scriptgen resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of scriptgen data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the scriptgen resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Generate(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the generate operation on the server.

        Generate a script of the currently loaded configuration using the options in the /globals/scriptgen hierarchy.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        generate(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        generate(Arg2=href, async_operation=bool)
        -----------------------------------------
        - Arg2 (obj(ixnetwork_restpy.files.Files)): A valid writeTo file handle the script will be written to.
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
        return self._execute("generate", payload=payload, response_object=None)

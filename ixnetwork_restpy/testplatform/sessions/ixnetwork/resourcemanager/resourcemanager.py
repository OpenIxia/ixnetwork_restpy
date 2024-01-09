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


class ResourceManager(Base):
    """Top level node for resource manager API
    The ResourceManager class encapsulates a required resourceManager resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "resourceManager"
    _SDM_ATT_MAP = {
        "GenerateAll": "generateAll",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ResourceManager, self).__init__(parent, list_op)

    @property
    def GenerateAll(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls the attributes to be generated during the export API calls (available on this node). If this is true, then 'generated', 'readonly', 'internal' etc attributes are also generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GenerateAll"])

    @GenerateAll.setter
    def GenerateAll(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GenerateAll"], value)

    def update(self, GenerateAll=None):
        # type: (bool) -> ResourceManager
        """Updates resourceManager resource on the server.

        Args
        ----
        - GenerateAll (bool): Controls the attributes to be generated during the export API calls (available on this node). If this is true, then 'generated', 'readonly', 'internal' etc attributes are also generated.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, GenerateAll=None):
        # type: (bool) -> ResourceManager
        """Finds and retrieves resourceManager resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve resourceManager resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all resourceManager resources from the server.

        Args
        ----
        - GenerateAll (bool): Controls the attributes to be generated during the export API calls (available on this node). If this is true, then 'generated', 'readonly', 'internal' etc attributes are also generated.

        Returns
        -------
        - self: This instance with matching resourceManager resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of resourceManager data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the resourceManager resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ExportConfig(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the exportConfig operation on the server.

        Export the entire configuration or fragments of it in a text based format.

        exportConfig(Arg2=list, Arg3=bool, Arg4=enum, async_operation=bool)string
        -------------------------------------------------------------------------
        - Arg2 (list(str)): A list of xpaths each of which is a starting point in the configuration. The only supported xpath notation is by index or descendant-or-self:*. To export the entire configuration specify /descendant-or-self:*
        - Arg3 (bool): True to include attributes that are equal to the default in the export, false to exclude them
        - Arg4 (str(json)): The format of the exported configuration
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: JSON configuration as a string

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
        return self._execute("exportConfig", payload=payload, response_object=None)

    def ExportConfigFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the exportConfigFile operation on the server.

        Export the entire configuration or fragments of it in a text based format.

        exportConfigFile(Arg2=list, Arg3=bool, Arg4=enum, Arg5=href, async_operation=bool)
        ----------------------------------------------------------------------------------
        - Arg2 (list(str)): A list of xpaths each of which is a starting point in the configuration. The only supported xpath notation is by index or descendant-or-self:*. To export the entire configuration specify /descendant-or-self:*
        - Arg3 (bool): True to include attributes that are equal to the default in the export, false to exclude them
        - Arg4 (str(json)): The format of the exported configuration
        - Arg5 (obj(ixnetwork_restpy.files.Files)): The file object to write the configuration to
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
        return self._execute("exportConfigFile", payload=payload, response_object=None)

    def GetSdmTreeNodesForExport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getSdmTreeNodesForExport operation on the server.

        getSdmTreeNodesForExport(Arg2=string, async_operation=bool)string
        -----------------------------------------------------------------
        - Arg2 (str):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
            "getSdmTreeNodesForExport", payload=payload, response_object=None
        )

    def ImportConfig(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the importConfig operation on the server.

        Create or update the test tool configuration.

        importConfig(Arg2=string, Arg3=bool, async_operation=bool)list
        --------------------------------------------------------------
        - Arg2 (str): The configuration as a string
        - Arg3 (bool): True to create a new configuration, false to update the current configuration
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): A list of errors that occurred during import

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
        return self._execute("importConfig", payload=payload, response_object=None)

    def ImportConfigFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the importConfigFile operation on the server.

        Create or update the test tool configuration.

        importConfigFile(Arg2=href, Arg3=bool, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (obj(ixnetwork_restpy.files.Files)): The file to read the configuration from
        - Arg3 (bool): True to create a new configuration, false to update the current configuration
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): A list of errors that occurred during the import

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
        return self._execute("importConfigFile", payload=payload, response_object=None)

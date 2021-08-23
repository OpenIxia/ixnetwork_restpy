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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files
from typing import List, Any, Union


class DcbxAppProtocolAtt(Base):
    """Application Protocol Id
    The DcbxAppProtocolAtt class encapsulates a list of dcbxAppProtocolAtt resources that are managed by the user.
    A list of resources can be retrieved from the server using the DcbxAppProtocolAtt.find() method.
    The list can be managed by using the DcbxAppProtocolAtt.add() and DcbxAppProtocolAtt.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxAppProtocolAtt'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'ObjectId': 'objectId',
        'PriorityMap': 'priorityMap',
        'ProtocolId': 'protocolId',
        'Sel': 'sel',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(DcbxAppProtocolAtt, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Include or exclude the mapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PriorityMap(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Priority value
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityMap'])
    @PriorityMap.setter
    def PriorityMap(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP['PriorityMap'], value)

    @property
    def ProtocolId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Protocol ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolId'])
    @ProtocolId.setter
    def ProtocolId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ProtocolId'], value)

    @property
    def Sel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sel'])
    @Sel.setter
    def Sel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Sel'], value)

    def update(self, Enabled=None, PriorityMap=None, ProtocolId=None, Sel=None):
        # type: (bool, List[int], str, int) -> DcbxAppProtocolAtt
        """Updates dcbxAppProtocolAtt resource on the server.

        Args
        ----
        - Enabled (bool): Include or exclude the mapping.
        - PriorityMap (list(number)): Priority value
        - ProtocolId (str): Protocol ID.
        - Sel (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, PriorityMap=None, ProtocolId=None, Sel=None):
        # type: (bool, List[int], str, int) -> DcbxAppProtocolAtt
        """Adds a new dcbxAppProtocolAtt resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Include or exclude the mapping.
        - PriorityMap (list(number)): Priority value
        - ProtocolId (str): Protocol ID.
        - Sel (number): 

        Returns
        -------
        - self: This instance with all currently retrieved dcbxAppProtocolAtt resources using find and the newly added dcbxAppProtocolAtt resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dcbxAppProtocolAtt resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, ObjectId=None, PriorityMap=None, ProtocolId=None, Sel=None):
        # type: (bool, str, List[int], str, int) -> DcbxAppProtocolAtt
        """Finds and retrieves dcbxAppProtocolAtt resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxAppProtocolAtt resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxAppProtocolAtt resources from the server.

        Args
        ----
        - Enabled (bool): Include or exclude the mapping.
        - ObjectId (str): Unique identifier for this object
        - PriorityMap (list(number)): Priority value
        - ProtocolId (str): Protocol ID.
        - Sel (number): 

        Returns
        -------
        - self: This instance with matching dcbxAppProtocolAtt resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxAppProtocolAtt data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxAppProtocolAtt resources from the server available through an iterator or index

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

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


class Value(Base):
    """Tlv value container
    The Value class encapsulates a required value resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'value'
    _SDM_ATT_MAP = {
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Value, self).__init__(parent, list_op)

    @property
    def Object(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object_1ba6063c8cfb61359d0cafa499ed49e4.Object): An instance of the Object class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object_1ba6063c8cfb61359d0cafa499ed49e4 import Object
        if self._properties.get('Object', None) is not None:
            return self._properties.get('Object')
        else:
            return Object(self)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the object
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Name=None):
        # type: (str) -> Value
        """Updates value resource on the server.

        Args
        ----
        - Name (str): The name of the object

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def GetMVPropertyCandidatesToSharePatternWith(self, *args, **kwargs):
        """Executes the getMVPropertyCandidatesToSharePatternWith operation on the server.

        Returns a list of MVProperties this pattern can be shared with.

        getMVPropertyCandidatesToSharePatternWith(async_operation=bool)list
        -------------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(list[str[None | /api/v1/sessions/1/ixnetwork//.../*]]): list of MVProperties this pattern can be shared with

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getMVPropertyCandidatesToSharePatternWith', payload=payload, response_object=None)

    def GetSharedPatternCandidates(self, *args, **kwargs):
        """Executes the getSharedPatternCandidates operation on the server.

        Returns a list of shared pattern candidates.

        getSharedPatternCandidates(async_operation=bool)list
        ----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(list[str[None | /api/v1/sessions/1/ixnetwork//.../*]]): list of patterns may be shared

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getSharedPatternCandidates', payload=payload, response_object=None)

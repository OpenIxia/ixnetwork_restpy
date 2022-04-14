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


class WriteSetField(Base):
    """NOT DEFINED
    The WriteSetField class encapsulates a required writeSetField resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "writeSetField"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(WriteSetField, self).__init__(parent, list_op)

    @property
    def Fields(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fields_28cbe17a5108f2df364f0596858829d7.Fields): An instance of the Fields class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fields_28cbe17a5108f2df364f0596858829d7 import (
            Fields,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fields", None) is not None:
                return self._properties.get("Fields")
        return Fields(self)._select()

    @property
    def MissFields(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.missfields_2a6ef672a75b7629c32ad54be7848261.MissFields): An instance of the MissFields class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.missfields_2a6ef672a75b7629c32ad54be7848261 import (
            MissFields,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MissFields", None) is not None:
                return self._properties.get("MissFields")
        return MissFields(self)._select()

    def find(self):
        """Finds and retrieves writeSetField resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve writeSetField resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all writeSetField resources from the server.

        Returns
        -------
        - self: This instance with matching writeSetField resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of writeSetField data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the writeSetField resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

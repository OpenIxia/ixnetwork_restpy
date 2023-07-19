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


class PacketOutActionTemplate(Base):
    """Global data for OpenFlow Action Builder template data extension.
    The PacketOutActionTemplate class encapsulates a required packetOutActionTemplate resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "packetOutActionTemplate"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PacketOutActionTemplate, self).__init__(parent, list_op)

    @property
    def ActionTemplate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.actiontemplate_fa40ad00e03788c7e139f3ecbe0f7842.ActionTemplate): An instance of the ActionTemplate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.actiontemplate_fa40ad00e03788c7e139f3ecbe0f7842 import (
            ActionTemplate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ActionTemplate", None) is not None:
                return self._properties.get("ActionTemplate")
        return ActionTemplate(self)

    @property
    def Predefined(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.predefined_240bc09f3e5f74cbccf8ba2d8f664986.Predefined): An instance of the Predefined class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.predefined_240bc09f3e5f74cbccf8ba2d8f664986 import (
            Predefined,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Predefined", None) is not None:
                return self._properties.get("Predefined")
        return Predefined(self)

    def find(self):
        """Finds and retrieves packetOutActionTemplate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve packetOutActionTemplate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all packetOutActionTemplate resources from the server.

        Returns
        -------
        - self: This instance with matching packetOutActionTemplate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of packetOutActionTemplate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the packetOutActionTemplate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

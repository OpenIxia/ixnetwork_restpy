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


class Static(Base):
    """This object controls the static configuration of ports.
    The Static class encapsulates a required static resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "static"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Static, self).__init__(parent, list_op)

    @property
    def Atm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atm_9bbaac5d21c0632b71ee4c92d14864c3.Atm): An instance of the Atm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atm_9bbaac5d21c0632b71ee4c92d14864c3 import (
            Atm,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Atm", None) is not None:
                return self._properties.get("Atm")
        return Atm(self)

    @property
    def Fr(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fr_ebc5d45018c74d53700c88afea530ca2.Fr): An instance of the Fr class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fr_ebc5d45018c74d53700c88afea530ca2 import (
            Fr,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fr", None) is not None:
                return self._properties.get("Fr")
        return Fr(self)

    @property
    def InterfaceGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacegroup_c2c90e7b7cf8bf4a351e197fc18ccb92.InterfaceGroup): An instance of the InterfaceGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacegroup_c2c90e7b7cf8bf4a351e197fc18ccb92 import (
            InterfaceGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InterfaceGroup", None) is not None:
                return self._properties.get("InterfaceGroup")
        return InterfaceGroup(self)

    @property
    def Ip(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ip_205717d3d79aa12a8dcea858982c666e.Ip): An instance of the Ip class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ip_205717d3d79aa12a8dcea858982c666e import (
            Ip,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ip", None) is not None:
                return self._properties.get("Ip")
        return Ip(self)

    @property
    def Lan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_a0c3771a1420d267c519e60205c6a8e6.Lan): An instance of the Lan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_a0c3771a1420d267c519e60205c6a8e6 import (
            Lan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lan", None) is not None:
                return self._properties.get("Lan")
        return Lan(self)

    def find(self):
        """Finds and retrieves static resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve static resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all static resources from the server.

        Returns
        -------
        - self: This instance with matching static resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of static data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the static resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

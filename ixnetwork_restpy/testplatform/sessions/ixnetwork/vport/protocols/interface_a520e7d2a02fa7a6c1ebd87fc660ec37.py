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


class Interface(Base):
    """This object holds the information for a single interface on the mplsTp router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "interface"
    _SDM_ATT_MAP = {
        "DutMacAddress": "dutMacAddress",
        "Enabled": "enabled",
        "Interfaces": "interfaces",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Interface, self).__init__(parent, list_op)

    @property
    def LspPwRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lsppwrange_a99d978c87681e8fd80d5560169a1dcf.LspPwRange): An instance of the LspPwRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lsppwrange_a99d978c87681e8fd80d5560169a1dcf import (
            LspPwRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LspPwRange", None) is not None:
                return self._properties.get("LspPwRange")
        return LspPwRange(self)

    @property
    def DutMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the MAC address of the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutMacAddress"])

    @DutMacAddress.setter
    def DutMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DutMacAddress"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the use of this interface for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Interfaces(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): This signifies the Interface that has been assigned for this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Interfaces"])

    @Interfaces.setter
    def Interfaces(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Interfaces"], value)

    def update(self, DutMacAddress=None, Enabled=None, Interfaces=None):
        # type: (str, bool, str) -> Interface
        """Updates interface resource on the server.

        Args
        ----
        - DutMacAddress (str): This signifies the MAC address of the DUT.
        - Enabled (bool): This signifies the enablement of the use of this interface for the simulated router.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This signifies the Interface that has been assigned for this range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DutMacAddress=None, Enabled=None, Interfaces=None):
        # type: (str, bool, str) -> Interface
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - DutMacAddress (str): This signifies the MAC address of the DUT.
        - Enabled (bool): This signifies the enablement of the use of this interface for the simulated router.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This signifies the Interface that has been assigned for this range.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DutMacAddress=None, Enabled=None, Interfaces=None):
        # type: (str, bool, str) -> Interface
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - DutMacAddress (str): This signifies the MAC address of the DUT.
        - Enabled (bool): This signifies the enablement of the use of this interface for the simulated router.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This signifies the Interface that has been assigned for this range.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

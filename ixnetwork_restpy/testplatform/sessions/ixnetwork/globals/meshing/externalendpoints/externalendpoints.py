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


class ExternalEndpoints(Base):
    """ExternalRedirection Device
    The ExternalEndpoints class encapsulates a list of externalEndpoints resources that are managed by the user.
    A list of resources can be retrieved from the server using the ExternalEndpoints.find() method.
    The list can be managed by using the ExternalEndpoints.add() and ExternalEndpoints.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "externalEndpoints"
    _SDM_ATT_MAP = {
        "Address": "address",
        "IxnAddress": "ixnAddress",
        "Name": "name",
        "Source": "source",
        "SourceIndex": "sourceIndex",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ExternalEndpoints, self).__init__(parent, list_op)

    @property
    def Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IPv4 or IPv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Address"])

    @Address.setter
    def Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Address"], value)

    @property
    def IxnAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IP address of RoCE in the IxNetwork topology.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxnAddress"])

    @IxnAddress.setter
    def IxnAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IxnAddress"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique name of the external device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @property
    def Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/meshing): Protocol of the source endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Source"])

    @Source.setter
    def Source(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Source"], value)

    @property
    def SourceIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Index of the endpoint in the source protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceIndex"])

    @SourceIndex.setter
    def SourceIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceIndex"], value)

    def update(self, Address=None, IxnAddress=None, Source=None, SourceIndex=None):
        # type: (str, str, str, int) -> ExternalEndpoints
        """Updates externalEndpoints resource on the server.

        Args
        ----
        - Address (str): IPv4 or IPv6 address.
        - IxnAddress (str): IP address of RoCE in the IxNetwork topology.
        - Source (str(None | /api/v1/sessions/1/ixnetwork/globals/meshing)): Protocol of the source endpoint.
        - SourceIndex (number): Index of the endpoint in the source protocol.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Address=None, IxnAddress=None, Source=None, SourceIndex=None):
        # type: (str, str, str, int) -> ExternalEndpoints
        """Adds a new externalEndpoints resource on the server and adds it to the container.

        Args
        ----
        - Address (str): IPv4 or IPv6 address.
        - IxnAddress (str): IP address of RoCE in the IxNetwork topology.
        - Source (str(None | /api/v1/sessions/1/ixnetwork/globals/meshing)): Protocol of the source endpoint.
        - SourceIndex (number): Index of the endpoint in the source protocol.

        Returns
        -------
        - self: This instance with all currently retrieved externalEndpoints resources using find and the newly added externalEndpoints resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained externalEndpoints resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self, Address=None, IxnAddress=None, Name=None, Source=None, SourceIndex=None
    ):
        # type: (str, str, str, str, int) -> ExternalEndpoints
        """Finds and retrieves externalEndpoints resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve externalEndpoints resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all externalEndpoints resources from the server.

        Args
        ----
        - Address (str): IPv4 or IPv6 address.
        - IxnAddress (str): IP address of RoCE in the IxNetwork topology.
        - Name (str): Unique name of the external device.
        - Source (str(None | /api/v1/sessions/1/ixnetwork/globals/meshing)): Protocol of the source endpoint.
        - SourceIndex (number): Index of the endpoint in the source protocol.

        Returns
        -------
        - self: This instance with matching externalEndpoints resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of externalEndpoints data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the externalEndpoints resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

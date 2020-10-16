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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class NacVendors(Base):
    """TLV Vendor ID
    The NacVendors class encapsulates a list of nacVendors resources that are managed by the user.
    A list of resources can be retrieved from the server using the NacVendors.find() method.
    The list can be managed by using the NacVendors.add() and NacVendors.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacVendors'
    _SDM_ATT_MAP = {
        'Name': 'name',
        'ObjectId': 'objectId',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(NacVendors, self).__init__(parent)

    @property
    def NacTypes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.vendorref.nactypes.nactypes.NacTypes): An instance of the NacTypes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.vendorref.nactypes.nactypes import NacTypes
        return NacTypes(self)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Vendor Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Value(self):
        """
        Returns
        -------
        - number: Vendor ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Name=None, Value=None):
        """Updates nacVendors resource on the server.

        Args
        ----
        - Name (str): Vendor Name.
        - Value (number): Vendor ID.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, Value=None):
        """Adds a new nacVendors resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Vendor Name.
        - Value (number): Vendor ID.

        Returns
        -------
        - self: This instance with all currently retrieved nacVendors resources using find and the newly added nacVendors resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained nacVendors resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None, ObjectId=None, Value=None):
        """Finds and retrieves nacVendors resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve nacVendors resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all nacVendors resources from the server.

        Args
        ----
        - Name (str): Vendor Name.
        - ObjectId (str): Unique identifier for this object
        - Value (number): Vendor ID.

        Returns
        -------
        - self: This instance with matching nacVendors resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of nacVendors data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the nacVendors resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

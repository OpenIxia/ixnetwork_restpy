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


class EviOpaqueTlv(Base):
    """Configures the opaque value element.
    The EviOpaqueTlv class encapsulates a list of eviOpaqueTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the EviOpaqueTlv.find() method.
    The list can be managed by using the EviOpaqueTlv.add() and EviOpaqueTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'eviOpaqueTlv'
    _SDM_ATT_MAP = {
        'Length': 'length',
        'Type': 'type',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(EviOpaqueTlv, self).__init__(parent)

    @property
    def Length(self):
        """
        Returns
        -------
        - number: The length of the TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])
    @Length.setter
    def Length(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Length'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - number: The type of TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: The value of the TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Length=None, Type=None, Value=None):
        """Updates eviOpaqueTlv resource on the server.

        Args
        ----
        - Length (number): The length of the TLV.
        - Type (number): The type of TLV.
        - Value (str): The value of the TLV.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Length=None, Type=None, Value=None):
        """Adds a new eviOpaqueTlv resource on the server and adds it to the container.

        Args
        ----
        - Length (number): The length of the TLV.
        - Type (number): The type of TLV.
        - Value (str): The value of the TLV.

        Returns
        -------
        - self: This instance with all currently retrieved eviOpaqueTlv resources using find and the newly added eviOpaqueTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained eviOpaqueTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Length=None, Type=None, Value=None):
        """Finds and retrieves eviOpaqueTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eviOpaqueTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eviOpaqueTlv resources from the server.

        Args
        ----
        - Length (number): The length of the TLV.
        - Type (number): The type of TLV.
        - Value (str): The value of the TLV.

        Returns
        -------
        - self: This instance with matching eviOpaqueTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eviOpaqueTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eviOpaqueTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

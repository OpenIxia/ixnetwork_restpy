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


class CustomValue(Base):
    """List of custom values.
    The CustomValue class encapsulates a list of customValue resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomValue.find() method.
    The list can be managed by using the CustomValue.add() and CustomValue.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customValue'
    _SDM_ATT_MAP = {
        'Percentage': 'percentage',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(CustomValue, self).__init__(parent)

    @property
    def Percentage(self):
        """
        Returns
        -------
        - number: How often this value occurs, as a percentage.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Percentage'])
    @Percentage.setter
    def Percentage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Percentage'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - number: Delay value, in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Percentage=None, Value=None):
        """Updates customValue resource on the server.

        Args
        ----
        - Percentage (number): How often this value occurs, as a percentage.
        - Value (number): Delay value, in microseconds.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Percentage=None, Value=None):
        """Adds a new customValue resource on the server and adds it to the container.

        Args
        ----
        - Percentage (number): How often this value occurs, as a percentage.
        - Value (number): Delay value, in microseconds.

        Returns
        -------
        - self: This instance with all currently retrieved customValue resources using find and the newly added customValue resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customValue resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Percentage=None, Value=None):
        """Finds and retrieves customValue resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customValue resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customValue resources from the server.

        Args
        ----
        - Percentage (number): How often this value occurs, as a percentage.
        - Value (number): Delay value, in microseconds.

        Returns
        -------
        - self: This instance with matching customValue resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customValue data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customValue resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

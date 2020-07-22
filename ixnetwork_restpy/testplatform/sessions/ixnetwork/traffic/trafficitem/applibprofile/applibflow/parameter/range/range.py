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


class Range(Base):
    """This specifies the range parameter of the properties.
    The Range class encapsulates a list of range resources that are managed by the system.
    A list of resources can be retrieved from the server using the Range.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'range'
    _SDM_ATT_MAP = {
        'From': 'from',
        'MaxValue': 'maxValue',
        'MinValue': 'minValue',
        'To': 'to',
    }

    def __init__(self, parent):
        super(Range, self).__init__(parent)

    @property
    def From(self):
        """
        Returns
        -------
        - number: Start range value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['From'])
    @From.setter
    def From(self, value):
        self._set_attribute(self._SDM_ATT_MAP['From'], value)

    @property
    def MaxValue(self):
        """
        Returns
        -------
        - number: (Read only) Maximum supported value for parameter range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxValue'])

    @property
    def MinValue(self):
        """
        Returns
        -------
        - number: (Read only) Minimum supported value for parameter range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinValue'])

    @property
    def To(self):
        """
        Returns
        -------
        - number: End range value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['To'])
    @To.setter
    def To(self, value):
        self._set_attribute(self._SDM_ATT_MAP['To'], value)

    def update(self, From=None, To=None):
        """Updates range resource on the server.

        Args
        ----
        - From (number): Start range value.
        - To (number): End range value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, From=None, MaxValue=None, MinValue=None, To=None):
        """Finds and retrieves range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all range resources from the server.

        Args
        ----
        - From (number): Start range value.
        - MaxValue (number): (Read only) Maximum supported value for parameter range.
        - MinValue (number): (Read only) Minimum supported value for parameter range.
        - To (number): End range value.

        Returns
        -------
        - self: This instance with matching range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the range resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

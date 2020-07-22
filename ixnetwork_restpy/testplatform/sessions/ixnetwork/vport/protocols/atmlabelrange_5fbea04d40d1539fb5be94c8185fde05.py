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


class AtmLabelRange(Base):
    """A single ATM label range of VPIs and VCIs used for ATM sessions.
    The AtmLabelRange class encapsulates a list of atmLabelRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the AtmLabelRange.find() method.
    The list can be managed by using the AtmLabelRange.add() and AtmLabelRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'atmLabelRange'
    _SDM_ATT_MAP = {
        'MaxVci': 'maxVci',
        'MaxVpi': 'maxVpi',
        'MinVci': 'minVci',
        'MinVpi': 'minVpi',
    }

    def __init__(self, parent):
        super(AtmLabelRange, self).__init__(parent)

    @property
    def MaxVci(self):
        """
        Returns
        -------
        - number: The maximum virtual circuit identifier (VCI) value that will be included in the ATM label range. The valid maximum VCI value = 65,535 [0xFFFF (hex)].
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxVci'])
    @MaxVci.setter
    def MaxVci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxVci'], value)

    @property
    def MaxVpi(self):
        """
        Returns
        -------
        - number: The maximum virtual path identifier (VPI) value that will be included in the ATM label range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxVpi'])
    @MaxVpi.setter
    def MaxVpi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxVpi'], value)

    @property
    def MinVci(self):
        """
        Returns
        -------
        - number: The minimum virtual circuit identifier (VCI) value that will be included in the ATM label range.The valid minimum VCI value = 33.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinVci'])
    @MinVci.setter
    def MinVci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinVci'], value)

    @property
    def MinVpi(self):
        """
        Returns
        -------
        - number: The minimum virtual path identifier (VPI) value that will be included in the ATM label range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinVpi'])
    @MinVpi.setter
    def MinVpi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinVpi'], value)

    def update(self, MaxVci=None, MaxVpi=None, MinVci=None, MinVpi=None):
        """Updates atmLabelRange resource on the server.

        Args
        ----
        - MaxVci (number): The maximum virtual circuit identifier (VCI) value that will be included in the ATM label range. The valid maximum VCI value = 65,535 [0xFFFF (hex)].
        - MaxVpi (number): The maximum virtual path identifier (VPI) value that will be included in the ATM label range.
        - MinVci (number): The minimum virtual circuit identifier (VCI) value that will be included in the ATM label range.The valid minimum VCI value = 33.
        - MinVpi (number): The minimum virtual path identifier (VPI) value that will be included in the ATM label range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MaxVci=None, MaxVpi=None, MinVci=None, MinVpi=None):
        """Adds a new atmLabelRange resource on the server and adds it to the container.

        Args
        ----
        - MaxVci (number): The maximum virtual circuit identifier (VCI) value that will be included in the ATM label range. The valid maximum VCI value = 65,535 [0xFFFF (hex)].
        - MaxVpi (number): The maximum virtual path identifier (VPI) value that will be included in the ATM label range.
        - MinVci (number): The minimum virtual circuit identifier (VCI) value that will be included in the ATM label range.The valid minimum VCI value = 33.
        - MinVpi (number): The minimum virtual path identifier (VPI) value that will be included in the ATM label range.

        Returns
        -------
        - self: This instance with all currently retrieved atmLabelRange resources using find and the newly added atmLabelRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained atmLabelRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxVci=None, MaxVpi=None, MinVci=None, MinVpi=None):
        """Finds and retrieves atmLabelRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve atmLabelRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all atmLabelRange resources from the server.

        Args
        ----
        - MaxVci (number): The maximum virtual circuit identifier (VCI) value that will be included in the ATM label range. The valid maximum VCI value = 65,535 [0xFFFF (hex)].
        - MaxVpi (number): The maximum virtual path identifier (VPI) value that will be included in the ATM label range.
        - MinVci (number): The minimum virtual circuit identifier (VCI) value that will be included in the ATM label range.The valid minimum VCI value = 33.
        - MinVpi (number): The minimum virtual path identifier (VPI) value that will be included in the ATM label range.

        Returns
        -------
        - self: This instance with matching atmLabelRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of atmLabelRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the atmLabelRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

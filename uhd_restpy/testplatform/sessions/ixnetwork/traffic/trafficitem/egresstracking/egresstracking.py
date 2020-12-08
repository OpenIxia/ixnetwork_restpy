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


class EgressTracking(Base):
    """Provides different options for Egress Tracking.
    The EgressTracking class encapsulates a list of egressTracking resources that are managed by the user.
    A list of resources can be retrieved from the server using the EgressTracking.find() method.
    The list can be managed by using the EgressTracking.add() and EgressTracking.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'egressTracking'
    _SDM_ATT_MAP = {
        'AvailableEncapsulations': 'availableEncapsulations',
        'AvailableOffsets': 'availableOffsets',
        'CustomOffsetBits': 'customOffsetBits',
        'CustomWidthBits': 'customWidthBits',
        'Encapsulation': 'encapsulation',
        'Offset': 'offset',
    }

    def __init__(self, parent):
        super(EgressTracking, self).__init__(parent)

    @property
    def FieldOffset(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.fieldoffset.fieldoffset.FieldOffset): An instance of the FieldOffset class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.fieldoffset.fieldoffset import FieldOffset
        return FieldOffset(self)._select()

    @property
    def AvailableEncapsulations(self):
        """
        Returns
        -------
        - list(str): (Read only) Specifies the available Encapsulations for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableEncapsulations'])

    @property
    def AvailableOffsets(self):
        """
        Returns
        -------
        - list(str): (Read only) Specifies the available Offsets for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableOffsets'])

    @property
    def CustomOffsetBits(self):
        """
        Returns
        -------
        - number: Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomOffsetBits'])
    @CustomOffsetBits.setter
    def CustomOffsetBits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomOffsetBits'], value)

    @property
    def CustomWidthBits(self):
        """
        Returns
        -------
        - number: Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomWidthBits'])
    @CustomWidthBits.setter
    def CustomWidthBits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomWidthBits'], value)

    @property
    def Encapsulation(self):
        """
        Returns
        -------
        - str: Specifies the Encapsulation for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Encapsulation'])
    @Encapsulation.setter
    def Encapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Encapsulation'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - str: Specifies the Offset for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    def update(self, CustomOffsetBits=None, CustomWidthBits=None, Encapsulation=None, Offset=None):
        """Updates egressTracking resource on the server.

        Args
        ----
        - CustomOffsetBits (number): Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        - CustomWidthBits (number): Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        - Encapsulation (str): Specifies the Encapsulation for Egress Tracking.
        - Offset (str): Specifies the Offset for Egress Tracking.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CustomOffsetBits=None, CustomWidthBits=None, Encapsulation=None, Offset=None):
        """Adds a new egressTracking resource on the server and adds it to the container.

        Args
        ----
        - CustomOffsetBits (number): Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        - CustomWidthBits (number): Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        - Encapsulation (str): Specifies the Encapsulation for Egress Tracking.
        - Offset (str): Specifies the Offset for Egress Tracking.

        Returns
        -------
        - self: This instance with all currently retrieved egressTracking resources using find and the newly added egressTracking resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained egressTracking resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AvailableEncapsulations=None, AvailableOffsets=None, CustomOffsetBits=None, CustomWidthBits=None, Encapsulation=None, Offset=None):
        """Finds and retrieves egressTracking resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egressTracking resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egressTracking resources from the server.

        Args
        ----
        - AvailableEncapsulations (list(str)): (Read only) Specifies the available Encapsulations for Egress Tracking.
        - AvailableOffsets (list(str)): (Read only) Specifies the available Offsets for Egress Tracking.
        - CustomOffsetBits (number): Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        - CustomWidthBits (number): Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings .
        - Encapsulation (str): Specifies the Encapsulation for Egress Tracking.
        - Offset (str): Specifies the Offset for Egress Tracking.

        Returns
        -------
        - self: This instance with matching egressTracking resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egressTracking data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egressTracking resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

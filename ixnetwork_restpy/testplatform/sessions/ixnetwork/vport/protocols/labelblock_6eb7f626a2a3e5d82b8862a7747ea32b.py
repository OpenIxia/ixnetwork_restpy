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


class LabelBlock(Base):
    """This object holds the labels to be used with an L2 VPN.
    The LabelBlock class encapsulates a list of labelBlock resources that are managed by the user.
    A list of resources can be retrieved from the server using the LabelBlock.find() method.
    The list can be managed by using the LabelBlock.add() and LabelBlock.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'labelBlock'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'LabelBlockOffsetIncrementAcrossL2Site': 'labelBlockOffsetIncrementAcrossL2Site',
        'LabelStartIncrementAcrossL2Site': 'labelStartIncrementAcrossL2Site',
        'NumberOfLabels': 'numberOfLabels',
        'Offset': 'offset',
        'Start': 'start',
        'TotalLabelCount': 'totalLabelCount',
    }

    def __init__(self, parent):
        super(LabelBlock, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables use of the L2 VPN label block.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def LabelBlockOffsetIncrementAcrossL2Site(self):
        """
        Returns
        -------
        - number: Signifies the increment of label block offset across L2 site
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelBlockOffsetIncrementAcrossL2Site'])
    @LabelBlockOffsetIncrementAcrossL2Site.setter
    def LabelBlockOffsetIncrementAcrossL2Site(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelBlockOffsetIncrementAcrossL2Site'], value)

    @property
    def LabelStartIncrementAcrossL2Site(self):
        """
        Returns
        -------
        - number: Starts the increment of label across L2 site
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelStartIncrementAcrossL2Site'])
    @LabelStartIncrementAcrossL2Site.setter
    def LabelStartIncrementAcrossL2Site(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelStartIncrementAcrossL2Site'], value)

    @property
    def NumberOfLabels(self):
        """
        Returns
        -------
        - number: The number of labels contained in the label block. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfLabels'])
    @NumberOfLabels.setter
    def NumberOfLabels(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfLabels'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: The VPLS block offset value used to create a unique subset of the label values. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    @property
    def Start(self):
        """
        Returns
        -------
        - number: The first label in the label block. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Start'])
    @Start.setter
    def Start(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Start'], value)

    @property
    def TotalLabelCount(self):
        """
        Returns
        -------
        - number: Signifies the total label count
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalLabelCount'])

    def update(self, Enabled=None, LabelBlockOffsetIncrementAcrossL2Site=None, LabelStartIncrementAcrossL2Site=None, NumberOfLabels=None, Offset=None, Start=None):
        """Updates labelBlock resource on the server.

        Args
        ----
        - Enabled (bool): Enables or disables use of the L2 VPN label block.
        - LabelBlockOffsetIncrementAcrossL2Site (number): Signifies the increment of label block offset across L2 site
        - LabelStartIncrementAcrossL2Site (number): Starts the increment of label across L2 site
        - NumberOfLabels (number): The number of labels contained in the label block. (default = 0)
        - Offset (number): The VPLS block offset value used to create a unique subset of the label values. (default = 0)
        - Start (number): The first label in the label block. (default = 0)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, LabelBlockOffsetIncrementAcrossL2Site=None, LabelStartIncrementAcrossL2Site=None, NumberOfLabels=None, Offset=None, Start=None):
        """Adds a new labelBlock resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables or disables use of the L2 VPN label block.
        - LabelBlockOffsetIncrementAcrossL2Site (number): Signifies the increment of label block offset across L2 site
        - LabelStartIncrementAcrossL2Site (number): Starts the increment of label across L2 site
        - NumberOfLabels (number): The number of labels contained in the label block. (default = 0)
        - Offset (number): The VPLS block offset value used to create a unique subset of the label values. (default = 0)
        - Start (number): The first label in the label block. (default = 0)

        Returns
        -------
        - self: This instance with all currently retrieved labelBlock resources using find and the newly added labelBlock resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained labelBlock resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, LabelBlockOffsetIncrementAcrossL2Site=None, LabelStartIncrementAcrossL2Site=None, NumberOfLabels=None, Offset=None, Start=None, TotalLabelCount=None):
        """Finds and retrieves labelBlock resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve labelBlock resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all labelBlock resources from the server.

        Args
        ----
        - Enabled (bool): Enables or disables use of the L2 VPN label block.
        - LabelBlockOffsetIncrementAcrossL2Site (number): Signifies the increment of label block offset across L2 site
        - LabelStartIncrementAcrossL2Site (number): Starts the increment of label across L2 site
        - NumberOfLabels (number): The number of labels contained in the label block. (default = 0)
        - Offset (number): The VPLS block offset value used to create a unique subset of the label values. (default = 0)
        - Start (number): The first label in the label block. (default = 0)
        - TotalLabelCount (number): Signifies the total label count

        Returns
        -------
        - self: This instance with matching labelBlock resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of labelBlock data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the labelBlock resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

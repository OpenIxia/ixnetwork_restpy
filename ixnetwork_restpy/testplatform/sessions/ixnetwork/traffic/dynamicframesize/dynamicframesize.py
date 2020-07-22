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


class DynamicFrameSize(Base):
    """This object fetches the options for setting dynamic frame size.
    The DynamicFrameSize class encapsulates a list of dynamicFrameSize resources that are managed by the system.
    A list of resources can be retrieved from the server using the DynamicFrameSize.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'dynamicFrameSize'
    _SDM_ATT_MAP = {
        'FixedSize': 'fixedSize',
        'HighLevelStreamName': 'highLevelStreamName',
        'RandomMax': 'randomMax',
        'RandomMin': 'randomMin',
        'TrafficItemName': 'trafficItemName',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(DynamicFrameSize, self).__init__(parent)

    @property
    def FixedSize(self):
        """
        Returns
        -------
        - number: Sets all frames to a specified constant size. The default is 64 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedSize'])
    @FixedSize.setter
    def FixedSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedSize'], value)

    @property
    def HighLevelStreamName(self):
        """
        Returns
        -------
        - str: The name of the high level stream
        """
        return self._get_attribute(self._SDM_ATT_MAP['HighLevelStreamName'])

    @property
    def RandomMax(self):
        """
        Returns
        -------
        - number: Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomMax'])
    @RandomMax.setter
    def RandomMax(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomMax'], value)

    @property
    def RandomMin(self):
        """
        Returns
        -------
        - number: Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomMin'])
    @RandomMin.setter
    def RandomMin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomMin'], value)

    @property
    def TrafficItemName(self):
        """
        Returns
        -------
        - str: The name of the parent traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemName'])

    @property
    def Type(self):
        """
        Returns
        -------
        - str(fixed | random): Sets the frame size to either fixed or random lengths in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, FixedSize=None, RandomMax=None, RandomMin=None, Type=None):
        """Updates dynamicFrameSize resource on the server.

        Args
        ----
        - FixedSize (number): Sets all frames to a specified constant size. The default is 64 bytes.
        - RandomMax (number): Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        - RandomMin (number): Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        - Type (str(fixed | random)): Sets the frame size to either fixed or random lengths in bytes.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, FixedSize=None, HighLevelStreamName=None, RandomMax=None, RandomMin=None, TrafficItemName=None, Type=None):
        """Finds and retrieves dynamicFrameSize resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dynamicFrameSize resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dynamicFrameSize resources from the server.

        Args
        ----
        - FixedSize (number): Sets all frames to a specified constant size. The default is 64 bytes.
        - HighLevelStreamName (str): The name of the high level stream
        - RandomMax (number): Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        - RandomMin (number): Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        - TrafficItemName (str): The name of the parent traffic item.
        - Type (str(fixed | random)): Sets the frame size to either fixed or random lengths in bytes.

        Returns
        -------
        - self: This instance with matching dynamicFrameSize resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dynamicFrameSize data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dynamicFrameSize resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

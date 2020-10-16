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


class Tracking(Base):
    """This object provides different options for tracking.
    The Tracking class encapsulates a list of tracking resources that are managed by the system.
    A list of resources can be retrieved from the server using the Tracking.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tracking'
    _SDM_ATT_MAP = {
        'AvailableProtocolOffsets': 'availableProtocolOffsets',
        'AvailableTrackBy': 'availableTrackBy',
        'AvailableTrackByInfos': 'availableTrackByInfos',
        'FieldWidth': 'fieldWidth',
        'Offset': 'offset',
        'OneToOneMesh': 'oneToOneMesh',
        'ProtocolOffset': 'protocolOffset',
        'TrackBy': 'trackBy',
        'Values': 'values',
    }

    def __init__(self, parent):
        super(Tracking, self).__init__(parent)

    @property
    def AvailableProtocolOffsets(self):
        """
        Returns
        -------
        - list(str): Specifies the available Protocol Offsets when the Flows of a Traffic Item are tracked by Custom Override.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableProtocolOffsets'])

    @property
    def AvailableTrackBy(self):
        """DEPRECATED 
        Returns
        -------
        - list(str): Returns list of available tracking field ids
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableTrackBy'])

    @property
    def AvailableTrackByInfos(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): Returns list of tracking fields with id/displayname
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableTrackByInfos'])

    @property
    def FieldWidth(self):
        """
        Returns
        -------
        - str(eightBits | sixteenBits | thirtyTwoBits | twentyFourBits): Specifies the Field Width when the flows of a Traffic Item are tracked by Custom Override.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldWidth'])
    @FieldWidth.setter
    def FieldWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FieldWidth'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: Specifies the Offset when the Flows of a Traffic Item are tracked by Custom Override.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    @property
    def OneToOneMesh(self):
        """
        Returns
        -------
        - bool: If true, one-one mesh is enabled when flows of a traffic item are tracked by Custom Override.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OneToOneMesh'])
    @OneToOneMesh.setter
    def OneToOneMesh(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OneToOneMesh'], value)

    @property
    def ProtocolOffset(self):
        """
        Returns
        -------
        - str: Specifies the Protocol Offset when flows of a Traffic Item are tracked by Custom Override.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolOffset'])
    @ProtocolOffset.setter
    def ProtocolOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolOffset'], value)

    @property
    def TrackBy(self):
        """
        Returns
        -------
        - list(str): Specifies the tracking option by which the Flows of a Traffic Item are tracked.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackBy'])
    @TrackBy.setter
    def TrackBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackBy'], value)

    @property
    def Values(self):
        """
        Returns
        -------
        - list(str): Specifies the Values when the Flows of a Traffic Item are tracked by Custom Override.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])
    @Values.setter
    def Values(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Values'], value)

    def update(self, FieldWidth=None, Offset=None, OneToOneMesh=None, ProtocolOffset=None, TrackBy=None, Values=None):
        """Updates tracking resource on the server.

        Args
        ----
        - FieldWidth (str(eightBits | sixteenBits | thirtyTwoBits | twentyFourBits)): Specifies the Field Width when the flows of a Traffic Item are tracked by Custom Override.
        - Offset (number): Specifies the Offset when the Flows of a Traffic Item are tracked by Custom Override.
        - OneToOneMesh (bool): If true, one-one mesh is enabled when flows of a traffic item are tracked by Custom Override.
        - ProtocolOffset (str): Specifies the Protocol Offset when flows of a Traffic Item are tracked by Custom Override.
        - TrackBy (list(str)): Specifies the tracking option by which the Flows of a Traffic Item are tracked.
        - Values (list(str)): Specifies the Values when the Flows of a Traffic Item are tracked by Custom Override.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableProtocolOffsets=None, AvailableTrackBy=None, AvailableTrackByInfos=None, FieldWidth=None, Offset=None, OneToOneMesh=None, ProtocolOffset=None, TrackBy=None, Values=None):
        """Finds and retrieves tracking resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tracking resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tracking resources from the server.

        Args
        ----
        - AvailableProtocolOffsets (list(str)): Specifies the available Protocol Offsets when the Flows of a Traffic Item are tracked by Custom Override.
        - AvailableTrackBy (list(str)): Returns list of available tracking field ids
        - AvailableTrackByInfos (list(dict(arg1:str,arg2:str))): Returns list of tracking fields with id/displayname
        - FieldWidth (str(eightBits | sixteenBits | thirtyTwoBits | twentyFourBits)): Specifies the Field Width when the flows of a Traffic Item are tracked by Custom Override.
        - Offset (number): Specifies the Offset when the Flows of a Traffic Item are tracked by Custom Override.
        - OneToOneMesh (bool): If true, one-one mesh is enabled when flows of a traffic item are tracked by Custom Override.
        - ProtocolOffset (str): Specifies the Protocol Offset when flows of a Traffic Item are tracked by Custom Override.
        - TrackBy (list(str)): Specifies the tracking option by which the Flows of a Traffic Item are tracked.
        - Values (list(str)): Specifies the Values when the Flows of a Traffic Item are tracked by Custom Override.

        Returns
        -------
        - self: This instance with matching tracking resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tracking data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tracking resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class MeterFeatureStatsLearnedInformation(Base):
    """NOT DEFINED
    The MeterFeatureStatsLearnedInformation class encapsulates a list of meterFeatureStatsLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the MeterFeatureStatsLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'meterFeatureStatsLearnedInformation'
    _SDM_ATT_MAP = {
        'BandTypes': 'bandTypes',
        'Capabilities': 'capabilities',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'MaxBands': 'maxBands',
        'MaxColor': 'maxColor',
        'MaxMeters': 'maxMeters',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
    }

    def __init__(self, parent):
        super(MeterFeatureStatsLearnedInformation, self).__init__(parent)

    @property
    def BandTypes(self):
        """
        Returns
        -------
        - str: Specifies Band Types in Meter Feature
        """
        return self._get_attribute(self._SDM_ATT_MAP['BandTypes'])

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - str: Specifies the Capabilities Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['Capabilities'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - number: The Data Path identifier of the OpenFlow Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: The Data Path identifier of the OpenFlow Controller in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: The error code of the received error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: The type of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: The latency measurement for the OpenFlow channel in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Indicates the local IP of the Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaxBands(self):
        """
        Returns
        -------
        - number: Specifies Maximum Band Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBands'])

    @property
    def MaxColor(self):
        """
        Returns
        -------
        - number: Specifies Maximum Color Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxColor'])

    @property
    def MaxMeters(self):
        """
        Returns
        -------
        - number: Specifies the Value of Maximum Meter
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxMeters'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: The Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    def find(self, BandTypes=None, Capabilities=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, Latency=None, LocalIp=None, MaxBands=None, MaxColor=None, MaxMeters=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves meterFeatureStatsLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve meterFeatureStatsLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all meterFeatureStatsLearnedInformation resources from the server.

        Args
        ----
        - BandTypes (str): Specifies Band Types in Meter Feature
        - Capabilities (str): Specifies the Capabilities Value
        - DataPathId (number): The Data Path identifier of the OpenFlow Controller.
        - DataPathIdAsHex (str): The Data Path identifier of the OpenFlow Controller in hexadecimal format.
        - ErrorCode (str): The error code of the received error.
        - ErrorType (str): The type of the error received.
        - Latency (number): The latency measurement for the OpenFlow channel in microseconds.
        - LocalIp (str): Indicates the local IP of the Controller.
        - MaxBands (number): Specifies Maximum Band Value
        - MaxColor (number): Specifies Maximum Color Value
        - MaxMeters (number): Specifies the Value of Maximum Meter
        - RemoteIp (str): The Remote IP address of the selected interface.
        - ReplyState (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching meterFeatureStatsLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of meterFeatureStatsLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the meterFeatureStatsLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

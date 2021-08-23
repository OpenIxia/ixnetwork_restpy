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
from typing import List, Any, Union


class SwitchMeterLearnedInfo(Base):
    """NOT DEFINED
    The SwitchMeterLearnedInfo class encapsulates a list of switchMeterLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchMeterLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchMeterLearnedInfo'
    _SDM_ATT_MAP = {
        'BytesInInput': 'bytesInInput',
        'DatapathId': 'datapathId',
        'DatapathIdAsHex': 'datapathIdAsHex',
        'DurationNSec': 'durationNSec',
        'DurationSec': 'durationSec',
        'FlowCount': 'flowCount',
        'LocalIp': 'localIp',
        'MeterConfigurationFlags': 'meterConfigurationFlags',
        'MeterId': 'meterId',
        'NumOfBands': 'numOfBands',
        'PacketsInInput': 'packetsInInput',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(SwitchMeterLearnedInfo, self).__init__(parent, list_op)

    @property
    def SwitchMeterBandLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterbandlearnedinfo_442d49cfc16498298dbe4a2d5ee71127.SwitchMeterBandLearnedInfo): An instance of the SwitchMeterBandLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterbandlearnedinfo_442d49cfc16498298dbe4a2d5ee71127 import SwitchMeterBandLearnedInfo
        if self._properties.get('SwitchMeterBandLearnedInfo', None) is not None:
            return self._properties.get('SwitchMeterBandLearnedInfo')
        else:
            return SwitchMeterBandLearnedInfo(self)

    @property
    def BytesInInput(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BytesInInput'])

    @property
    def DatapathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathId'])

    @property
    def DatapathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathIdAsHex'])

    @property
    def DurationNSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationNSec'])

    @property
    def DurationSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationSec'])

    @property
    def FlowCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowCount'])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MeterConfigurationFlags(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterConfigurationFlags'])

    @property
    def MeterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterId'])

    @property
    def NumOfBands(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumOfBands'])

    @property
    def PacketsInInput(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsInInput'])

    def add(self):
        """Adds a new switchMeterLearnedInfo resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved switchMeterLearnedInfo resources using find and the newly added switchMeterLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, BytesInInput=None, DatapathId=None, DatapathIdAsHex=None, DurationNSec=None, DurationSec=None, FlowCount=None, LocalIp=None, MeterConfigurationFlags=None, MeterId=None, NumOfBands=None, PacketsInInput=None):
        # type: (int, str, str, int, int, int, str, str, int, int, int) -> SwitchMeterLearnedInfo
        """Finds and retrieves switchMeterLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchMeterLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchMeterLearnedInfo resources from the server.

        Args
        ----
        - BytesInInput (number): NOT DEFINED
        - DatapathId (str): NOT DEFINED
        - DatapathIdAsHex (str): NOT DEFINED
        - DurationNSec (number): NOT DEFINED
        - DurationSec (number): NOT DEFINED
        - FlowCount (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - MeterConfigurationFlags (str): NOT DEFINED
        - MeterId (number): NOT DEFINED
        - NumOfBands (number): NOT DEFINED
        - PacketsInInput (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchMeterLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchMeterLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchMeterLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

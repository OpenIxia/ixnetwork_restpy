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


class TxLane(Base):
    """This object contains the TxLane parameters.
    The TxLane class encapsulates a required txLane resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'txLane'
    _SDM_ATT_MAP = {
        'IsSkewSynchronized': 'isSkewSynchronized',
        'LaneMappingType': 'laneMappingType',
        'MaxSkewVal': 'maxSkewVal',
        'MinSkewVal': 'minSkewVal',
        'NoOfLanes': 'noOfLanes',
        'PcsLane': 'pcsLane',
        'PhysicalLanes': 'physicalLanes',
        'Resolution': 'resolution',
        'SkewValues': 'skewValues',
        'SynchronizedSkewVal': 'synchronizedSkewVal',
    }

    def __init__(self, parent):
        super(TxLane, self).__init__(parent)

    @property
    def IsSkewSynchronized(self):
        """
        Returns
        -------
        - bool: If true, skew value will apply for all the lanes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsSkewSynchronized'])
    @IsSkewSynchronized.setter
    def IsSkewSynchronized(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsSkewSynchronized'], value)

    @property
    def LaneMappingType(self):
        """
        Returns
        -------
        - str(custom | decrement | default | increment | random): Lane Mapping
        """
        return self._get_attribute(self._SDM_ATT_MAP['LaneMappingType'])
    @LaneMappingType.setter
    def LaneMappingType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LaneMappingType'], value)

    @property
    def MaxSkewVal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxSkewVal'])

    @property
    def MinSkewVal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinSkewVal'])

    @property
    def NoOfLanes(self):
        """
        Returns
        -------
        - number: Number of lanes
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfLanes'])

    @property
    def PcsLane(self):
        """
        Returns
        -------
        - list(number): Pcs Lane
        """
        return self._get_attribute(self._SDM_ATT_MAP['PcsLane'])
    @PcsLane.setter
    def PcsLane(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PcsLane'], value)

    @property
    def PhysicalLanes(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PhysicalLanes'])

    @property
    def Resolution(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Resolution'])

    @property
    def SkewValues(self):
        """
        Returns
        -------
        - list(number): Skew Values
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkewValues'])
    @SkewValues.setter
    def SkewValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkewValues'], value)

    @property
    def SynchronizedSkewVal(self):
        """
        Returns
        -------
        - number: Synchronized Skew Values
        """
        return self._get_attribute(self._SDM_ATT_MAP['SynchronizedSkewVal'])
    @SynchronizedSkewVal.setter
    def SynchronizedSkewVal(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SynchronizedSkewVal'], value)

    def update(self, IsSkewSynchronized=None, LaneMappingType=None, PcsLane=None, SkewValues=None, SynchronizedSkewVal=None):
        """Updates txLane resource on the server.

        Args
        ----
        - IsSkewSynchronized (bool): If true, skew value will apply for all the lanes.
        - LaneMappingType (str(custom | decrement | default | increment | random)): Lane Mapping
        - PcsLane (list(number)): Pcs Lane
        - SkewValues (list(number)): Skew Values
        - SynchronizedSkewVal (number): Synchronized Skew Values

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
    """
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
        - bool: 
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
        - str(custom | decrement | default | increment | random): 
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
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfLanes'])

    @property
    def PcsLane(self):
        """
        Returns
        -------
        - list(number): 
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
        - list(number): 
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
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SynchronizedSkewVal'])
    @SynchronizedSkewVal.setter
    def SynchronizedSkewVal(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SynchronizedSkewVal'], value)

    def update(self, IsSkewSynchronized=None, LaneMappingType=None, PcsLane=None, SkewValues=None, SynchronizedSkewVal=None):
        """Updates txLane resource on the server.

        Args
        ----
        - IsSkewSynchronized (bool): 
        - LaneMappingType (str(custom | decrement | default | increment | random)): 
        - PcsLane (list(number)): 
        - SkewValues (list(number)): 
        - SynchronizedSkewVal (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

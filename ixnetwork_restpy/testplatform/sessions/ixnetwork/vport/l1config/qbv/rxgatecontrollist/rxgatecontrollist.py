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


class RxGateControlList(Base):
    """
    The RxGateControlList class encapsulates a list of rxGateControlList resources that are managed by the system.
    A list of resources can be retrieved from the server using the RxGateControlList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'rxGateControlList'
    _SDM_ATT_MAP = {
        'BaseTimeOffset': 'baseTimeOffset',
        'GateControlList': 'gateControlList',
        'UnitOfTime': 'unitOfTime',
    }

    def __init__(self, parent):
        super(RxGateControlList, self).__init__(parent)

    @property
    def BaseTimeOffset(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseTimeOffset'])
    @BaseTimeOffset.setter
    def BaseTimeOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BaseTimeOffset'], value)

    @property
    def GateControlList(self):
        """
        Returns
        -------
        - list(list[str]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GateControlList'])
    @GateControlList.setter
    def GateControlList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GateControlList'], value)

    @property
    def UnitOfTime(self):
        """
        Returns
        -------
        - str(MicroSecond | MilliSecond | NanoSecond): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnitOfTime'])
    @UnitOfTime.setter
    def UnitOfTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnitOfTime'], value)

    def update(self, BaseTimeOffset=None, GateControlList=None, UnitOfTime=None):
        """Updates rxGateControlList resource on the server.

        Args
        ----
        - BaseTimeOffset (number): 
        - GateControlList (list(list[str])): 
        - UnitOfTime (str(MicroSecond | MilliSecond | NanoSecond)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, BaseTimeOffset=None, GateControlList=None, UnitOfTime=None):
        """Finds and retrieves rxGateControlList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rxGateControlList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rxGateControlList resources from the server.

        Args
        ----
        - BaseTimeOffset (number): 
        - GateControlList (list(list[str])): 
        - UnitOfTime (str(MicroSecond | MilliSecond | NanoSecond)): 

        Returns
        -------
        - self: This instance with matching rxGateControlList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rxGateControlList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rxGateControlList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

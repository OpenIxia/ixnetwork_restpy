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


class LckLearnedInfo(Base):
    """NOT DEFINED
    The LckLearnedInfo class encapsulates a list of lckLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LckLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'lckLearnedInfo'
    _SDM_ATT_MAP = {
        'BVlan': 'bVlan',
        'CVlan': 'cVlan',
        'MepMacAddress': 'mepMacAddress',
        'RemoteMepMacAddress': 'remoteMepMacAddress',
        'RxCount': 'rxCount',
        'RxInterval': 'rxInterval',
        'RxState': 'rxState',
        'SVlan': 'sVlan',
        'TxCount': 'txCount',
        'TxState': 'txState',
    }

    def __init__(self, parent):
        super(LckLearnedInfo, self).__init__(parent)

    @property
    def BVlan(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlan'])

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])

    @property
    def MepMacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MepMacAddress'])

    @property
    def RemoteMepMacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMepMacAddress'])

    @property
    def RxCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxCount'])

    @property
    def RxInterval(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxInterval'])

    @property
    def RxState(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxState'])

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])

    @property
    def TxCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxCount'])

    @property
    def TxState(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxState'])

    def find(self, BVlan=None, CVlan=None, MepMacAddress=None, RemoteMepMacAddress=None, RxCount=None, RxInterval=None, RxState=None, SVlan=None, TxCount=None, TxState=None):
        """Finds and retrieves lckLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lckLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lckLearnedInfo resources from the server.

        Args
        ----
        - BVlan (str): NOT DEFINED
        - CVlan (str): NOT DEFINED
        - MepMacAddress (str): NOT DEFINED
        - RemoteMepMacAddress (str): NOT DEFINED
        - RxCount (number): NOT DEFINED
        - RxInterval (str): NOT DEFINED
        - RxState (str): NOT DEFINED
        - SVlan (str): NOT DEFINED
        - TxCount (number): NOT DEFINED
        - TxState (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching lckLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lckLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lckLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

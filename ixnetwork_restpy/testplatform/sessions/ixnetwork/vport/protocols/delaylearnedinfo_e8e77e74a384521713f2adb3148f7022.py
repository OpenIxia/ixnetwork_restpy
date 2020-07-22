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


class DelayLearnedInfo(Base):
    """This object contains the learned delay information for the bridge.
    The DelayLearnedInfo class encapsulates a list of delayLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the DelayLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'delayLearnedInfo'
    _SDM_ATT_MAP = {
        'CVlan': 'cVlan',
        'DstMacAddress': 'dstMacAddress',
        'MdLevel': 'mdLevel',
        'SVlan': 'sVlan',
        'SrcMacAddress': 'srcMacAddress',
        'ValueInNanoSec': 'valueInNanoSec',
        'ValueInSec': 'valueInSec',
    }

    def __init__(self, parent):
        super(DelayLearnedInfo, self).__init__(parent)

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: (read only) The learned C-VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])

    @property
    def DstMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The learned destination MAC address for the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DstMacAddress'])

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - number: (read only) The learned MD level for the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdLevel'])

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: (read only) The learned S-VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])

    @property
    def SrcMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The learned source MAC address for the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcMacAddress'])

    @property
    def ValueInNanoSec(self):
        """
        Returns
        -------
        - number: (read only) The delay measurement in nanoseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueInNanoSec'])

    @property
    def ValueInSec(self):
        """
        Returns
        -------
        - number: (read only) The delay measurement in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueInSec'])

    def find(self, CVlan=None, DstMacAddress=None, MdLevel=None, SVlan=None, SrcMacAddress=None, ValueInNanoSec=None, ValueInSec=None):
        """Finds and retrieves delayLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve delayLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all delayLearnedInfo resources from the server.

        Args
        ----
        - CVlan (str): (read only) The learned C-VLAN identifier.
        - DstMacAddress (str): (read only) The learned destination MAC address for the bridge.
        - MdLevel (number): (read only) The learned MD level for the bridge.
        - SVlan (str): (read only) The learned S-VLAN identifier.
        - SrcMacAddress (str): (read only) The learned source MAC address for the bridge.
        - ValueInNanoSec (number): (read only) The delay measurement in nanoseconds.
        - ValueInSec (number): (read only) The delay measurement in seconds.

        Returns
        -------
        - self: This instance with matching delayLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of delayLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the delayLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

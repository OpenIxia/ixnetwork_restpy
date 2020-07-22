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


class LearnedMdtInfo(Base):
    """Learned information associated with a PIM-SM interface.
    The LearnedMdtInfo class encapsulates a list of learnedMdtInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedMdtInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedMdtInfo'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'CeGroupAddress': 'ceGroupAddress',
        'CeSourceAddress': 'ceSourceAddress',
        'MdtGroupAddress': 'mdtGroupAddress',
        'MdtSourceAddress': 'mdtSourceAddress',
    }

    def __init__(self, parent):
        super(LearnedMdtInfo, self).__init__(parent)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: The amount of time (in seconds) remaining before this TLV times out.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def CeGroupAddress(self):
        """
        Returns
        -------
        - str: The CE group address contained in this data MDT TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CeGroupAddress'])

    @property
    def CeSourceAddress(self):
        """
        Returns
        -------
        - str: The CE source address contained in this data MDT TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CeSourceAddress'])

    @property
    def MdtGroupAddress(self):
        """
        Returns
        -------
        - str: The MDT (PE) group address contained in this data MDT TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdtGroupAddress'])

    @property
    def MdtSourceAddress(self):
        """
        Returns
        -------
        - str: The MDT (PE) source address contained in this data MDT TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdtSourceAddress'])

    def find(self, Age=None, CeGroupAddress=None, CeSourceAddress=None, MdtGroupAddress=None, MdtSourceAddress=None):
        """Finds and retrieves learnedMdtInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedMdtInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedMdtInfo resources from the server.

        Args
        ----
        - Age (number): The amount of time (in seconds) remaining before this TLV times out.
        - CeGroupAddress (str): The CE group address contained in this data MDT TLV.
        - CeSourceAddress (str): The CE source address contained in this data MDT TLV.
        - MdtGroupAddress (str): The MDT (PE) group address contained in this data MDT TLV.
        - MdtSourceAddress (str): The MDT (PE) source address contained in this data MDT TLV.

        Returns
        -------
        - self: This instance with matching learnedMdtInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedMdtInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedMdtInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

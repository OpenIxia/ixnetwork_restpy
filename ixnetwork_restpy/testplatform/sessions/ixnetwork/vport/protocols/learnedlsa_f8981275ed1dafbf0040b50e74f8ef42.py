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


class LearnedLsa(Base):
    """The learned Link State Advertisements on this interface.
    The LearnedLsa class encapsulates a list of learnedLsa resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedLsa.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedLsa'
    _SDM_ATT_MAP = {
        'AdvRouterId': 'advRouterId',
        'Age': 'age',
        'LinkStateId': 'linkStateId',
        'LsaType': 'lsaType',
        'SeqNumber': 'seqNumber',
    }

    def __init__(self, parent):
        super(LearnedLsa, self).__init__(parent)

    @property
    def AdvRouterId(self):
        """
        Returns
        -------
        - str: The router ID of the router that is originating the LSA. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvRouterId'])

    @property
    def Age(self):
        """
        Returns
        -------
        - number: Read only. Only available when this command is used to access a learned LSA. This value holds the age of the LSA extracted from the LSA header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def LinkStateId(self):
        """
        Returns
        -------
        - str: The router ID of the originating router. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkStateId'])

    @property
    def LsaType(self):
        """
        Returns
        -------
        - str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope): Read-only. The current LSA type. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaType'])

    @property
    def SeqNumber(self):
        """
        Returns
        -------
        - str: Read only. Only available when this command is used to access a learned LSA. This value holds the sequence number of the LSA extracted from the LSA header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeqNumber'])

    def find(self, AdvRouterId=None, Age=None, LinkStateId=None, LsaType=None, SeqNumber=None):
        """Finds and retrieves learnedLsa resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedLsa resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedLsa resources from the server.

        Args
        ----
        - AdvRouterId (str): The router ID of the router that is originating the LSA. (default = 0.0.0.0)
        - Age (number): Read only. Only available when this command is used to access a learned LSA. This value holds the age of the LSA extracted from the LSA header.
        - LinkStateId (str): The router ID of the originating router. (default = 0.0.0.0)
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)): Read-only. The current LSA type. (default = 0)
        - SeqNumber (str): Read only. Only available when this command is used to access a learned LSA. This value holds the sequence number of the LSA extracted from the LSA header.

        Returns
        -------
        - self: This instance with matching learnedLsa resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedLsa data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedLsa resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

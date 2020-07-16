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


class RdInfo(Base):
    """(Read Only) List of RDs learned from a next hop.
    The RdInfo class encapsulates a list of rdInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the RdInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'rdInfo'
    _SDM_ATT_MAP = {
        'Rd': 'rd',
    }

    def __init__(self, parent):
        super(RdInfo, self).__init__(parent)

    @property
    def EthernetTagInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettaginfo_d714970f0d8b53a3aeb11fbf4e70ffe5.EthernetTagInfo): An instance of the EthernetTagInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettaginfo_d714970f0d8b53a3aeb11fbf4e70ffe5 import EthernetTagInfo
        return EthernetTagInfo(self)

    @property
    def Rd(self):
        """
        Returns
        -------
        - str: RD value in X:Y format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rd'])

    def find(self, Rd=None):
        """Finds and retrieves rdInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rdInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rdInfo resources from the server.

        Args
        ----
        - Rd (str): RD value in X:Y format.

        Returns
        -------
        - self: This instance with matching rdInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rdInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rdInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
    """(Read Only) The list of RDs.
    The RdInfo class encapsulates a list of rdInfo resources that is managed by the system.
    A list of resources can be retrieved from the server using the RdInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'rdInfo'

    def __init__(self, parent):
        super(RdInfo, self).__init__(parent)

    @property
    def OpaqueElementInfo(self):
        """An instance of the OpaqueElementInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaqueelementinfo_18a4a5c0fbf314ab3c2b286d7d250d24.OpaqueElementInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaqueelementinfo_18a4a5c0fbf314ab3c2b286d7d250d24 import OpaqueElementInfo
        return OpaqueElementInfo(self)

    @property
    def EthernetTagList(self):
        """(Read Only) Ethernet Tag Id in hex format.

        Returns:
            list(str)
        """
        return self._get_attribute('ethernetTagList')

    @property
    def Rd(self):
        """(Read Only) RD value in X:Y format.

        Returns:
            str
        """
        return self._get_attribute('rd')

    @property
    def TunnelIdentifier(self):
        """(Read Only) P2P or P2MP Tunnel Identifier.

        Returns:
            str
        """
        return self._get_attribute('tunnelIdentifier')

    def find(self, EthernetTagList=None, Rd=None, TunnelIdentifier=None):
        """Finds and retrieves rdInfo data from the server.

        All named parameters support regex and can be used to selectively retrieve rdInfo data from the server.
        By default the find method takes no parameters and will retrieve all rdInfo data from the server.

        Args:
            EthernetTagList (list(str)): (Read Only) Ethernet Tag Id in hex format.
            Rd (str): (Read Only) RD value in X:Y format.
            TunnelIdentifier (str): (Read Only) P2P or P2MP Tunnel Identifier.

        Returns:
            self: This instance with matching rdInfo data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of rdInfo data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the rdInfo data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

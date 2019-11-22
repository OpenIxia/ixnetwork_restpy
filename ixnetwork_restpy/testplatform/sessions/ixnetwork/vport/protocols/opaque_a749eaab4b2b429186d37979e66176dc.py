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


class Opaque(Base):
    """
    The Opaque class encapsulates a list of opaque resources that is managed by the system.
    A list of resources can be retrieved from the server using the Opaque.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'opaque'

    def __init__(self, parent):
        super(Opaque, self).__init__(parent)

    @property
    def LinkTlv(self):
        """An instance of the LinkTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linktlv_97a3eb5080e3c27fd5db1b93b81ce400.LinkTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linktlv_97a3eb5080e3c27fd5db1b93b81ce400 import LinkTlv
        return LinkTlv(self)

    @property
    def RouterTlv(self):
        """An instance of the RouterTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routertlv_2c6ca07de5dca608cc948dca04c128f9.RouterTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routertlv_2c6ca07de5dca608cc948dca04c128f9 import RouterTlv
        return RouterTlv(self)

    @property
    def EnableRouterTlv(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('enableRouterTlv')
    @EnableRouterTlv.setter
    def EnableRouterTlv(self, value):
        self._set_attribute('enableRouterTlv', value)

    def update(self, EnableRouterTlv=None):
        """Updates a child instance of opaque on the server.

        Args:
            EnableRouterTlv (bool): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, EnableRouterTlv=None):
        """Finds and retrieves opaque data from the server.

        All named parameters support regex and can be used to selectively retrieve opaque data from the server.
        By default the find method takes no parameters and will retrieve all opaque data from the server.

        Args:
            EnableRouterTlv (bool): 

        Returns:
            self: This instance with matching opaque data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of opaque data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the opaque data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

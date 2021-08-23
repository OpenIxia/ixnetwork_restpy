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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class Link(Base):
    """List of impairment links.  Each link consists of a pair of ports.
    The Link class encapsulates a list of link resources that are managed by the system.
    A list of resources can be retrieved from the server using the Link.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'link'
    _SDM_ATT_MAP = {
        'ForwardingInterruption': 'forwardingInterruption',
        'Name': 'name',
        'RxPortName': 'rxPortName',
        'TxPortName': 'txPortName',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Link, self).__init__(parent, list_op)

    @property
    def LosLof(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.link.loslof.loslof.LosLof): An instance of the LosLof class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.link.loslof.loslof import LosLof
        if self._properties.get('LosLof', None) is not None:
            return self._properties.get('LosLof')
        else:
            return LosLof(self)._select()

    @property
    def ForwardingInterruption(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Emulate a link fault. Drop all packets received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForwardingInterruption'])
    @ForwardingInterruption.setter
    def ForwardingInterruption(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ForwardingInterruption'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the link: receiving port -> transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def RxPortName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the receiving port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxPortName'])

    @property
    def TxPortName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxPortName'])

    def update(self, ForwardingInterruption=None):
        # type: (bool) -> Link
        """Updates link resource on the server.

        Args
        ----
        - ForwardingInterruption (bool): Emulate a link fault. Drop all packets received.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ForwardingInterruption=None):
        # type: (bool) -> Link
        """Adds a new link resource on the json, only valid with config assistant

        Args
        ----
        - ForwardingInterruption (bool): Emulate a link fault. Drop all packets received.

        Returns
        -------
        - self: This instance with all currently retrieved link resources using find and the newly added link resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ForwardingInterruption=None, Name=None, RxPortName=None, TxPortName=None):
        # type: (bool, str, str, str) -> Link
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - ForwardingInterruption (bool): Emulate a link fault. Drop all packets received.
        - Name (str): The name of the link: receiving port -> transmitting port.
        - RxPortName (str): The name of the receiving port.
        - TxPortName (str): The name of the transmitting port.

        Returns
        -------
        - self: This instance with matching link resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the link resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

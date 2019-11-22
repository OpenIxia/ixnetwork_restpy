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


class Link(Base):
    """
    The Link class encapsulates a list of link resources that is managed by the system.
    A list of resources can be retrieved from the server using the Link.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'link'

    def __init__(self, parent):
        super(Link, self).__init__(parent)

    @property
    def CountLsa(self):
        """

        Returns:
            number
        """
        return self._get_attribute('countLsa')
    @CountLsa.setter
    def CountLsa(self, value):
        self._set_attribute('countLsa', value)

    @property
    def IncrLinkStateId(self):
        """

        Returns:
            str
        """
        return self._get_attribute('incrLinkStateId')
    @IncrLinkStateId.setter
    def IncrLinkStateId(self, value):
        self._set_attribute('incrLinkStateId', value)

    @property
    def LocalInterfaceAddress(self):
        """

        Returns:
            str
        """
        return self._get_attribute('localInterfaceAddress')
    @LocalInterfaceAddress.setter
    def LocalInterfaceAddress(self, value):
        self._set_attribute('localInterfaceAddress', value)

    @property
    def OptBitDc(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitDc')
    @OptBitDc.setter
    def OptBitDc(self, value):
        self._set_attribute('optBitDc', value)

    @property
    def OptBitE(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitE')
    @OptBitE.setter
    def OptBitE(self, value):
        self._set_attribute('optBitE', value)

    @property
    def OptBitMc(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitMc')
    @OptBitMc.setter
    def OptBitMc(self, value):
        self._set_attribute('optBitMc', value)

    @property
    def OptBitN(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitN')
    @OptBitN.setter
    def OptBitN(self, value):
        self._set_attribute('optBitN', value)

    @property
    def OptBitR(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitR')
    @OptBitR.setter
    def OptBitR(self, value):
        self._set_attribute('optBitR', value)

    @property
    def OptBitV6(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitV6')
    @OptBitV6.setter
    def OptBitV6(self, value):
        self._set_attribute('optBitV6', value)

    @property
    def Option(self):
        """

        Returns:
            number
        """
        return self._get_attribute('option')
    @Option.setter
    def Option(self, value):
        self._set_attribute('option', value)

    @property
    def Prefixes(self):
        """

        Returns:
            list(dict(arg1:str,arg2:number,arg3:number,arg4:number))
        """
        return self._get_attribute('prefixes')
    @Prefixes.setter
    def Prefixes(self, value):
        self._set_attribute('prefixes', value)

    @property
    def RouterPriority(self):
        """

        Returns:
            number
        """
        return self._get_attribute('routerPriority')
    @RouterPriority.setter
    def RouterPriority(self, value):
        self._set_attribute('routerPriority', value)

    def update(self, CountLsa=None, IncrLinkStateId=None, LocalInterfaceAddress=None, OptBitDc=None, OptBitE=None, OptBitMc=None, OptBitN=None, OptBitR=None, OptBitV6=None, Option=None, Prefixes=None, RouterPriority=None):
        """Updates a child instance of link on the server.

        Args:
            CountLsa (number): 
            IncrLinkStateId (str): 
            LocalInterfaceAddress (str): 
            OptBitDc (bool): 
            OptBitE (bool): 
            OptBitMc (bool): 
            OptBitN (bool): 
            OptBitR (bool): 
            OptBitV6 (bool): 
            Option (number): 
            Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number))): 
            RouterPriority (number): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, CountLsa=None, IncrLinkStateId=None, LocalInterfaceAddress=None, OptBitDc=None, OptBitE=None, OptBitMc=None, OptBitN=None, OptBitR=None, OptBitV6=None, Option=None, Prefixes=None, RouterPriority=None):
        """Finds and retrieves link data from the server.

        All named parameters support regex and can be used to selectively retrieve link data from the server.
        By default the find method takes no parameters and will retrieve all link data from the server.

        Args:
            CountLsa (number): 
            IncrLinkStateId (str): 
            LocalInterfaceAddress (str): 
            OptBitDc (bool): 
            OptBitE (bool): 
            OptBitMc (bool): 
            OptBitN (bool): 
            OptBitR (bool): 
            OptBitV6 (bool): 
            Option (number): 
            Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number))): 
            RouterPriority (number): 

        Returns:
            self: This instance with matching link data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the link data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

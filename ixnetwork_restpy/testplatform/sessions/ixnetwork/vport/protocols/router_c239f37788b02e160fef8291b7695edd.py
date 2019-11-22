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


class Router(Base):
    """
    The Router class encapsulates a list of router resources that is managed by the system.
    A list of resources can be retrieved from the server using the Router.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'router'

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def BBit(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('bBit')
    @BBit.setter
    def BBit(self, value):
        self._set_attribute('bBit', value)

    @property
    def EBit(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('eBit')
    @EBit.setter
    def EBit(self, value):
        self._set_attribute('eBit', value)

    @property
    def Interfaces(self):
        """

        Returns:
            list(dict(arg1:str,arg2:str,arg3:str[pointToPoint|transit|stub|virtual],arg4:number))
        """
        return self._get_attribute('interfaces')
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute('interfaces', value)

    @property
    def VBit(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('vBit')
    @VBit.setter
    def VBit(self, value):
        self._set_attribute('vBit', value)

    def update(self, BBit=None, EBit=None, Interfaces=None, VBit=None):
        """Updates a child instance of router on the server.

        Args:
            BBit (bool): 
            EBit (bool): 
            Interfaces (list(dict(arg1:str,arg2:str,arg3:str[pointToPoint|transit|stub|virtual],arg4:number))): 
            VBit (bool): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, BBit=None, EBit=None, Interfaces=None, VBit=None):
        """Finds and retrieves router data from the server.

        All named parameters support regex and can be used to selectively retrieve router data from the server.
        By default the find method takes no parameters and will retrieve all router data from the server.

        Args:
            BBit (bool): 
            EBit (bool): 
            Interfaces (list(dict(arg1:str,arg2:str,arg3:str[pointToPoint|transit|stub|virtual],arg4:number))): 
            VBit (bool): 

        Returns:
            self: This instance with matching router data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the router data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class IntraAreaPrefix(Base):
    """
    The IntraAreaPrefix class encapsulates a list of intraAreaPrefix resources that is managed by the system.
    A list of resources can be retrieved from the server using the IntraAreaPrefix.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'intraAreaPrefix'

    def __init__(self, parent):
        super(IntraAreaPrefix, self).__init__(parent)

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
    def Prefixes(self):
        """

        Returns:
            list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number))
        """
        return self._get_attribute('prefixes')
    @Prefixes.setter
    def Prefixes(self, value):
        self._set_attribute('prefixes', value)

    @property
    def RefLinkStateId(self):
        """

        Returns:
            str
        """
        return self._get_attribute('refLinkStateId')
    @RefLinkStateId.setter
    def RefLinkStateId(self, value):
        self._set_attribute('refLinkStateId', value)

    @property
    def RefRouterId(self):
        """

        Returns:
            str
        """
        return self._get_attribute('refRouterId')
    @RefRouterId.setter
    def RefRouterId(self, value):
        self._set_attribute('refRouterId', value)

    @property
    def ReferenceType(self):
        """

        Returns:
            str(routerLsa|networkLsa)
        """
        return self._get_attribute('referenceType')
    @ReferenceType.setter
    def ReferenceType(self, value):
        self._set_attribute('referenceType', value)

    def update(self, CountLsa=None, IncrLinkStateId=None, Prefixes=None, RefLinkStateId=None, RefRouterId=None, ReferenceType=None):
        """Updates a child instance of intraAreaPrefix on the server.

        Args:
            CountLsa (number): 
            IncrLinkStateId (str): 
            Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number))): 
            RefLinkStateId (str): 
            RefRouterId (str): 
            ReferenceType (str(routerLsa|networkLsa)): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, CountLsa=None, IncrLinkStateId=None, Prefixes=None, RefLinkStateId=None, RefRouterId=None, ReferenceType=None):
        """Finds and retrieves intraAreaPrefix data from the server.

        All named parameters support regex and can be used to selectively retrieve intraAreaPrefix data from the server.
        By default the find method takes no parameters and will retrieve all intraAreaPrefix data from the server.

        Args:
            CountLsa (number): 
            IncrLinkStateId (str): 
            Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number))): 
            RefLinkStateId (str): 
            RefRouterId (str): 
            ReferenceType (str(routerLsa|networkLsa)): 

        Returns:
            self: This instance with matching intraAreaPrefix data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of intraAreaPrefix data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the intraAreaPrefix data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

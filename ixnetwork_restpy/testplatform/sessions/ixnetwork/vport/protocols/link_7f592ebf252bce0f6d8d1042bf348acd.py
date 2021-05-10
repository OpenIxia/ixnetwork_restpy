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


class Link(Base):
    """
    The Link class encapsulates a list of link resources that are managed by the system.
    A list of resources can be retrieved from the server using the Link.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'link'
    _SDM_ATT_MAP = {
        'CountLsa': 'countLsa',
        'IncrLinkStateId': 'incrLinkStateId',
        'LocalInterfaceAddress': 'localInterfaceAddress',
        'OptBitDc': 'optBitDc',
        'OptBitE': 'optBitE',
        'OptBitMc': 'optBitMc',
        'OptBitN': 'optBitN',
        'OptBitR': 'optBitR',
        'OptBitV6': 'optBitV6',
        'Option': 'option',
        'Prefixes': 'prefixes',
        'RouterPriority': 'routerPriority',
    }

    def __init__(self, parent):
        super(Link, self).__init__(parent)

    @property
    def CountLsa(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountLsa'])
    @CountLsa.setter
    def CountLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountLsa'], value)

    @property
    def IncrLinkStateId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrLinkStateId'])
    @IncrLinkStateId.setter
    def IncrLinkStateId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrLinkStateId'], value)

    @property
    def LocalInterfaceAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalInterfaceAddress'])
    @LocalInterfaceAddress.setter
    def LocalInterfaceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalInterfaceAddress'], value)

    @property
    def OptBitDc(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitDc'])
    @OptBitDc.setter
    def OptBitDc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitDc'], value)

    @property
    def OptBitE(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitE'])
    @OptBitE.setter
    def OptBitE(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitE'], value)

    @property
    def OptBitMc(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitMc'])
    @OptBitMc.setter
    def OptBitMc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitMc'], value)

    @property
    def OptBitN(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitN'])
    @OptBitN.setter
    def OptBitN(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitN'], value)

    @property
    def OptBitR(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitR'])
    @OptBitR.setter
    def OptBitR(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitR'], value)

    @property
    def OptBitV6(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitV6'])
    @OptBitV6.setter
    def OptBitV6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitV6'], value)

    @property
    def Option(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Option'])
    @Option.setter
    def Option(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Option'], value)

    @property
    def Prefixes(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:number,arg3:number,arg4:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Prefixes'])
    @Prefixes.setter
    def Prefixes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Prefixes'], value)

    @property
    def RouterPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterPriority'])
    @RouterPriority.setter
    def RouterPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterPriority'], value)

    def update(self, CountLsa=None, IncrLinkStateId=None, LocalInterfaceAddress=None, OptBitDc=None, OptBitE=None, OptBitMc=None, OptBitN=None, OptBitR=None, OptBitV6=None, Option=None, Prefixes=None, RouterPriority=None):
        """Updates link resource on the server.

        Args
        ----
        - CountLsa (number): 
        - IncrLinkStateId (str): 
        - LocalInterfaceAddress (str): 
        - OptBitDc (bool): 
        - OptBitE (bool): 
        - OptBitMc (bool): 
        - OptBitN (bool): 
        - OptBitR (bool): 
        - OptBitV6 (bool): 
        - Option (number): 
        - Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number))): 
        - RouterPriority (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CountLsa=None, IncrLinkStateId=None, LocalInterfaceAddress=None, OptBitDc=None, OptBitE=None, OptBitMc=None, OptBitN=None, OptBitR=None, OptBitV6=None, Option=None, Prefixes=None, RouterPriority=None):
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - CountLsa (number): 
        - IncrLinkStateId (str): 
        - LocalInterfaceAddress (str): 
        - OptBitDc (bool): 
        - OptBitE (bool): 
        - OptBitMc (bool): 
        - OptBitN (bool): 
        - OptBitR (bool): 
        - OptBitV6 (bool): 
        - Option (number): 
        - Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number))): 
        - RouterPriority (number): 

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

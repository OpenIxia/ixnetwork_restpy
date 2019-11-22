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


class InterAreaPrefix(Base):
    """
    The InterAreaPrefix class encapsulates a list of interAreaPrefix resources that is managed by the system.
    A list of resources can be retrieved from the server using the InterAreaPrefix.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'interAreaPrefix'

    def __init__(self, parent):
        super(InterAreaPrefix, self).__init__(parent)

    @property
    def AddPrefixLength(self):
        """

        Returns:
            number
        """
        return self._get_attribute('addPrefixLength')
    @AddPrefixLength.setter
    def AddPrefixLength(self, value):
        self._set_attribute('addPrefixLength', value)

    @property
    def AddressPrefix(self):
        """

        Returns:
            str
        """
        return self._get_attribute('addressPrefix')
    @AddressPrefix.setter
    def AddressPrefix(self, value):
        self._set_attribute('addressPrefix', value)

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
    def LsaCount(self):
        """

        Returns:
            number
        """
        return self._get_attribute('lsaCount')
    @LsaCount.setter
    def LsaCount(self, value):
        self._set_attribute('lsaCount', value)

    @property
    def Metric(self):
        """

        Returns:
            number
        """
        return self._get_attribute('metric')
    @Metric.setter
    def Metric(self, value):
        self._set_attribute('metric', value)

    @property
    def OptBitLa(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitLa')
    @OptBitLa.setter
    def OptBitLa(self, value):
        self._set_attribute('optBitLa', value)

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
    def OptBitNu(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitNu')
    @OptBitNu.setter
    def OptBitNu(self, value):
        self._set_attribute('optBitNu', value)

    @property
    def OptBitP(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('optBitP')
    @OptBitP.setter
    def OptBitP(self, value):
        self._set_attribute('optBitP', value)

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
    def PrefixAddressIncrementBy(self):
        """

        Returns:
            number
        """
        return self._get_attribute('prefixAddressIncrementBy')
    @PrefixAddressIncrementBy.setter
    def PrefixAddressIncrementBy(self, value):
        self._set_attribute('prefixAddressIncrementBy', value)

    def update(self, AddPrefixLength=None, AddressPrefix=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, Option=None, PrefixAddressIncrementBy=None):
        """Updates a child instance of interAreaPrefix on the server.

        Args:
            AddPrefixLength (number): 
            AddressPrefix (str): 
            IncrLinkStateId (str): 
            LsaCount (number): 
            Metric (number): 
            OptBitLa (bool): 
            OptBitMc (bool): 
            OptBitNu (bool): 
            OptBitP (bool): 
            Option (number): 
            PrefixAddressIncrementBy (number): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, AddPrefixLength=None, AddressPrefix=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, Option=None, PrefixAddressIncrementBy=None):
        """Finds and retrieves interAreaPrefix data from the server.

        All named parameters support regex and can be used to selectively retrieve interAreaPrefix data from the server.
        By default the find method takes no parameters and will retrieve all interAreaPrefix data from the server.

        Args:
            AddPrefixLength (number): 
            AddressPrefix (str): 
            IncrLinkStateId (str): 
            LsaCount (number): 
            Metric (number): 
            OptBitLa (bool): 
            OptBitMc (bool): 
            OptBitNu (bool): 
            OptBitP (bool): 
            Option (number): 
            PrefixAddressIncrementBy (number): 

        Returns:
            self: This instance with matching interAreaPrefix data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of interAreaPrefix data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the interAreaPrefix data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

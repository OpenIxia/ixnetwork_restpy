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


class InterAreaPrefix(Base):
    """
    The InterAreaPrefix class encapsulates a list of interAreaPrefix resources that are managed by the system.
    A list of resources can be retrieved from the server using the InterAreaPrefix.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'interAreaPrefix'
    _SDM_ATT_MAP = {
        'AddPrefixLength': 'addPrefixLength',
        'AddressPrefix': 'addressPrefix',
        'IncrLinkStateId': 'incrLinkStateId',
        'LsaCount': 'lsaCount',
        'Metric': 'metric',
        'OptBitLa': 'optBitLa',
        'OptBitMc': 'optBitMc',
        'OptBitNu': 'optBitNu',
        'OptBitP': 'optBitP',
        'Option': 'option',
        'PrefixAddressIncrementBy': 'prefixAddressIncrementBy',
    }

    def __init__(self, parent):
        super(InterAreaPrefix, self).__init__(parent)

    @property
    def AddPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddPrefixLength'])
    @AddPrefixLength.setter
    def AddPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddPrefixLength'], value)

    @property
    def AddressPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressPrefix'])
    @AddressPrefix.setter
    def AddressPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressPrefix'], value)

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
    def LsaCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaCount'])
    @LsaCount.setter
    def LsaCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaCount'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def OptBitLa(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitLa'])
    @OptBitLa.setter
    def OptBitLa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitLa'], value)

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
    def OptBitNu(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitNu'])
    @OptBitNu.setter
    def OptBitNu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitNu'], value)

    @property
    def OptBitP(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitP'])
    @OptBitP.setter
    def OptBitP(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitP'], value)

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
    def PrefixAddressIncrementBy(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixAddressIncrementBy'])
    @PrefixAddressIncrementBy.setter
    def PrefixAddressIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixAddressIncrementBy'], value)

    def update(self, AddPrefixLength=None, AddressPrefix=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, Option=None, PrefixAddressIncrementBy=None):
        """Updates interAreaPrefix resource on the server.

        Args
        ----
        - AddPrefixLength (number): 
        - AddressPrefix (str): 
        - IncrLinkStateId (str): 
        - LsaCount (number): 
        - Metric (number): 
        - OptBitLa (bool): 
        - OptBitMc (bool): 
        - OptBitNu (bool): 
        - OptBitP (bool): 
        - Option (number): 
        - PrefixAddressIncrementBy (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AddPrefixLength=None, AddressPrefix=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, Option=None, PrefixAddressIncrementBy=None):
        """Finds and retrieves interAreaPrefix resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interAreaPrefix resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interAreaPrefix resources from the server.

        Args
        ----
        - AddPrefixLength (number): 
        - AddressPrefix (str): 
        - IncrLinkStateId (str): 
        - LsaCount (number): 
        - Metric (number): 
        - OptBitLa (bool): 
        - OptBitMc (bool): 
        - OptBitNu (bool): 
        - OptBitP (bool): 
        - Option (number): 
        - PrefixAddressIncrementBy (number): 

        Returns
        -------
        - self: This instance with matching interAreaPrefix resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interAreaPrefix data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interAreaPrefix resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

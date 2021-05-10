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


class AsExternal(Base):
    """
    The AsExternal class encapsulates a list of asExternal resources that are managed by the system.
    A list of resources can be retrieved from the server using the AsExternal.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'asExternal'
    _SDM_ATT_MAP = {
        'AddPrefix': 'addPrefix',
        'AddPrefixIncrementBy': 'addPrefixIncrementBy',
        'AddPrefixLength': 'addPrefixLength',
        'AddPrefixOption': 'addPrefixOption',
        'EBit': 'eBit',
        'ExternalRouteTag': 'externalRouteTag',
        'FBit': 'fBit',
        'ForwardingAddress': 'forwardingAddress',
        'IncrLinkStateId': 'incrLinkStateId',
        'LsaCount': 'lsaCount',
        'Metric': 'metric',
        'OptBitLa': 'optBitLa',
        'OptBitMc': 'optBitMc',
        'OptBitNu': 'optBitNu',
        'OptBitP': 'optBitP',
        'ReferenceLinkStateId': 'referenceLinkStateId',
        'ReferenceLsType': 'referenceLsType',
        'TBit': 'tBit',
    }

    def __init__(self, parent):
        super(AsExternal, self).__init__(parent)

    @property
    def AddPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddPrefix'])
    @AddPrefix.setter
    def AddPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddPrefix'], value)

    @property
    def AddPrefixIncrementBy(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddPrefixIncrementBy'])
    @AddPrefixIncrementBy.setter
    def AddPrefixIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddPrefixIncrementBy'], value)

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
    def AddPrefixOption(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddPrefixOption'])
    @AddPrefixOption.setter
    def AddPrefixOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddPrefixOption'], value)

    @property
    def EBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EBit'])
    @EBit.setter
    def EBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EBit'], value)

    @property
    def ExternalRouteTag(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalRouteTag'])
    @ExternalRouteTag.setter
    def ExternalRouteTag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalRouteTag'], value)

    @property
    def FBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FBit'])
    @FBit.setter
    def FBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FBit'], value)

    @property
    def ForwardingAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForwardingAddress'])
    @ForwardingAddress.setter
    def ForwardingAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForwardingAddress'], value)

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
    def ReferenceLinkStateId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReferenceLinkStateId'])
    @ReferenceLinkStateId.setter
    def ReferenceLinkStateId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReferenceLinkStateId'], value)

    @property
    def ReferenceLsType(self):
        """
        Returns
        -------
        - str(ignore | routerLsa | networkLsa): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReferenceLsType'])
    @ReferenceLsType.setter
    def ReferenceLsType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReferenceLsType'], value)

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TBit'])
    @TBit.setter
    def TBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TBit'], value)

    def update(self, AddPrefix=None, AddPrefixIncrementBy=None, AddPrefixLength=None, AddPrefixOption=None, EBit=None, ExternalRouteTag=None, FBit=None, ForwardingAddress=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, ReferenceLinkStateId=None, ReferenceLsType=None, TBit=None):
        """Updates asExternal resource on the server.

        Args
        ----
        - AddPrefix (str): 
        - AddPrefixIncrementBy (number): 
        - AddPrefixLength (number): 
        - AddPrefixOption (number): 
        - EBit (bool): 
        - ExternalRouteTag (str): 
        - FBit (bool): 
        - ForwardingAddress (str): 
        - IncrLinkStateId (str): 
        - LsaCount (number): 
        - Metric (number): 
        - OptBitLa (bool): 
        - OptBitMc (bool): 
        - OptBitNu (bool): 
        - OptBitP (bool): 
        - ReferenceLinkStateId (str): 
        - ReferenceLsType (str(ignore | routerLsa | networkLsa)): 
        - TBit (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AddPrefix=None, AddPrefixIncrementBy=None, AddPrefixLength=None, AddPrefixOption=None, EBit=None, ExternalRouteTag=None, FBit=None, ForwardingAddress=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, ReferenceLinkStateId=None, ReferenceLsType=None, TBit=None):
        """Finds and retrieves asExternal resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve asExternal resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all asExternal resources from the server.

        Args
        ----
        - AddPrefix (str): 
        - AddPrefixIncrementBy (number): 
        - AddPrefixLength (number): 
        - AddPrefixOption (number): 
        - EBit (bool): 
        - ExternalRouteTag (str): 
        - FBit (bool): 
        - ForwardingAddress (str): 
        - IncrLinkStateId (str): 
        - LsaCount (number): 
        - Metric (number): 
        - OptBitLa (bool): 
        - OptBitMc (bool): 
        - OptBitNu (bool): 
        - OptBitP (bool): 
        - ReferenceLinkStateId (str): 
        - ReferenceLsType (str(ignore | routerLsa | networkLsa)): 
        - TBit (bool): 

        Returns
        -------
        - self: This instance with matching asExternal resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of asExternal data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the asExternal resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class AsExternal(Base):
    """
    The AsExternal class encapsulates a list of asExternal resources that is managed by the system.
    A list of resources can be retrieved from the server using the AsExternal.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'asExternal'

    def __init__(self, parent):
        super(AsExternal, self).__init__(parent)

    @property
    def AddPrefix(self):
        """

        Returns:
            str
        """
        return self._get_attribute('addPrefix')
    @AddPrefix.setter
    def AddPrefix(self, value):
        self._set_attribute('addPrefix', value)

    @property
    def AddPrefixIncrementBy(self):
        """

        Returns:
            number
        """
        return self._get_attribute('addPrefixIncrementBy')
    @AddPrefixIncrementBy.setter
    def AddPrefixIncrementBy(self, value):
        self._set_attribute('addPrefixIncrementBy', value)

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
    def AddPrefixOption(self):
        """

        Returns:
            number
        """
        return self._get_attribute('addPrefixOption')
    @AddPrefixOption.setter
    def AddPrefixOption(self, value):
        self._set_attribute('addPrefixOption', value)

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
    def ExternalRouteTag(self):
        """

        Returns:
            str
        """
        return self._get_attribute('externalRouteTag')
    @ExternalRouteTag.setter
    def ExternalRouteTag(self, value):
        self._set_attribute('externalRouteTag', value)

    @property
    def FBit(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('fBit')
    @FBit.setter
    def FBit(self, value):
        self._set_attribute('fBit', value)

    @property
    def ForwardingAddress(self):
        """

        Returns:
            str
        """
        return self._get_attribute('forwardingAddress')
    @ForwardingAddress.setter
    def ForwardingAddress(self, value):
        self._set_attribute('forwardingAddress', value)

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
    def ReferenceLinkStateId(self):
        """

        Returns:
            str
        """
        return self._get_attribute('referenceLinkStateId')
    @ReferenceLinkStateId.setter
    def ReferenceLinkStateId(self, value):
        self._set_attribute('referenceLinkStateId', value)

    @property
    def ReferenceLsType(self):
        """

        Returns:
            str(ignore|routerLsa|networkLsa)
        """
        return self._get_attribute('referenceLsType')
    @ReferenceLsType.setter
    def ReferenceLsType(self, value):
        self._set_attribute('referenceLsType', value)

    @property
    def TBit(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('tBit')
    @TBit.setter
    def TBit(self, value):
        self._set_attribute('tBit', value)

    def update(self, AddPrefix=None, AddPrefixIncrementBy=None, AddPrefixLength=None, AddPrefixOption=None, EBit=None, ExternalRouteTag=None, FBit=None, ForwardingAddress=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, ReferenceLinkStateId=None, ReferenceLsType=None, TBit=None):
        """Updates a child instance of asExternal on the server.

        Args:
            AddPrefix (str): 
            AddPrefixIncrementBy (number): 
            AddPrefixLength (number): 
            AddPrefixOption (number): 
            EBit (bool): 
            ExternalRouteTag (str): 
            FBit (bool): 
            ForwardingAddress (str): 
            IncrLinkStateId (str): 
            LsaCount (number): 
            Metric (number): 
            OptBitLa (bool): 
            OptBitMc (bool): 
            OptBitNu (bool): 
            OptBitP (bool): 
            ReferenceLinkStateId (str): 
            ReferenceLsType (str(ignore|routerLsa|networkLsa)): 
            TBit (bool): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, AddPrefix=None, AddPrefixIncrementBy=None, AddPrefixLength=None, AddPrefixOption=None, EBit=None, ExternalRouteTag=None, FBit=None, ForwardingAddress=None, IncrLinkStateId=None, LsaCount=None, Metric=None, OptBitLa=None, OptBitMc=None, OptBitNu=None, OptBitP=None, ReferenceLinkStateId=None, ReferenceLsType=None, TBit=None):
        """Finds and retrieves asExternal data from the server.

        All named parameters support regex and can be used to selectively retrieve asExternal data from the server.
        By default the find method takes no parameters and will retrieve all asExternal data from the server.

        Args:
            AddPrefix (str): 
            AddPrefixIncrementBy (number): 
            AddPrefixLength (number): 
            AddPrefixOption (number): 
            EBit (bool): 
            ExternalRouteTag (str): 
            FBit (bool): 
            ForwardingAddress (str): 
            IncrLinkStateId (str): 
            LsaCount (number): 
            Metric (number): 
            OptBitLa (bool): 
            OptBitMc (bool): 
            OptBitNu (bool): 
            OptBitP (bool): 
            ReferenceLinkStateId (str): 
            ReferenceLsType (str(ignore|routerLsa|networkLsa)): 
            TBit (bool): 

        Returns:
            self: This instance with matching asExternal data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of asExternal data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the asExternal data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

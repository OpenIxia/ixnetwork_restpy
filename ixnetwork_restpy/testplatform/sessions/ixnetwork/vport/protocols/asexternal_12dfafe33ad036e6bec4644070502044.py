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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class AsExternal(Base):
    """
    The AsExternal class encapsulates a list of asExternal resources that are managed by the system.
    A list of resources can be retrieved from the server using the AsExternal.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "asExternal"
    _SDM_ATT_MAP = {
        "AddPrefix": "addPrefix",
        "AddPrefixIncrementBy": "addPrefixIncrementBy",
        "AddPrefixLength": "addPrefixLength",
        "AddPrefixOption": "addPrefixOption",
        "EBit": "eBit",
        "ExternalRouteTag": "externalRouteTag",
        "FBit": "fBit",
        "ForwardingAddress": "forwardingAddress",
        "IncrLinkStateId": "incrLinkStateId",
        "LsaCount": "lsaCount",
        "Metric": "metric",
        "OptBitLa": "optBitLa",
        "OptBitMc": "optBitMc",
        "OptBitNu": "optBitNu",
        "OptBitP": "optBitP",
        "ReferenceLinkStateId": "referenceLinkStateId",
        "ReferenceLsType": "referenceLsType",
        "TBit": "tBit",
    }
    _SDM_ENUM_MAP = {
        "referenceLsType": ["ignore", "routerLsa", "networkLsa"],
    }

    def __init__(self, parent, list_op=False):
        super(AsExternal, self).__init__(parent, list_op)

    @property
    def AddPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddPrefix"])

    @AddPrefix.setter
    def AddPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddPrefix"], value)

    @property
    def AddPrefixIncrementBy(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddPrefixIncrementBy"])

    @AddPrefixIncrementBy.setter
    def AddPrefixIncrementBy(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddPrefixIncrementBy"], value)

    @property
    def AddPrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddPrefixLength"])

    @AddPrefixLength.setter
    def AddPrefixLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddPrefixLength"], value)

    @property
    def AddPrefixOption(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddPrefixOption"])

    @AddPrefixOption.setter
    def AddPrefixOption(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddPrefixOption"], value)

    @property
    def EBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EBit"])

    @EBit.setter
    def EBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EBit"], value)

    @property
    def ExternalRouteTag(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExternalRouteTag"])

    @ExternalRouteTag.setter
    def ExternalRouteTag(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExternalRouteTag"], value)

    @property
    def FBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FBit"])

    @FBit.setter
    def FBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FBit"], value)

    @property
    def ForwardingAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForwardingAddress"])

    @ForwardingAddress.setter
    def ForwardingAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForwardingAddress"], value)

    @property
    def IncrLinkStateId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrLinkStateId"])

    @IncrLinkStateId.setter
    def IncrLinkStateId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrLinkStateId"], value)

    @property
    def LsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsaCount"])

    @LsaCount.setter
    def LsaCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsaCount"], value)

    @property
    def Metric(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Metric"])

    @Metric.setter
    def Metric(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Metric"], value)

    @property
    def OptBitLa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitLa"])

    @OptBitLa.setter
    def OptBitLa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitLa"], value)

    @property
    def OptBitMc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitMc"])

    @OptBitMc.setter
    def OptBitMc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitMc"], value)

    @property
    def OptBitNu(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitNu"])

    @OptBitNu.setter
    def OptBitNu(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitNu"], value)

    @property
    def OptBitP(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitP"])

    @OptBitP.setter
    def OptBitP(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitP"], value)

    @property
    def ReferenceLinkStateId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReferenceLinkStateId"])

    @ReferenceLinkStateId.setter
    def ReferenceLinkStateId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReferenceLinkStateId"], value)

    @property
    def ReferenceLsType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ignore | routerLsa | networkLsa):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReferenceLsType"])

    @ReferenceLsType.setter
    def ReferenceLsType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReferenceLsType"], value)

    @property
    def TBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TBit"])

    @TBit.setter
    def TBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TBit"], value)

    def update(
        self,
        AddPrefix=None,
        AddPrefixIncrementBy=None,
        AddPrefixLength=None,
        AddPrefixOption=None,
        EBit=None,
        ExternalRouteTag=None,
        FBit=None,
        ForwardingAddress=None,
        IncrLinkStateId=None,
        LsaCount=None,
        Metric=None,
        OptBitLa=None,
        OptBitMc=None,
        OptBitNu=None,
        OptBitP=None,
        ReferenceLinkStateId=None,
        ReferenceLsType=None,
        TBit=None,
    ):
        # type: (str, int, int, int, bool, str, bool, str, str, int, int, bool, bool, bool, bool, str, str, bool) -> AsExternal
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

    def add(
        self,
        AddPrefix=None,
        AddPrefixIncrementBy=None,
        AddPrefixLength=None,
        AddPrefixOption=None,
        EBit=None,
        ExternalRouteTag=None,
        FBit=None,
        ForwardingAddress=None,
        IncrLinkStateId=None,
        LsaCount=None,
        Metric=None,
        OptBitLa=None,
        OptBitMc=None,
        OptBitNu=None,
        OptBitP=None,
        ReferenceLinkStateId=None,
        ReferenceLsType=None,
        TBit=None,
    ):
        # type: (str, int, int, int, bool, str, bool, str, str, int, int, bool, bool, bool, bool, str, str, bool) -> AsExternal
        """Adds a new asExternal resource on the json, only valid with batch add utility

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
        - self: This instance with all currently retrieved asExternal resources using find and the newly added asExternal resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AddPrefix=None,
        AddPrefixIncrementBy=None,
        AddPrefixLength=None,
        AddPrefixOption=None,
        EBit=None,
        ExternalRouteTag=None,
        FBit=None,
        ForwardingAddress=None,
        IncrLinkStateId=None,
        LsaCount=None,
        Metric=None,
        OptBitLa=None,
        OptBitMc=None,
        OptBitNu=None,
        OptBitP=None,
        ReferenceLinkStateId=None,
        ReferenceLsType=None,
        TBit=None,
    ):
        # type: (str, int, int, int, bool, str, bool, str, str, int, int, bool, bool, bool, bool, str, str, bool) -> AsExternal
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

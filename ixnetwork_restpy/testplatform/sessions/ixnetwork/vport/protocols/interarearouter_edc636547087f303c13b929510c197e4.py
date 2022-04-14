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


class InterAreaRouter(Base):
    """
    The InterAreaRouter class encapsulates a list of interAreaRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the InterAreaRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "interAreaRouter"
    _SDM_ATT_MAP = {
        "IncrLinkStateId": "incrLinkStateId",
        "LsaCount": "lsaCount",
        "Metric": "metric",
        "OptBitDc": "optBitDc",
        "OptBitE": "optBitE",
        "OptBitMc": "optBitMc",
        "OptBitN": "optBitN",
        "OptBitR": "optBitR",
        "OptBitV6": "optBitV6",
        "Option": "option",
        "RouterId": "routerId",
        "RouterIdIncrementBy": "routerIdIncrementBy",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(InterAreaRouter, self).__init__(parent, list_op)

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
    def OptBitDc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitDc"])

    @OptBitDc.setter
    def OptBitDc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitDc"], value)

    @property
    def OptBitE(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitE"])

    @OptBitE.setter
    def OptBitE(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitE"], value)

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
    def OptBitN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitN"])

    @OptBitN.setter
    def OptBitN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitN"], value)

    @property
    def OptBitR(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitR"])

    @OptBitR.setter
    def OptBitR(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitR"], value)

    @property
    def OptBitV6(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitV6"])

    @OptBitV6.setter
    def OptBitV6(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitV6"], value)

    @property
    def Option(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Option"])

    @Option.setter
    def Option(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Option"], value)

    @property
    def RouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterId"])

    @RouterId.setter
    def RouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterId"], value)

    @property
    def RouterIdIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterIdIncrementBy"])

    @RouterIdIncrementBy.setter
    def RouterIdIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterIdIncrementBy"], value)

    def update(
        self,
        IncrLinkStateId=None,
        LsaCount=None,
        Metric=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
        RouterId=None,
        RouterIdIncrementBy=None,
    ):
        # type: (str, int, int, bool, bool, bool, bool, bool, bool, int, str, str) -> InterAreaRouter
        """Updates interAreaRouter resource on the server.

        Args
        ----
        - IncrLinkStateId (str):
        - LsaCount (number):
        - Metric (number):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):
        - RouterId (str):
        - RouterIdIncrementBy (str):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        IncrLinkStateId=None,
        LsaCount=None,
        Metric=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
        RouterId=None,
        RouterIdIncrementBy=None,
    ):
        # type: (str, int, int, bool, bool, bool, bool, bool, bool, int, str, str) -> InterAreaRouter
        """Adds a new interAreaRouter resource on the json, only valid with batch add utility

        Args
        ----
        - IncrLinkStateId (str):
        - LsaCount (number):
        - Metric (number):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):
        - RouterId (str):
        - RouterIdIncrementBy (str):

        Returns
        -------
        - self: This instance with all currently retrieved interAreaRouter resources using find and the newly added interAreaRouter resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        IncrLinkStateId=None,
        LsaCount=None,
        Metric=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
        RouterId=None,
        RouterIdIncrementBy=None,
    ):
        # type: (str, int, int, bool, bool, bool, bool, bool, bool, int, str, str) -> InterAreaRouter
        """Finds and retrieves interAreaRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interAreaRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interAreaRouter resources from the server.

        Args
        ----
        - IncrLinkStateId (str):
        - LsaCount (number):
        - Metric (number):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):
        - RouterId (str):
        - RouterIdIncrementBy (str):

        Returns
        -------
        - self: This instance with matching interAreaRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interAreaRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interAreaRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

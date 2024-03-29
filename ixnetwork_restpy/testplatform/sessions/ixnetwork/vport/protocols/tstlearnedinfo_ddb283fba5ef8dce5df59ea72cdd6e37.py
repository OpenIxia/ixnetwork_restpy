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


class TstLearnedInfo(Base):
    """NOT DEFINED
    The TstLearnedInfo class encapsulates a list of tstLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the TstLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "tstLearnedInfo"
    _SDM_ATT_MAP = {
        "BVlan": "bVlan",
        "CVlan": "cVlan",
        "MepMacAddress": "mepMacAddress",
        "OutOfSequenceTstCount": "outOfSequenceTstCount",
        "PrbsBitErrorCount": "prbsBitErrorCount",
        "RemoteMepMacAddress": "remoteMepMacAddress",
        "RxCount": "rxCount",
        "SVlan": "sVlan",
        "TxCount": "txCount",
        "TxState": "txState",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TstLearnedInfo, self).__init__(parent, list_op)

    @property
    def BVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlan"])

    @property
    def CVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CVlan"])

    @property
    def MepMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepMacAddress"])

    @property
    def OutOfSequenceTstCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutOfSequenceTstCount"])

    @property
    def PrbsBitErrorCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsBitErrorCount"])

    @property
    def RemoteMepMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteMepMacAddress"])

    @property
    def RxCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxCount"])

    @property
    def SVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SVlan"])

    @property
    def TxCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxCount"])

    @property
    def TxState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxState"])

    def add(self):
        """Adds a new tstLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved tstLearnedInfo resources using find and the newly added tstLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BVlan=None,
        CVlan=None,
        MepMacAddress=None,
        OutOfSequenceTstCount=None,
        PrbsBitErrorCount=None,
        RemoteMepMacAddress=None,
        RxCount=None,
        SVlan=None,
        TxCount=None,
        TxState=None,
    ):
        # type: (str, str, str, int, int, str, int, str, int, str) -> TstLearnedInfo
        """Finds and retrieves tstLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tstLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tstLearnedInfo resources from the server.

        Args
        ----
        - BVlan (str): NOT DEFINED
        - CVlan (str): NOT DEFINED
        - MepMacAddress (str): NOT DEFINED
        - OutOfSequenceTstCount (number): NOT DEFINED
        - PrbsBitErrorCount (number): NOT DEFINED
        - RemoteMepMacAddress (str): NOT DEFINED
        - RxCount (number): NOT DEFINED
        - SVlan (str): NOT DEFINED
        - TxCount (number): NOT DEFINED
        - TxState (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching tstLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tstLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tstLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

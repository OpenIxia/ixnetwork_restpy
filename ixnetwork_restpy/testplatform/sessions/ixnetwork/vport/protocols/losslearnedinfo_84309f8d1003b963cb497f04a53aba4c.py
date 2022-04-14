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


class LossLearnedInfo(Base):
    """NOT DEFINED
    The LossLearnedInfo class encapsulates a list of lossLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LossLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "lossLearnedInfo"
    _SDM_ATT_MAP = {
        "BVlan": "bVlan",
        "CVlan": "cVlan",
        "DestinationMacAddress": "destinationMacAddress",
        "FarEndLoss": "farEndLoss",
        "FarEndLossRatio": "farEndLossRatio",
        "LmrReceived": "lmrReceived",
        "MdLevel": "mdLevel",
        "NearEndLoss": "nearEndLoss",
        "NearEndLossRatio": "nearEndLossRatio",
        "SVlan": "sVlan",
        "SourceMacAddress": "sourceMacAddress",
        "SourceMepId": "sourceMepId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LossLearnedInfo, self).__init__(parent, list_op)

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
    def DestinationMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationMacAddress"])

    @property
    def FarEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FarEndLoss"])

    @property
    def FarEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FarEndLossRatio"])

    @property
    def LmrReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmrReceived"])

    @property
    def MdLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel"])

    @property
    def NearEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NearEndLoss"])

    @property
    def NearEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NearEndLossRatio"])

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
    def SourceMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceMacAddress"])

    @property
    def SourceMepId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceMepId"])

    def add(self):
        """Adds a new lossLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved lossLearnedInfo resources using find and the newly added lossLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BVlan=None,
        CVlan=None,
        DestinationMacAddress=None,
        FarEndLoss=None,
        FarEndLossRatio=None,
        LmrReceived=None,
        MdLevel=None,
        NearEndLoss=None,
        NearEndLossRatio=None,
        SVlan=None,
        SourceMacAddress=None,
        SourceMepId=None,
    ):
        # type: (str, str, str, int, str, bool, int, int, str, str, str, int) -> LossLearnedInfo
        """Finds and retrieves lossLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lossLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lossLearnedInfo resources from the server.

        Args
        ----
        - BVlan (str): NOT DEFINED
        - CVlan (str): NOT DEFINED
        - DestinationMacAddress (str): NOT DEFINED
        - FarEndLoss (number): NOT DEFINED
        - FarEndLossRatio (str): NOT DEFINED
        - LmrReceived (bool): NOT DEFINED
        - MdLevel (number): NOT DEFINED
        - NearEndLoss (number): NOT DEFINED
        - NearEndLossRatio (str): NOT DEFINED
        - SVlan (str): NOT DEFINED
        - SourceMacAddress (str): NOT DEFINED
        - SourceMepId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching lossLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lossLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lossLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

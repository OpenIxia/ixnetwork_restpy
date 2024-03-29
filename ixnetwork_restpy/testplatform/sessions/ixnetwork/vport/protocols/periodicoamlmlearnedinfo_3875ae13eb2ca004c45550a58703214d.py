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


class PeriodicOamLmLearnedInfo(Base):
    """NOT DEFINED
    The PeriodicOamLmLearnedInfo class encapsulates a list of periodicOamLmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PeriodicOamLmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "periodicOamLmLearnedInfo"
    _SDM_ATT_MAP = {
        "AvgFarEndLoss": "avgFarEndLoss",
        "AvgNearEndLoss": "avgNearEndLoss",
        "BVlan": "bVlan",
        "CVlan": "cVlan",
        "CcmReceivedCount": "ccmReceivedCount",
        "CcmSentCount": "ccmSentCount",
        "CurrentFarEndLoss": "currentFarEndLoss",
        "CurrentFarEndLossRatio": "currentFarEndLossRatio",
        "CurrentNearEndLoss": "currentNearEndLoss",
        "CurrentNearEndLossRatio": "currentNearEndLossRatio",
        "DestinationMacAddress": "destinationMacAddress",
        "LmmSentCount": "lmmSentCount",
        "MaxFarEndLoss": "maxFarEndLoss",
        "MaxFarEndLossRatio": "maxFarEndLossRatio",
        "MaxNearEndLoss": "maxNearEndLoss",
        "MaxNearEndLossRatio": "maxNearEndLossRatio",
        "MdLevel": "mdLevel",
        "MinFarEndLoss": "minFarEndLoss",
        "MinFarEndLossRatio": "minFarEndLossRatio",
        "MinNearEndLoss": "minNearEndLoss",
        "MinNearEndLossRatio": "minNearEndLossRatio",
        "NoReplyCount": "noReplyCount",
        "SVlan": "sVlan",
        "SourceMacAddress": "sourceMacAddress",
        "SourceMepId": "sourceMepId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PeriodicOamLmLearnedInfo, self).__init__(parent, list_op)

    @property
    def AvgFarEndLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvgFarEndLoss"])

    @property
    def AvgNearEndLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvgNearEndLoss"])

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
    def CcmReceivedCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmReceivedCount"])

    @property
    def CcmSentCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmSentCount"])

    @property
    def CurrentFarEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentFarEndLoss"])

    @property
    def CurrentFarEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentFarEndLossRatio"])

    @property
    def CurrentNearEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentNearEndLoss"])

    @property
    def CurrentNearEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentNearEndLossRatio"])

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
    def LmmSentCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmmSentCount"])

    @property
    def MaxFarEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxFarEndLoss"])

    @property
    def MaxFarEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxFarEndLossRatio"])

    @property
    def MaxNearEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxNearEndLoss"])

    @property
    def MaxNearEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxNearEndLossRatio"])

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
    def MinFarEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinFarEndLoss"])

    @property
    def MinFarEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinFarEndLossRatio"])

    @property
    def MinNearEndLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinNearEndLoss"])

    @property
    def MinNearEndLossRatio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinNearEndLossRatio"])

    @property
    def NoReplyCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoReplyCount"])

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
        """Adds a new periodicOamLmLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved periodicOamLmLearnedInfo resources using find and the newly added periodicOamLmLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvgFarEndLoss=None,
        AvgNearEndLoss=None,
        BVlan=None,
        CVlan=None,
        CcmReceivedCount=None,
        CcmSentCount=None,
        CurrentFarEndLoss=None,
        CurrentFarEndLossRatio=None,
        CurrentNearEndLoss=None,
        CurrentNearEndLossRatio=None,
        DestinationMacAddress=None,
        LmmSentCount=None,
        MaxFarEndLoss=None,
        MaxFarEndLossRatio=None,
        MaxNearEndLoss=None,
        MaxNearEndLossRatio=None,
        MdLevel=None,
        MinFarEndLoss=None,
        MinFarEndLossRatio=None,
        MinNearEndLoss=None,
        MinNearEndLossRatio=None,
        NoReplyCount=None,
        SVlan=None,
        SourceMacAddress=None,
        SourceMepId=None,
    ):
        # type: (str, str, str, str, int, int, int, str, int, str, str, int, int, str, int, str, int, int, str, int, str, int, str, str, int) -> PeriodicOamLmLearnedInfo
        """Finds and retrieves periodicOamLmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve periodicOamLmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all periodicOamLmLearnedInfo resources from the server.

        Args
        ----
        - AvgFarEndLoss (str): NOT DEFINED
        - AvgNearEndLoss (str): NOT DEFINED
        - BVlan (str): NOT DEFINED
        - CVlan (str): NOT DEFINED
        - CcmReceivedCount (number): NOT DEFINED
        - CcmSentCount (number): NOT DEFINED
        - CurrentFarEndLoss (number): NOT DEFINED
        - CurrentFarEndLossRatio (str): NOT DEFINED
        - CurrentNearEndLoss (number): NOT DEFINED
        - CurrentNearEndLossRatio (str): NOT DEFINED
        - DestinationMacAddress (str): NOT DEFINED
        - LmmSentCount (number): NOT DEFINED
        - MaxFarEndLoss (number): NOT DEFINED
        - MaxFarEndLossRatio (str): NOT DEFINED
        - MaxNearEndLoss (number): NOT DEFINED
        - MaxNearEndLossRatio (str): NOT DEFINED
        - MdLevel (number): NOT DEFINED
        - MinFarEndLoss (number): NOT DEFINED
        - MinFarEndLossRatio (str): NOT DEFINED
        - MinNearEndLoss (number): NOT DEFINED
        - MinNearEndLossRatio (str): NOT DEFINED
        - NoReplyCount (number): NOT DEFINED
        - SVlan (str): NOT DEFINED
        - SourceMacAddress (str): NOT DEFINED
        - SourceMepId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching periodicOamLmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of periodicOamLmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the periodicOamLmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

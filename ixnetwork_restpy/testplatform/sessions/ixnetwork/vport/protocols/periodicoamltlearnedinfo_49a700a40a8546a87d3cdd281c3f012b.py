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


class PeriodicOamLtLearnedInfo(Base):
    """This object holds the periodic OAM link trace learned information.
    The PeriodicOamLtLearnedInfo class encapsulates a list of periodicOamLtLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PeriodicOamLtLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "periodicOamLtLearnedInfo"
    _SDM_ATT_MAP = {
        "AverageHopCount": "averageHopCount",
        "CVlan": "cVlan",
        "CompleteReplyCount": "completeReplyCount",
        "DstMacAddress": "dstMacAddress",
        "LtmSentCount": "ltmSentCount",
        "MdLevel": "mdLevel",
        "NoReplyCount": "noReplyCount",
        "PartialReplyCount": "partialReplyCount",
        "RecentHopCount": "recentHopCount",
        "RecentHops": "recentHops",
        "RecentReplyStatus": "recentReplyStatus",
        "SVlan": "sVlan",
        "SrcMacAddress": "srcMacAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PeriodicOamLtLearnedInfo, self).__init__(parent, list_op)

    @property
    def LtLearnedHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_c9dfd2b401fd7b7df6753d431bdbe5b5.LtLearnedHop): An instance of the LtLearnedHop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_c9dfd2b401fd7b7df6753d431bdbe5b5 import (
            LtLearnedHop,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LtLearnedHop", None) is not None:
                return self._properties.get("LtLearnedHop")
        return LtLearnedHop(self)

    @property
    def AverageHopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned average hop count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageHopCount"])

    @property
    def CVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned C-VLAN identifier. (CFM only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CVlan"])

    @property
    def CompleteReplyCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of complete replies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CompleteReplyCount"])

    @property
    def DstMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DstMacAddress"])

    @property
    def LtmSentCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of Link Trace messages sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtmSentCount"])

    @property
    def MdLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned MD level.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel"])

    @property
    def NoReplyCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of no replies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoReplyCount"])

    @property
    def PartialReplyCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of partial replies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PartialReplyCount"])

    @property
    def RecentHopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned recent hop count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentHopCount"])

    @property
    def RecentHops(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned recent hops.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentHops"])

    @property
    def RecentReplyStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned recent replies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentReplyStatus"])

    @property
    def SVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned S-VLAN identifier. (CFM only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SVlan"])

    @property
    def SrcMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMacAddress"])

    def add(self):
        """Adds a new periodicOamLtLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved periodicOamLtLearnedInfo resources using find and the newly added periodicOamLtLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AverageHopCount=None,
        CVlan=None,
        CompleteReplyCount=None,
        DstMacAddress=None,
        LtmSentCount=None,
        MdLevel=None,
        NoReplyCount=None,
        PartialReplyCount=None,
        RecentHopCount=None,
        RecentHops=None,
        RecentReplyStatus=None,
        SVlan=None,
        SrcMacAddress=None,
    ):
        # type: (int, str, int, str, int, int, int, int, int, str, str, str, str) -> PeriodicOamLtLearnedInfo
        """Finds and retrieves periodicOamLtLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve periodicOamLtLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all periodicOamLtLearnedInfo resources from the server.

        Args
        ----
        - AverageHopCount (number): (read only) The learned average hop count.
        - CVlan (str): (read only) The learned C-VLAN identifier. (CFM only)
        - CompleteReplyCount (number): (read only) The learned number of complete replies.
        - DstMacAddress (str): (read only) The learned destination MAC address.
        - LtmSentCount (number): (read only) The learned number of Link Trace messages sent.
        - MdLevel (number): (read only) The learned MD level.
        - NoReplyCount (number): (read only) The learned number of no replies.
        - PartialReplyCount (number): (read only) The learned number of partial replies.
        - RecentHopCount (number): (read only) The learned recent hop count.
        - RecentHops (str): (read only) The learned recent hops.
        - RecentReplyStatus (str): (read only) The learned recent replies.
        - SVlan (str): (read only) The learned S-VLAN identifier. (CFM only)
        - SrcMacAddress (str): (read only) The learned source MAC address.

        Returns
        -------
        - self: This instance with matching periodicOamLtLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of periodicOamLtLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the periodicOamLtLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

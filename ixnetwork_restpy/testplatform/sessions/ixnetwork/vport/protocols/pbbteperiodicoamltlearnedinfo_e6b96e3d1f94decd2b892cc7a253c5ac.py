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


class PbbTePeriodicOamLtLearnedInfo(Base):
    """The pbbTeperiodicOamLtLearnedInfo object holds the PBB-TE periodic OAM link trace learned information.
    The PbbTePeriodicOamLtLearnedInfo class encapsulates a list of pbbTePeriodicOamLtLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PbbTePeriodicOamLtLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pbbTePeriodicOamLtLearnedInfo"
    _SDM_ATT_MAP = {
        "AverageHopCount": "averageHopCount",
        "BVlan": "bVlan",
        "CompleteReplyCount": "completeReplyCount",
        "DstMacAddress": "dstMacAddress",
        "LtmSentCount": "ltmSentCount",
        "MdLevel": "mdLevel",
        "NoReplyCount": "noReplyCount",
        "PartialReplyCount": "partialReplyCount",
        "RecentHopCount": "recentHopCount",
        "RecentHops": "recentHops",
        "RecentReplyStatus": "recentReplyStatus",
        "SrcMacAddress": "srcMacAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PbbTePeriodicOamLtLearnedInfo, self).__init__(parent, list_op)

    @property
    def LtLearnedHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_19e7e0d81477ac3abf65c44eff4f3a8a.LtLearnedHop): An instance of the LtLearnedHop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_19e7e0d81477ac3abf65c44eff4f3a8a import (
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
    def BVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned B-VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlan"])

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
    def SrcMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMacAddress"])

    def add(self):
        """Adds a new pbbTePeriodicOamLtLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved pbbTePeriodicOamLtLearnedInfo resources using find and the newly added pbbTePeriodicOamLtLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AverageHopCount=None,
        BVlan=None,
        CompleteReplyCount=None,
        DstMacAddress=None,
        LtmSentCount=None,
        MdLevel=None,
        NoReplyCount=None,
        PartialReplyCount=None,
        RecentHopCount=None,
        RecentHops=None,
        RecentReplyStatus=None,
        SrcMacAddress=None,
    ):
        # type: (int, str, int, str, int, int, int, int, int, str, str, str) -> PbbTePeriodicOamLtLearnedInfo
        """Finds and retrieves pbbTePeriodicOamLtLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pbbTePeriodicOamLtLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pbbTePeriodicOamLtLearnedInfo resources from the server.

        Args
        ----
        - AverageHopCount (number): (read only) The learned average hop count.
        - BVlan (str): (read only) The learned B-VLAN identifier.
        - CompleteReplyCount (number): (read only) The learned number of complete replies.
        - DstMacAddress (str): (read only) The learned destination MAC address.
        - LtmSentCount (number): (read only) The learned number of Link Trace messages sent.
        - MdLevel (number): (read only) The learned MD level.
        - NoReplyCount (number): (read only) The learned number of no replies.
        - PartialReplyCount (number): (read only) The learned number of partial replies.
        - RecentHopCount (number): (read only) The learned recent hop count.
        - RecentHops (str): (read only) The learned recent hops.
        - RecentReplyStatus (str): (read only) The learned recent replies.
        - SrcMacAddress (str): (read only) The learned source MAC address.

        Returns
        -------
        - self: This instance with matching pbbTePeriodicOamLtLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pbbTePeriodicOamLtLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pbbTePeriodicOamLtLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class PeriodicOamDmLearnedInfo(Base):
    """The periodicOamDmLearnedInfo object holds the periodic OAM delay measurement learned information
    The PeriodicOamDmLearnedInfo class encapsulates a list of periodicOamDmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PeriodicOamDmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "periodicOamDmLearnedInfo"
    _SDM_ATT_MAP = {
        "AverageDelayNanoSec": "averageDelayNanoSec",
        "AverageDelaySec": "averageDelaySec",
        "AverageDelayVariationNanoSec": "averageDelayVariationNanoSec",
        "AverageDelayVariationSec": "averageDelayVariationSec",
        "CVlan": "cVlan",
        "DmmCountSent": "dmmCountSent",
        "DstMacAddress": "dstMacAddress",
        "MdLevel": "mdLevel",
        "NoReplyCount": "noReplyCount",
        "OneDmReceivedCount": "oneDmReceivedCount",
        "RecentDelayNanoSec": "recentDelayNanoSec",
        "RecentDelaySec": "recentDelaySec",
        "RecentDelayVariationNanoSec": "recentDelayVariationNanoSec",
        "RecentDelayVariationSec": "recentDelayVariationSec",
        "SVlan": "sVlan",
        "SrcMacAddress": "srcMacAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PeriodicOamDmLearnedInfo, self).__init__(parent, list_op)

    @property
    def AverageDelayNanoSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned average delay in nanoseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageDelayNanoSec"])

    @property
    def AverageDelaySec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned average delay in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageDelaySec"])

    @property
    def AverageDelayVariationNanoSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned most recent delay variation in nano seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageDelayVariationNanoSec"])

    @property
    def AverageDelayVariationSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned most recent delay variation in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageDelayVariationSec"])

    @property
    def CVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned C-VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CVlan"])

    @property
    def DmmCountSent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of DMMs sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmmCountSent"])

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
    def MdLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned MD level for the periodic OAM.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel"])

    @property
    def NoReplyCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of periodic OAM no replies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoReplyCount"])

    @property
    def OneDmReceivedCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of DM received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OneDmReceivedCount"])

    @property
    def RecentDelayNanoSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned most recent delay measurement in nanoseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentDelayNanoSec"])

    @property
    def RecentDelaySec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned most recent delay measurement in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentDelaySec"])

    @property
    def RecentDelayVariationNanoSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned most recent delay variation in nano seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentDelayVariationNanoSec"])

    @property
    def RecentDelayVariationSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned most recent delay variation in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentDelayVariationSec"])

    @property
    def SVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned S-VLAN identifier.
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
        """Adds a new periodicOamDmLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved periodicOamDmLearnedInfo resources using find and the newly added periodicOamDmLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AverageDelayNanoSec=None,
        AverageDelaySec=None,
        AverageDelayVariationNanoSec=None,
        AverageDelayVariationSec=None,
        CVlan=None,
        DmmCountSent=None,
        DstMacAddress=None,
        MdLevel=None,
        NoReplyCount=None,
        OneDmReceivedCount=None,
        RecentDelayNanoSec=None,
        RecentDelaySec=None,
        RecentDelayVariationNanoSec=None,
        RecentDelayVariationSec=None,
        SVlan=None,
        SrcMacAddress=None,
    ):
        # type: (int, int, int, int, str, int, str, int, int, int, int, int, int, int, str, str) -> PeriodicOamDmLearnedInfo
        """Finds and retrieves periodicOamDmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve periodicOamDmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all periodicOamDmLearnedInfo resources from the server.

        Args
        ----
        - AverageDelayNanoSec (number): (read only) The learned average delay in nanoseconds.
        - AverageDelaySec (number): (read only) The learned average delay in seconds.
        - AverageDelayVariationNanoSec (number): (read only) The learned most recent delay variation in nano seconds.
        - AverageDelayVariationSec (number): (read only) The learned most recent delay variation in seconds.
        - CVlan (str): (read only) The learned C-VLAN identifier.
        - DmmCountSent (number): (read only) The learned number of DMMs sent.
        - DstMacAddress (str): (read only) The learned destination MAC address.
        - MdLevel (number): (read only) The learned MD level for the periodic OAM.
        - NoReplyCount (number): (read only) The learned number of periodic OAM no replies.
        - OneDmReceivedCount (number): (read only) The learned number of DM received.
        - RecentDelayNanoSec (number): (read only) The learned most recent delay measurement in nanoseconds.
        - RecentDelaySec (number): (read only) The learned most recent delay measurement in seconds.
        - RecentDelayVariationNanoSec (number): (read only) The learned most recent delay variation in nano seconds.
        - RecentDelayVariationSec (number): (read only) The learned most recent delay variation in seconds.
        - SVlan (str): (read only) The learned S-VLAN identifier.
        - SrcMacAddress (str): (read only) The learned source MAC address.

        Returns
        -------
        - self: This instance with matching periodicOamDmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of periodicOamDmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the periodicOamDmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class DmLearnedInfo(Base):
    """This object holds lists of the dm learned information.
    The DmLearnedInfo class encapsulates a list of dmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the DmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "dmLearnedInfo"
    _SDM_ATT_MAP = {
        "AverageLooseRtt": "averageLooseRtt",
        "AverageLooseRttVariation": "averageLooseRttVariation",
        "AverageStrictRtt": "averageStrictRtt",
        "AverageStrictRttVariation": "averageStrictRttVariation",
        "DmQueriesSent": "dmQueriesSent",
        "DmResponsesReceived": "dmResponsesReceived",
        "IncomingLabelOuterInner": "incomingLabelOuterInner",
        "MaxLooseRtt": "maxLooseRtt",
        "MaxStrictRtt": "maxStrictRtt",
        "MinLooseRtt": "minLooseRtt",
        "MinStrictRtt": "minStrictRtt",
        "OutgoingLabelOuterInner": "outgoingLabelOuterInner",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DmLearnedInfo, self).__init__(parent, list_op)

    @property
    def AverageLooseRtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the average loose RTT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageLooseRtt"])

    @property
    def AverageLooseRttVariation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the average loose RTT variation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageLooseRttVariation"])

    @property
    def AverageStrictRtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the average strict RTT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageStrictRtt"])

    @property
    def AverageStrictRttVariation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the average strict RTT variation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AverageStrictRttVariation"])

    @property
    def DmQueriesSent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of DM queries sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmQueriesSent"])

    @property
    def DmResponsesReceived(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the total number of DM responses received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmResponsesReceived"])

    @property
    def IncomingLabelOuterInner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the incoming label information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncomingLabelOuterInner"])

    @property
    def MaxLooseRtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the maximum loose RTT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxLooseRtt"])

    @property
    def MaxStrictRtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the maximum strict RTT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxStrictRtt"])

    @property
    def MinLooseRtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the minimum loose RTT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinLooseRtt"])

    @property
    def MinStrictRtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the minimum strict RTT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinStrictRtt"])

    @property
    def OutgoingLabelOuterInner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the Outgoing Label information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutgoingLabelOuterInner"])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the type of the learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    def add(self):
        """Adds a new dmLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved dmLearnedInfo resources using find and the newly added dmLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AverageLooseRtt=None,
        AverageLooseRttVariation=None,
        AverageStrictRtt=None,
        AverageStrictRttVariation=None,
        DmQueriesSent=None,
        DmResponsesReceived=None,
        IncomingLabelOuterInner=None,
        MaxLooseRtt=None,
        MaxStrictRtt=None,
        MinLooseRtt=None,
        MinStrictRtt=None,
        OutgoingLabelOuterInner=None,
        Type=None,
    ):
        # type: (str, str, str, str, int, int, str, str, str, str, str, str, str) -> DmLearnedInfo
        """Finds and retrieves dmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dmLearnedInfo resources from the server.

        Args
        ----
        - AverageLooseRtt (str): This signifies the average loose RTT.
        - AverageLooseRttVariation (str): This signifies the average loose RTT variation.
        - AverageStrictRtt (str): This signifies the average strict RTT.
        - AverageStrictRttVariation (str): This signifies the average strict RTT variation.
        - DmQueriesSent (number): This signifies the number of DM queries sent.
        - DmResponsesReceived (number): This signifies the total number of DM responses received.
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - MaxLooseRtt (str): This signifies the maximum loose RTT.
        - MaxStrictRtt (str): This signifies the maximum strict RTT.
        - MinLooseRtt (str): This signifies the minimum loose RTT.
        - MinStrictRtt (str): This signifies the minimum strict RTT.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - Type (str): This signifies the type of the learned information.

        Returns
        -------
        - self: This instance with matching dmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

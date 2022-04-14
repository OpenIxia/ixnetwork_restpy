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


class TraceRouteLearnedInfo(Base):
    """This object holds lists of the trace route learned information.
    The TraceRouteLearnedInfo class encapsulates a list of traceRouteLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the TraceRouteLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "traceRouteLearnedInfo"
    _SDM_ATT_MAP = {
        "IncomingLabelOuterInner": "incomingLabelOuterInner",
        "NumberOfReplyingHops": "numberOfReplyingHops",
        "OutgoingLabelOuterInner": "outgoingLabelOuterInner",
        "Reachability": "reachability",
        "SenderHandle": "senderHandle",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TraceRouteLearnedInfo, self).__init__(parent, list_op)

    @property
    def Hops(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hops_db4316dd77cab088f2212f004300bf3c.Hops): An instance of the Hops class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hops_db4316dd77cab088f2212f004300bf3c import (
            Hops,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Hops", None) is not None:
                return self._properties.get("Hops")
        return Hops(self)

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
    def NumberOfReplyingHops(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the total number of replying hops.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfReplyingHops"])

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
    def Reachability(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This specifies whether the queried MEP could be reached or not, Failure or, Partial or, Complete.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Reachability"])

    @property
    def SenderHandle(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the sender handle details.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SenderHandle"])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the type of path over which the traceroute is carried over, can be LSP, PW or Nested PW and LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    def add(self):
        """Adds a new traceRouteLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved traceRouteLearnedInfo resources using find and the newly added traceRouteLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        IncomingLabelOuterInner=None,
        NumberOfReplyingHops=None,
        OutgoingLabelOuterInner=None,
        Reachability=None,
        SenderHandle=None,
        Type=None,
    ):
        # type: (str, int, str, str, int, str) -> TraceRouteLearnedInfo
        """Finds and retrieves traceRouteLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve traceRouteLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all traceRouteLearnedInfo resources from the server.

        Args
        ----
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - NumberOfReplyingHops (number): This signifies the total number of replying hops.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - Reachability (str): This specifies whether the queried MEP could be reached or not, Failure or, Partial or, Complete.
        - SenderHandle (number): This signifies the sender handle details.
        - Type (str): This signifies the type of path over which the traceroute is carried over, can be LSP, PW or Nested PW and LSP.

        Returns
        -------
        - self: This instance with matching traceRouteLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of traceRouteLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the traceRouteLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

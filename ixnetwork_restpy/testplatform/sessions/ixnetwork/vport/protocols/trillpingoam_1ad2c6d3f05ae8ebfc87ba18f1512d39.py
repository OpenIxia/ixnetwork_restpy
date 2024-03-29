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


class TrillPingOam(Base):
    """NOT DEFINED
    The TrillPingOam class encapsulates a required trillPingOam resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "trillPingOam"
    _SDM_ATT_MAP = {
        "AlertFlag": "alertFlag",
        "DestinationNickname": "destinationNickname",
        "EtherType": "etherType",
        "HopCount": "hopCount",
        "NativeFlag": "nativeFlag",
        "NoOfPingRequests": "noOfPingRequests",
        "SilentFlag": "silentFlag",
        "SourceNickname": "sourceNickname",
        "TimeOut": "timeOut",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TrillPingOam, self).__init__(parent, list_op)

    @property
    def AlertFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlertFlag"])

    @AlertFlag.setter
    def AlertFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlertFlag"], value)

    @property
    def DestinationNickname(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationNickname"])

    @DestinationNickname.setter
    def DestinationNickname(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationNickname"], value)

    @property
    def EtherType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EtherType"])

    @EtherType.setter
    def EtherType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EtherType"], value)

    @property
    def HopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["HopCount"])

    @HopCount.setter
    def HopCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HopCount"], value)

    @property
    def NativeFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NativeFlag"])

    @NativeFlag.setter
    def NativeFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NativeFlag"], value)

    @property
    def NoOfPingRequests(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfPingRequests"])

    @NoOfPingRequests.setter
    def NoOfPingRequests(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfPingRequests"], value)

    @property
    def SilentFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SilentFlag"])

    @SilentFlag.setter
    def SilentFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SilentFlag"], value)

    @property
    def SourceNickname(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceNickname"])

    @SourceNickname.setter
    def SourceNickname(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceNickname"], value)

    @property
    def TimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimeOut"])

    @TimeOut.setter
    def TimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimeOut"], value)

    def update(
        self,
        AlertFlag=None,
        DestinationNickname=None,
        EtherType=None,
        HopCount=None,
        NativeFlag=None,
        NoOfPingRequests=None,
        SilentFlag=None,
        SourceNickname=None,
        TimeOut=None,
    ):
        # type: (bool, int, int, int, bool, int, bool, int, int) -> TrillPingOam
        """Updates trillPingOam resource on the server.

        Args
        ----
        - AlertFlag (bool): NOT DEFINED
        - DestinationNickname (number): NOT DEFINED
        - EtherType (number): NOT DEFINED
        - HopCount (number): NOT DEFINED
        - NativeFlag (bool): NOT DEFINED
        - NoOfPingRequests (number): NOT DEFINED
        - SilentFlag (bool): NOT DEFINED
        - SourceNickname (number): NOT DEFINED
        - TimeOut (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AlertFlag=None,
        DestinationNickname=None,
        EtherType=None,
        HopCount=None,
        NativeFlag=None,
        NoOfPingRequests=None,
        SilentFlag=None,
        SourceNickname=None,
        TimeOut=None,
    ):
        # type: (bool, int, int, int, bool, int, bool, int, int) -> TrillPingOam
        """Finds and retrieves trillPingOam resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trillPingOam resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trillPingOam resources from the server.

        Args
        ----
        - AlertFlag (bool): NOT DEFINED
        - DestinationNickname (number): NOT DEFINED
        - EtherType (number): NOT DEFINED
        - HopCount (number): NOT DEFINED
        - NativeFlag (bool): NOT DEFINED
        - NoOfPingRequests (number): NOT DEFINED
        - SilentFlag (bool): NOT DEFINED
        - SourceNickname (number): NOT DEFINED
        - TimeOut (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching trillPingOam resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trillPingOam data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trillPingOam resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

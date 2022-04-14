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


class SwitchMeterBandLearnedInfo(Base):
    """NOT DEFINED
    The SwitchMeterBandLearnedInfo class encapsulates a list of switchMeterBandLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchMeterBandLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "switchMeterBandLearnedInfo"
    _SDM_ATT_MAP = {
        "BandRate": "bandRate",
        "BandType": "bandType",
        "BurstSize": "burstSize",
        "ByteCount": "byteCount",
        "DatapathId": "datapathId",
        "DatapathIdAsHex": "datapathIdAsHex",
        "DropPrecedenceLevel": "dropPrecedenceLevel",
        "LocalIp": "localIp",
        "MeterId": "meterId",
        "PacketCount": "packetCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SwitchMeterBandLearnedInfo, self).__init__(parent, list_op)

    @property
    def BandRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BandRate"])

    @property
    def BandType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BandType"])

    @property
    def BurstSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstSize"])

    @property
    def ByteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ByteCount"])

    @property
    def DatapathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DatapathId"])

    @property
    def DatapathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DatapathIdAsHex"])

    @property
    def DropPrecedenceLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DropPrecedenceLevel"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def MeterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeterId"])

    @property
    def PacketCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketCount"])

    def add(self):
        """Adds a new switchMeterBandLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved switchMeterBandLearnedInfo resources using find and the newly added switchMeterBandLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BandRate=None,
        BandType=None,
        BurstSize=None,
        ByteCount=None,
        DatapathId=None,
        DatapathIdAsHex=None,
        DropPrecedenceLevel=None,
        LocalIp=None,
        MeterId=None,
        PacketCount=None,
    ):
        # type: (int, str, int, int, str, str, int, str, int, int) -> SwitchMeterBandLearnedInfo
        """Finds and retrieves switchMeterBandLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchMeterBandLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchMeterBandLearnedInfo resources from the server.

        Args
        ----
        - BandRate (number): NOT DEFINED
        - BandType (str): NOT DEFINED
        - BurstSize (number): NOT DEFINED
        - ByteCount (number): NOT DEFINED
        - DatapathId (str): NOT DEFINED
        - DatapathIdAsHex (str): NOT DEFINED
        - DropPrecedenceLevel (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - MeterId (number): NOT DEFINED
        - PacketCount (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchMeterBandLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchMeterBandLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchMeterBandLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

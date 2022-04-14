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


class SwitchHostRangeHopsLearnedInfo(Base):
    """NOT DEFINED
    The SwitchHostRangeHopsLearnedInfo class encapsulates a list of switchHostRangeHopsLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchHostRangeHopsLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "switchHostRangeHopsLearnedInfo"
    _SDM_ATT_MAP = {
        "Action": "action",
        "DestinationHostMac": "destinationHostMac",
        "InputPort": "inputPort",
        "InputTimeInMs": "inputTimeInMs",
        "OutputPort": "outputPort",
        "OutputTimeInMs": "outputTimeInMs",
        "SourceHostMac": "sourceHostMac",
        "SwitchDataPathId": "switchDataPathId",
        "SwitchIp": "switchIp",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SwitchHostRangeHopsLearnedInfo, self).__init__(parent, list_op)

    @property
    def Action(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Action"])

    @property
    def DestinationHostMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationHostMac"])

    @property
    def InputPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputPort"])

    @property
    def InputTimeInMs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputTimeInMs"])

    @property
    def OutputPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutputPort"])

    @property
    def OutputTimeInMs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutputTimeInMs"])

    @property
    def SourceHostMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceHostMac"])

    @property
    def SwitchDataPathId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchDataPathId"])

    @property
    def SwitchIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchIp"])

    def add(self):
        """Adds a new switchHostRangeHopsLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved switchHostRangeHopsLearnedInfo resources using find and the newly added switchHostRangeHopsLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Action=None,
        DestinationHostMac=None,
        InputPort=None,
        InputTimeInMs=None,
        OutputPort=None,
        OutputTimeInMs=None,
        SourceHostMac=None,
        SwitchDataPathId=None,
        SwitchIp=None,
    ):
        # type: (str, str, int, int, int, int, str, int, str) -> SwitchHostRangeHopsLearnedInfo
        """Finds and retrieves switchHostRangeHopsLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchHostRangeHopsLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchHostRangeHopsLearnedInfo resources from the server.

        Args
        ----
        - Action (str): NOT DEFINED
        - DestinationHostMac (str): NOT DEFINED
        - InputPort (number): NOT DEFINED
        - InputTimeInMs (number): NOT DEFINED
        - OutputPort (number): NOT DEFINED
        - OutputTimeInMs (number): NOT DEFINED
        - SourceHostMac (str): NOT DEFINED
        - SwitchDataPathId (number): NOT DEFINED
        - SwitchIp (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchHostRangeHopsLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchHostRangeHopsLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchHostRangeHopsLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

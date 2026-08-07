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


class RxCtlOSDrop(Base):
    """
    The RxCtlOSDrop class encapsulates a required rxCtlOSDrop resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rxCtlOSDrop"
    _SDM_ATT_MAP = {
        "Continuous": "continuous",
        "EnableDropAck": "enableDropAck",
        "EnableDropInit": "enableDropInit",
        "EnableDropInitEcho": "enableDropInitEcho",
        "EnableDropNack": "enableDropNack",
        "TestState": "testState",
        "TestStatus": "testStatus",
    }
    _SDM_ENUM_MAP = {
        "testState": ["notRunning", "running", "stopping", "error"],
    }

    def __init__(self, parent, list_op=False):
        super(RxCtlOSDrop, self).__init__(parent, list_op)

    @property
    def Continuous(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, the configured Rx CtlOS drops are applied continuously instead of only once.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Continuous"])

    @property
    def EnableDropAck(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, discard incoming LLR_ACK CtlOS frames before the LLR processes them.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropAck"])

    @EnableDropAck.setter
    def EnableDropAck(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropAck"], value)

    @property
    def EnableDropInit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, discard incoming INIT CtlOS frames before the LLR processes them.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropInit"])

    @EnableDropInit.setter
    def EnableDropInit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropInit"], value)

    @property
    def EnableDropInitEcho(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, discard incoming INIT_ECHO CtlOS frames before the LLR processes them.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropInitEcho"])

    @EnableDropInitEcho.setter
    def EnableDropInitEcho(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropInitEcho"], value)

    @property
    def EnableDropNack(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, discard incoming LLR_NACK CtlOS frames before the LLR processes them.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropNack"])

    @EnableDropNack.setter
    def EnableDropNack(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropNack"], value)

    @property
    def TestState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notRunning | running | stopping | error): Current execution state of the impairment test (Not Running / Running / Stopping / Error).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestState"])

    @property
    def TestStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Status of the impairment test's last/current run (e.g., Started, Stopped, error details).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestStatus"])

    def update(
        self,
        EnableDropAck=None,
        EnableDropInit=None,
        EnableDropInitEcho=None,
        EnableDropNack=None,
    ):
        # type: (bool, bool, bool, bool) -> RxCtlOSDrop
        """Updates rxCtlOSDrop resource on the server.

        Args
        ----
        - EnableDropAck (bool): When ON, discard incoming LLR_ACK CtlOS frames before the LLR processes them.
        - EnableDropInit (bool): When ON, discard incoming INIT CtlOS frames before the LLR processes them.
        - EnableDropInitEcho (bool): When ON, discard incoming INIT_ECHO CtlOS frames before the LLR processes them.
        - EnableDropNack (bool): When ON, discard incoming LLR_NACK CtlOS frames before the LLR processes them.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Continuous=None,
        EnableDropAck=None,
        EnableDropInit=None,
        EnableDropInitEcho=None,
        EnableDropNack=None,
        TestState=None,
        TestStatus=None,
    ):
        # type: (bool, bool, bool, bool, bool, str, str) -> RxCtlOSDrop
        """Finds and retrieves rxCtlOSDrop resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rxCtlOSDrop resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rxCtlOSDrop resources from the server.

        Args
        ----
        - Continuous (bool): When ON, the configured Rx CtlOS drops are applied continuously instead of only once.
        - EnableDropAck (bool): When ON, discard incoming LLR_ACK CtlOS frames before the LLR processes them.
        - EnableDropInit (bool): When ON, discard incoming INIT CtlOS frames before the LLR processes them.
        - EnableDropInitEcho (bool): When ON, discard incoming INIT_ECHO CtlOS frames before the LLR processes them.
        - EnableDropNack (bool): When ON, discard incoming LLR_NACK CtlOS frames before the LLR processes them.
        - TestState (str(notRunning | running | stopping | error)): Current execution state of the impairment test (Not Running / Running / Stopping / Error).
        - TestStatus (str): Status of the impairment test's last/current run (e.g., Started, Stopped, error details).

        Returns
        -------
        - self: This instance with matching rxCtlOSDrop resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rxCtlOSDrop data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rxCtlOSDrop resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

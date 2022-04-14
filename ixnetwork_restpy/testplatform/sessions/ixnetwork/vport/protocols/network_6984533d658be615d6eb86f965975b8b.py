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


class Network(Base):
    """
    The Network class encapsulates a list of network resources that are managed by the system.
    A list of resources can be retrieved from the server using the Network.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "network"
    _SDM_ATT_MAP = {
        "AttachedRouters": "attachedRouters",
        "OptBitDc": "optBitDc",
        "OptBitE": "optBitE",
        "OptBitMc": "optBitMc",
        "OptBitN": "optBitN",
        "OptBitR": "optBitR",
        "OptBitV6": "optBitV6",
        "Option": "option",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Network, self).__init__(parent, list_op)

    @property
    def AttachedRouters(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str):
        """
        return self._get_attribute(self._SDM_ATT_MAP["AttachedRouters"])

    @AttachedRouters.setter
    def AttachedRouters(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["AttachedRouters"], value)

    @property
    def OptBitDc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitDc"])

    @OptBitDc.setter
    def OptBitDc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitDc"], value)

    @property
    def OptBitE(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitE"])

    @OptBitE.setter
    def OptBitE(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitE"], value)

    @property
    def OptBitMc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitMc"])

    @OptBitMc.setter
    def OptBitMc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitMc"], value)

    @property
    def OptBitN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitN"])

    @OptBitN.setter
    def OptBitN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitN"], value)

    @property
    def OptBitR(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitR"])

    @OptBitR.setter
    def OptBitR(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitR"], value)

    @property
    def OptBitV6(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitV6"])

    @OptBitV6.setter
    def OptBitV6(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitV6"], value)

    @property
    def Option(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Option"])

    @Option.setter
    def Option(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Option"], value)

    def update(
        self,
        AttachedRouters=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
    ):
        # type: (List[str], bool, bool, bool, bool, bool, bool, int) -> Network
        """Updates network resource on the server.

        Args
        ----
        - AttachedRouters (list(str)):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AttachedRouters=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
    ):
        # type: (List[str], bool, bool, bool, bool, bool, bool, int) -> Network
        """Adds a new network resource on the json, only valid with batch add utility

        Args
        ----
        - AttachedRouters (list(str)):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):

        Returns
        -------
        - self: This instance with all currently retrieved network resources using find and the newly added network resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AttachedRouters=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
    ):
        # type: (List[str], bool, bool, bool, bool, bool, bool, int) -> Network
        """Finds and retrieves network resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve network resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all network resources from the server.

        Args
        ----
        - AttachedRouters (list(str)):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):

        Returns
        -------
        - self: This instance with matching network resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of network data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the network resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

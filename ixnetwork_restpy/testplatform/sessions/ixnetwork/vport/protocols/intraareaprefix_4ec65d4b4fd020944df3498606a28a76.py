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


class IntraAreaPrefix(Base):
    """
    The IntraAreaPrefix class encapsulates a list of intraAreaPrefix resources that are managed by the system.
    A list of resources can be retrieved from the server using the IntraAreaPrefix.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "intraAreaPrefix"
    _SDM_ATT_MAP = {
        "CountLsa": "countLsa",
        "IncrLinkStateId": "incrLinkStateId",
        "Prefixes": "prefixes",
        "RefLinkStateId": "refLinkStateId",
        "RefRouterId": "refRouterId",
        "ReferenceType": "referenceType",
    }
    _SDM_ENUM_MAP = {
        "referenceType": ["routerLsa", "networkLsa"],
    }

    def __init__(self, parent, list_op=False):
        super(IntraAreaPrefix, self).__init__(parent, list_op)

    @property
    def CountLsa(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountLsa"])

    @CountLsa.setter
    def CountLsa(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountLsa"], value)

    @property
    def IncrLinkStateId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrLinkStateId"])

    @IncrLinkStateId.setter
    def IncrLinkStateId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrLinkStateId"], value)

    @property
    def Prefixes(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number)):
        """
        return self._get_attribute(self._SDM_ATT_MAP["Prefixes"])

    @Prefixes.setter
    def Prefixes(self, value):
        self._set_attribute(self._SDM_ATT_MAP["Prefixes"], value)

    @property
    def RefLinkStateId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RefLinkStateId"])

    @RefLinkStateId.setter
    def RefLinkStateId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RefLinkStateId"], value)

    @property
    def RefRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RefRouterId"])

    @RefRouterId.setter
    def RefRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RefRouterId"], value)

    @property
    def ReferenceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(routerLsa | networkLsa):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReferenceType"])

    @ReferenceType.setter
    def ReferenceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReferenceType"], value)

    def update(
        self,
        CountLsa=None,
        IncrLinkStateId=None,
        Prefixes=None,
        RefLinkStateId=None,
        RefRouterId=None,
        ReferenceType=None,
    ):
        """Updates intraAreaPrefix resource on the server.

        Args
        ----
        - CountLsa (number):
        - IncrLinkStateId (str):
        - Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number))):
        - RefLinkStateId (str):
        - RefRouterId (str):
        - ReferenceType (str(routerLsa | networkLsa)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        CountLsa=None,
        IncrLinkStateId=None,
        Prefixes=None,
        RefLinkStateId=None,
        RefRouterId=None,
        ReferenceType=None,
    ):
        """Adds a new intraAreaPrefix resource on the json, only valid with batch add utility

        Args
        ----
        - CountLsa (number):
        - IncrLinkStateId (str):
        - Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number))):
        - RefLinkStateId (str):
        - RefRouterId (str):
        - ReferenceType (str(routerLsa | networkLsa)):

        Returns
        -------
        - self: This instance with all currently retrieved intraAreaPrefix resources using find and the newly added intraAreaPrefix resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CountLsa=None,
        IncrLinkStateId=None,
        Prefixes=None,
        RefLinkStateId=None,
        RefRouterId=None,
        ReferenceType=None,
    ):
        """Finds and retrieves intraAreaPrefix resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve intraAreaPrefix resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all intraAreaPrefix resources from the server.

        Args
        ----
        - CountLsa (number):
        - IncrLinkStateId (str):
        - Prefixes (list(dict(arg1:str,arg2:number,arg3:number,arg4:number,arg5:number))):
        - RefLinkStateId (str):
        - RefRouterId (str):
        - ReferenceType (str(routerLsa | networkLsa)):

        Returns
        -------
        - self: This instance with matching intraAreaPrefix resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of intraAreaPrefix data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the intraAreaPrefix resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

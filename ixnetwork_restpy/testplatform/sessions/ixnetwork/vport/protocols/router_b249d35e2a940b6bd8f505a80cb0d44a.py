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


class Router(Base):
    """
    The Router class encapsulates a list of router resources that are managed by the system.
    A list of resources can be retrieved from the server using the Router.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "router"
    _SDM_ATT_MAP = {
        "BBit": "bBit",
        "EBit": "eBit",
        "Interfaces": "interfaces",
        "OptBitDc": "optBitDc",
        "OptBitE": "optBitE",
        "OptBitMc": "optBitMc",
        "OptBitN": "optBitN",
        "OptBitR": "optBitR",
        "OptBitV6": "optBitV6",
        "Option": "option",
        "VBit": "vBit",
        "WBit": "wBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def BBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["BBit"])

    @BBit.setter
    def BBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BBit"], value)

    @property
    def EBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EBit"])

    @EBit.setter
    def EBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EBit"], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str,arg4:str[transit | pointToPoint | virtual],arg5:number)):
        """
        return self._get_attribute(self._SDM_ATT_MAP["Interfaces"])

    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP["Interfaces"], value)

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

    @property
    def VBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["VBit"])

    @VBit.setter
    def VBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VBit"], value)

    @property
    def WBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["WBit"])

    @WBit.setter
    def WBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WBit"], value)

    def update(
        self,
        BBit=None,
        EBit=None,
        Interfaces=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
        VBit=None,
        WBit=None,
    ):
        """Updates router resource on the server.

        Args
        ----
        - BBit (bool):
        - EBit (bool):
        - Interfaces (list(dict(arg1:number,arg2:number,arg3:str,arg4:str[transit | pointToPoint | virtual],arg5:number))):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):
        - VBit (bool):
        - WBit (bool):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BBit=None,
        EBit=None,
        Interfaces=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
        VBit=None,
        WBit=None,
    ):
        """Adds a new router resource on the json, only valid with batch add utility

        Args
        ----
        - BBit (bool):
        - EBit (bool):
        - Interfaces (list(dict(arg1:number,arg2:number,arg3:str,arg4:str[transit | pointToPoint | virtual],arg5:number))):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):
        - VBit (bool):
        - WBit (bool):

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BBit=None,
        EBit=None,
        Interfaces=None,
        OptBitDc=None,
        OptBitE=None,
        OptBitMc=None,
        OptBitN=None,
        OptBitR=None,
        OptBitV6=None,
        Option=None,
        VBit=None,
        WBit=None,
    ):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - BBit (bool):
        - EBit (bool):
        - Interfaces (list(dict(arg1:number,arg2:number,arg3:str,arg4:str[transit | pointToPoint | virtual],arg5:number))):
        - OptBitDc (bool):
        - OptBitE (bool):
        - OptBitMc (bool):
        - OptBitN (bool):
        - OptBitR (bool):
        - OptBitV6 (bool):
        - Option (number):
        - VBit (bool):
        - WBit (bool):

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

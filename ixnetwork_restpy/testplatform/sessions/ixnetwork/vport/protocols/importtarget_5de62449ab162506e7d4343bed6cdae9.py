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


class ImportTarget(Base):
    """This object controls the configuration of L3 Site imported targets.
    The ImportTarget class encapsulates a required importTarget resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "importTarget"
    _SDM_ATT_MAP = {
        "ImportTargetList": "importTargetList",
        "ImportTargetListEx": "importTargetListEx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ImportTarget, self).__init__(parent, list_op)

    @property
    def ImportTargetList(self):
        """DEPRECATED
        Returns
        -------
        - list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number)): Configures a target attribute to be associated with advertised L3 VPN route ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImportTargetList"])

    @ImportTargetList.setter
    def ImportTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP["ImportTargetList"], value)

    @property
    def ImportTargetListEx(self):
        """
        Returns
        -------
        - list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number,arg5:number,arg6:number,arg7:str)): Configures a list of export targets to be associated with advertised L3 VPN routeranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImportTargetListEx"])

    @ImportTargetListEx.setter
    def ImportTargetListEx(self, value):
        self._set_attribute(self._SDM_ATT_MAP["ImportTargetListEx"], value)

    def update(self, ImportTargetList=None, ImportTargetListEx=None):
        """Updates importTarget resource on the server.

        Args
        ----
        - ImportTargetList (list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number))): Configures a target attribute to be associated with advertised L3 VPN route ranges.
        - ImportTargetListEx (list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number,arg5:number,arg6:number,arg7:str))): Configures a list of export targets to be associated with advertised L3 VPN routeranges.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ImportTargetList=None, ImportTargetListEx=None):
        """Finds and retrieves importTarget resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve importTarget resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all importTarget resources from the server.

        Args
        ----
        - ImportTargetList (list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number))): Configures a target attribute to be associated with advertised L3 VPN route ranges.
        - ImportTargetListEx (list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number,arg5:number,arg6:number,arg7:str))): Configures a list of export targets to be associated with advertised L3 VPN routeranges.

        Returns
        -------
        - self: This instance with matching importTarget resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of importTarget data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the importTarget resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

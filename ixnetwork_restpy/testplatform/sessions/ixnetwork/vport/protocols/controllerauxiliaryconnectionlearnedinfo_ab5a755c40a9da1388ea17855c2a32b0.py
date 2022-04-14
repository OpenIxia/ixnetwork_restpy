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


class ControllerAuxiliaryConnectionLearnedInfo(Base):
    """This object allows to configure the controller auxiliary connection learned information.
    The ControllerAuxiliaryConnectionLearnedInfo class encapsulates a list of controllerAuxiliaryConnectionLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the ControllerAuxiliaryConnectionLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "controllerAuxiliaryConnectionLearnedInfo"
    _SDM_ATT_MAP = {
        "AuxiliaryId": "auxiliaryId",
        "ConnectionType": "connectionType",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "LocalIp": "localIp",
        "LocalPort": "localPort",
        "RemoteIp": "remoteIp",
        "RemotePort": "remotePort",
    }
    _SDM_ENUM_MAP = {
        "connectionType": ["tcp", "tls", "udp"],
    }

    def __init__(self, parent, list_op=False):
        super(ControllerAuxiliaryConnectionLearnedInfo, self).__init__(parent, list_op)

    @property
    def AuxiliaryId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the identifier for auxiliary connections.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuxiliaryId"])

    @property
    def ConnectionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tcp | tls | udp): Specifies how this controllerPort is connected to another controller (internal/external) or host or there is no connection (noConnection)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectionType"])

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the datapath ID of the OpenFlow controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the datapath ID of the OpenFlow controller in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathIdAsHex"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the local IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def LocalPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the local port number identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPort"])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the IP address of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def RemotePort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the remote port number identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePort"])

    def add(self):
        """Adds a new controllerAuxiliaryConnectionLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved controllerAuxiliaryConnectionLearnedInfo resources using find and the newly added controllerAuxiliaryConnectionLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AuxiliaryId=None,
        ConnectionType=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        LocalIp=None,
        LocalPort=None,
        RemoteIp=None,
        RemotePort=None,
    ):
        # type: (int, str, str, str, str, int, str, int) -> ControllerAuxiliaryConnectionLearnedInfo
        """Finds and retrieves controllerAuxiliaryConnectionLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve controllerAuxiliaryConnectionLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all controllerAuxiliaryConnectionLearnedInfo resources from the server.

        Args
        ----
        - AuxiliaryId (number): This describes the identifier for auxiliary connections.
        - ConnectionType (str(tcp | tls | udp)): Specifies how this controllerPort is connected to another controller (internal/external) or host or there is no connection (noConnection)
        - DataPathId (str): Indicates the datapath ID of the OpenFlow controller.
        - DataPathIdAsHex (str): Indicates the datapath ID of the OpenFlow controller in hexadecimal format.
        - LocalIp (str): Signifies the local IP address of the selected interface.
        - LocalPort (number): This describes the local port number identifier.
        - RemoteIp (str): This describes the IP address of the remote end of the OF Channel.
        - RemotePort (number): This describes the remote port number identifier.

        Returns
        -------
        - self: This instance with matching controllerAuxiliaryConnectionLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of controllerAuxiliaryConnectionLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the controllerAuxiliaryConnectionLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

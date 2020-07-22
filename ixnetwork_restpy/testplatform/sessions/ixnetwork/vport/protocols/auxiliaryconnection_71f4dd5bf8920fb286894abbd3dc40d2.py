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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AuxiliaryConnection(Base):
    """A high level object that allows to define the auxiliary connection configurations for the OpenFlow switch.
    The AuxiliaryConnection class encapsulates a list of auxiliaryConnection resources that are managed by the user.
    A list of resources can be retrieved from the server using the AuxiliaryConnection.find() method.
    The list can be managed by using the AuxiliaryConnection.add() and AuxiliaryConnection.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'auxiliaryConnection'
    _SDM_ATT_MAP = {
        'AuxiliaryId': 'auxiliaryId',
        'ConnectionType': 'connectionType',
        'Enable': 'enable',
        'UdpSourcePortNumber': 'udpSourcePortNumber',
    }

    def __init__(self, parent):
        super(AuxiliaryConnection, self).__init__(parent)

    @property
    def AuxiliaryId(self):
        """
        Returns
        -------
        - number: Indicates the Id of the auxiliary connection.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuxiliaryId'])
    @AuxiliaryId.setter
    def AuxiliaryId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuxiliaryId'], value)

    @property
    def ConnectionType(self):
        """
        Returns
        -------
        - str(tcp | tls | udp): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionType'])
    @ConnectionType.setter
    def ConnectionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectionType'], value)

    @property
    def Enable(self):
        """
        Returns
        -------
        - bool: If true, the object is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enable'])
    @Enable.setter
    def Enable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enable'], value)

    @property
    def UdpSourcePortNumber(self):
        """
        Returns
        -------
        - number: Specify the UDP source port number. The default value is 0. This field is available only if the Connection Type specified is UDP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSourcePortNumber'])
    @UdpSourcePortNumber.setter
    def UdpSourcePortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSourcePortNumber'], value)

    def update(self, AuxiliaryId=None, ConnectionType=None, Enable=None, UdpSourcePortNumber=None):
        """Updates auxiliaryConnection resource on the server.

        Args
        ----
        - AuxiliaryId (number): Indicates the Id of the auxiliary connection.
        - ConnectionType (str(tcp | tls | udp)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        - Enable (bool): If true, the object is enabled.
        - UdpSourcePortNumber (number): Specify the UDP source port number. The default value is 0. This field is available only if the Connection Type specified is UDP.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AuxiliaryId=None, ConnectionType=None, Enable=None, UdpSourcePortNumber=None):
        """Adds a new auxiliaryConnection resource on the server and adds it to the container.

        Args
        ----
        - AuxiliaryId (number): Indicates the Id of the auxiliary connection.
        - ConnectionType (str(tcp | tls | udp)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        - Enable (bool): If true, the object is enabled.
        - UdpSourcePortNumber (number): Specify the UDP source port number. The default value is 0. This field is available only if the Connection Type specified is UDP.

        Returns
        -------
        - self: This instance with all currently retrieved auxiliaryConnection resources using find and the newly added auxiliaryConnection resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained auxiliaryConnection resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AuxiliaryId=None, ConnectionType=None, Enable=None, UdpSourcePortNumber=None):
        """Finds and retrieves auxiliaryConnection resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve auxiliaryConnection resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all auxiliaryConnection resources from the server.

        Args
        ----
        - AuxiliaryId (number): Indicates the Id of the auxiliary connection.
        - ConnectionType (str(tcp | tls | udp)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        - Enable (bool): If true, the object is enabled.
        - UdpSourcePortNumber (number): Specify the UDP source port number. The default value is 0. This field is available only if the Connection Type specified is UDP.

        Returns
        -------
        - self: This instance with matching auxiliaryConnection resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of auxiliaryConnection data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the auxiliaryConnection resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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


class SwitchOfChannel(Base):
    """A high level object that allows to define the OpenFlow Channel configurations for the switch.
    The SwitchOfChannel class encapsulates a list of switchOfChannel resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchOfChannel.find() method.
    The list can be managed by using the SwitchOfChannel.add() and SwitchOfChannel.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchOfChannel'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'Enabled': 'enabled',
        'RemoteIp': 'remoteIp',
    }

    def __init__(self, parent):
        super(SwitchOfChannel, self).__init__(parent)

    @property
    def AuxiliaryConnection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.auxiliaryconnection_71f4dd5bf8920fb286894abbd3dc40d2.AuxiliaryConnection): An instance of the AuxiliaryConnection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.auxiliaryconnection_71f4dd5bf8920fb286894abbd3dc40d2 import AuxiliaryConnection
        return AuxiliaryConnection(self)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description of the object
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the object is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Signifies the Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])
    @RemoteIp.setter
    def RemoteIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemoteIp'], value)

    def update(self, Description=None, Enabled=None, RemoteIp=None):
        """Updates switchOfChannel resource on the server.

        Args
        ----
        - Description (str): A description of the object
        - Enabled (bool): If true, the object is enabled.
        - RemoteIp (str): Signifies the Remote IP address of the selected interface.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, Enabled=None, RemoteIp=None):
        """Adds a new switchOfChannel resource on the server and adds it to the container.

        Args
        ----
        - Description (str): A description of the object
        - Enabled (bool): If true, the object is enabled.
        - RemoteIp (str): Signifies the Remote IP address of the selected interface.

        Returns
        -------
        - self: This instance with all currently retrieved switchOfChannel resources using find and the newly added switchOfChannel resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchOfChannel resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Description=None, Enabled=None, RemoteIp=None):
        """Finds and retrieves switchOfChannel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchOfChannel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchOfChannel resources from the server.

        Args
        ----
        - Description (str): A description of the object
        - Enabled (bool): If true, the object is enabled.
        - RemoteIp (str): Signifies the Remote IP address of the selected interface.

        Returns
        -------
        - self: This instance with matching switchOfChannel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchOfChannel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchOfChannel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

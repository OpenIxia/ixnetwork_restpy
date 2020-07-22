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


class IxVmCard(Base):
    """Retrieves the list of cards existent on the virtual chassis
    The IxVmCard class encapsulates a list of ixVmCard resources that are managed by the user.
    A list of resources can be retrieved from the server using the IxVmCard.find() method.
    The list can be managed by using the IxVmCard.add() and IxVmCard.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ixVmCard'
    _SDM_ATT_MAP = {
        'CardId': 'cardId',
        'CardName': 'cardName',
        'CardState': 'cardState',
        'KeepAliveTimeout': 'keepAliveTimeout',
        'ManagementIp': 'managementIp',
    }

    def __init__(self, parent):
        super(IxVmCard, self).__init__(parent)

    @property
    def IxVmPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.ixvmcard.ixvmport.ixvmport.IxVmPort): An instance of the IxVmPort class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.ixvmcard.ixvmport.ixvmport import IxVmPort
        return IxVmPort(self)

    @property
    def CardId(self):
        """
        Returns
        -------
        - str: Represents slot on the chassis
        """
        return self._get_attribute(self._SDM_ATT_MAP['CardId'])
    @CardId.setter
    def CardId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CardId'], value)

    @property
    def CardName(self):
        """
        Returns
        -------
        - str: Represents the card name
        """
        return self._get_attribute(self._SDM_ATT_MAP['CardName'])
    @CardName.setter
    def CardName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CardName'], value)

    @property
    def CardState(self):
        """
        Returns
        -------
        - str(cardDisconnected | cardIpInUse | cardOK | cardRemoved | cardUnableToConnect | cardUnitialized | cardUnknownError | cardUnsynchronized | cardVersionMismatch): Represents the card state
        """
        return self._get_attribute(self._SDM_ATT_MAP['CardState'])

    @property
    def KeepAliveTimeout(self):
        """
        Returns
        -------
        - number: Represents the keepalive timeout
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeepAliveTimeout'])
    @KeepAliveTimeout.setter
    def KeepAliveTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeepAliveTimeout'], value)

    @property
    def ManagementIp(self):
        """
        Returns
        -------
        - str: Represents the management Ip
        """
        return self._get_attribute(self._SDM_ATT_MAP['ManagementIp'])
    @ManagementIp.setter
    def ManagementIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ManagementIp'], value)

    def update(self, CardId=None, CardName=None, KeepAliveTimeout=None, ManagementIp=None):
        """Updates ixVmCard resource on the server.

        Args
        ----
        - CardId (str): Represents slot on the chassis
        - CardName (str): Represents the card name
        - KeepAliveTimeout (number): Represents the keepalive timeout
        - ManagementIp (str): Represents the management Ip

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CardId=None, CardName=None, KeepAliveTimeout=None, ManagementIp=None):
        """Adds a new ixVmCard resource on the server and adds it to the container.

        Args
        ----
        - CardId (str): Represents slot on the chassis
        - CardName (str): Represents the card name
        - KeepAliveTimeout (number): Represents the keepalive timeout
        - ManagementIp (str): Represents the management Ip

        Returns
        -------
        - self: This instance with all currently retrieved ixVmCard resources using find and the newly added ixVmCard resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ixVmCard resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CardId=None, CardName=None, CardState=None, KeepAliveTimeout=None, ManagementIp=None):
        """Finds and retrieves ixVmCard resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ixVmCard resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ixVmCard resources from the server.

        Args
        ----
        - CardId (str): Represents slot on the chassis
        - CardName (str): Represents the card name
        - CardState (str(cardDisconnected | cardIpInUse | cardOK | cardRemoved | cardUnableToConnect | cardUnitialized | cardUnknownError | cardUnsynchronized | cardVersionMismatch)): Represents the card state
        - KeepAliveTimeout (number): Represents the keepalive timeout
        - ManagementIp (str): Represents the management Ip

        Returns
        -------
        - self: This instance with matching ixVmCard resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ixVmCard data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ixVmCard resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

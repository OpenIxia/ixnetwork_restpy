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


class OrganizationSpecificOamPduData(Base):
    """
    The OrganizationSpecificOamPduData class encapsulates a list of organizationSpecificOamPduData resources that are managed by the user.
    A list of resources can be retrieved from the server using the OrganizationSpecificOamPduData.find() method.
    The list can be managed by using the OrganizationSpecificOamPduData.add() and OrganizationSpecificOamPduData.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'organizationSpecificOamPduData'
    _SDM_ATT_MAP = {
        'Oui': 'oui',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(OrganizationSpecificOamPduData, self).__init__(parent)

    @property
    def Oui(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Oui'])
    @Oui.setter
    def Oui(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Oui'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Oui=None, Value=None):
        """Updates organizationSpecificOamPduData resource on the server.

        Args
        ----
        - Oui (str): 
        - Value (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Oui=None, Value=None):
        """Adds a new organizationSpecificOamPduData resource on the server and adds it to the container.

        Args
        ----
        - Oui (str): 
        - Value (str): 

        Returns
        -------
        - self: This instance with all currently retrieved organizationSpecificOamPduData resources using find and the newly added organizationSpecificOamPduData resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained organizationSpecificOamPduData resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Oui=None, Value=None):
        """Finds and retrieves organizationSpecificOamPduData resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve organizationSpecificOamPduData resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all organizationSpecificOamPduData resources from the server.

        Args
        ----
        - Oui (str): 
        - Value (str): 

        Returns
        -------
        - self: This instance with matching organizationSpecificOamPduData resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of organizationSpecificOamPduData data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the organizationSpecificOamPduData resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
